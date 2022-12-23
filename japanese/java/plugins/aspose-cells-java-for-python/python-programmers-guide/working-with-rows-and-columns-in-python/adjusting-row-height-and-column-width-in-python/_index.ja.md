---
title: Python で行の高さと列の幅を調整する
type: docs
weight: 10
url: /ja/java/adjusting-row-height-and-column-width-in-python/
keywords: create XLSX in Python, create XLS in Python, XLS python, XLSX python, row height python, column width python, Excel pytho
description: Python Excel API を使用して、Python で Excel ファイルを作成します。MS Office を使用しない Python アプリケーションでは、XLSX または XLS で行の高さと列の幅を調整します。
---
## **Python の Excel スプレッドシート - 行の高さと列の幅の調整**
### **行の高さの設定**
Aspose.Cells では、Cells コレクションの setRowHeight メソッドを呼び出すことで、Python の 1 つの行の高さを設定できます。 setRowHeight メソッドは、次のパラメーターを取ります。

- **行インデックス**、高さを変更する行のインデックス。
- **行の高さ**、行に適用する行の高さ。

**Python コード**

{{< highlight "python" >}}

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
### **列幅の設定**
Cells コレクションの setColumnWidth メソッドを呼び出して、列の幅を設定します。 setColumnWidth メソッドは、次のパラメーターを取ります。

- **列インデックス**、幅を変更する列のインデックス。
- **列幅**、目的の列幅。

**Python コード**

{{< highlight "python" >}}

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
## **実行中のコードをダウンロード**
ダウンロード**行の高さと列の幅を調整する (Aspose.Cells)**以下のソーシャルコーディングサイトのいずれかから：

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
