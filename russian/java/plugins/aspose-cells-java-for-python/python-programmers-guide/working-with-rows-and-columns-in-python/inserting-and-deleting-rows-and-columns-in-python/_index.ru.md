---
title: Вставка и удаление строк и столбцов в Python
type: docs
weight: 60
url: /ru/java/inserting-and-deleting-rows-and-columns-in-python/
keywords: "создать XLSX в Python, создать XLS в Python, XLS Python, XLSX Python, XLT Python, XLTX Python, вставить строку Python, вставить столбец Python, Excel Python"
description: Используйте Python Excel API для создания электронных таблиц Excel в Python. Вставляйте или удаляйте строки из XLSX или XLS в ваших приложениях Python без MS Office.
---

## **Создание электронных таблиц Excel в Python - Управление строками/столбцами**
### **Вставка строки**
Вставьте строку в любом месте, вызвав метод insertRows коллекции Cells. Метод insertRows принимает индекс строки, куда будет вставлена новая строка, в качестве первого аргумента, и количество строк, которые будут вставлены, в качестве второго аргумента. Вот шаги:

- Загрузите книгу Excel XLS или XLSX
- Получите доступ к листу Excel
- Вставьте строку
- Сохраните книгу XLS или XLSX

**Код Python**

{{< highlight python >}}

 def insert_row(self):

\# Instantiating a Workbook object by excel file path

workbook = self.Workbook(self.dataDir + "Book1.xls")

\# Accessing the first worksheet in the Excel file

worksheet = workbook.getWorksheets().get(0)

\# Inserting a row into the worksheet at 3rd position

worksheet.getCells().insertRows(2,1)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Insert Row.xls")

print "Insert Row Successfully." 

{{< /highlight >}}
### **Вставка нескольких строк**
Чтобы вставить несколько строк в лист, вызовите метод insertRows коллекции Cells. Метод InsertRows принимает два параметра:

- Индекс строки, индекс строки, с которой будут вставлены новые строки.
- Количество строк, общее число строк, которые необходимо вставить.

**Код Python**

{{< highlight python >}}

 def insert_multiple_rows(self):

\# Instantiating a Workbook object by excel file path

workbook = self.Workbook(self.dataDir + 'Book1.xls')

\# Accessing the first worksheet in the Excel file

worksheet = workbook.getWorksheets().get(0)

\# Inserting a row into the worksheet at 3rd position

worksheet.getCells().insertRows(2,10)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Insert Multiple Rows.xls")

print "Insert Multiple Rows Successfully." 


{{< /highlight >}}
### **Удаление строки**
Для удаления строки в любом месте вызовите метод deleteRows коллекции Cells. Метод DeleteRows принимает два параметра:

- Индекс строки, индекс строки, с которой строки будут удалены.
- Количество строк, общее количество строк, которые необходимо удалить.

**Код Python**

{{< highlight python >}}

 def delete_row(self):

\# Instantiating a Workbook object by excel file path

workbook = self.Workbook(self.dataDir + 'Book1.xls')

\# Accessing the first worksheet in the Excel file

worksheet = workbook.getWorksheets().get(0)

\# Deleting 3rd row from the worksheet

worksheet.getCells().deleteRows(2,1,True)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Delete Row.xls")

print "Delete Row Successfully." 

{{< /highlight >}}
### **Удаление нескольких строк**
Чтобы удалить несколько строк из листа, вызовите метод deleteRows коллекции Cells. Метод DeleteRows принимает два параметра:

- Индекс строки, индекс строки, с которой строки будут удалены.
- Количество строк, общее количество строк, которые необходимо удалить.

**Код Python**

{{< highlight python >}}

 def delete_multiple_rows(self):

\# Instantiating a Workbook object by excel file path

workbook = self.Workbook(self.dataDir + 'Book1.xls')

\# Accessing the first worksheet in the Excel file

worksheet = workbook.getWorksheets().get(0)

\# Deleting 10 rows from the worksheet starting from 3rd row

worksheet.getCells().deleteRows(2,10,True)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Delete Multiple Rows.xls")

print "Delete Multiple Rows Successfully." 


{{< /highlight >}}
### **Вставка столбца**
Разработчики также могут вставить столбец в лист в любом месте, вызвав метод insertColumns коллекции Cells. Метод insertColumns принимает два параметра:

- Индекс столбца, индекс столбца, в который будет вставлен столбец
- Количество столбцов, общее количество столбцов, которые нужно вставить.

**Код Python**

{{< highlight python >}}

 def insert_column(self):

\# Instantiating a Workbook object by excel file path

workbook = self.Workbook(self.dataDir + 'Book1.xls')

\# Accessing the first worksheet in the Excel file

worksheet = workbook.getWorksheets().get(0)

\# Inserting a column into the worksheet at 2nd position

worksheet.getCells().insertColumns(1,1)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Insert Column.xls")

print "Insert Column Successfully." 


{{< /highlight >}}
### **Удаление столбца**
Чтобы удалить столбец из листа в любом месте, вызовите метод deleteColumns коллекции Cells. Метод deleteColumns принимает следующие параметры:

- Индекс столбца, индекс столбца, откуда будет удален столбец.
- Количество столбцов, общее количество столбцов, которые необходимо удалить.
- Сдвиг ячеек, логический параметр, указывающий, следует ли сдвигать ячейки влево после удаления.

**Код Python**

{{< highlight python >}}

 def delete_column(self):

\# Instantiating a Workbook object by excel file path

workbook = self.Workbook(self.dataDir + 'Book1.xls')

\# Accessing the first worksheet in the Excel file

worksheet = workbook.getWorksheets().get(0)

\# Deleting a column from the worksheet at 2nd position

worksheet.getCells().deleteColumns(1,1,True)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Delete Column.xls")

print "Delete Column Successfully." 


{{< /highlight >}}
## **Скачать работающий код**
Скачать **Управление строками/столбцами (Aspose.Cells)** с любого из упомянутых ниже сайтов для социального кодирования:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
