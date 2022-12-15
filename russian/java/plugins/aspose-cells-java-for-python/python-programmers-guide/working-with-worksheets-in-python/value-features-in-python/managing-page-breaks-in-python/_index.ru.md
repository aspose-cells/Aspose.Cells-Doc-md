---
title: Управление разрывами страниц в Python
type: docs
weight: 20
url: /ru/java/managing-page-breaks-in-python/
---
## **Aspose.Cells - Управление разрывами страниц**
### **Добавление разрывов страниц**
 Чтобы добавить разрывы страниц с помощью**Aspose.Cells Java для рубина** , вызов**add_page_breaks** метод**разрывы страниц** модуль. Ниже вы можете увидеть пример кода.

**Python Код**

{{< highlight "python" >}}

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
### **Удаление всех разрывов страниц**
 Чтобы очистить все разрывы страниц с помощью**Aspose.Cells Java for Python** , вызов**clear_all_page_breaks** метод**разрывы страниц** модуль. Ниже вы можете увидеть пример кода.

**Python Код**

{{< highlight "python" >}}



def clear_all_page_breaks(self):

\# Instantiating a Workbook object

workbook = self.Workbook(self.dataDir + "Book1.xls")


workbook.getWorksheets().get(0).getHorizontalPageBreaks().clear()

workbook.getWorksheets().get(0).getVerticalPageBreaks().clear()

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Clear All Page Breaks.xls")

print "Clear all page breaks, please check the output file."


{{< /highlight >}}
### **Удаление определенного разрыва страницы**
 Чтобы удалить определенный разрыв страницы, используя**Aspose.Cells Java for Python** , вызов**remove_page_break** метод**разрывы страниц** модуль. Ниже вы можете увидеть пример кода.

**Python Код**

{{< highlight "python" >}}



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
## **Скачать рабочий код**
 Скачать**Управление разрывами страниц (Aspose.Cells)** с любого из нижеперечисленных сайтов социального кодирования:

- [Гитхаб](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
