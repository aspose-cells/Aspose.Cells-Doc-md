---
title: تحويل ملفات Excel إلى HTML بلغة Ruby
type: docs
weight: 20
url: /ar/java/converting-excel-files-to-html-in-ruby/
---
## **Aspose.Cells - تحويل ملفات Excel إلى HTML**
لتحويل Excel إلى HTML باستخدام Aspose.Cells for Java في Ruby ، ما عليك سوى استدعاء ورقة العمل_إلى_html () طريقة وحدة المحول.

**كود روبي**

{{< highlight "ruby" >}}

 def worksheet_to_html(workbook)

    save_format = Rjb::import('com.aspose.cells.SaveFormat')

    # Specify the HTML saving options

    save = Rjb::import('com.aspose.cells.HtmlSaveOptions').new(save_format.M_HTML)

    # Save the document

    workbook.save(@data_dir + "output.html", save)

    puts "HTML saved successfully."

end 

{{< /highlight >}}
## **قم بتنزيل كود التشغيل**
تحميل**تحويل ملفات Excel إلى HTML (Aspose.Cells)**من أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/converter.rb)
