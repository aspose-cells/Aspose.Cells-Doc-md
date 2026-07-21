---
title: تحديد الموقع المطلق للعناصر المحورية باستخدام Golang عبر C++
linktitle: تحديد الموقع المطلق لعنصر الجدول المحوري
type: docs
weight: 50
url: /ar/go-cpp/specifying-the-absolute-position-of-the-pivot-item/
description: تعلم كيف تحدد الموقع المطلق لعناصر Pivot في C++ باستخدام Aspose.Cells.
---

{{% alert color="primary" %}}

أحيانًا، يحتاج المستخدمون إلى تحديد الموقع المطلق لعناصر Pivot. لقد كشفت واجهة برمجة التطبيقات Aspose.Cells عن بعض الخصائص الجديدة وطريقة لتحقيق هذا المطلب.

- تمت إضافة [**PivotItem.GetPosition()**](https://reference.aspose.com/cells/go-cpp/pivotitem/getposition/) الخاصية التي يمكن استخدامها لتحديد مؤشر الموقع في كافة PivotItems بغض النظر عن العقدة الأم. تمت إضافة [**PivotItem.GetPositionInSameParentNode()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivotitem/getpositioninsameparentnode/) للخاصية التي يمكن استخدامها لتحديد مؤشر الموقع في PivotItems تحت نفس العقدة الأم.
- أضيفت الطريقة [**PivotItem.Move(int count, bool isSameParent)**](https://reference.aspose.com/cells/go-cpp/pivotitem/move/) لتحريك العنصر للأعلى أو الأسفل بناءً على قيمة العد، حيث أن العد هو عدد المواقع التي يتم تحريك عنصر Pivot فيها للأعلى أو الأسفل. إذا كانت قيمة العد أقل من الصفر، سيتم تحريك العنصر للأعلى، وإذا كانت أكبر من الصفر، سينتقل عنصر Pivot للأسفل. يُحدد معامل النوع Boolean `isSameParent` ما إذا كانت عملية التحريك يجب أن تُنفذ في نفس العقدة الأصلية أم لا.
- تم إلغاء دعم طريقة `PivotItem.Move(int count)`؛ لذلك يوصى باستخدام الطريقة الجديدة [**PivotItem.Move(int count, bool isSameParent)**](https://reference.aspose.com/cells/go-cpp/pivotitem/move/) بدلاً منها.

{{% /alert %}}

يخلق الكود النموذجي التالي جدول Pivot ثم يحدد مواقع عناصر Pivot في نفس العقدة الأصلية. يمكنك تحميل ملف Excel المصدر وملف Excel الناتج للمراجعة. إذا فتحت ملف Excel الناتج، سترى أن عنصر Pivot "4H12" في الموقع 0 في الأصل "K11" و"DIF400" في الموقع 3. وبالمثل، CA32 في الموقع 1 وAAA3 في الموقع 2.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SpecifyingTheAbsolutePositionOfThePivotItem.go" >}}
{{% alert color="primary" %}}

يرجى ملاحظة، أنه من الضروري استدعاء طرق `PivotTable.RefreshData` و `PivotTable.CalculateData` قبل استخدام [**PivotItem.GetPosition()**](https://reference.aspose.com/cells/go-cpp/pivotitem/getposition/)، [**PivotItem.GetPositionInSameParentNode()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivotitem/getpositioninsameparentnode/)، و [**PivotItem.Move(int count, bool isSameParent)**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivotitem/move/).

{{% /alert %}}
