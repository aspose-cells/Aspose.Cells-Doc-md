---
title: عامل تكبير الاستخدام باستخدام Apache POI و Aspose.Cells
type: docs
weight: 70
url: /ar/java/zoom-factor-using-apache-poi-and-aspose-cells/
---

## **Aspose.Cells - عامل التكبير**
توفر Microsoft Excel ميزة تمكن المستخدمين من تعيين معامل تكبير أو تصغير لورقة العمل. تساعد هذه الميزة المستخدمين على رؤية محتويات ورقة العمل بعرض صغير أو أكبر.

توفر Aspose.Cells فئة Workbook التي تمثل ملف Microsoft Excel. تحتوي فئة Workbook على WorksheetCollection التي تسمح بالوصول إلى كل ورقة عمل في ملف Excel.

يتم تمثيل ورقة العمل بواسطة فئة Worksheet. توفر فئة Worksheet مجموعة واسعة من الخصائص والأساليب لإدارة ورقات العمل. لتعيين معامل التكبير لورقة العمل، استخدم طريقة setZoom في فئة Worksheet.

**Java**

{{< highlight java >}}

 Worksheet worksheet = worksheets.get(0);

//Setting the zoom factor of the worksheet to 75

worksheet.setZoom(75);

{{< /highlight >}}
## **Apache POI SS - HSSF XSSF - معامل التكبير**
يوفر Apache POI طريقة Sheet.setZoom() لتوفير ميزة التكبير.

**Java**

{{< highlight java >}}

 Sheet sheet1 = wb.createSheet("new sheet");

sheet1.setZoom(3,4);   // 75 percent magnification

{{< /highlight >}}
## **تحميل رمز التشغيل**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **تحميل رمز عينة**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/worksheets/zoomfactor)
{{< app/cells/assistant language="java" >}}
