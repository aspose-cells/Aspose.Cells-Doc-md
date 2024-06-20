---
title: Pythonでグリッド線を表示または非表示にする
type: docs
weight: 10
url: /ja/java/display-or-hide-gridlines-in-python/
description: Aspose.Cells for Python Via Java APIを介してグリッド線を表示または非表示にする方法を学ぶ
keywords: Python Via Javaでグリッド線を表示または非表示にする方法、Python Via Javaを使用してグリッド線を表示または非表示にする方法、Pythonでグリッド線を表示または非表示にする 
---

## **Aspose.Cells - グリッド線の表示または非表示の方法**
### **グリッド線を非表示にする方法**
**Aspose.Cells Java for Ruby**を使用してワークシートを非表示にするには、**displayhidegridlines**モジュールを呼び出します。

**Pythonコード**

{{< highlight java >}}

 workbook = self.Workbook(self.dataDir + "Book1.xls")

#Accessing the first worksheet in the Excel file

worksheets = workbook.getWorksheets()

worksheet = worksheets.get(0)

#Hiding the grid lines of the first worksheet of the Excel file

worksheet.setGridlinesVisible(False)

#Saving the modified Excel file in default (that is Excel 2000) format

workbook.save(self.dataDir + "output.xls")

\# Print message

print "Grid lines are now hidden on sheet 1, please check the output document."

{{< /highlight >}}
### **グリッド線の表示方法**
グリッド線を表示するには、WorksheetクラスのsetGridlinesVisible(true)メソッドを使用します。

**Pythonコード**

{{< highlight python >}}

 # Displaying the gridlines of the worksheet

worksheet.setGridlinesVisible(True)

{{< /highlight >}}
## **ランニングコードのダウンロード**
以下のいずれかのソーシャルコーディングサイトから**DisplayHideGridlines (Aspose.Cells)**をダウンロード:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
