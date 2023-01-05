---
title: Python の行と列の自動調整
type: docs
weight: 20
url: /ja/java/autofit-rows-and-columns-in-python/
---
## **Aspose.Cells - 行と列の自動調整**
### **行の自動調整**
行の幅と高さを自動的にサイズ変更する最も簡単な方法は、Worksheet クラスの autoFitRow メソッドを呼び出すことです。 autoFitRow メソッドは、(サイズ変更する行の) 行インデックスをパラメーターとして受け取ります。

**Python コード**

{{< highlight "python" >}}

 def autofit_row(self):

\# Instantiating a Workbook object by excel file path

workbook = self.Workbook(self.dataDir + 'Book1.xls')

\# Accessing the first worksheet in the Excel file

worksheet = workbook.getWorksheets().get(0)

\# Auto-fitting the 3rd row of the worksheet

worksheet.autoFitRow(2)

\# Auto-fitting the 3rd row of the worksheet based on the contents in a range of

\# cells (from 1st to 9th column) within the row

# worksheet.autoFitRow(2,0,8) # Uncomment this line if you to do AutoFit Row in a Range of Cells. Also, comment line 288.

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Autofit Row.xls")

print "Autofit Row Successfully." 

{{< /highlight >}}
### **列の自動調整**
列の幅と高さを自動的にサイズ変更する最も簡単な方法は、Worksheet クラスの autoFitColumn メソッドを呼び出すことです。 autoFitColumn メソッドは、(サイズ変更しようとしている列の) 列インデックスをパラメーターとして受け取ります。

**Python コード**

{{< highlight "python" >}}

 def autofit_column(self):

\# Instantiating a Workbook object by excel file path

workbook = self.Workbook(self.dataDir + 'Book1.xls')

\# Accessing the first worksheet in the Excel file

worksheet = workbook.getWorksheets().get(0)

\# Auto-fitting the 4th column of the worksheet

worksheet.autoFitColumn(3)

\# Auto-fitting the 4th column of the worksheet based on the contents in a range of

\# cells (from 1st to 9th row) within the column

# worksheet.autoFitColumn(3,0,8) #Uncomment this line if you to do AutoFit Column in a Range of Cells. Also, comment line 310.

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Autofit Column.xls")

print "Autofit Column Successfully." 

{{< /highlight >}}
## **実行中のコードをダウンロード**
ダウンロード**行と列の自動調整 (Aspose.Cells)**以下のソーシャルコーディングサイトのいずれかから：

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
