---
title: تحويل إلى ملفات MHTML في Python
type: docs
weight: 30
url: /ar/java/converting-to-mhtml-files-in-python/
---

## **Aspose.Cells - تحويل إلى MHTML**
لتحويل ورق العمل إلى ملف MHTML باستخدام Aspose.Cells for Java في Python، قم ببساطة باستدعاء طريقة worksheet_to_mhtml() في وحدة الـ Converter.

**كود Python**

{{< highlight java >}}

 saveFormat = self.SaveFormat

#Specify the file path

filePath = self.dataDir + "Book1.xlsx"

#Specify the HTML saving options

sv = self.HtmlSaveOptions(saveFormat.M_HTML)

#Instantiate a workbook and open the template XLSX file

wb = self.Workbook(filePath)

#Save the MHT file

wb.save(filePath + ".out.mht", sv)

\# Print message

print "Excel to MHTML conversion performed successfully."

{{< /highlight >}}
## **تحميل رمز التشغيل**
تحميل **تحويل إلى MHTML (Aspose.Cells)** من أي من المواقع الاجتماعية للبرمجة المذكورة أدناه:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
