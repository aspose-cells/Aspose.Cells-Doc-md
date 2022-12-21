---
title: Python で Excel ファイルを HTML に変換する
type: docs
weight: 10
url: /ja/java/converting-excel-files-to-html-in-python/
---
## **Aspose.Cells - Excel ファイルを HTML に変換する**
Python の Aspose.Cells for Java を使用して Excel を HTML に変換するには、単にワークシートを呼び出します。_に_Converter モジュールの html() メソッド。

**Python コード**

{{< highlight "python" >}}

 saveFormat = self.SaveFormat

workbook = self.Workbook(self.dataDir + "Book1.xls")

# Save the document in PDF format

workbook.save(self.dataDir + "OutBook1.html", saveFormat.HTML)

\# Print message

print "\n Excel to HTML conversion performed successfully."


{{< /highlight >}}
## **実行中のコードをダウンロード**
ダウンロード**Excel ファイルを HTML に変換中 (Aspose.Cells)**以下のソーシャルコーディングサイトのいずれかから：

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
