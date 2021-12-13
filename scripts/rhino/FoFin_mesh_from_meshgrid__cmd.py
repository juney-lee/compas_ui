from compas_ui.app import App
# from compas_fofin.ui import FofinApp


def RunCommand(interactive=True):

    # make App a singleton
    # and intialize a session when the singleton is created
    app = App('FoFin')
    app.controller.mesh_from_meshgrid()


# ******************************************************************************
# Run as Script
# ******************************************************************************

if __name__ == "__main__":
    RunCommand()
