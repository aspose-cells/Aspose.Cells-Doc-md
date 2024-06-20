---
title: عرض أو إخفاء علامات التبويب في Ruby
type: docs
weight: 40
url: /ar/java/display-or-hide-tabs-in-ruby/
---

## **Aspose.Cells - عرض أو إخفاء علامات التبويب**
### **إخفاء علامات التبويب**
لإخفاء علامات التبويب باستخدام **Aspose.Cells جافا لـ Ruby**، اتصل بوحدة **displayhidetabs**.

**كود Ruby**

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
### **جعل علامات التبويب مرئية**
اجعل علامات التبويب مرئية بواسطة الطبقة المحورية مع طريقة *setSheetTabBarHidden(false)* من فئة *Workbook*.

**كود Ruby**

{{< highlight ruby >}}

 # Displaying the tabs of the Excel file

workbook.getSettings().setSowTabs(true)

{{< /highlight >}}
## **تحميل رمز التشغيل**
تنزيل **إخفاء أو عرض أو إخفاء علامات التبويب (Aspose.Cells)** من أي من مواقع البرمجة الاجتماعية المذكورة أدناه:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/displayhidetabs.rb)
