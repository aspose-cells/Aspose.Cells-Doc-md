---
title: Python の行と列のグループ化とグループ解除
type: docs
weight: 40
url: /ja/java/grouping-and-ungrouping-rows-and-columns-in-python/
description: Aspose.Cells for Python Via Java API を通じて行と列をグループ化およびグループ解除する方法を学びます。
keywords: How to Group and Ungroup Rows and Columns in Python Via Java, Group Rows and Columns using Python Via Java, Python Via Java Ungroup Rows and Columns. 
---
##  **Aspose.Cells for Python via Java の行と列のグループ化およびグループ化解除の管理**
###  **Python で行と列をグループ化する方法**
Cells コレクションの groupRows メソッドと groupColumns メソッドを呼び出すことで、行または列をグループ化することができます。どちらのメソッドも次のパラメータを受け取ります。

- 最初の行/列インデックス、グループ内の最初の行または列。
- 最後の行/列のインデックス、グループ内の最後の行または列。
- hidden は、グループ化後に行/列を非表示にするかどうかを指定するブール型パラメーターです。

**Python コード**

{{< highlight "python" >}}

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
###  **Python を使用して行と列のグループを解除する方法**
Cells コレクションの UngroupRows メソッドおよび UngroupColumns メソッドを呼び出して、グループ化された行または列のグループ化を解除します。どちらのメソッドも同じパラメータを受け取ります。

- 最初の行または列のインデックス、グループ化を解除する最初の行/列。
- 最後の行または列のインデックス、グループ化を解除する最後の行/列。

**Python コード**

{{< highlight "python" >}}

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
##  **実行コードをダウンロード**
ダウンロード**行と列のグループ化とグループ解除 (Aspose.Cells)**以下のソーシャル コーディング サイトのいずれかから:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
