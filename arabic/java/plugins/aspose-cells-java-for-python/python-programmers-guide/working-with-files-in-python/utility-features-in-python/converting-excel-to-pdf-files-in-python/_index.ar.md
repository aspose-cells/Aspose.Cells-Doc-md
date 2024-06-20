---
title: تحويل ملف Excel إلى ملفات PDF في Python
type: docs
weight: 20
url: /ar/java/converting-excel-to-pdf-files-in-python/
---

## **Aspose.Cells - تحويل Excel إلى Pdf**
لتحويل ملف Excel إلى ملف Pdf باستخدام Aspose.Cells for Java في Python، قم ببساطة باستدعاء طريقة excel_to_pdf() في وحدة الـ Converter.

**كود Python**

{{< highlight python >}}

 saveFormat = self.SaveFormat

workbook = self.Workbook(self.dataDir + "Book1.xls")

#Save the document in PDF format

workbook.save(self.dataDir + "OutBook1.pdf", saveFormat.PDF)

\# Print message

print "\n Excel to PDF conversion performed successfully."

{{< /highlight >}}
## **تحميل رمز التشغيل**
تحميل **تحويل ملف Excel إلى Pdf (Aspose.Cells)** من أي من المواقع الاجتماعية للبرمجة المذكورة أدناه:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
