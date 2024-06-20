---
title: Pythonで行と列をグループ化およびグループ解除する
type: docs
weight: 40
url: /ja/java/grouping-and-ungrouping-rows-and-columns-in-python/
description: Aspose.Cells for Python Via Java APIを使用してPythonで行と列をグループ化およびグループ解除する方法を学びます。
keywords: Python Via Javaを使用して行と列をグループ化およびグループ解除する方法、Python Via Javaを使用して行と列をグループ化する方法、Python Via Javaを使用して行と列をグループ解除する方法。 
---

## **Aspose.Cells for Python via Javaにおける行と列のグループ化およびグループ解除の管理**
### **Pythonで行と列をグループ化する方法**
CellsコレクションのgroupRowsおよびgroupColumnsメソッドを呼び出すことで、行または列をグループ化することが可能です。両方のメソッドには、次のパラメーターがあります：

- 最初の行/列インデックス、グループ内の最初の行または列
 - グループ内の最後の行/列のインデックス、最後の行または列。
- 非表示かどうか、グループ化後に行または列を非表示にするかどうかを指定するブールパラメータ。

**Pythonコード**

{{< highlight python >}}

 def group_rows_columns(self):

\# Instantiating a Workbook object by excel file path

workbook = self.Workbook(self.dataDir + 'Book1.xls')

\# Accessing the first worksheet in the Excel file

worksheet = workbook.getWorksheets().get(0)

cells = worksheet.getCells()

\# Grouping first six rows (from 0 to 5) and making them hidden by passing true

cells.groupRows(0,5,True)

\# Grouping first three columns (from 0 to 2) and making them hidden by passing true

cells.groupColumns(0,2,True)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Group Rows And Columns.xls")

print "Group Rows And Columns Successfully." 

{{< /highlight >}}
### **Pythonを使用して行および列をグループ解除する方法**
UngroupRowsとUngroupColumnsメソッドを使用して、Cellsコレクションのグループ化された行や列を解除できます。両方のメソッドには、次のパラメーターがあります：

- 最初の行または列のインデックス、グループ化を解除する最初の行/列。
- 最後の行または列のインデックス、グループ化を解除する最後の行/列。

**Pythonコード**

{{< highlight python >}}

 def ungroup_rows_columns(self):

\# Instantiating a Workbook object by excel file path

workbook = self.Workbook(self.dataDir + 'Group Rows And Columns.xls')

\# Accessing the first worksheet in the Excel file

worksheet = workbook.getWorksheets().get(0)

cells = worksheet.getCells()

\# Ungrouping first six rows (from 0 to 5)

cells.ungroupRows(0,5)

\# Ungrouping first three columns (from 0 to 2)

cells.ungroupColumns(0,2)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Ungroup Rows And Columns.xls")

print "Ungroup Rows And Columns Successfully." 

{{< /highlight >}}
## **ランニングコードのダウンロード**
以下のいずれかのソーシャルコーディングサイトから**グループとアングループの行と列（Aspose.Cells）**をダウンロードしてください。

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
