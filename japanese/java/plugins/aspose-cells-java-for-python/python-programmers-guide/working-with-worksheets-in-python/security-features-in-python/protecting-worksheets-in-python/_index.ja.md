---
title: Python でのワークシートの保護
type: docs
weight: 10
url: /ja/java/protecting-worksheets-in-python/
---
## **Aspose.Cells - ワークシートの保護**
を使用してワークシートを保護するには**Aspose.Cells Java for Python**、 電話**保護ワークシート**方法**保護**モジュール。

**Python コード**

{{< highlight "java" >}}

 #Instantiating a Excel object by excel file path

excel = self.Workbook(self.dataDir + "Book1.xls")

# Accessing the first worksheet in the Excel file

worksheets = excel.getWorksheets()

worksheet = worksheets.get(0)

protection = worksheet.getProtection()

# The following 3 methods are only for Excel 2000 and earlier formats

protection.setAllowEditingContent(False)

protection.setAllowEditingObject(False)

protection.setAllowEditingScenario(False)

# Protects the first worksheet with a password "1234"

protection.setPassword("1234")

# Saving the modified Excel file in default format

excel.save(self.dataDir + "output.xls")

# Print Message

print "Sheet protected successfully."

{{< /highlight >}}
## **実行中のコードをダウンロード**
ダウンロード**ワークシートの保護 (Aspose.Cells)**以下のソーシャルコーディングサイトのいずれかから：

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
