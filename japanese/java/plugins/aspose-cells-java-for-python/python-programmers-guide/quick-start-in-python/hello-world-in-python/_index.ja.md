---
title: Python でのHello World
type: docs
weight: 10
url: /ja/java/hello-world-in-python/
---

## **Aspose.Cells - Hello World**
Aspose.Cells Javaを使用したPythonでのHello World、単純にDocumentクラスのHelloWorld()メソッドを呼び出し、末尾に追加する第2のドキュメントを指定します。

**Pythonコード**

{{< highlight java >}}

 workbook = self.Workbook()

sheet = workbook.getWorksheets().get(0)

cell = sheet.getCells().get("A1")

cell.setValue("Hello World!")

file_format_type = self.FileFormatType

workbook.save(self.dataDir + "HelloWorld.xls" , file_format_type.EXCEL_97_TO_2003 )

print "Document has been saved, please check the output file.";

{{< /highlight >}}
## **ランニングコードのダウンロード**
以下のソーシャルコーディングサイトから**Hello World (Aspose.Cells)**をダウンロードしてください:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
