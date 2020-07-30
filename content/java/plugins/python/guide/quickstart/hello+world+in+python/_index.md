---
title : "Hello World in Python" 
description : "" 
weight : 20744 
toc : false
type: docs
url: /java/plugins/python/guide/quickstart/hello+world+in+python/
---

# Aspose.Cells for Java : Hello World in Python


## Aspose.Cells - Hello World

Hello World using Aspose.Cells Java in Python, simply invoke the HelloWorld() method of Document class and specify the second document to append at end.

**Python Code**

workbook = self.Workbook()sheet = workbook.getWorksheets().get(0)cell = sheet.getCells().get("A1")cell.setValue("Hello World!")file\_format\_type = self.FileFormatTypeworkbook.save(self.dataDir + "HelloWorld.xls" , file\_format\_type.EXCEL\_97\_TO\_2003 )print "Document has been saved, please check the output file.";

## Download Running Code

Download **Hello World (Aspose.Cells)** from any of the below mentioned social coding sites:

*   [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
*   [CodePlex](https://asposecellsjavapython.codeplex.com/releases/view/620185)

