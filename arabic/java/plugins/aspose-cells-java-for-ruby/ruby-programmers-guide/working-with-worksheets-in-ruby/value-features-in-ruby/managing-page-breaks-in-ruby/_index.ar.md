---
title: إدارة فواصل الصفحات في Ruby
type: docs
weight: 20
url: /ar/java/managing-page-breaks-in-ruby/
---

## **Aspose.Cells - إدارة فواصل الصفحات**
### **إضافة فواصل الصفحات**
لإضافة فواصل الصفحات باستخدام **Aspose.Cells Java for Ruby**، اُنادي بطريقة **add_page_breaks** لوحدة **pagebreaks**. يمكنك أدناه رؤية مثال على الكود.

**كود Ruby**

{{< highlight ruby >}}

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
لمسح كافة فواصل الصفحات باستخدام **Aspose.Cells Java for Ruby**، اُنادي بطريقة **clear_all_page_breaks** لوحدة **pagebreaks**. يمكنك أدناه رؤية مثال على الكود.

**كود Ruby**

{{< highlight ruby >}}

 def clear_all_page_breaks(workbook)

    workbook.getWorksheets().get(0).getHorizontalPageBreaks().clear()

    workbook.getWorksheets().get(0).getVerticalPageBreaks().clear()

    # Saving the modified Excel file in default (that is Excel 2003) format

    workbook.save(@data_dir + "Clear All Page Breaks.xls")

    puts "Clear all page breaks, please check the output file."

end 

{{< /highlight >}}
### **إزالة فاصل صفحة محدد**
لإزالة فاصل الصفحة المحدد باستخدام **Aspose.Cells Java for Ruby**، اُنادي بطريقة **remove_page_break** لوحدة **pagebreaks**. يمكنك أدناه رؤية مثال على الكود.

**كود Ruby**

{{< highlight ruby >}}

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
## **تحميل رمز التشغيل**
تنزيل **إدارة فواصل الصفحات (Aspose.Cells)** من أي من مواقع التعاون الاجتماعي التالية:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/pagebreaks.rb)
