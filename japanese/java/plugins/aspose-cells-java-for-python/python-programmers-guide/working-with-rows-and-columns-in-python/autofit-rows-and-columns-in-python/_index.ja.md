---
title: Pythonで行と列を自動調整
type: docs
weight: 20
url: /ja/java/autofit-rows-and-columns-in-python/
description: Aspose.Cells for Python Via Java APIを使用して、Pythonで行と列を自動調整する方法を学びます。
keywords: Python Via Javaで行と列を自動調整する方法、Python Via Javaを使用してワークブック内の行データを自動調整する方法、Python Via Javaで列データを自動調整する方法。 
---

## **行と列を自動調整する方法**
### **行を自動調整する方法**
行の幅と高さを自動調整する最も直感的な方法は、Worksheet クラスのautoFitRowメソッドを呼び出すことです。autoFitRowメソッドは、サイズ変更する行のインデックス（row index）をパラメーターとして取ります。

**Pythonコード**

{{< highlight python >}}

 def autofit_row(self):

\# Instantiating a Workbook object by excel file path

workbook = self.Workbook(self.dataDir + 'Book1.xls')

\# Accessing the first worksheet in the Excel file

worksheet = workbook.getWorksheets().get(0)

\# Auto-fitting the 3rd row of the worksheet

worksheet.autoFitRow(2)

\# Auto-fitting the 3rd row of the worksheet based on the contents in a range of

\# cells (from 1st to 9th column) within the row

#worksheet.autoFitRow(2,0,8) # Uncomment this line if you to do AutoFit Row in a Range of Cells. Also, comment line 288.

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Autofit Row.xls")

print "Autofit Row Successfully." 

{{< /highlight >}}
### **列を自動調整する方法**
列の幅と高さを自動調整する最も簡単な方法は、Worksheet クラスのautoFitColumnメソッドを呼び出すことです。autoFitColumnメソッドは、サイズ変更する列のインデックス（column index）をパラメーターとして取ります。

**Pythonコード**

{{< highlight python >}}

 def autofit_column(self):

\# Instantiating a Workbook object by excel file path

workbook = self.Workbook(self.dataDir + 'Book1.xls')

\# Accessing the first worksheet in the Excel file

worksheet = workbook.getWorksheets().get(0)

\# Auto-fitting the 4th column of the worksheet

worksheet.autoFitColumn(3)

\# Auto-fitting the 4th column of the worksheet based on the contents in a range of

\# cells (from 1st to 9th row) within the column

#worksheet.autoFitColumn(3,0,8) #Uncomment this line if you to do AutoFit Column in a Range of Cells. Also, comment line 310.

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Autofit Column.xls")

print "Autofit Column Successfully." 

{{< /highlight >}}
## **ランニングコードのダウンロード**
以下に挙げるどのソーシャルコーディングサイトから、**行と列の自動調整（Aspose.Cells）**をダウンロードしてください：

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
