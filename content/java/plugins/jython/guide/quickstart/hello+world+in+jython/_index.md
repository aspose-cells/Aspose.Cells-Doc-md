---
title : "Hello World in Jython" 
description : "" 
weight : 20786 
toc : false
type: docs
url: /java/plugins/jython/guide/quickstart/hello+world+in+jython/
---

# Aspose.Cells for Java : Hello World in Jython


## Aspose.Cells - Hello World

To append documents using **Aspose.Cells Java for Jython**. Here you can see example code.

**Jython Code**

from asposewords import Settingsfrom com.aspose.Cells import Documentfrom com.aspose.Cells import ImportFormatModeclass HelloWorld:    def \_\_init\_\_(self):        dataDir = Settings.dataDir + 'quickstart/'                workbook = Workbook()                sheet = workbook.getWorksheets().get(0)                cell = sheet.getCells().get("A1")                cell.setValue("Hello World!")                file\_format\_type = FileFormatType                workbook.save(dataDir + "HelloWorld.xls" , file\_format\_type.EXCEL\_97\_TO\_2003 )                print "Document has been saved, please check the output file.";if \_\_name\_\_ == '\_\_main\_\_':            HelloWorld()

## Download Running Code

Download **Append Documents (Aspose.Cells)** from any of the below mentioned social coding sites:

*   [CodePlex](http://asposecellsjavajython.codeplex.com/SourceControl/latest#asposecells/quickstart/HelloWorld.py)
*   [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose-Cells-Java-for-Jython/asposecells/quickstart/HelloWorld.py)

