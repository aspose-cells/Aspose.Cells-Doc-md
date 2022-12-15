---
title: قم بإلغاء حماية ورقة العمل في Ruby
type: docs
weight: 20
url: /ar/java/unprotect-a-worksheet-in-ruby/
---
## **Aspose.Cells - إلغاء حماية ورقة العمل**
 لحماية ورقة العمل باستخدام**Aspose.Cells Java لروبي** ، مكالمة**unotect_worksheet** طريقة**الحماية** وحدة.

**كود روبي**

{{< highlight "ruby" >}}

 def unprotect_worksheet()

    data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'



    # Instantiating a Workbook object by excel file path

    workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')



    # Accessing the first worksheet in the Excel file

    worksheets = workbook.getWorksheets()

    worksheet = worksheets.get(0)

    protection = worksheet.getProtection()

    # The following 3 methods are only for Excel 2000 and earlier formats

    protection.setAllowEditingContent(false)

    protection.setAllowEditingObject(false)

    protection.setAllowEditingScenario(false)

    # Unprotecting the worksheet with a password

    worksheet.unprotect("1234")



    # Saving the modified Excel file in default (that is Excel 2003) format

    workbook.save(data_dir + "Unprotect Worksheet.xls")

    puts "Unprotect a Worksheet, please check the output file."

end   

{{< /highlight >}}
## **تحميل كود الجري**
تحميل**إلغاء حماية ورقة العمل (Aspose.Cells)**من أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/protection.rb)
