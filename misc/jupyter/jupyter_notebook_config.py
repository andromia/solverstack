import io
import os
from subprocess import check_call
from notebook.utils import to_api_path

_script_exporter = None

def scrub_output_pre_save(model, **kwargs):
    """scrub output before saving notebooks"""
    # only run on notebooks
    if model['type'] != 'notebook':
        return
    # only run on nbformat v4
    if model['content']['nbformat'] != 4:
        return

    for cell in model['content']['cells']:
        if cell['cell_type'] != 'code':
            continue
        cell['outputs'] = []
        cell['execution_count'] = None

def script_post_save(model, os_path, contents_manager, **kwargs):
    """convert notebooks to Python script after save with nbconvert

    replaces `jupyter notebook --script`
    """
    from nbconvert.exporters.script import ScriptExporter

    if model['type'] != 'notebook':
        return

    global _script_exporter

    if _script_exporter is None:
        _script_exporter = ScriptExporter(parent=contents_manager)

    log = contents_manager.log

    d, fname = os.path.split(os_path)

    py_dir = os.path.join(os.path.dirname(os_path), 'py')
    if not os.path.exists(py_dir):
        os.makedirs(py_dir)

    py_args = ['jupyter', 'nbconvert',
                '--output-dir=./py',
                '--to', 'script', fname]

    if not fname.startswith('Untitled'):
        check_call(py_args, cwd=d)

c.FileContentsManager.pre_save_hook = scrub_output_pre_save
c.FileContentsManager.post_save_hook = script_post_save
