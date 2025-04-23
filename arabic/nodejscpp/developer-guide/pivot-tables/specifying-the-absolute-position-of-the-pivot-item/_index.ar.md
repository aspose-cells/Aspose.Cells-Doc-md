---
title: تحديد الموقع المطلق لعنصر الجدول المحوري
type: docs
weight: 50
url: /ar/nodejs-cpp/specifying-the-absolute-position-of-the-pivot-item/
---

{{% alert color="primary" %}}

أحيانًا، يحتاج المستخدم إلى تحديد الموقع المطلق لعناصر Pivot، وقد كشفت واجهات برمجة التطبيقات Aspose.Cells for Node.js via C++ عن بعض الخصائص والأساليب الجديدة لتحقيق متطلب المستخدم.

- تمت إضافة [**PivotItem.setPosition**](https://reference.aspose.com/cells/nodejs-cpp/pivotitem/#setPosition-number-) الخاصية التي يمكن استخدامها لتحديد مؤشر الموقع في كافة PivotItems بغض النظر عن العقدة الأم. تمت إضافة [**PivotItem.setPositionInSameParentNode**](https://reference.aspose.com/cells/nodejs-cpp/pivotitem/#setPositionInSameParentNode-number-) للخاصية التي يمكن استخدامها لتحديد مؤشر الموقع في PivotItems تحت نفس العقدة الأم.
- تمت إضافة طريقة [**PivotItem.move**](https://reference.aspose.com/cells/nodejs-cpp/pivotitem/#move-number-boolean-) لنقل العنصر لأعلى أو لأسفل بناءً على قيمة العدد، حيث يعد العدد هو عدد الموقع الذي سيتم نقل عنصر الجدول المحوري إليه. إذا كانت قيمة العدد أقل من الصفر، سيتم نقل العنصر لأعلى، بينما إذا كانت قيمة العدد أكبر من الصفر، فإن عنصر الجدول المحوري سيتم نقله لأسفل. يقوم المعامل من نوع Boolean، isSameParent، بتحديد ما إذا كانت العملية المتحركة يجب أن تتم في نفس العقد الأصلي أم لا.
- تم إلغاء طريقة *PivotItem.move(int count)*، لذا يُنصح باستخدام الأسلوب [**PivotItem.move(number, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/pivotitem/#move-number-boolean-) الذي تمت إضافته حديثًا بدلاً من ذلك.

{{% /alert %}}

الشيفرة التجريبية التالية تقوم بإنشاء جدول محوري ثم تحدد مواقع عناصر الجدول المحوري في نفس العقد الأصلي. يمكنك تنزيل [ملف إكسل المصدر](5112632.xlsx) و[ملف إكسل الناتج](5112619.xlsx) للإشارة إليه. إذا قمت بفتح ملف إكسل الناتج، سترى أن عنصر الجدول المحوري "4H12" عند الموضع 0 في العقد "K11" و"DIF400" في الموضع 3. بالمثل، CA32 في الموضع 1 وAAA3 في الموضع 2.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-SpecifyAbsolutePositionOfPivotItem.js" >}}

{{% alert color="primary" %}}

يرجى ملاحظة أنه من الضروري استدعاء طرق PivotTable.RefreshData وPivotTable.CalculateData قبل استخدام الخصائص [**PivotItem.setPosition**](https://reference.aspose.com/cells/nodejs-cpp/pivotitem/#setPosition-number-)، [**PivotItem.setPositionInSameParentNode**](https://reference.aspose.com/cells/nodejs-cpp/pivotitem/#setPositionInSameParentNode-number-) والطريقة [**PivotItem.move**](https://reference.aspose.com/cells/nodejs-cpp/pivotitem/#move-number-boolean-).

{{% /alert %}}

