---
title: كيفية تعيين خاصية الاسترداد التلقائي للمصنف
type: docs
weight: 220
url: /ar/net/how-to-set-autorecover-property-of-workbook/
---
{{% alert color="primary" %}}

 يمكنك استخدام Aspose.Cells لتعيين خاصية الاسترداد التلقائي للمصنف. القيمة الافتراضية لهذه الخاصية هي**حقيقي** . عندما تقوم بتعيينه**خاطئة** في مصنف ، يقوم Microsoft Excel بتعطيل الاسترداد التلقائي (الحفظ التلقائي) في ملف Excel هذا.

 يوفر Aspose.Cells[**المصنف ، الإعدادات ، الاسترداد التلقائي**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/autorecover) الخاصية لتمكين أو تعطيل هذا الخيار.

{{% /alert %}}

 يشرح الكود التالي كيفية الاستخدام[**المصنف ، الإعدادات ، الاسترداد التلقائي**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/autorecover) خاصية المصنف. يقرأ الكود أولاً القيمة الافتراضية لهذه الخاصية وهي**حقيقي** ، ثم يضعها على أنها**خاطئة** ويحفظ المصنف. ثم يقرأ المصنف مرة أخرى ويقرأ قيمة هذه الخاصية وهي**خاطئة** في هذا الوقت.

## كود C# لتعيين خاصية الاسترداد التلقائي للمصنف

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-SetAutoRecovery-SetAutoRecovery.cs" >}}

## **انتاج |**

هنا هو إخراج وحدة التحكم من نموذج التعليمات البرمجية أعلاه.

{{< highlight "java" >}}

AutoRecover: True

AutoRecover: False

{{< /highlight >}}
