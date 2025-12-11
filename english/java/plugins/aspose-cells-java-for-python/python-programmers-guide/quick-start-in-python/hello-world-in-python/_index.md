---
title: Hello World in Python
type: docs
weight: 10
url: /java/hello-world-in-python/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Aspose.Cells - Hello World**
Hello World using Aspose.Cells for Java in Python. Simply invoke the HelloWorld() method of the Document class and specify the second document to append at the end.

**Python Code**

{{< highlight java >}}

 workbook = self.Workbook()

sheet = workbook.getWorksheets().get(0)

cell = sheet.getCells().get("A1")

cell.setValue("Hello World!")

file_format_type = self.FileFormatType

workbook.save(self.dataDir + "HelloWorld.xls" , file_format_type.EXCEL_97_TO_2003 )

print "Document has been saved, please check the output file.";

{{< /highlight >}}

## **Download Running Code**
Download **Hello World (Aspose.Cells)** from any of the below‑mentioned social coding sites:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
