---
title: تحويل ملفات إكسل إلى ملفات PDF في روبي
type: docs
weight: 30
url: /ar/java/converting-excel-to-pdf-files-in-ruby/
---

## **Aspose.Cells - تحويل إكسل إلى ملفات PDF**
لتحويل إكسل إلى ملف Pdf باستخدام Aspose.Cells for Java في روبي، قم ببساطة بالاستدعاء الطريقة excel_to_pdf() من وحدة المحول.

**كود Ruby**

{{< highlight ruby >}}

 def excel_to_pdf(workbook)

    save_format = Rjb::import('com.aspose.cells.SaveFormat')

    # Save the document in PDF format

    workbook.save(@data_dir + "MyPdfFile.pdf", save_format.PDF)

    puts "Pdf saved successfully."

end 

{{< /highlight >}}
## **تحميل رمز التشغيل**
تنزيل **تحويل إكسل إلى ملفات PDF (Aspose.Cells)** من أي من مواقع البرمجة الاجتماعية المذكورة أدناه:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/converter.rb)
