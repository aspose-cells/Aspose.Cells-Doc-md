---
title: عرض أو إخفاء أشرطة التمرير في Ruby
type: docs
weight: 30
url: /ar/java/display-or-hide-scroll-bars-in-ruby/
---

## **Aspose.Cells - عرض أو إخفاء أشرطة التمرير**
### **إخفاء أشرطة التمرير**
لإخفاء أشرطة التمرير باستخدام **Aspose.Cells جافا لـ Ruby**، اتصل بوحدة **displayhidescrollbars**.

**كود Ruby**

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
### **جعل أشرطة التمرير مرئية**
جعل أشرطة التمرير مرئية عن طريق ضبط methods الكائن من الصفحة Workbook باستخدام setVerticalScrollBarHidden() أو setHorizontalScrollBarHidden() إلى true.

**كود Ruby**

{{< highlight ruby >}}

 # Displaying the vertical scroll bar of the Excel file

workbook.getSettings().setVScrollBarVisible(true)

\# Displaying the horizontal scroll bar of the Excel file

workbook.getSettings().setHScrollBarVisible(true)

{{< /highlight >}}
## **تحميل رمز التشغيل**
تنزيل **إظهار أو إخفاء أشرطة التمرير (Aspose.Cells)** من أي من مواقع البرمجة الاجتماعية المذكورة أدناه:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/displayhidescrollbars.rb)
