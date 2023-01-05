---
title: Python でワークシートを非表示または再表示する
type: docs
weight: 50
url: /ja/java/hide-or-unhide-a-worksheet-in-python/
---
## **Aspose.Cells - ワークシートを非表示または再表示する**
### **ワークシートを非表示にする**
Ruby で Aspose.Cells Java を使用してワークシートを非表示にするには、次のように呼び出します。**hideunhideワークシート**モジュール。

**Python コード**

{{< highlight "java" >}}

 workbook = self.Workbook(self.dataDir + "Book1.xls")

# Accessing the first worksheet in the Excel file

worksheets = workbook.getWorksheets()

worksheet = worksheets.get(0)

# Hiding the first worksheet of the Excel file

worksheet.setVisible(True)

# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "output.xls")

\# Print message

print "Worksheet 1 is now hidden, please check the output document."

{{< /highlight >}}
### **ワークシートの表示**
開発者は、*setVisible(* *真実* *)*の方法**ワークシート**クラス。

**Python コード**

{{< highlight "python" >}}

 # Displaying the worksheet of the Excel file

worksheet.setVisible(true)

{{< /highlight >}}
## **実行中のコードをダウンロード**
ダウンロード**ワークシートを非表示または再表示する (Aspose.Cells)**以下のソーシャルコーディングサイトのいずれかから：

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
