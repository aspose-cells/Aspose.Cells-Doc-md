+++
title = "Setting Page Options in Jython" 
description = "" 
weight = 20817 
+++

Aspose.Cells for Java : Setting Page Options in Jython  

# Aspose.Cells for Java : Setting Page Options in Jython


## Aspose.Cells - Setting Page Options

To append documents using **Aspose.Cells Java for Jython**. Here you can see example code.

**Jython Code**

from aspose-cells import Settingsfrom com.aspose.cells import Workbookfrom com.aspose.cells import PageOrientationTypefrom java.io import FileInputStreamclass SettingPageOptions:    def \_\_init\_\_(self):                        self.page\_orientation()        self.scaling()    def page\_orientation(dataDir):                dataDir = Settings.dataDir + 'WorkingWithWorksheets/SettingPageOptions/'        # Instantiating a Workbook object by excel file path        workbook = Workbook()        # Accessing the first worksheet in the Excel file        worksheets = workbook.getWorksheets()        sheet\_index = worksheets.add()        sheet = worksheets.get(sheet\_index)        # Setting the orientation to Portrait        page\_setup = sheet.getPageSetup()        page\_orientation\_type = PageOrientationType        page\_setup.setOrientation(page\_orientation\_type.PORTRAIT)        # Saving the modified Excel file in default (that is Excel 2003) format        workbook.save(dataDir + "Page Orientation.xls")        print "Set page orientation, please check the output file."        def scaling(dataDir):        dataDir = Settings.dataDir + 'WorkingWithWorksheets/SettingPageOptions/'                # Instantiating a Workbook object by excel file path        workbook = Workbook(dataDir + 'Book1.xls')        # Accessing the first worksheet in the Excel file        worksheets = workbook.getWorksheets()        sheet\_index = worksheets.add()        sheet = worksheets.get(sheet\_index)        # Setting the scaling factor to 100        page\_setup = sheet.getPageSetup()        page\_setup.setZoom(100)        # Saving the modified Excel file in default (that is Excel 2003) format        workbook.save(dataDir + "Scaling.xls")        print "Set scaling, please check the output file."if \_\_name\_\_ == '\_\_main\_\_':            SettingPageOptions()

## Download Running Code

Download **Append Documents (Aspose.Cells)** from any of the below mentioned social coding sites:

*   [CodePlex](http://asposecellsjavajython.codeplex.com/SourceControl/latest#asposecells/WorkingWithWorksheets/SettingPageOptions.py)
*   [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose-Cells-Java-for-Jython/asposecells/WorkingWithWorksheets/SettingPageOptions.py)

