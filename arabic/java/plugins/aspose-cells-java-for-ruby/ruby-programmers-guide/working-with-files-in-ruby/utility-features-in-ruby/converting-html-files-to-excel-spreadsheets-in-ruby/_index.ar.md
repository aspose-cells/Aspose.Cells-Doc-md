---
title: تحويل ملفات HTML إلى جداول بيانات إكسل بلغة روبي
type: docs
weight: 40
url: /ar/java/converting-html-files-to-excel-spreadsheets-in-ruby/
---
## **Aspose.Cells - تحويل ملفات HTML إلى جداول بيانات Excel**
لتحويل HTML إلى جدول بيانات باستخدام Aspose.Cells for Java في Ruby ، ما عليك سوى استدعاء html_إلى_excel () طريقة وحدة المحول.

**كود روبي**

{{< highlight "ruby" >}}

 def html_to_excel()

    load_format = Rjb::import('com.aspose.cells.LoadFormat')

    # Create an instance of HTMLLoadOptions and initiate it with appropriate LoadFormat

    options = Rjb::import('com.aspose.cells.HTMLLoadOptions').new(load_format.HTML)



    # Load the Html file through file path while passing the instance of HTMLLoadOptions class

    workbook = Rjb::import('com.aspose.cells.Workbook').new(@data_dir + "index.html", options)



    save_format = Rjb::import('com.aspose.cells.SaveFormat')

    #Save the results to disc in Xlsx format

    workbook.save(@data_dir + "output.xlsx", save_format.XLSX)

    puts "XLSX saved successfully."

end

{{< /highlight >}}
## **قم بتنزيل كود التشغيل**
تحميل**تحويل ملفات HTML إلى جداول بيانات Excel (Aspose.Cells)**من أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/converter.rb)
