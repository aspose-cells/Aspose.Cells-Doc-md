---
title: تحويل ملفات Excel إلى ملفات PDF في Python
type: docs
weight: 20
url: /ar/java/converting-excel-to-pdf-files-in-python/
---
## **Aspose.Cells - تحويل Excel إلى PDF**
لتحويل ملف Excel إلى Pdf باستخدام Aspose.Cells for Java في Python ، ما عليك سوى استدعاء Excel_إلى_pdf () طريقة وحدة المحول.

**Python كود**

{{< highlight "python" >}}

 saveFormat = self.SaveFormat

workbook = self.Workbook(self.dataDir + "Book1.xls")

# Save the document in PDF format

workbook.save(self.dataDir + "OutBook1.pdf", saveFormat.PDF)

\# Print message

print "\n Excel to PDF conversion performed successfully."

{{< /highlight >}}
## **تحميل كود الجري**
 تحميل**تحويل ملف Excel إلى PDF (Aspose.Cells)** من أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
