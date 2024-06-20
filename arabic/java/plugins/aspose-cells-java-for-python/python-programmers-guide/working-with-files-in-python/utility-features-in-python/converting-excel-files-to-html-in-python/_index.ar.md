---
title: تحويل ملفات Excel إلى HTML في Python
type: docs
weight: 10
url: /ar/java/converting-excel-files-to-html-in-python/
---

## **Aspose.Cells - تحويل ملف Excel إلى HTML**
لتحويل Excel إلى HTML باستخدام Aspose.Cells for Java في Python ، قم ببساطة بدعوة الطريقة worksheet_to_html() من وحدة Converter.

**كود Python**

{{< highlight python >}}

 saveFormat = self.SaveFormat

workbook = self.Workbook(self.dataDir + "Book1.xls")

#Save the document in PDF format

workbook.save(self.dataDir + "OutBook1.html", saveFormat.HTML)

\# Print message

print "\n Excel to HTML conversion performed successfully."


{{< /highlight >}}
## **تحميل رمز التشغيل**
قم بتنزيل **تحويل ملف Excel إلى HTML (Aspose.Cells)** من أي من المواقع الاجتماعية للبرمجة المذكورة أدناه:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
