---
title: كيفية تعيين خاصية AutoRecover للفصل
type: docs
weight: 220
url: /ar/net/how-to-set-autorecover-property-of-workbook/
---

{{% alert color="primary" %}}

يمكنك استخدام Aspose.Cells لتعيين خاصية AutoRecover للفصل. القيمة الافتراضية لهذه الخاصية هي **true**. عندما تقوم بتعيينها إلى **false** على فصل، يعطّل Microsoft Excel AutoRecover (الحفظ التلقائي) على ذلك الملف في Excel.

يوفر Aspose.Cells خاصية [**Workbook.Settings.AutoRecover**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/autorecover) لتمكين أو تعطيل هذا الخيار.

{{% /alert %}}

الكود التالي يشرح كيفية استخدام خاصية [**Workbook.Settings.AutoRecover**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/autorecover) للفصل. يقرأ الكود أولا القيمة الافتراضية لهذه الخاصية وهي **true**، ثم يعيد تعيينها إلى **false** ويحفظ الفصل. ثم يقرأ الفصل مرة أخرى ويقرأ قيمة هذه الخاصية التي هي **false** في تلك اللحظة.

## الكود C# لتعيين خاصية AutoRecover للفصل

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-SetAutoRecovery-SetAutoRecovery.cs" >}}

## **الناتج**

فيما يلي مخرجات وحدة الإدخال الخاصة بالكود المصدري أعلاه.

{{< highlight java >}}

AutoRecover: True

AutoRecover: False

{{< /highlight >}}
