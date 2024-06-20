---
title: تقسيم المعاينة إلى صفحات في Python
type: docs
weight: 60
url: /ar/java/page-break-preview-in-python/
---

## **Aspose.Cells - Hello World**
لتعيين ورقة العمل إلى معاينة الصفحات باستخدام **Aspose.Cells Java لـ Python**، قم ببساطة باستدعاء وحدة **PageBreakPreview**.

**كود Python**

{{< highlight java >}}

 workbook = self.Workbook(self.dataDir + "Book1.xls")

#Adding a new worksheet to the Workbook object

worksheets = workbook.getWorksheets()

worksheet = worksheets.get(0)

#Displaying the worksheet in page break preview

worksheet.setPageBreakPreview(True)

#Saving the modified Excel file in default format

workbook.save(self.dataDir + "output.xls")

\# Print message

print "Page break preview is enabled for sheet 1, please check the output document." 

{{< /highlight >}}
## **تحميل رمز التشغيل**
قم بتنزيل **معاينة الصفحات (Aspose.Cells)** من أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
