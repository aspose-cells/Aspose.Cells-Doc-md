---
title: Python で Excel ファイルを PDF に変換する
type: docs
weight: 20
url: /ja/java/converting-excel-to-pdf-files-in-python/
---

## **Aspose.Cells - Excel を PDF に変換する**
PythonでAspose.Cells for Javaを使用してExcelをPDFファイルに変換するには、Converterモジュールのexcel_to_pdf()メソッドを単純に呼び出します。

**Pythonコード**

{{< highlight python >}}

 saveFormat = self.SaveFormat

workbook = self.Workbook(self.dataDir + "Book1.xls")

#Save the document in PDF format

workbook.save(self.dataDir + "OutBook1.pdf", saveFormat.PDF)

\# Print message

print "\n Excel to PDF conversion performed successfully."

{{< /highlight >}}
## **ランニングコードのダウンロード**
以下のいずれかのソーシャルコーディングサイトから、**Excel を PDF に変換する (Aspose.Cells)** をダウンロードしてください:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
