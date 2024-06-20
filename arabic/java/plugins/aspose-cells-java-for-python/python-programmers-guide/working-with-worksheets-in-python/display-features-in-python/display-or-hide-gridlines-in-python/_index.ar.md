---
title: عرض أو إخفاء خطوط الشبكة في Python
type: docs
weight: 10
url: /ar/java/display-or-hide-gridlines-in-python/
description: تعلم كيفية عرض أو إخفاء خطوط الشبكة من خلال Aspose.Cells لبايثون عبر واجهة برمجة تطبيقات جافا.
keywords: كيفية عرض أو إخفاء خطوط الشبكة في بايثون عبر جاڤا, عرض أو إخفاء خطوط الشبكة باستخدام بايثون عبر جاڤا, إظهار أو إخفاء خطوط الشبكة في بايثون. 
---

## **Aspose.Cells - كيفية عرض أو إخفاء خطوط الشبكة**
### **كيفية إخفاء خطوط الشبكة**
لإخفاء ورقة العمل باستخدام **Aspose.Cells Java for Ruby**, اتصل بوحدة **displayhidegridlines**.

**كود Python**

{{< highlight java >}}

 workbook = self.Workbook(self.dataDir + "Book1.xls")

#Accessing the first worksheet in the Excel file

worksheets = workbook.getWorksheets()

worksheet = worksheets.get(0)

#Hiding the grid lines of the first worksheet of the Excel file

worksheet.setGridlinesVisible(False)

#Saving the modified Excel file in default (that is Excel 2000) format

workbook.save(self.dataDir + "output.xls")

\# Print message

print "Grid lines are now hidden on sheet 1, please check the output document."

{{< /highlight >}}
### **كيفية عرض خطوط الشبكة**
لجعل خطوط الشبكة مرئية، استخدم الوسيطة setGridlinesVisible(true) في فئة Worksheet.

**كود Python**

{{< highlight python >}}

 # Displaying the gridlines of the worksheet

worksheet.setGridlinesVisible(True)

{{< /highlight >}}
## **تحميل رمز التشغيل**
تحميل **DisplayHideGridlines (Aspose.Cells)** من أي من مواقع الترميز الاجتماعية المذكورة أدناه:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
