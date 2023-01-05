---
title: Python のワークシートの保護を解除する
type: docs
weight: 20
url: /ja/java/unprotect-a-worksheet-in-python/
---
## **Aspose.Cells - ワークシートの保護を解除する**
を使用してワークシートを保護するには**Aspose.Cells Java for Python**、 電話**unprotect_worksheet**方法**保護**モジュール。

**Python コード**

{{< highlight "java" >}}

 filesFormatType = self.FileFormatType

# Instantiating a Workbook object

workbook = self.Workbook(self.dataDir + "Book1.xls")

worksheets = workbook.getWorksheets()

worksheet = worksheets.get(0)

protection = worksheet.getProtection()

# The following 3 methods are only for Excel 2000 and earlier formats

protection.setAllowEditingContent(False)

protection.setAllowEditingObject(False)

protection.setAllowEditingScenario(False)

# Unprotecting the worksheet

worksheet.unprotect()

\# Save the excel file.

workbook.save(self.dataDir + "output.xls", filesFormatType.EXCEL_97_TO_2003)

# Print Message

print "Worksheet unprotected successfully."

{{< /highlight >}}
## **実行中のコードをダウンロード**
ダウンロード**ワークシートの保護を解除する (Aspose.Cells)**以下のソーシャルコーディングサイトのいずれかから：

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
