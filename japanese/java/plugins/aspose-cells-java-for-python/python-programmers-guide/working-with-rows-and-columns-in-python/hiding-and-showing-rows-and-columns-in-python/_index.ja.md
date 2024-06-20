---
title: Pythonで行と列を非表示および表示する方法
type: docs
weight: 50
url: /ja/java/hiding-and-showing-rows-and-columns-in-python/
description: Aspose.Cells for Python Via Java APIを使用してPythonで行と列を非表示および表示する方法を学びます。
keywords: Python Via Javaを使用して行と列を非表示および表示する方法、Python Via Javaを使用して行を非表示および表示する方法、Python Via Javaを使用して列を非表示および表示する方法。 
---

## **Aspose.Cells - 行と列の表示/非表示を制御**
### **行や列の非表示方法**
開発者はCellsコレクションのHideRowおよびHideColumnメソッドを呼び出すことで、特定の行または列を非表示にできます。両方のメソッドは、非表示にする特定の行または列のインデックスをパラメータとして取ります。

**Ruby Code**

{{< highlight ruby >}}

 def hide_rows_columns(self):

\# Instantiating a Workbook object by excel file path

workbook = self.Workbook(self.dataDir + 'Book1.xls')

\# Accessing the first worksheet in the Excel file

worksheet = workbook.getWorksheets().get(0)

cells = worksheet.getCells()

\# Hiding the 3rd row of the worksheet

cells.hideRow(2)

\# Hiding the 2nd column of the worksheet

cells.hideColumn(1)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Hide Rows And Columns.xls")

print "Hide Rows And Columns Successfully." 

{{< /highlight >}}
### **行や列の表示方法**
開発者は、CellsコレクションのUnhideRowおよびUnhideColumnメソッドを呼び出すことで、非表示になっている行または列を元に戻すことができます。両方のメソッドは2つのパラメータを取ります:

- **行または列のインデックス** - 特定の行または列を表示するために使用される行または列のインデックス。
- **行の高さまたは列の幅** - 行または列が表示された後に割り当てられた行の高さまたは列の幅。

**Ruby Code**

{{< highlight ruby >}}

 def unhide_rows_columns(self):

\# Instantiating a Workbook object by excel file path

workbook = self.Workbook(self.dataDir + 'Book1.xls')

\# Accessing the first worksheet in the Excel file

worksheet = workbook.getWorksheets().get(0)

cells = worksheet.getCells()

\# Unhiding the 3rd row and setting its height to 13.5

cells.unhideRow(2,13.5)

\# Unhiding the 2nd column and setting its width to 8.5

cells.unhideColumn(1,8.5)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Unhide Rows And Columns.xls")

print "Unhide Rows And Columns Successfully." 

{{< /highlight >}}
## **ランニングコードのダウンロード**
以下のいずれかのソーシャルコーディングサイトから**行と列の表示/非表示を制御（Aspose.Cells）**をダウンロードしてください。

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
