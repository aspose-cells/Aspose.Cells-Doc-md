---
title: كيفية تعيين خاصية AutoRecover للفصل
type: docs
weight: 160
url: /ar/java/how-to-set-autorecover-property-of-workbook/
---

{{% alert color="primary" %}}

يمكنك استخدام Aspose.Cells لضبط خاصية AutoRecover للمصنف. القيمة الافتراضية لهذه الخاصية هي **true**. عندما تقوم بتعيينها **false** على مصنف، يعطل Microsoft Excel خاصية الانتعاش التلقائي (الحفظ التلقائي) على ذلك الملف Excel.

يوفر Aspose.Cells خاصية [**Workbook.getSettings().setAutoRecover()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#AutoRecover) لتمكين أو تعطيل هذا الخيار.

{{% /alert %}}

## الكود Java لضبط خاصية AutoRecover للمصنف

يشرح الكود التالي كيفية استخدام خاصية [**Workbook.getSettings().setAutoRecover()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#AutoRecover) للمصنف. يقوم الكود أولاً بقراءة القيمة الافتراضية لهذه الخاصية التي تكون **true**، ثم يضبطها على **false** ويحفظ المصنف. بعد ذلك يقوم بقراءة المصنف مرة أخرى ويقرأ قيمة هذه الخاصية التي هي false في ذلك الوقت.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SetAutoRecoverProperty-SetAutoRecoverProperty.java" >}}

## الإخراج الناتج من الكود العينة

فيما يلي مخرجات وحدة الإدخال الخاصة بالكود المصدري أعلاه.

{{< highlight java >}}

AutoRecover: true

AutoRecover: false

{{< /highlight >}}
