---
title : "Converting ExcelFiles To Html in Jython" 
description : "" 
weight : 20788 
toc : false
type: docs
url: /java/plugins/jython/guide/files/converting+excelfiles+to+html+in+jython/
---

# Aspose.Cells for Java : Converting ExcelFiles To Html in Jython


## Aspose.Cells - Converting ExcelFiles To Html

To append documents using **Aspose.Cells Java for Jython**. Here you can see example code.

**Jython Code**

from aspose-cells import Settingsfrom com.aspose.cells import Workbookfrom com.aspose.cells import SaveFormatclass ConvertingExcelFilesToHtml:    def \_\_init\_\_(self):        dataDir = Settings.dataDir + 'WorkingWithFiles/ConvertingExcelFilesToHtml/'                saveFormat = SaveFormat        workbook = Workbook(dataDir + "Book1.xls")        #Save the document in PDF format        workbook.save(dataDir + "OutBook1.html", saveFormat.HTML)        # Print message        print "\\n Excel to HTML conversion performed successfully." if \_\_name\_\_ == '\_\_main\_\_':            ConvertingExcelFilesToHtml()

## Download Running Code

Download **Append Documents (Aspose.Cells)** from any of the below mentioned social coding sites:

*   [CodePlex](http://asposecellsjavajython.codeplex.com/SourceControl/latest#asposecells/WorkingWithFiles/ConvertingExcelFilesToHtml.py)
*   [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose-Cells-Java-for-Jython/asposecells/WorkingWithFiles/ConvertingExcelFilesToHtml.py)

