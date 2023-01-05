---
title: Вставка и удаление строк и столбцов в Python
type: docs
weight: 60
url: /ru/java/inserting-and-deleting-rows-and-columns-in-python/
keywords: create XLSX in Python, create XLS in Python, XLS python, XLSX python, XLT python, XLTX python, insert row python, insert column python, Excel pytho
description: Используйте Python Excel API для создания электронных таблиц Excel в Python. Вставляйте или удаляйте строки из XLSX или XLS в ваших приложениях Python без MS Office.
---
## **Создание электронных таблиц Excel в Python — Управление строками/столбцами**
### **Вставка строки**
Вставьте строку в любое место, вызвав метод insertRows коллекции Cells. Метод insertRows принимает индекс строки, в которую будет вставлена новая строка, в качестве первого аргумента и количество вставляемых строк в качестве второго аргумента. Ниже приведены шаги:

- Загрузите книгу XLS или XLSX
- Доступ к рабочему листу
- Вставьте строку
- Сохранить как книгу XLS или XLSX

**Python Код**

{{< highlight "python" >}}

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
Чтобы вставить несколько строк на лист, вызовите метод insertRows коллекции Cells. Метод InsertRows принимает два параметра:

- Индекс строки, индекс строки, из которой будут вставлены новые строки.
- Количество строк, общее количество строк, которые необходимо вставить.

**Python Код**

{{< highlight "python" >}}

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
Чтобы удалить строку в любом месте, вызовите метод deleteRows коллекции Cells. Метод DeleteRows принимает два параметра:

- Индекс строки, индекс строки, из которой строки будут удалены.
- Количество строк, общее количество строк, которые необходимо удалить.

**Python Код**

{{< highlight "python" >}}

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
Чтобы удалить несколько строк с листа, вызовите метод deleteRows коллекции Cells. Метод DeleteRows принимает два параметра:

- Индекс строки, индекс строки, из которой строки будут удалены.
- Количество строк, общее количество строк, которые необходимо удалить.

**Python Код**

{{< highlight "python" >}}

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
Разработчики также могут вставить столбец на лист в любом месте, вызвав метод insertColumns коллекции Cells. Метод insertColumns принимает два параметра:

- Индекс столбца, индекс столбца, из которого столбец будет вставлен
- Количество столбцов, общее количество столбцов, которые необходимо вставить

**Python Код**

{{< highlight "python" >}}

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
Чтобы удалить столбец из листа в любом месте, вызовите метод deleteColumns коллекции Cells. Метод deleteColumns принимает следующие параметры:

- Индекс столбца, индекс столбца, из которого столбец будет удален.
- Количество столбцов, общее количество столбцов, которые необходимо удалить.
- Сдвиг ячеек, логический параметр, указывающий, следует ли смещать ячейки, оставшиеся после удаления.

**Python Код**

{{< highlight "python" >}}

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
## **Скачать рабочий код**
 Скачать**Управление строками/столбцами (Aspose.Cells)**с любого из нижеперечисленных сайтов социального кодирования:

- [Гитхаб](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
