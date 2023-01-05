---
title: تحديد الموضع المطلق للعنصر المحوري
type: docs
weight: 50
url: /ar/net/specifying-the-absolute-position-of-the-pivot-item/
---
{{% alert color="primary" %}}

في بعض الأحيان ، يحتاج المستخدم إلى تحديد الموضع المطلق للعناصر المحورية ، وقد كشف Aspose.Cells API عن بعض الخصائص الجديدة وطريقة لتحقيق متطلبات المستخدم.

-  مضاف[**PivotItem. الوظيفة**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotitem/properties/position) الخاصية التي يمكن استخدامها لتحديد فهرس الموضع في جميع عناصر PivotItems بغض النظر عن العقدة الأصلية. مضاف[**PivotItem.PositionInSameParentNode**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotitem/properties/positioninsameparentnode) الخاصية التي يمكن استخدامها لتحديد فهرس الموضع في PivotItems ضمن نفس العقدة الأصلية.
-  مضاف[**PivotItem.Move (عدد صحيح ، منطقي هو نفس الأصل)**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotitem/methods/move)لتحريك العنصر لأعلى أو لأسفل استنادًا إلى قيمة الجرد ، حيث يكون العدد هو رقم الموضع لتحريك PivotItem لأعلى أو لأسفل. إذا كانت قيمة العد أقل من الصفر ، فسيتم نقل العنصر لأعلى حيث كما لو كانت قيمة العد أكبر من الصفر ، سينتقل PivotItem إلى أسفل ، والنوع المنطقي هو نفس المعلمة الأصلية تحدد ما إذا كان يجب تنفيذ عملية النقل في نفس العقدة الأصلية أم لا.
-  عفا عليها الزمن*PivotItem.Move (عدد العمليات)* لذلك يُقترح استخدام الطريقة المضافة حديثًا[**PivotItem.Move (عدد صحيح ، منطقي هو نفس الأصل)**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotitem/methods/move) بدلاً من.

{{% /alert %}}

 ينشئ نموذج التعليمات البرمجية التالي جدولاً محوريًا ثم يحدد مواضع العناصر المحورية في نفس العقدة الأصلية. يمكنك تنزيل ملف[مصدر Excel](5112632.xlsx) و[الإخراج إكسل](5112619.xlsx) ملفات للرجوع اليها. إذا فتحت ملف Excel الناتج ، فسترى العنصر المحوري "4H12" في الموضع 0 في الأصل "K11" و "DIF400" في المركز الثالث. وبالمثل ، فإن CA32 في الموضع 1 و AAA3 في الموضع 2

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-PivotTablesAndPivotCharts-SpecifyAbsolutePositionOfPivotItem-SpecifyAbsolutePositionOfPivotItem.cs" >}}

{{% alert color="primary" %}}

يرجى ملاحظة أنه من الضروري استدعاء أساليب PivotTable.RefreshData و PivotTable.CalculateData قبل استخدام[**PivotItem. الوظيفة**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotitem/properties/position), [**PivotItem.PositionInSameParentNode**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotitem/properties/positioninsameparentnode) خصائص و[**PivotItem.Move (عدد صحيح ، منطقي هو نفس الأصل)**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotitem/methods/move) طريقة.

{{% /alert %}}
