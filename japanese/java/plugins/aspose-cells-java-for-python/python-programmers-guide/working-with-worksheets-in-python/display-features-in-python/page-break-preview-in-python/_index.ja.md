---
title: Pythonでページ区切りプレビュー
type: docs
weight: 60
url: /ja/java/page-break-preview-in-python/
---

## **Aspose.Cells - Hello World**
**Aspose.Cells Java for Python**を使用してワークシートをページ区切りプレビューに設定するには、**PageBreakPreview**モジュールを呼び出すだけです。

**Pythonコード**

{{< highlight java >}}

 workbook = self.Workbook(self.dataDir + "Book1.xls")

#Adding a new worksheet to the Workbook object

worksheets = workbook.getWorksheets()

worksheet = worksheets.get(0)

#Displaying the worksheet in page break preview

worksheet.setPageBreakPreview(True)

#Saving the modified Excel file in default format

workbook.save(self.dataDir + "output.xls")

\# Print message

print "Page break preview is enabled for sheet 1, please check the output document." 

{{< /highlight >}}
## **ランニングコードのダウンロード**
以下のソーシャルコーディングサイトから**Page Break Preview (Aspose.Cells)**をダウンロードしてください:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
