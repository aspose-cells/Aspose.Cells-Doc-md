---
title: عرض أو إخفاء علامات التبويب في روبي
type: docs
weight: 40
url: /ar/java/display-or-hide-tabs-in-ruby/
---
## **Aspose.Cells - عرض أو إخفاء علامات التبويب**
### **علامات التبويب الاختباء**
 لإخفاء علامات التبويب باستخدام ملفات**Aspose.Cells Java لروبي** ، مكالمة**عرض** وحدة.

**كود روبي**

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
### **جعل علامات التبويب مرئية**
اجعل علامات التبويب مرئية باستخدام أسلوب setSheetTabBarHidden (false) لفئة المصنف.

**كود روبي**

{{< highlight "ruby" >}}

 # Displaying the tabs of the Excel file

workbook.getSettings().setSowTabs(true)

{{< /highlight >}}
## **قم بتنزيل كود التشغيل**
تحميل**إخفاء أو عرض أو إخفاء علامات التبويب (Aspose.Cells)**من أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/displayhidetabs.rb)
