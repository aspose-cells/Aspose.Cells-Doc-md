---
title: تحويل ملفات Excel إلى ملفات PDF بلغة Ruby
type: docs
weight: 30
url: /ar/java/converting-excel-to-pdf-files-in-ruby/
---
## **Aspose.Cells - تحويل ملفات Excel إلى ملفات PDF**
لتحويل ملف Excel إلى Pdf باستخدام Aspose.Cells for Java في Ruby ، ما عليك سوى استدعاء excel_إلى_pdf () طريقة وحدة المحول.

**كود روبي**

{{< highlight "ruby" >}}

 def excel_to_pdf(workbook)

    save_format = Rjb::import('com.aspose.cells.SaveFormat')

    # Save the document in PDF format

    workbook.save(@data_dir + "MyPdfFile.pdf", save_format.PDF)

    puts "Pdf saved successfully."

end 

{{< /highlight >}}
## **قم بتنزيل كود التشغيل**
تحميل**تحويل ملفات Excel إلى ملفات PDF (Aspose.Cells)**من أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/converter.rb)
