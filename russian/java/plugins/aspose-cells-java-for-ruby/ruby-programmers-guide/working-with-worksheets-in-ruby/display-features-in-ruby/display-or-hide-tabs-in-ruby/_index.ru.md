---
title: Отображение или скрытие вкладок в Ruby
type: docs
weight: 40
url: /ru/java/display-or-hide-tabs-in-ruby/
---
## **Aspose.Cells — Показать или скрыть вкладки**
### **Скрытие вкладок**
 Чтобы скрыть вкладки с помощью**Aspose.Cells Java для рубина** , вызов**показать скрыть вкладки** модуль.

**Рубиновый код**

{{< highlight "ruby" >}}

 data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'

\# Instantiating a Workbook object by excel file path

workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')

\# Hiding the tabs of the Excel file

workbook.getSettings().setShowTabs(false)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(data_dir + "output.xls")

puts "Tabs are now hidden, please check the output file."

{{< /highlight >}}
### **Делаем вкладки видимыми**
Сделайте вкладки видимыми с помощью метода setSheetTabBarHidden(false) класса Workbook.

**Рубиновый код**

{{< highlight "ruby" >}}

 # Displaying the tabs of the Excel file

workbook.getSettings().setSowTabs(true)

{{< /highlight >}}
## **Скачать рабочий код**
Скачать**Скрыть или отобразить или скрыть вкладки (Aspose.Cells)**с любого из нижеперечисленных сайтов социального кодирования:

- [Гитхаб](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/displayhidetabs.rb)
