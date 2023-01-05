---
title: Настройка высоты строки и ширины столбца в Python
type: docs
weight: 10
url: /ru/java/adjusting-row-height-and-column-width-in-python/
keywords: create XLSX in Python, create XLS in Python, XLS python, XLSX python, row height python, column width python, Excel pytho
description: Используйте Python Excel API для создания файлов Excel в Python. Отрегулируйте высоту строки и ширину столбца в XLSX или XLS в приложениях Python без MS Office.
---
## **Электронные таблицы Excel в Python — Настройка высоты строки и ширины столбца**
### **Настройка высоты строки**
С помощью Aspose.Cells можно установить высоту одной строки в Python, вызвав метод setRowHeight коллекции Cells. Метод setRowHeight принимает следующие параметры:

- **Индекс строки**, индекс строки, высоту которой вы меняете.
- **Высота строки**, высота строки, применяемая к строке.

**Python Код**

{{< highlight "python" >}}

 def set_row_height(self):

\# Instantiating a Workbook object by excel file path

workbook = self.Workbook(self.self.dataDir + 'Book1.xls')

\# Accessing the first worksheet in the Excel file

worksheet = workbook.getWorksheets().get(0)

cells = worksheet.getCells()

\# Setting the height of the second row to 13

cells.setRowHeight(1, 13)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Set Row Height.xls")

print "Set Row Height Successfully." 

{{< /highlight >}}
### **Настройка ширины столбца**
Установите ширину столбца, вызвав метод setColumnWidth коллекции Cells. Метод setColumnWidth принимает следующие параметры:

- **Индекс столбца**, индекс столбца, ширину которого вы меняете.
- **Ширина колонки**, желаемая ширина столбца.

**Python Код**

{{< highlight "python" >}}

 def set_column_width(self):

\# Instantiating a Workbook object by excel file path

workbook = self.Workbook(self.dataDir + 'Book1.xls')

\# Accessing the first worksheet in the Excel file

worksheet = workbook.getWorksheets().get(0)

cells = worksheet.getCells()

\# Setting the width of the second column to 17.5

cells.setColumnWidth(1, 17.5)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Set Column Width.xls")

print "Set Column Width Successfully." 

{{< /highlight >}}
## **Скачать рабочий код**
Скачать**Настройка высоты строки и ширины столбца (Aspose.Cells)**с любого из нижеперечисленных сайтов социального кодирования:

- [Гитхаб](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
