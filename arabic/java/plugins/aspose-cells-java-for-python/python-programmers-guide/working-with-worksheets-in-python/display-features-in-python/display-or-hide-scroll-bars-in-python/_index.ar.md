---
title: عرض أو إخفاء أشرطة التمرير في بايثون
type: docs
weight: 20
url: /ar/java/display-or-hide-scroll-bars-in-python/
---

## **Aspose.Cells - عرض أو إخفاء أشرطة التمرير**
### **إخفاء رؤوس الصف/العمود**
لإخفاء رؤوس الصف العمود باستخدام **Aspose.Cells جاڤا لبايثون**, اطلب وحدة **DisplayHideRowColumnHeaders**.

**كود Python**

{{< highlight python >}}

 workbook = self.Workbook(self.dataDir + "Book1.xls")

#Hiding the vertical scroll bar of the Excel file

workbook.getSettings().setVScrollBarVisible(False)

#Hiding the horizontal scroll bar of the Excel file

workbook.getSettings().setHScrollBarVisible(False)

#Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "output.xls")

\# Print message

print "Scroll bars are now hidden, please check the output document."

{{< /highlight >}}
### **جعل رؤوس الصف/العمود مرئية**
جعل رؤوس الصف والعمود مرئية باستخدام الوسيطة setRowColumnHeadersVisible(true) في فئة Worksheet.

**كود Python**

{{< highlight python >}}

 # Displaying the headers of rows and columns

worksheet.setRowColumnHeadersVisible(true)

{{< /highlight >}}
## **تحميل رمز التشغيل**
تحميل **مرحبًا بالعالم (Aspose.Cells)** من أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
