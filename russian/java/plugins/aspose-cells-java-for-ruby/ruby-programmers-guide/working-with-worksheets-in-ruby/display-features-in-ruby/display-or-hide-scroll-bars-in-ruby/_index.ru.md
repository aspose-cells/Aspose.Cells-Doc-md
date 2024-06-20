---
title: Показать или скрыть полосы прокрутки в Ruby
type: docs
weight: 30
url: /ru/java/display-or-hide-scroll-bars-in-ruby/
---

## **Aspose.Cells - Показать или скрыть полосы прокрутки**
### **Скрытие полос прокрутки**
Чтобы скрыть полосы прокрутки с использованием **Aspose.Cells Java для Ruby**, вызовите модуль **displayhidescrollbars**.

**Код на Ruby**

{{< highlight ruby >}}

 data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'

\# Instantiating a Workbook object by excel file path

workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')

\# Hiding the vertical scroll bar of the Excel file

workbook.getSettings().setVScrollBarVisible(false)

\# Hiding the horizontal scroll bar of the Excel file

workbook.getSettings().setHScrollBarVisible(false)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(data_dir + "output.xls")

puts "Scroll Bars are now hidden, please check the output file."

{{< /highlight >}}
### **Отображение полос прокрутки**
Сделать полосы прокрутки видимыми, установив методы setVerticalScrollBarHidden() или setHorizontalScrollBarHidden() класса Workbook в true.

**Код на Ruby**

{{< highlight ruby >}}

 # Displaying the vertical scroll bar of the Excel file

workbook.getSettings().setVScrollBarVisible(true)

\# Displaying the horizontal scroll bar of the Excel file

workbook.getSettings().setHScrollBarVisible(true)

{{< /highlight >}}
## **Скачать работающий код**
Скачать **Показать или скрыть полосы прокрутки (Aspose.Cells)** с любого из указанных ниже сайтов социального кодирования:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/displayhidescrollbars.rb)
