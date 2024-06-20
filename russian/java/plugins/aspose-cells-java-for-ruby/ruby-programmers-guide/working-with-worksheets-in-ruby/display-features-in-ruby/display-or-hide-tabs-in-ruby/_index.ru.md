---
title: Отображение или скрытие вкладок в Ruby
type: docs
weight: 40
url: /ru/java/display-or-hide-tabs-in-ruby/
---

## **Aspose.Cells - Отображение или скрытие вкладок**
### **Скрытие вкладок**
Чтобы скрыть вкладки с помощью **Aspose.Cells Java для Ruby**, вызовите модуль **displayhidetabs**.

**Код на Ruby**

{{< highlight ruby >}}

 data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'

\# Instantiating a Workbook object by excel file path

workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')

\# Hiding the tabs of the Excel file

workbook.getSettings().setShowTabs(false)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(data_dir + "output.xls")

puts "Tabs are now hidden, please check the output file."

{{< /highlight >}}
### **Отображение вкладок**
Сделайте вкладки видимыми с помощью метода setSheetTabBarHidden(false) класса Workbook.

**Код на Ruby**

{{< highlight ruby >}}

 # Displaying the tabs of the Excel file

workbook.getSettings().setSowTabs(true)

{{< /highlight >}}
## **Скачать работающий код**
Скачать **Скрыть или отобразить вкладки (Aspose.Cells)** с любого из указанных ниже сайтов социального кодирования:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/displayhidetabs.rb)
