---
title: Python でグリッド線を表示または非表示にする
type: docs
weight: 10
url: /ja/java/display-or-hide-gridlines-in-python/
---
## **Aspose.Cells - 表示非表示グリッド線**
### **グリッド線を非表示にする**
を使用してワークシートを非表示にするには**Aspose.Cells Ruby の場合は Java**、 電話**表示非表示グリッド線**モジュール。

**Python コード**

{{< highlight "java" >}}

 workbook = self.Workbook(self.dataDir + "Book1.xls")

# Accessing the first worksheet in the Excel file

worksheets = workbook.getWorksheets()

worksheet = worksheets.get(0)

# Hiding the grid lines of the first worksheet of the Excel file

worksheet.setGridlinesVisible(False)

# Saving the modified Excel file in default (that is Excel 2000) format

workbook.save(self.dataDir + "output.xls")

\# Print message

print "Grid lines are now hidden on sheet 1, please check the output document."

{{< /highlight >}}
### **グリッド線を表示する**
グリッド線を表示するには、Worksheet クラスの setGridlinesVisible(true) メソッドを使用します。

**Python コード**

{{< highlight "python" >}}

 # Displaying the gridlines of the worksheet

worksheet.setGridlinesVisible(True)

{{< /highlight >}}
## **実行中のコードをダウンロード**
ダウンロード**DisplayHideGridlines (Aspose.Cells)**以下のソーシャルコーディングサイトのいずれかから：

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
