---
title: تجميع حقول الجدول المحوري في جدول الدوران
type: docs
weight: 90
url: /ar/java/group-pivot-fields-in-the-pivot-table/
---

## **سيناريوهات الاستخدام المحتملة**

يسمح برنامج Microsoft Excel لك بتجميع حقول الجدول المحوري للجدول المحوري. عندما يكون هناك كمية كبيرة من البيانات تتصل بحقل محور، فمن المفيد غالبًا تجميعها إلى أقسام. Aspose.Cells يوفر أيضًا هذه الميزة باستخدام الطريقة [**PivotTable.setManualGroupField()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#setManualGroupField-com.aspose.cells.PivotField-com.aspose.cells.DateTime-com.aspose.cells.DateTime-java.util.ArrayList-int-).

## **تجميع حقول الجدول المحوري**

كود العينة التالي يحمل [ملف إكسل عينة](64716838.xlsx) ويقوم بتجميع الحقل المحوري الأول باستخدام الطريقة [**PivotTable.setManualGroupField()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#setManualGroupField-com.aspose.cells.PivotField-com.aspose.cells.DateTime-com.aspose.cells.DateTime-java.util.ArrayList-int-). ثم يقوم بتحديث وحساب بيانات الجدول المحوري ويحفظ المصنف كـ [ملف إكسل الناتج](64716837.xlsx). يُظهر لقطة الشاشة تأثير كود العينة على ملف إكسل العينة. كما ترون في لقطة الشاشة، تم تجميع الحقل المحوري الأول الآن حسب الشهور والربع السنوي.

![todo:image_alt_text](group-pivot-fields-in-the-pivot-table_1.png)

## **الكود المثالي**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "PivotTables-GroupPivotFieldsInPivotTable.java" >}}
{{< app/cells/assistant language="java" >}}
