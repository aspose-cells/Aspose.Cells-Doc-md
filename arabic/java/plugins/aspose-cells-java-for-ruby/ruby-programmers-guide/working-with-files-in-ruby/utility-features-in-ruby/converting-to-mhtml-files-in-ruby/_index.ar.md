---
title: تحويل ملفات MHTML في Ruby
type: docs
weight: 50
url: /ar/java/converting-to-mhtml-files-in-ruby/
---

## **Aspose.Cells - تحويل ملفات MHTML**
لتحويل ورقة عمل إلى ملف MHTML باستخدام Aspose.Cells for Java في Ruby، قم ببساطة باستدعاء طريقة worksheet_to_mhtml() من وحدة Converter.

**كود Ruby**

{{< highlight ruby >}}

 def worksheet_to_mhtml(workbook)

    save_format = Rjb::import('com.aspose.cells.SaveFormat')

    # Specify the HTML saving options

    sv = Rjb::import('com.aspose.cells.HtmlSaveOptions').new(save_format.M_HTML)

    # Save the document

    workbook.save(@data_dir + "convert.mht", sv)

    puts "MHTML saved successfully."

end

{{< /highlight >}}
## **تحميل رمز التشغيل**
تحميل **تحويل ملفات MHTML (Aspose.Cells)** من أي من مواقع البرمجة الاجتماعية المذكورة أدناه:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/converter.rb)
