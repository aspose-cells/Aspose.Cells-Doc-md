---
title: تجميع الحقول المحورية في الجدول المحوري
type: docs
weight: 90
url: /ar/java/group-pivot-fields-in-the-pivot-table/
---
## **سيناريوهات الاستخدام الممكنة**

Microsoft يسمح لك Excel بتجميع الحقول المحورية للجدول المحوري. عندما يكون هناك قدر كبير من البيانات المتعلقة بحقل محوري ، فمن المفيد غالبًا تجميعها في أقسام. يوفر Aspose.Cells أيضًا هذه الميزة باستخدام امتداد[**PivotTable.setManualGroupField ()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#setManualGroupField(com.aspose.cells.PivotField,%20com.aspose.cells.DateTime,%20com.aspose.cells.DateTime,%20java.util.ArrayList,%20int)) طريقة.

## **تجميع الحقول المحورية في الجدول المحوري**

يقوم نموذج التعليمات البرمجية التالي بتحميل ملف[نموذج لملف Excel](64716838.xlsx)وينفذ التجميع في أول حقل محوري باستخدام[**PivotTable.setManualGroupField ()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#setManualGroupField(com.aspose.cells.PivotField,%20com.aspose.cells.DateTime,%20com.aspose.cells.DateTime,%20java.util.ArrayList,%20int)) طريقة. يقوم بعد ذلك بتحديث بيانات الجدول المحوري وحسابها وحفظ المصنف كملف[إخراج ملف Excel](64716837.xlsx). تُظهر لقطة الشاشة تأثير نموذج التعليمات البرمجية على نموذج ملف Excel. كما ترى في لقطة الشاشة ، يتم الآن تجميع الحقل المحوري الأول حسب الأشهر والأرباع.

![ما يجب القيام به: image_بديل_نص](group-pivot-fields-in-the-pivot-table_1.png)

## **عينة من الرموز**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "PivotTables-GroupPivotFieldsInPivotTable.java" >}}
