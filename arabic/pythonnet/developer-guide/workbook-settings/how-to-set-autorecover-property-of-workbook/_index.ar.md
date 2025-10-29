---
title: كيفية تعيين خاصية AutoRecover للفصل
type: docs
weight: 220
url: /ar/python-net/how-to-set-autorecover-property-of-workbook/
---

{{% alert color="primary" %}}

يمكنك استخدام Aspose.Cells for Python via .NET لضبط خاصية AutoRecover للمصنف. القيمة الافتراضية لهذه الخاصية هي **true**. عندما تضبطها على **false**، يقوم Microsoft Excel بتعطيل خاصية AutoRecover (الحفظ التلقائي) لهذا الملف.

يوفر Aspose.Cells for Python via .NET الخاصية [**Workbook.settings.auto_recover**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/auto_recover) لتمكين أو تعطيل هذا الخيار.

{{% /alert %}}

يوضح الكود التالي كيفية استخدام خاصية [**Workbook.settings.auto_recover**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/auto_recover) للمصنف. يقرأ الكود أولاً القيمة الافتراضية لهذه الخاصية وهي **true**، ثم يغيرها إلى **false** ويحفظ المصنف. بعد ذلك يستخدمه مرة أخرى ويقرأ قيمة الخاصية التي تكون **false** في ذلك الوقت.

## الكود C# لتعيين خاصية AutoRecover للفصل

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "WorkbookSettings-SetAutoRecovery.py" >}}

## **الناتج**

فيما يلي مخرجات وحدة الإدخال الخاصة بالكود المصدري أعلاه.

{{< highlight java >}}

AutoRecover: True

AutoRecover: False

{{< /highlight >}}

{{< app/cells/assistant language="python-net" >}}
