---
title: تحويل ملفات Excel إلى HTML في Python
type: docs
weight: 10
url: /ar/java/converting-excel-files-to-html-in-python/
---
## **Aspose.Cells - تحويل ملف Excel إلى HTML**
لتحويل Excel إلى HTML باستخدام Aspose.Cells for Java في Python ، ما عليك سوى استدعاء ورقة العمل_إلى_html () طريقة وحدة المحول.

**Python كود**

{{< highlight "python" >}}

 saveFormat = self.SaveFormat

workbook = self.Workbook(self.dataDir + "Book1.xls")

# Save the document in PDF format

workbook.save(self.dataDir + "OutBook1.html", saveFormat.HTML)

\# Print message

print "\n Excel to HTML conversion performed successfully."


{{< /highlight >}}
## **قم بتنزيل كود التشغيل**
 تحميل**تحويل ملف Excel إلى HTML (Aspose.Cells)** من أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
