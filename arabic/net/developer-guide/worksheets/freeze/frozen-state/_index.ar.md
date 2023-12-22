---
title: كيفية التحقق من الحالة المجمدة بدون برنامج Excel.
linktitle: الدولة المجمدة
type: docs
weight: 190
url: /ar/net/how-to-check-frozen-state-of-excel-worksheet
description: ستتعلم في هذه المقالة كيفية التحقق من الحالة المجمدة لورقة عمل Excel برمجيًا باستخدام مكتبة C# مع .NET API.
---
{{% alert color="primary" %}}

في هذه المقالة، سوف نتعلم كيفية التحقق من الحالة المجمدة لورقة عمل إكسل برمجيا.
يمكننا ببساطة معرفة ما إذا كانت ورقة العمل مجمدة أو مقسمة في برنامج MS Excel. ولكن هل هناك طريقة لمعرفة ما إذا كانت مجمدة أو مقسمة باستخدام CSharp.
يمكننا القيام بذلك ببساطة باستخدام Aspose.Cells لـ .Net.
{{% /alert %}}

##  **هل تم تجميد أجزاء النافذة؟**
باستخدام Aspose.Cells لـ .Net، يمكننا التحقق مما إذا كانت النافذة مجمدة وعدد الصفوف والأعمدة المقفلة.

 الرجاء استخدام[**ورقة عمل.PaneState**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/PaneState/) الخاصية للتحقق من حالة أجزاء النافذة
 ويحصل على الصفوف والأعمدة المقفلة[**ورقة عمل.GetFreezedPanes**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/GetFreezedPanes/)طريقة.
1. إنشاء مصنف لفتح الملف.
2. تحقق مما إذا كانت ورقة العمل مجمدة.
3. يحصل على الصف والأعمدة المقفلة

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Is-Worksheet-Frozen.cs" >}}