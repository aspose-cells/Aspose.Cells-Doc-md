---
title: Python で Excel を PDF ファイルに変換する
type: docs
weight: 20
url: /ja/java/converting-excel-to-pdf-files-in-python/
---
## **Aspose.Cells - Excel から Pdf への変換**
Python の Aspose.Cells for Java を使用して Excel を Pdf ファイルに変換するには、単に Excel を呼び出します。_に_Converter モジュールの pdf() メソッド。

**Python コード**

{{< highlight "python" >}}

 saveFormat = self.SaveFormat

workbook = self.Workbook(self.dataDir + "Book1.xls")

# Save the document in PDF format

workbook.save(self.dataDir + "OutBook1.pdf", saveFormat.PDF)

\# Print message

print "\n Excel to PDF conversion performed successfully."

{{< /highlight >}}
## **実行中のコードをダウンロード**
ダウンロード**Excel を PDF に変換する (Aspose.Cells)**以下のソーシャルコーディングサイトのいずれかから：

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
