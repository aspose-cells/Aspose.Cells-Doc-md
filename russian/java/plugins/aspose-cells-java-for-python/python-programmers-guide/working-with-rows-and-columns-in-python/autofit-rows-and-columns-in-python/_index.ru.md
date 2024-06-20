---
title: Автоматическая подгонка строк и столбцов в Python
type: docs
weight: 20
url: /ru/java/autofit-rows-and-columns-in-python/
description: Узнайте, как выполнить автоматическую подгонку строк и столбцов через Aspose.Cells для Python через API Java.
keywords: Как выполнить автоматическую подгонку строк и столбцов в Python через Java, автоматическая подгонка данных строк в книге с использованием Python через Java, автоматическая подгонка данных столбцов в Python через Java. 
---

## **Как выполнить автоматическую подгонку строк и столбцов**
### **Как выполнить автоматическую подгонку строки**
Самым простым способом автоматического изменения ширины и высоты строки является вызов метода autoFitRow класса Worksheet. Метод autoFitRow принимает индекс строки (столбец для изменения размера) в качестве параметра.

**Код Python**

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
### **Как выполнить автоматическую подгонку столбца**
Самым простым способом автоматического изменения ширины и высоты столбца является вызов метода autoFitColumn класса Worksheet. Метод autoFitColumn принимает индекс столбца (столбец, который требуется изменить) в качестве параметра.

**Код Python**

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
## **Скачать работающий код**
Скачать **Автоподбор строк и столбцов (Aspose.Cells)** с любого из перечисленных ниже сайтов социальной разработки:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
