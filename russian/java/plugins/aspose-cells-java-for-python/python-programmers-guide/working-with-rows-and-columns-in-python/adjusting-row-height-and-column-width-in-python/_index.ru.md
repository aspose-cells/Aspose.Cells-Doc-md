---
title: Регулировка высоты строки и ширины столбца в Python
type: docs
weight: 10
url: /ru/java/adjusting-row-height-and-column-width-in-python/
keywords: "создать XLSX в Python, создать XLS в Python, XLS python, XLSX python, высота строки python, ширина столбца python, Excel python"
description: Используйте Python Excel API для создания файлов Excel в Python. Настройте высоту строки и ширину столбца в XLSX или XLS в ваших приложениях на Python без MS Office.
---

## **Электронные таблицы Excel в Python - Настройка высоты строки и ширины столбца**
### **Установка высоты строки**
С помощью Aspose.Cells можно установить высоту одной строки в Python, вызвав метод setRowHeight коллекции Cells. Метод setRowHeight принимает следующие параметры:

- **Индекс строки**, индекс строки, высоту которой вы изменяете.
- **Высота строки**, высота строки, применяемая к строке.

**Код Python**

{{< highlight python >}}

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
### **Установка ширины столбца**
Установите ширину столбца, вызвав метод setColumnWidth коллекции Cells. Метод setColumnWidth принимает следующие параметры:

- **Индекс колонки**, индекс колонки, ширину которой вы изменяете.
- **Ширина колонки**, желаемая ширина колонки.

**Код Python**

{{< highlight python >}}

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
## **Скачать работающий код**
Скачать **Настройка высоты строки и ширины столбца (Aspose.Cells)** с любого из перечисленных ниже сайтов социальной разработки:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
