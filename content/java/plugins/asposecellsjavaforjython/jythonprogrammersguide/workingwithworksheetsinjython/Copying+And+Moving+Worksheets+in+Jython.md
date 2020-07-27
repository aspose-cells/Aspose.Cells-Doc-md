+++
title = "Copying And Moving Worksheets in Jython" 
description = "" 
weight = 20806 
+++

Aspose.Cells for Java : Copying And Moving Worksheets in Jython  

# Aspose.Cells for Java : Copying And Moving Worksheets in Jython


## Aspose.Cells - Copying And Moving Worksheets

To append documents using **Aspose.Cells Java for Jython**. Here you can see example code.

**Jython Code**

from aspose-cells import Settingsfrom com.aspose.cells import Workbookfrom com.aspose.cells import SaveFormatclass CopyingAndMovingWorksheets:    def \_\_init\_\_(self):        # Copy Worksheets within a Workbook        self.copy\_worksheet()        # Move Worksheets within Workbook        self.move\_worksheet()            def copy\_worksheet(dataDir):                  dataDir = Settings.dataDir + 'WorkingWithWorksheets/CopyingAndMovingWorksheets/'                 # Instantiating a Workbook object by excel file path        workbook = Workbook(dataDir + "Book1.xls")                # Create a Worksheets object with reference to the sheets of the Workbook.        sheets = workbook.getWorksheets()        # Copy data to a new sheet from an existing sheet within the Workbook.        sheets.addCopy("Sheet1")        # Saving the modified Excel file in default (that is Excel 2003) format        workbook.save(dataDir + "Copy Worksheet.xls")        print "Copy worksheet, please check the output file."        def move\_worksheet(dataDir):                dataDir = Settings.dataDir + 'WorkingWithWorksheets/CopyingAndMovingWorksheets/'                 # Instantiating a Workbook object by excel file path        workbook = Workbook(dataDir + "Book1.xls")            # Get the first worksheet in the book.        sheet = workbook.getWorksheets().get(0)        # Move the first sheet to the third position in the workbook.        sheet.moveTo(2)        # Saving the modified Excel file in default (that is Excel 2003) format        workbook.save(dataDir + "Move Worksheet.xls")        print "Move worksheet, please check the output file."    if \_\_name\_\_ == '\_\_main\_\_':            CopyingAndMovingWorksheets()

## Download Running Code

Download **Append Documents (Aspose.Cells)** from any of the below mentioned social coding sites:

*   [CodePlex](http://asposecellsjavajython.codeplex.com/SourceControl/latest#asposecells/WorkingWithWorksheets/CopyingAndMovingWorksheets.py)
*   [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose-Cells-Java-for-Jython/asposecells/WorkingWithWorksheets/CopyingAndMovingWorksheets.py)

