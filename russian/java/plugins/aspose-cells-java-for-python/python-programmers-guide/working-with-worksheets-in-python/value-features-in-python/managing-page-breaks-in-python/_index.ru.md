---
title: Управление разрывами страниц в Python
type: docs
weight: 20
url: /ru/java/managing-page-breaks-in-python/
---

## **Aspose.Cells - Управление разрывами страниц**
### **Добавление разрывов страниц**
Чтобы добавить разрывы страниц с помощью **Aspose.Cells Java для Ruby**, вызовите метод **add_page_breaks** модуля **pagebreaks**. Ниже приведен пример кода.

**Код Python**

{{< highlight python >}}

 def add_page_breaks(self):

\# Instantiating a Workbook object

workbook = self.Workbook(self.dataDir + "Book1.xls")

worksheets = workbook.getWorksheets()

worksheet = worksheets.get(0)

h_page_breaks = worksheet.getHorizontalPageBreaks()

h_page_breaks.add("Y30")

v_page_breaks = worksheet.getVerticalPageBreaks()

v_page_breaks.add("Y30")

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Add Page Breaks.xls")

print "Add page breaks, please check the output file."


{{< /highlight >}}
### **Очистка всех разрывов страниц**
Для удаления всех разрывов страниц с использованием **Aspose.Cells Java для Python**, вызовите метод **clear_all_page_breaks** модуля **pagebreaks**. Ниже вы можете увидеть пример кода.

**Код Python**

{{< highlight python >}}



def clear_all_page_breaks(self):

\# Instantiating a Workbook object

workbook = self.Workbook(self.dataDir + "Book1.xls")


workbook.getWorksheets().get(0).getHorizontalPageBreaks().clear()

workbook.getWorksheets().get(0).getVerticalPageBreaks().clear()

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Clear All Page Breaks.xls")

print "Clear all page breaks, please check the output file."


{{< /highlight >}}
### **Удаление конкретного разрыва страницы**
Чтобы удалить конкретный разрыв страницы с использованием **Aspose.Cells Java для Python**, вызовите метод **remove_page_break** модуля **pagebreaks**. Ниже приведен пример кода.

**Код Python**

{{< highlight python >}}



def remove_page_break(self):

\# Instantiating a Workbook object

workbook = self.Workbook(self.dataDir + "Book1.xls")

worksheets = workbook.getWorksheets()

worksheet = worksheets.get(0)

h_page_breaks = worksheet.getHorizontalPageBreaks()

h_page_breaks.removeAt(0)

v_page_breaks = worksheet.getVerticalPageBreaks()

v_page_breaks.removeAt(0)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Remove Page Break.xls")

print "Remove page break, please check the output file."


{{< /highlight >}}
## **Скачать работающий код**
Скачать **Управление Разрывами Страницы (Aspose.Cells)** с любого из упомянутых ниже социальных сайтов для кодирования:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
