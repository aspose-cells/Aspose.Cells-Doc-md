---
title: كيفية تعيين خاصية الاسترداد التلقائي للمصنف
type: docs
weight: 160
url: /ar/java/how-to-set-autorecover-property-of-workbook/
---
{{% alert color="primary" %}}

 يمكنك استخدام Aspose.Cells لتعيين خاصية الاسترداد التلقائي للمصنف. القيمة الافتراضية لهذه الخاصية هي**حقيقي** . عندما تقوم بتعيينه**خاطئة**في أحد المصنفات ، يقوم Microsoft Excel بتعطيل الاسترداد التلقائي (الحفظ التلقائي) في ملف Excel هذا.

 يوفر Aspose.Cells[**Workbook.getSettings (). setAutoRecover ()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#AutoRecover) الخاصية لتمكين أو تعطيل هذا الخيار.

{{% /alert %}}

## كود Java لتعيين خاصية الاسترداد التلقائي للمصنف

 يشرح الكود التالي كيفية الاستخدام[**Workbook.getSettings (). setAutoRecover ()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#AutoRecover) خاصية المصنف. يقرأ الكود أولاً القيمة الافتراضية لهذه الخاصية وهي**حقيقي** ، ثم يضعها على أنها**خاطئة** ويحفظ المصنف. ثم يقرأ المصنف مرة أخرى ويقرأ قيمة هذه الخاصية الخاطئة في هذا الوقت.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SetAutoRecoverProperty-SetAutoRecoverProperty.java" >}}

## الناتج الناتج عن نموذج التعليمات البرمجية

هنا هو إخراج وحدة التحكم من نموذج التعليمات البرمجية أعلاه.

{{< highlight "java" >}}

AutoRecover: true

AutoRecover: false

{{< /highlight >}}
