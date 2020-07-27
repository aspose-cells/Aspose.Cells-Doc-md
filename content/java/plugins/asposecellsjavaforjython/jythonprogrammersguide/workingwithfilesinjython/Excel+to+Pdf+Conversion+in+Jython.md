+++
title = "Excel to Pdf Conversion in Jython" 
description = "" 
weight = 20792 
+++

Aspose.Cells for Java : Excel to Pdf Conversion in Jython  

# Aspose.Cells for Java : Excel to Pdf Conversion in Jython


## Aspose.Cells - Excel to Pdf Conversion

To append documents using **Aspose.Cells Java for Jython**. Here you can see example code.

**Jython Code**

from aspose-cells import Settingsfrom com.aspose.cells import Workbookfrom com.aspose.cells import SaveFormatclass Excel2PdfConversion:    def \_\_init\_\_(self):        dataDir = Settings.dataDir + 'WorkingWithFiles/Excel2PdfConversion/'                saveFormat = SaveFormat        workbook = Workbook(dataDir + "Book1.xls")        #Save the document in PDF format        workbook.save(dataDir + "OutBook1.pdf", saveFormat.PDF)        # Print message        print "\\n Excel to PDF conversion performed successfully." if \_\_name\_\_ == '\_\_main\_\_':            Excel2PdfConversion()

## Download Running Code

Download **Append Documents (Aspose.Cells)** from any of the below mentioned social coding sites:

*   [CodePlex](http://asposecellsjavajython.codeplex.com/SourceControl/latest#asposecells/WorkingWithFiles/Excel2PdfConversion.py)
*   [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose-Cells-Java-for-Jython/asposecells/WorkingWithFiles/Excel2PdfConversion.py)

