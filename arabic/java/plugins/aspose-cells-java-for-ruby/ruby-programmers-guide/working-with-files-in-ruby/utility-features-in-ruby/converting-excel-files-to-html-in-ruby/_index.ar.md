---
title: تحويل ملفات إكسل إلى HTML في روبي
type: docs
weight: 20
url: /ar/java/converting-excel-files-to-html-in-ruby/
---

## **Aspose.Cells - تحويل ملفات إكسل إلى HTML**
لتحويل إكسل إلى HTML باستخدام Aspose.Cells for Java في روبي، قم ببساطة باستدعاء طريقة worksheet_to_html() من وحدة الجدول المحول.

**كود Ruby**

{{< highlight ruby >}}

 def worksheet_to_html(workbook)

    save_format = Rjb::import('com.aspose.cells.SaveFormat')

    # Specify the HTML saving options

    save = Rjb::import('com.aspose.cells.HtmlSaveOptions').new(save_format.M_HTML)

    # Save the document

    workbook.save(@data_dir + "output.html", save)

    puts "HTML saved successfully."

end 

{{< /highlight >}}
## **تحميل رمز التشغيل**
تنزيل **تحويل ملفات إكسل إلى HTML (Aspose.Cells)** من أي من مواقع البرمجة الاجتماعية المذكورة أدناه:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/converter.rb)
