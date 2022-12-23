---
title: التحويل إلى MHTML ملفات في روبي
type: docs
weight: 50
url: /ar/java/converting-to-mhtml-files-in-ruby/
---
## **Aspose.Cells - التحويل إلى ملفات MHTML**
لتحويل ورقة العمل إلى ملف MHTML باستخدام Aspose.Cells for Java في روبي ، ما عليك سوى استدعاء ورقة العمل_إلى_mhtml () طريقة وحدة المحول.

**كود روبي**

{{< highlight "ruby" >}}

 def worksheet_to_mhtml(workbook)

    save_format = Rjb::import('com.aspose.cells.SaveFormat')

    # Specify the HTML saving options

    sv = Rjb::import('com.aspose.cells.HtmlSaveOptions').new(save_format.M_HTML)

    # Save the document

    workbook.save(@data_dir + "convert.mht", sv)

    puts "MHTML saved successfully."

end

{{< /highlight >}}
## **قم بتنزيل كود التشغيل**
تحميل**التحويل إلى ملفات MHTML (Aspose.Cells)**من أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/converter.rb)
