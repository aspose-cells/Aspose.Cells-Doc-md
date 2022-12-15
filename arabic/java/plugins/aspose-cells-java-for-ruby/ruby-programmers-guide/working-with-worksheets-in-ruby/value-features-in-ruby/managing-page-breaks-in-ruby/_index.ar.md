---
title: إدارة فواصل الصفحات في روبي
type: docs
weight: 20
url: /ar/java/managing-page-breaks-in-ruby/
---
## **Aspose.Cells - إدارة فواصل الصفحات**
### **مضيفا فواصل الصفحات**
 لإضافة فواصل الصفحات باستخدام**Aspose.Cells Java لروبي** ، مكالمة**add_page_breaks** طريقة**فواصل الصفحة** وحدة. أدناه يمكنك مشاهدة مثال رمز.

**كود روبي**

{{< highlight "ruby" >}}

 def add_page_breaks(workbook)

    worksheets = workbook.getWorksheets()

    worksheet = worksheets.get(0)

    h_page_breaks = worksheet.getHorizontalPageBreaks()

    h_page_breaks.add("Y30")



    v_page_breaks = worksheet.getVerticalPageBreaks()

    v_page_breaks.add("Y30")

    # Saving the modified Excel file in default (that is Excel 2003) format

    workbook.save(@data_dir + "Add Page Breaks.xls")

    puts "Add page breaks, please check the output file."

end   

{{< /highlight >}}
### **مسح كافة فواصل الصفحات**
 لمسح كافة فواصل الصفحات باستخدام**Aspose.Cells Java لروبي** ، مكالمة**clear_all_page_breaks** طريقة**فواصل الصفحة** وحدة. أدناه يمكنك مشاهدة مثال رمز.

**كود روبي**

{{< highlight "ruby" >}}

 def clear_all_page_breaks(workbook)

    workbook.getWorksheets().get(0).getHorizontalPageBreaks().clear()

    workbook.getWorksheets().get(0).getVerticalPageBreaks().clear()

    # Saving the modified Excel file in default (that is Excel 2003) format

    workbook.save(@data_dir + "Clear All Page Breaks.xls")

    puts "Clear all page breaks, please check the output file."

end 

{{< /highlight >}}
### **إزالة فاصل صفحة معين**
 لإزالة فاصل صفحة معين باستخدام**Aspose.Cells Java لروبي** ، مكالمة**remove_page_break** طريقة**فواصل الصفحة** وحدة. أدناه يمكنك مشاهدة مثال رمز.

**كود روبي**

{{< highlight "ruby" >}}

 def remove_page_break(workbook)

    worksheets = workbook.getWorksheets()

    worksheet = worksheets.get(0)



    h_page_breaks = worksheet.getHorizontalPageBreaks()

    h_page_breaks.removeAt(0)



    v_page_breaks = worksheet.getVerticalPageBreaks()

    v_page_breaks.removeAt(0)

    # Saving the modified Excel file in default (that is Excel 2003) format

    workbook.save(@data_dir + "Remove Page Break.xls")

    puts "Remove page break, please check the output file."

end 

{{< /highlight >}}
## **تحميل كود الجري**
تحميل**إدارة فواصل الصفحات (Aspose.Cells)**من أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/pagebreaks.rb)
