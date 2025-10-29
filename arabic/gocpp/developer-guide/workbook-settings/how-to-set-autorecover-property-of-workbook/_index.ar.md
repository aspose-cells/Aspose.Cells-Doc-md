---
title: كيفية إعداد خاصية الاسترداد التلقائي للمصنف باستخدام Golang عبر C++
linktitle: كيفية تعيين خاصية AutoRecover للفصل
type: docs
weight: 220
url: /ar/go-cpp/how-to-set-autorecover-property-of-workbook/
description: تعلم كيفية تفعيل أو تعطيل خاصية AutoRecover للمصنف باستخدام Aspose.Cells for C++.
---

{{% alert color="primary" %}}

يمكنك استخدام Aspose.Cells لضبط خاصية AutoRecover للمصنف. القيمة الافتراضية لهذه الخاصية هي **true**. عند تعيينها إلى **false**، يقوم Microsoft Excel بتعطيل AutoRecover (الحفظ التلقائي) على ملف Excel هذا.

 يوفر Aspose.Cells الخاصية [**Workbook.GetAutoRecover()**](https://reference.aspose.com/cells/go-cpp/workbooksettings/getautorecover/) لتمكين أو تعطيل هذا الخيار.

{{% /alert %}}

يشرح الكود التالي كيفية استخدام خاصية [**Workbook.GetAutoRecover()**](https://reference.aspose.com/cells/go-cpp/workbooksettings/getautorecover/) للمصنف. يبدأ بقراءة القيمة الافتراضية لهذه الخاصية، والتي هي **true**، ثم يغيرها إلى **false** ويحفظ المصنف. ثم يقرأ المصنف مرة أخرى ويلاحظ قيمة هذه الخاصية، والتي تكون **false** في ذلك الحين.

## كود C++ لضبط خاصية AutoRecover للمصنف

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-HowToSetAutorecoverPropertyOfWorkbook.go" >}}
## **الناتج**

فيما يلي مخرجات وحدة الإدخال الخاصة بالكود المصدري أعلاه.

{{< highlight java >}}

AutoRecover: True

AutoRecover: False

{{< /highlight >}}
