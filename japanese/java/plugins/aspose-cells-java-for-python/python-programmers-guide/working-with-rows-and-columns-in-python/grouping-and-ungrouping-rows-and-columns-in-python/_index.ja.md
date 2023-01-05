---
title: Python の行と列のグループ化とグループ解除
type: docs
weight: 40
url: /ja/java/grouping-and-ungrouping-rows-and-columns-in-python/
---
## **Aspose.Cells - 行と列のグループ管理**
### **行と列のグループ化**
Cells コレクションの groupRows および groupColumns メソッドを呼び出して、行または列をグループ化することができます。どちらのメソッドも、次のパラメーターを取ります。

- 最初の行/列インデックス、グループ内の最初の行または列。
- 最後の行/列インデックス、グループ内の最後の行または列。
- グループ化後に行/列を非表示にするかどうかを指定するブール値パラメーターです。

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
### **行と列のグループ解除**
Cells コレクションの UngroupRows メソッドと UngroupColumns メソッドを呼び出して、グループ化された行または列のグループ化を解除します。どちらのメソッドも同じパラメーターを取ります。

- 最初の行または列のインデックス。グループ化を解除する最初の行/列。
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
## **実行中のコードをダウンロード**
ダウンロード**行と列のグループ化とグループ解除 (Aspose.Cells)**以下のソーシャルコーディングサイトのいずれかから：

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
