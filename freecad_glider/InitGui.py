import os
try:
    import FreeCADGui as Gui
    import FreeCAD
except ImportError:
    print("module not loaded with FreeCAD")

import glider_metadata
Dir = os.path.dirname(glider_metadata.__file__)

Gui.addIconPath(Dir + "/icons")


class gliderWorkbench(Gui.Workbench):
    """probe workbench object"""
    MenuText = "glider"
    ToolTip = "glider workbench"
    Icon = "glider_workbench.svg"
    toolBox = [
        "CreateGlider",
        "ImportGlider",
        "ShapeCommand",
        "ArcCommand",
        "AoaCommand",
        "ZrotCommand",
        "AirfoilCommand",
        "AirfoilMergeCommand",
        "BallooningCommand",
        "BallooningMergeCommand",
        "CellCommand",
        "LineCommand",
        "DesignCommand",
        "Gl2dExport"]

    productionBox = [
        "PatternCommand",
        "PanelCommand",
        "PolarsCommand"
        ]

    devBox = [
        "RefreshCommand"
        ]

    def GetClassName(self):
        return "Gui::PythonWorkbench"

    def Initialize(self):
        import tools
        global Dir
        
        Gui.addCommand('CreateGlider', tools.CreateGlider())
        Gui.addCommand('ShapeCommand', tools.ShapeCommand())
        Gui.addCommand('AirfoilCommand', tools.AirfoilCommand())
        Gui.addCommand('ArcCommand', tools.ArcCommand())
        Gui.addCommand("AoaCommand", tools.AoaCommand())
        Gui.addCommand("BallooningCommand", tools.BallooningCommand())
        Gui.addCommand("LineCommand", tools.LineCommand())

        Gui.addCommand("ImportGlider", tools.ImportGlider())
        Gui.addCommand("Gl2dExport", tools.Gl2dExport())
        Gui.addCommand("AirfoilMergeCommand", tools.AirfoilMergeCommand())
        Gui.addCommand("BallooningMergeCommand", tools.BallooningMergCommand())
        Gui.addCommand("CellCommand", tools.CellCommand())
        Gui.addCommand("ZrotCommand", tools.ZrotCommand())
        Gui.addCommand("DesignCommand", tools.DesignCommand())

        Gui.addCommand("PatternCommand", tools.PatternCommand())
        Gui.addCommand("PanelCommand", tools.PanelCommand())
        Gui.addCommand("PolarsCommand", tools.PolarsCommand())

        Gui.addCommand("RefreshCommand", tools.RefreshCommand())

        self.appendToolbar("Tools", self.toolBox)
        self.appendToolbar("Production", self.productionBox)
        self.appendToolbar("Develop", self.devBox)
        self.appendMenu("Tools", self.toolBox)
        self.appendMenu("Production", self.productionBox)

        Gui.addPreferencePage(Dir + "/ui/preferences.ui", "Display")

    def Activated(self):
        pass

    def Deactivated(self):
        pass

Gui.addWorkbench(gliderWorkbench())