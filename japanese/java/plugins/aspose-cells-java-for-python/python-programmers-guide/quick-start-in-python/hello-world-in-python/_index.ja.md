---
title: PythonのHello World
type: docs
weight: 10
url: /ja/java/hello-world-in-python/
---
## **Aspose.Cells - Hello World**
Hello World Python で Aspose.Cells Java を使用するには、単純に Document クラスの HelloWorld() メソッドを呼び出し、最後に追加する 2 番目のドキュメントを指定します。

**Python コード**

{{< highlight "java" >}}

 workbook = self.Workbook()

sheet = workbook.getWorksheets().get(0)

cell = sheet.getCells().get("A1")

cell.setValue("Hello World!")

file_format_type = self.FileFormatType

workbook.save(self.dataDir + "HelloWorld.xls" , file_format_type.EXCEL_97_TO_2003 )

print "Document has been saved, please check the output file.";

{{< /highlight >}}
## **実行中のコードをダウンロード**
ダウンロード**Hello World (Aspose.Cells)**以下のソーシャルコーディングサイトのいずれかから：

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
