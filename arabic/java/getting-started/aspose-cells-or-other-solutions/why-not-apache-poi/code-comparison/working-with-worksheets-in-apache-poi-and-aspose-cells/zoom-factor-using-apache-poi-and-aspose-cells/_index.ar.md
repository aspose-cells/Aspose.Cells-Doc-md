---
title: عامل التكبير باستخدام Apache POI و Aspose.Cells
type: docs
weight: 70
url: /ar/java/zoom-factor-using-apache-poi-and-aspose-cells/
---
## **Aspose.Cells - عامل التكبير**
يوفر Microsoft Excel ميزة تتيح للمستخدمين تعيين تكبير / تصغير ورقة العمل أو عامل التحجيم. تساعد هذه الميزة المستخدمين على رؤية محتويات ورقة العمل في طرق عرض أصغر أو أكبر.

يوفر Aspose.Cells فئة ، مصنف ، يمثل ملف إكسل Microsoft. تحتوي فئة المصنف على مجموعة أوراق العمل التي تتيح الوصول إلى كل ورقة عمل في ملف Excel.

يتم تمثيل ورقة العمل بواسطة فئة ورقة العمل. توفر فئة ورقة العمل نطاقًا واسعًا من الخصائص والأساليب لإدارة أوراق العمل. لتعيين عامل التكبير / التصغير الخاص بورقة العمل ، استخدم طريقة setZoom لفئة ورقة العمل.

**Java**

{{< highlight "java" >}}

 Worksheet worksheet = worksheets.get(0);

//Setting the zoom factor of the worksheet to 75

worksheet.setZoom(75);

{{< /highlight >}}
## **Apache POI SS - HSSF XSSF - عامل التكبير**
يوفر Apache POI طريقة Sheet.setZoom () الاستفادة من ميزة التكبير / التصغير.

**Java**

{{< highlight "java" >}}

 Sheet sheet1 = wb.createSheet("new sheet");

sheet1.setZoom(3,4);   // 75 percent magnification

{{< /highlight >}}
## **تحميل كود الجري**
- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **تنزيل نموذج التعليمات البرمجية**
- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/ src / main / java / com / aspose / خلية / أمثلة / featurescomparison / أوراق العمل / zoomfactor)
