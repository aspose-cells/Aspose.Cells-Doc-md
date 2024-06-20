---
title: كيفية التحقق من الحالة المجمدة وذلك بدون إكسل.
linktitle: الحالة المجمدة
type: docs
weight: 190
url: /ar/net/how-to-check-frozen-state-of-excel-worksheet
description: في هذه المقالة، ستتعلم كيفية فحص حالة تجميد ورقة عمل إكسيل برمجياً باستخدام مكتبة C# مع واجهة برمجة تطبيقات .NET.

---

## **مقدمة**

في هذا المقال، سوف نتعلم كيفية التحقق من حالة تجميد ورقة العمل في إكسل برمجيًا. يمكننا ببساطة العثور على ما إذا كانت ورقة العمل قد تم تجميدها أم تقسيمها في MS Excel. ولكن هل هناك طريقة لمعرفة ما إذا كانت مجمدة أم مقسمة بـ CSharp. يمكننا ببساطة القيام بذلك باستخدام Aspose.Cells for .Net.

## **هل النوافذ مجمدة**
مع Aspose.Cells لـ .Net، يمكننا التحقق ما إذا كانت النافذة مجمدة وكم عدد الصفوف والأعمدة مقفلة.

يرجى استخدام الخاصية [**Worksheet.PaneState**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/PaneState/) لفحص حالة النوافذ 
والحصول على الصفوف والأعمدة المقفلة باستخدام الطريقة [**Worksheet.GetFreezedPanes**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/GetFreezedPanes/).
1. إنشاء سجل العمل لفتح الملف.
2. التحقق ما إذا كانت ورقة العمل مجمدة.
3. الحصول على الصفوف والأعمدة المقفلة

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Is-Worksheet-Frozen.cs" >}}
