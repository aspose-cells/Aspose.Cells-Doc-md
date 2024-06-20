---
title: Копирование строк и столбцов в Python
type: docs
weight: 30
url: /ru/java/copying-rows-and-columns-in-python/
---

## **Aspose.Cells - Копирование строк и столбцов**
### **Копирование строк**
Aspose.Cells предоставляет метод copyRow класса Cells. Этот метод копирует все типы данных, включая формулы, значения, комментарии, форматы ячеек, скрытые ячейки, изображения и другие объекты рисования из исходной строки в целевую строку.

Метод copyRow принимает следующие параметры:

- исходный объект Cells,
- индекс исходной строки, и
- индекс строки назначения.

**Код Python**

{{< highlight java >}}

 def copy_rows(self):

\# Instantiating a Workbook object by excel file path

workbook = self.Workbook(self.dataDir + 'Book1.xls')

\# Accessing the first worksheet in the Excel file

worksheet = workbook.getWorksheets().get(0)

\# Copy the second row with data, formattings, images and drawing objects

\# to the 12th row in the worksheet.

worksheet.getCells().copyRow(worksheet.getCells(),1,11)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Copy Rows.xls")

print "Copy Rows Successfully." 

{{< /highlight >}}
### **Копирование столбцов**
Aspose.Cells предоставляет метод copyColumn класса Cells, этот метод копирует все типы данных, включая формулы - с обновленными ссылками - и значения, комментарии, форматы ячеек, скрытые ячейки, изображения и другие объекты рисования из исходной колонки в целевую колонку.

Метод copyColumn принимает следующие параметры:

- исходный объект Cells,
- индекс исходного столбца, и
- индекс столбца назначения.

**Код Python**

{{< highlight ruby >}}



def copy_columns(self):

\# Instantiating a Workbook object by excel file path

workbook = self.Workbook()

\# Accessing the first worksheet in the Excel file

worksheet = workbook.getWorksheets().get(0)

\# Put some data into header rows (A1:A4)

i = 0

while i < 5:

worksheet.getCells().get(i, 0).setValue("Header Row #i")





\# Put some detail data (A5:A999)

i = 5

while i < 1000:

worksheet.getCells().get(i, 0).setValue("Detail Row #i")


\# Create another Workbook.

workbook1 = Workbook()

\# Get the first worksheet in the book.

worksheet1 = workbook1.getWorksheets().get(0)

\# Copy the first column from the first worksheet of the first workbook into

\# the first worksheet of the second workbook.

worksheet1.getCells().copyColumn(worksheet.getCells(),0,2)

\# Autofit the column.

worksheet1.autoFitColumn(2)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Copy Columns.xls")

print "Copy Columns Successfully." 

{{< /highlight >}}
## **Скачать работающий код**
Загрузите **Копирование строк и столбцов (Aspose.Cells)** с любого из упомянутых ниже сайтов для социального кодирования:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
