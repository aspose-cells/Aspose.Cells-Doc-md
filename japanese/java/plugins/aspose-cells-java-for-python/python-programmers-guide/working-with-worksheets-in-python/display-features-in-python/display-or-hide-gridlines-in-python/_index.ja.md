---
title: Python のグリッド線の表示または非表示
type: docs
weight: 10
url: /ja/java/display-or-hide-gridlines-in-python/
description: Aspose.Cells for Python Via Java API を通じてグリッド線を表示または非表示にする方法について説明します。
keywords: How to Display or Hide Gridlines in Python Via Java, Display or Hide Gridlines using Python Via Java, Python Show or Hide Gridlines. 
---
##  **Aspose.Cells - グリッド線を表示または非表示にする方法**
###  **グリッド線を非表示にする方法**
を使用してワークシートを非表示にするには**Aspose.Cells Java (Ruby** の場合)、**displayhidegridlines を呼び出します**モジュール。

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
###  **グリッド線を表示する方法**
グリッド線を表示するには、Worksheet クラスの setGridlinesVisible(true) メソッドを使用します。

**Python コード**

{{< highlight "python" >}}

 # Displaying the gridlines of the worksheet

worksheet.setGridlinesVisible(True)

{{< /highlight >}}
##  **実行コードをダウンロード**
ダウンロード**グリッド線を表示しない (Aspose.Cells)**以下のソーシャル コーディング サイトのいずれかから:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
