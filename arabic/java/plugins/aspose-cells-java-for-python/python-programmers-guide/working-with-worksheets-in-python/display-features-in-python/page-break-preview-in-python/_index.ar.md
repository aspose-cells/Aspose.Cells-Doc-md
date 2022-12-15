---
title: معاينة فاصل الصفحة في Python
type: docs
weight: 60
url: /ar/java/page-break-preview-in-python/
---
## **Aspose.Cells - Hello World**
 لتعيين ورقة العمل لمعاينة فاصل الصفحة باستخدام**Aspose.Cells Java for Python** ، ببساطة استدعاء**معاينة PageBreak** وحدة.

**Python كود**

{{< highlight "java" >}}

 workbook = self.Workbook(self.dataDir + "Book1.xls")

# Adding a new worksheet to the Workbook object

worksheets = workbook.getWorksheets()

worksheet = worksheets.get(0)

# Displaying the worksheet in page break preview

worksheet.setPageBreakPreview(True)

# Saving the modified Excel file in default format

workbook.save(self.dataDir + "output.xls")

\# Print message

print "Page break preview is enabled for sheet 1, please check the output document." 

{{< /highlight >}}
## **تحميل كود الجري**
 تحميل**معاينة فاصل الصفحة (Aspose.Cells)** من أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
