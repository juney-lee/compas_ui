from __future__ import print_function
from __future__ import absolute_import
from __future__ import division

from compas_ui.app import App
from compas_ui.rhino.forms import error


__commandname__ = 'COMPAS_redo'


@error()
def RunCommand(is_interactive):

    app = App()
    app.redo()


if __name__ == '__main__':
    RunCommand(True)
