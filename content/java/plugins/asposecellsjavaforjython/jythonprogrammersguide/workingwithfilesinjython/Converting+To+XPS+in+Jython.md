+++
title = "Converting To XPS in Jython" 
description = "" 
weight = 20790 
+++

Aspose.Cells for Java : Converting To XPS in Jython  

# Aspose.Cells for Java : Converting To XPS in Jython


## Aspose.Cells - Converting To XPS

To append documents using **Aspose.Cells Java for Jython**. Here you can see example code.

**Jython Code**

from aspose-cells import Settingsfrom com.aspose.cells import Workbookfrom com.aspose.cells import ImageFormat;from com.aspose.cells import ImageOrPrintOptions;from com.aspose.cells import SheetRender;from com.aspose.cells import SaveFormat;class ConvertingToXPS:    def \_\_init\_\_(self):        dataDir = Settings.dataDir + 'WorkingWithFiles/ConvertingToXPS/'                saveFormat = SaveFormat        workbook = Workbook(dataDir + "Book1.xls")        #Get the first worksheet.        sheet = workbook.getWorksheets().get(0)        #Apply different Image and Print options        options = ImageOrPrintOptions()        #Set the Format        options.setSaveFormat(saveFormat.XPS)        # Render the sheet with respect to specified printing options        sr = SheetRender(sheet, options)        sr.toImage(0, dataDir + "out\_printingxps.xps")        #Save the complete Workbook in XPS format        workbook.save(dataDir + "out\_whole\_printingxps", saveFormat.XPS)        # Print message        print "Excel to XPS conversion performed successfully." if \_\_name\_\_ == '\_\_main\_\_':            ConvertingToXPS()

## Download Running Code

Download **Append Documents (Aspose.Cells)** from any of the below mentioned social coding sites:

*   [CodePlex](http://asposecellsjavajython.codeplex.com/SourceControl/latest#asposecells/WorkingWithFiles/ConvertingToXPS.py)
*   [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose-Cells-Java-for-Jython/asposecells/WorkingWithFiles/ConvertingToXPS.py)

