---
title: تحديد الموقع المطلق لعنصر الجدول المحوري
type: docs
weight: 50
url: /ar/net/specifying-the-absolute-position-of-the-pivot-item/
---

{{% alert color="primary" %}}

بعض الأحيان، يحتاج المستخدم إلى تحديد الموقع المطلق لعناصر الجدول المحوري، وقد قامت واجهة برمجة التطبيقات لـ Aspose.Cells بفتح بعض الخصائص الجديدة والطريقة لتحقيق متطلبات المستخدم.

- تمت إضافة [**PivotItem.Position**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotitem/properties/position) الخاصية التي يمكن استخدامها لتحديد مؤشر الموقع في كافة PivotItems بغض النظر عن العقدة الأم. تمت إضافة [**PivotItem.PositionInSameParentNode**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotitem/properties/positioninsameparentnode) للخاصية التي يمكن استخدامها لتحديد مؤشر الموقع في PivotItems تحت نفس العقدة الأم.
- تمت إضافة طريقة [**PivotItem.Move(int count, bool isSameParent)**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotitem/methods/move) لنقل العنصر لأعلى أو لأسفل بناءً على قيمة العدد، حيث يعد العدد هو عدد الموقع الذي سيتم نقل عنصر الجدول المحوري إليه. إذا كانت قيمة العدد أقل من الصفر، سيتم نقل العنصر لأعلى، بينما إذا كانت قيمة العدد أكبر من الصفر، فإن عنصر الجدول المحوري سيتم نقله لأسفل. يقوم المعامل من نوع Boolean، isSameParent، بتحديد ما إذا كانت العملية المتحركة يجب أن تتم في نفس العقد الأصلي أم لا.
- تم تجاهل *طريقة PivotItem.Move(int count)* ومن ثم يُفضل استخدام الطريقة المضافة حديثًا [**PivotItem.Move(int count, bool isSameParent)**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotitem/methods/move) بدلاً منها.

{{% /alert %}}

الشيفرة التجريبية التالية تقوم بإنشاء جدول محوري ثم تحدد مواقع عناصر الجدول المحوري في نفس العقد الأصلي. يمكنك تنزيل [ملف إكسل المصدر](5112632.xlsx) و[ملف إكسل الناتج](5112619.xlsx) للإشارة إليه. إذا قمت بفتح ملف إكسل الناتج، سترى أن عنصر الجدول المحوري "4H12" عند الموضع 0 في العقد "K11" و"DIF400" في الموضع 3. بالمثل، CA32 في الموضع 1 وAAA3 في الموضع 2.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-PivotTablesAndPivotCharts-SpecifyAbsolutePositionOfPivotItem-SpecifyAbsolutePositionOfPivotItem.cs" >}}

{{% alert color="primary" %}}

يرجى ملاحظة أنه من الضروري استدعاء طرق PivotTable.RefreshData وPivotTable.CalculateData قبل استخدام الخصائص [**PivotItem.Position**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotitem/properties/position)، [**PivotItem.PositionInSameParentNode**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotitem/properties/positioninsameparentnode) والطريقة [**PivotItem.Move(int count, bool isSameParent)**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotitem/methods/move).

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
