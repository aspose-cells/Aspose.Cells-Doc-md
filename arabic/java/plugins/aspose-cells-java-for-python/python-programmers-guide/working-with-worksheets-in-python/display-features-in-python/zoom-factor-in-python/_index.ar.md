---
title: معامل التكبير في Python
type: docs
weight: 80
url: /ar/java/zoom-factor-in-python/
---

## **Aspose.Cells - عامل التكبير**
لتعيين معامل التكبير باستخدام **Aspose.Cells Java for Python**, قم ببساطة بالاستدعاء وحدة **ZoomFactor**.

**كود Python**

{{< highlight java >}}

 workbook = self.Workbook(self.dataDir + "Book1.xls")

#Accessing the first worksheet in the Excel file

worksheets = workbook.getWorksheets()

worksheet = worksheets.get(0)

#Setting the zoom factor of the worksheet to 75

worksheet.setZoom(75)

#Saving the modified Excel file in default format

workbook.save(self.dataDir + "output.xls")

\# Print message

print "Zoom factor set to 75% for sheet 1, please check the output document."

{{< /highlight >}}
## **تحميل رمز التشغيل**
تنزيل **معامل التكبير (Aspose.Cells)** من أي من مواقع البرمجة الاجتماعية المذكورة أدناه:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
