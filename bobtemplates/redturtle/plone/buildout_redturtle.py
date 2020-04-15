# -*- coding: utf-8 -*-
from bobtemplates.plone.base import git_commit
from bobtemplates.plone.base import git_init
from bobtemplates.plone.base import make_path

import os
import shutil


def prepare_renderer(configurator):
    configurator.variables['template_id'] = 'buildout_redturtle'


def remove_not_selected_pm(configurator):
    delimiter = configurator.raw_questions['process_manager'][
        'choices_delimiter'
    ]
    choices = configurator.raw_questions['process_manager']['choices'].split(
        delimiter
    )
    selected = configurator.variables['process_manager']
    for choice in choices:
        if choice != selected:
            shutil.rmtree(make_path(configurator.target_directory, choice))


def fix_process_manager(configurator):
    pm_path = make_path(
        configurator.target_directory,
        configurator.variables['process_manager'],
    )
    remove_not_selected_pm(configurator)
    for f in os.listdir(pm_path):
        file_path = make_path(pm_path, f)
        shutil.move(file_path, configurator.target_directory)
    shutil.rmtree(pm_path)


def post_renderer(configurator):
    fix_process_manager(configurator)
    git_init_status = git_init(configurator)
    name = os.path.basename(configurator.target_directory)
    if git_init_status:
        git_commit(configurator, 'Create Plone buildout: {0}'.format(name))
