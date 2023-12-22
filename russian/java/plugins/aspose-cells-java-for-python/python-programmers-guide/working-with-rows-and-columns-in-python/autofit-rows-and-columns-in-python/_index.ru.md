---
title: Автоподбор строк и столбцов в Python
type: docs
weight: 20
url: /ru/java/autofit-rows-and-columns-in-python/
description: Узнайте, как автоматически подогнать строки и столбцы с помощью Aspose.Cells for Python через Java API.
keywords: How to Autofit Rows and Columns in Python Via Java, Autofit Rows Data in workbook using Python Via Java, Python Via Java Autofit Columns Data. 
---
##  **Как автоматически подогнать строки и столбцы**
###  **Как автоподбор строки**
Самый простой подход к автоматическому изменению ширины и высоты строки — вызвать метод autoFitRow класса Worksheet. Метод autoFitRow принимает в качестве параметра индекс строки (строки, размер которой нужно изменить).

**Код Python**

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
###  **Как автоматически подогнать столбец**
Самый простой способ автоматически настроить ширину и высоту столбца — вызвать метод autoFitColumn класса Worksheet. Метод autoFitColumn принимает индекс столбца (столбца, размер которого будет изменен) в качестве параметра.

**Код Python**

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
##  **Загрузить рабочий код**
Скачать**Автоподбор строк и столбцов (Aspose.Cells)**с любого из перечисленных ниже сайтов социального кодирования:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
