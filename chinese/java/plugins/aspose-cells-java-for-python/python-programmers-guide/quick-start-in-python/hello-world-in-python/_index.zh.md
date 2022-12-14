---
title: Hello World 在 Python
type: docs
weight: 10
url: /zh/java/hello-world-in-python/
---
## **Aspose.Cells - Hello World**
Hello World 在 Python 中使用 Aspose.Cells Java，只需调用 Document 类的 HelloWorld() 方法并指定要在末尾追加的第二个文档。

**Python 代码**

{{< highlight "java" >}}

 workbook = self.Workbook()

sheet = workbook.getWorksheets().get(0)

cell = sheet.getCells().get("A1")

cell.setValue("Hello World!")

file_format_type = self.FileFormatType

workbook.save(self.dataDir + "HelloWorld.xls" , file_format_type.EXCEL_97_TO_2003 )

print "Document has been saved, please check the output file.";

{{< /highlight >}}
## **下载运行代码**
下载**Hello World (Aspose.Cells)**来自以下任何社交编码网站：

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
