---
title: Pythonにおける行の高さと列の幅の調整
type: docs
weight: 10
url: /ja/java/adjusting-row-height-and-column-width-in-python/
keywords: PythonでXLSXを作成、PythonでXLSを作成、XLS python、XLSX python、行の高さ python、列の幅 python、Excel pythonの作成
description: PythonでExcelファイルを作成するためにPython Excel APIを使用します。MS Officeを使用せずに、PythonアプリケーションでXLSXまたはXLSの行の高さと列の幅を調整します。
---

## **PythonでExcelスプレッドシート - 行の高さと列の幅を調整**
### **行の高さの設定**
Aspose.Cellsを使用すると、CellsコレクションのsetRowHeightメソッドを呼び出すことで、Pythonで単一の行の高さを設定できます。setRowHeightメソッドには以下のパラメータが必要です。

- **行インデックス**：高さを変更する行のインデックス。
- **行の高さ**：行に適用する行の高さ。

**Pythonコード**

{{< highlight python >}}

 def set_row_height(self):

\# Instantiating a Workbook object by excel file path

workbook = self.Workbook(self.self.dataDir + 'Book1.xls')

\# Accessing the first worksheet in the Excel file

worksheet = workbook.getWorksheets().get(0)

cells = worksheet.getCells()

\# Setting the height of the second row to 13

cells.setRowHeight(1, 13)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Set Row Height.xls")

print "Set Row Height Successfully." 

{{< /highlight >}}
### **列の幅の設定**
Cells 集合の setColumnWidth メソッドを呼び出すことで、列の幅を設定することが可能です。 setColumnWidth メソッドは、以下のパラメータを取ります。

- **列インデックス**：幅を変更する列のインデックス。
- **列の幅**：設定したい列の幅。

**Pythonコード**

{{< highlight python >}}

 def set_column_width(self):

\# Instantiating a Workbook object by excel file path

workbook = self.Workbook(self.dataDir + 'Book1.xls')

\# Accessing the first worksheet in the Excel file

worksheet = workbook.getWorksheets().get(0)

cells = worksheet.getCells()

\# Setting the width of the second column to 17.5

cells.setColumnWidth(1, 17.5)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Set Column Width.xls")

print "Set Column Width Successfully." 

{{< /highlight >}}
## **ランニングコードのダウンロード**
以下のソーシャルコーディングサイトから、**Adjusting Row Height and Column Width (Aspose.Cells)** をダウンロードしてください：

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
