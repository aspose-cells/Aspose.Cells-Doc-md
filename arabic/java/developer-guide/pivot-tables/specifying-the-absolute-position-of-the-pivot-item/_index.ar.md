---
title: تحديد الموضع المطلق للعنصر المحوري
type: docs
weight: 40
url: /ar/java/specifying-the-absolute-position-of-the-pivot-item/
---
{{% alert color="primary" %}}

في بعض الأحيان ، يحتاج المستخدم إلى تحديد الموضع المطلق للعناصر المحورية ، وقد كشف Aspose.Cells API بعض الخصائص الجديدة وطريقة لتحقيق متطلبات المستخدم هذه.

-  مضاف[**PivotItem.setPosition ()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotitem#Position) الخاصية التي يمكن استخدامها لتحديد فهرس الموضع في جميع عناصر PivotItems بغض النظر عن العقدة الأصلية. مضاف[**PivotItem.setPositionInSameParentNode ()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotitem#PositionInSameParentNode) الخاصية التي يمكن استخدامها لتحديد فهرس الموضع في PivotItems ضمن نفس العقدة الأصلية.
-  مضاف[**PivotItem.move (عدد صحيح ، منطقي هو نفس الوالدين)**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotitem#move(int,%20boolean)لتحريك العنصر لأعلى أو لأسفل استنادًا إلى قيمة الجرد ، حيث يكون العدد هو عدد المواضع لتحريك PivotItem لأعلى أو لأسفل. إذا كانت قيمة العدد أقل من الصفر ، فسيتم نقل العنصر لأعلى بينما إذا كانت قيمة العدد أكبر من الصفر ، سينتقل PivotItem لأسفل ، والنوع المنطقي هو المعلمة SameParent التي تحدد ما إذا كان يجب تنفيذ عملية النقل في نفس العقدة الأصلية أو ليس.
-  عفا عليها الزمن*PivotItem.move (العدد الفعلي)* الطريقة ، لذلك ، يُقترح استخدام الطريقة المضافة حديثًا[**PivotItem.move (عدد صحيح ، منطقي هو نفس الوالدين)**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotitem#move(int,%20boolean)) في حين أن.

 يرجى ملاحظة أنه من الضروري الاتصال بـ[**PivotTable.refreshData**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#refreshData() ) و[**PivotTable.calculateData**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#calculateData() ) قبل الاستخدام[**PivotItem.setPosition ()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotitem#Position), [**PivotItem.setPositionInSameParentNode ()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotitem#PositionInSameParentNode) خصائص و[**PivotItem.move (عدد صحيح ، منطقي هو نفس الوالدين)**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotitem#move(int,%20boolean)) طريقة.

{{% /alert %}}

## عينة من الرموز

ينشئ نموذج التعليمات البرمجية التالي جدولاً محوريًا ثم يحدد مواضع العناصر المحورية في نفس العقدة الأصلية.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SpecifyAbsolutePositionOfPivotItem-SpecifyAbsolutePositionOfPivotItem.java" >}}
