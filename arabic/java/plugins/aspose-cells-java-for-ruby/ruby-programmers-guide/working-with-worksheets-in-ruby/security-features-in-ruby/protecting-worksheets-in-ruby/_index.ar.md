---
title: حماية أوراق العمل في روبي
type: docs
weight: 10
url: /ar/java/protecting-worksheets-in-ruby/
---
## **Aspose.Cells - حماية أوراق العمل**
 لحماية ورقة العمل باستخدام**Aspose.Cells Java لروبي** ، مكالمة**حماية_ورقة العمل** طريقة**الحماية** وحدة.

**كود روبي**

{{< highlight "ruby" >}}

 def protect_worksheet()

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

    # Protects the first worksheet with a password "1234"

    protection.setPassword("1234")



    # Saving the modified Excel file in default (that is Excel 2003) format

    workbook.save(data_dir + "Protect Worksheet.xls")

    puts "Protect a Worksheet, please check the output file."

end   

{{< /highlight >}}
## **قم بتنزيل كود التشغيل**
تحميل**حماية أوراق العمل (Aspose.Cells)**من أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/protection.rb)
