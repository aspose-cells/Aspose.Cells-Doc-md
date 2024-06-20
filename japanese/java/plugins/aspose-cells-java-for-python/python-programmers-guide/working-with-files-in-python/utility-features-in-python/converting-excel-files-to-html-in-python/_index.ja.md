---
title: PythonでのExcelファイルをHTMLに変換
type: docs
weight: 10
url: /ja/java/converting-excel-files-to-html-in-python/
---

## **Aspose.Cells - ExcelファイルをHTMLに変換**
PythonでAspose.Cells for Javaを使用してExcelをHTMLに変換するには、Converterモジュールのworksheet_to_html()メソッドを単純に呼び出します。

**Pythonコード**

{{< highlight python >}}

 saveFormat = self.SaveFormat

workbook = self.Workbook(self.dataDir + "Book1.xls")

#Save the document in PDF format

workbook.save(self.dataDir + "OutBook1.html", saveFormat.HTML)

\# Print message

print "\n Excel to HTML conversion performed successfully."


{{< /highlight >}}
## **ランニングコードのダウンロード**
以下のいずれかのソーシャルコーディングサイトから、**Aspose.Cells**の**ExcelファイルをHTMLに変換**をダウンロードしてください:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
