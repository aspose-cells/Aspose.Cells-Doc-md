---
title: قفل أو فتح الشكل
linktitle: قفل أو فتح الشكل
type: docs
weight: 200
url: /ar/net/lock-or-unlock-shapes/
---

{{% alert color="primary" %}}

أحيانًا، تحتاج إلى حماية جميع الأشكال في بعض الأوراق لمنع تدميرها من قبل مواقف غير مرغوب فيها. في هذه الحالة، تحتاج إلى قفل جميع الأشكال في الورقة المحددة.

أحيانًا، تحتاج إلى تعديل بعض الأشكال في بعض الأوراق المحمية، في هذه الحالة، تحتاج إلى فتح هذه الأشكال.

سيقدم هذا المقال كيفية قفل وفتح الأشكال المحددة بالتفصيل.

{{% /alert %}}

## **حماية جميع الأشكال في ورقة عمل محددة**

لحماية كافة الأشكال في ورقة العمل المحددة، استخدم طريقة [Worksheet.Protect( ProtectionType.Objects)](https://reference.aspose.com/cells/net/aspose.cells/worksheet/protect/#protect)، كما هو موضح في رمز العينة التالي.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Lock-Or-Unlock-Shapes-1.cs" >}}

## **فتح الأشكال المحددة في ورقة عمل محمية**

لفتح الشكل المحدد في ورقة عمل محمية، استخدم [shape.IsLocked](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/islocked/)، كما هو موضح في رمز العينة التالي.

ملاحظة: [shape.IsLocked](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/islocked/) ذو دلالة فقط عندما تكون ورقة العمل محمية.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Lock-Or-Unlock-Shapes-2.cs" >}}

