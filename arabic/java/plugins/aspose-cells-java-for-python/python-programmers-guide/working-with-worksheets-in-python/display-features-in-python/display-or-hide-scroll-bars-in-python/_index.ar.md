---
title: عرض أو إخفاء أشرطة التمرير في Python
type: docs
weight: 20
url: /ar/java/display-or-hide-scroll-bars-in-python/
---
## **Aspose.Cells - عرض أو إخفاء أشرطة التمرير**
### **إخفاء رؤوس الصفوف / الأعمدة**
 لإخفاء رؤوس الصفوف / الأعمدة باستخدام**Aspose.Cells Java لـ Python** ، مكالمة**DisplayHideRowColumnHeaders** وحدة.

**Python كود**

{{< highlight "python" >}}

 workbook = self.Workbook(self.dataDir + "Book1.xls")

# Hiding the vertical scroll bar of the Excel file

workbook.getSettings().setVScrollBarVisible(False)

# Hiding the horizontal scroll bar of the Excel file

workbook.getSettings().setHScrollBarVisible(False)

# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "output.xls")

\# Print message

print "Scroll bars are now hidden, please check the output document."

{{< /highlight >}}
### **جعل رؤوس الصفوف / الأعمدة مرئية**
اجعل رؤوس الصفوف والأعمدة مرئية باستخدام أسلوب setRowColumnHeadersVisible (true) لفئة ورقة العمل.

**Python كود**

{{< highlight "python" >}}

 # Displaying the headers of rows and columns

worksheet.setRowColumnHeadersVisible(true)

{{< /highlight >}}
## **قم بتنزيل كود التشغيل**
 تحميل**Hello World (Aspose.Cells)** من أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
