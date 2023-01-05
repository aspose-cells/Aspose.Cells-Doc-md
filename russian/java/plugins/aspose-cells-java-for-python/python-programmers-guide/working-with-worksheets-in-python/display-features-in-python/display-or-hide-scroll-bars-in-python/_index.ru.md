---
title: Показать или скрыть полосы прокрутки в Python
type: docs
weight: 20
url: /ru/java/display-or-hide-scroll-bars-in-python/
---
## **Aspose.Cells — Показать или скрыть полосы прокрутки**
### **Скрытие заголовков строк/столбцов**
 Чтобы скрыть заголовки строк/столбцов с помощью**Aspose.Cells Java for Python** , вызов**DisplayHideRowColumnHeaders** модуль.

**Python Код**

{{< highlight "python" >}}

 workbook = self.Workbook(self.dataDir + "Book1.xls")

# Hiding the vertical scroll bar of the Excel file

workbook.getSettings().setVScrollBarVisible(False)

# Hiding the horizontal scroll bar of the Excel file

workbook.getSettings().setHScrollBarVisible(False)

# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "output.xls")

\# Print message

print "Scroll bars are now hidden, please check the output document."

{{< /highlight >}}
### **Отображение заголовков строк/столбцов**
Сделайте заголовки строк и столбцов видимыми с помощью метода setRowColumnHeadersVisible(true) класса Worksheet.

**Python Код**

{{< highlight "python" >}}

 # Displaying the headers of rows and columns

worksheet.setRowColumnHeadersVisible(true)

{{< /highlight >}}
## **Скачать рабочий код**
 Скачать**Hello World (Aspose.Cells)** с любого из нижеперечисленных сайтов социального кодирования:

- [Гитхаб](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
