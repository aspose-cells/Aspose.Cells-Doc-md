---
title: إنشاء مُقطَّع إلى جدول محوري
type: docs
weight: 10
url: /ar/java/create-slicer-to-a-pivot-table/
---

## **سيناريوهات الاستخدام المحتملة**
يُستخدم المُقطَّع لتصفية البيانات بسرعة. يمكن استخدامه لتصفية البيانات سواء في جدول أو جدول محوري. تسمح Microsoft Excel لك بإنشاء مُقطَّع عن طريق تحديد جدول أو جدول محوري ثم النقر فوق *إدراج > مُقطَّع*. كما تسمح Aspose.Cells أيضًا بإنشاء مُقطَّع باستخدام الطريقة [Worksheet.getSlicers().add()](https://reference.aspose.com/cells/java/com.aspose.cells/slicercollection#add\(com.aspose.cells.PivotTable,%20int,%20int,%20com.aspose.cells.PivotField\)).
## **إنشاء مُقطَّع إلى جدول محوري**
يرجى الاطلاع على رمز العينة التالي. يقوم بتحميل ملف Excel العيني ([67338498.xlsx](67338498.xlsx)) الذي يحتوي على الجدول المحوري. ثم يقوم بإنشاء المُقطَّع بناءً على أول حقل محوري. أخيرًا، يحفظ برنامج العمل بتنسيق [XLSX](67338497.xlsx) و [XLSB](67338496.xlsb). يُظهر اللقطة الشاشية التالية المُقطَّع الذي أنشأته Aspose.Cells في ملف الإكسل الناتج.

![todo:image_alt_text](create-slicer-to-a-pivot-table_1.png)
## **الكود المثالي**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Slicers-CreateSlicerToPivotTable.java" >}}
