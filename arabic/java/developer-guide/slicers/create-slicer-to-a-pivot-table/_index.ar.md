---
title: إنشاء مقسم إلى جدول محوري
type: docs
weight: 10
url: /ar/java/create-slicer-to-a-pivot-table/
---
## **سيناريوهات الاستخدام الممكنة**
تُستخدم أداة تقطيع الشرائح لتصفية البيانات بسرعة. يمكن استخدامه لتصفية البيانات سواء في الجدول أو الجدول المحوري. Microsoft يسمح لك Excel بإنشاء أداة تقطيع عن طريق تحديد جدول أو جدول محوري ثم النقر فوق الزر*إدراج> قطاعة شرائح*. يتيح لك Aspose.Cells أيضًا إنشاء أداة تقطيع باستخدام امتداد[Worksheet.getSlicers (). add ()](https://reference.aspose.com/cells/java/com.aspose.cells/slicercollection#add\(com.aspose.cells.PivotTable,%20int,%20int,%20com.aspose.cells.PivotField\)) طريقة.
## **إنشاء مقسم إلى جدول محوري**
يرجى الاطلاع على نموذج التعليمات البرمجية التالي. يقوم بتحميل ملف[نموذج لملف Excel](67338498.xlsx)الذي يحتوي على الجدول المحوري. ثم يقوم بإنشاء أداة التقطيع بناءً على الحقل المحوري الأساسي الأول. أخيرًا ، يحفظ المصنف بتنسيق[الإخراج XLSX](67338497.xlsx)و[الإخراج XLSB](67338496.xlsb)صيغة. تُظهر لقطة الشاشة التالية أداة التقطيع التي تم إنشاؤها بواسطة Aspose.Cells في ملف Excel الناتج.

![ما يجب القيام به: image_بديل_نص](create-slicer-to-a-pivot-table_1.png)
## **عينة من الرموز**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Slicers-CreateSlicerToPivotTable.java" >}}
