---
title : "Download and Configure Aspose.Cells in Jython" 
description : "" 
weight : 12783 
toc : false
type: docs
url: /java/plugins/jython/download+and+configure+aspose.cells+in+jython/
---

# Aspose.Cells for Java : Download and Configure Aspose.Cells in Jython


### Downloading

**Download Examples from social coding websites**

Following releases of running examples are available to download on all of the below mentioned social coding sites:

*   [CodePlex](http://asposecellsjavajython.codeplex.com/)
*   [Github](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose-Cells-Java-for-Jython)

**Download Aspose.Cells for Java component**

*   [Aspose.Cells for Java](http://www.aspose.com/community/files/72/java-components/aspose.cells-for-java/default.aspx)

### Installing

*   Place downloaded Aspose.Cells for Java jar file into "lib" directory.
*   Replace "your-lib" with the downloaded jar filename in \_*init*\_.py file.

### Using

You can create HelloWorld document using following example code:

from aspose-cells  import Settingsfrom com.aspose.Cells import Documentfrom com.aspose.Cells import DocumentBuilderclass HelloWorld:    def \_\_init\_\_(self):        dataDir = Settings.dataDir + 'quickstart/'                workbook = Workbook()                sheet = workbook.getWorksheets().get(0)                cell = sheet.getCells().get("A1")                cell.setValue("Hello World!")                file\_format\_type = FileFormatType                workbook.save(dataDir + "HelloWorld.xls" , file\_format\_type.EXCEL\_97\_TO\_2003 )                print "Document has been saved, please check the output file.";if \_\_name\_\_ == '\_\_main\_\_':    HelloWorld()

