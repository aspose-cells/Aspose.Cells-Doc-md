---
title: 改ページプレビュー in Python
type: docs
weight: 60
url: /ja/java/page-break-preview-in-python/
---
## **Aspose.Cells - Hello World**
を使用してワークシートを改ページプレビューに設定するには**Aspose.Cells Java for Python**、単に呼び出す**改ページプレビュー**モジュール。

**Python コード**

{{< highlight "java" >}}

 workbook = self.Workbook(self.dataDir + "Book1.xls")

# Adding a new worksheet to the Workbook object

worksheets = workbook.getWorksheets()

worksheet = worksheets.get(0)

# Displaying the worksheet in page break preview

worksheet.setPageBreakPreview(True)

# Saving the modified Excel file in default format

workbook.save(self.dataDir + "output.xls")

\# Print message

print "Page break preview is enabled for sheet 1, please check the output document." 

{{< /highlight >}}
## **実行中のコードをダウンロード**
ダウンロード**改ページプレビュー (Aspose.Cells)**以下のソーシャルコーディングサイトのいずれかから：

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
