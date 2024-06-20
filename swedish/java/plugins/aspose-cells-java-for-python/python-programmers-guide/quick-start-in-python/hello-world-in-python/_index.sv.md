---
title: Hello World i Python
type: docs
weight: 10
url: /sv/java/hello-world-in-python/
---

## **Aspose.Cells - Hello World**
Hello World med Aspose.Cells Java i Python, helt enkelt anropa metoden HelloWorld() från Document-klassen och ange den andra dokumentet att lägga till i slutet.

**Python-kod**

{{< highlight java >}}

 workbook = self.Workbook()

sheet = workbook.getWorksheets().get(0)

cell = sheet.getCells().get("A1")

cell.setValue("Hello World!")

file_format_type = self.FileFormatType

workbook.save(self.dataDir + "HelloWorld.xls" , file_format_type.EXCEL_97_TO_2003 )

print "Document has been saved, please check the output file.";

{{< /highlight >}}
## **Ladda ned körbar kod**
Ladda ner **Hello World (Aspose.Cells)** från någon av nedan nämnda sociala kodningssidor:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
