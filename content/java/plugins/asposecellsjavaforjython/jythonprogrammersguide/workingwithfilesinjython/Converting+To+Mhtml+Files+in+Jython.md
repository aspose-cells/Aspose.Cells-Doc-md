+++
title = "Converting To Mhtml Files in Jython" 
description = "" 
weight = 20789 
+++

Aspose.Cells for Java : Converting To Mhtml Files in Jython  

# Aspose.Cells for Java : Converting To Mhtml Files in Jython


## Aspose.Cells - Converting To Mhtml Files

To append documents using **Aspose.Cells Java for Jython**. Here you can see example code.

**Jython Code**

from aspose-cells import Settingsfrom com.aspose.cells import Workbookfrom com.aspose.cells import HtmlSaveOptionsfrom com.aspose.cells import SaveFormatclass ConvertingToMhtmlFiles:    def \_\_init\_\_(self):        dataDir = Settings.dataDir + 'WorkingWithFiles/ConvertingToMhtmlFiles/'                saveFormat = SaveFormat        #Specify the file path        filePath = dataDir + "Book1.xlsx"        #Specify the HTML saving options        sv = HtmlSaveOptions(saveFormat.M\_HTML)        #Instantiate a workbook and open the template XLSX file        wb = Workbook(filePath)        #Save the MHT file        wb.save(filePath + ".out.mht", sv)        # Print message        print "Excel to MHTML conversion performed successfully." if \_\_name\_\_ == '\_\_main\_\_':            ConvertingToMhtmlFiles()

## Download Running Code

Download **Append Documents (Aspose.Cells)** from any of the below mentioned social coding sites:

*   [CodePlex](http://asposecellsjavajython.codeplex.com/SourceControl/latest#asposecells/WorkingWithFiles/ConvertingToMhtmlFiles.py)
*   [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose-Cells-Java-for-Jython/asposecells/WorkingWithFiles/ConvertingToMhtmlFiles.py)

