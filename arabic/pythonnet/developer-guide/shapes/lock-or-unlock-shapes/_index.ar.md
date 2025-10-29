---
title: قفل أو فتح الشكل
linktitle: قفل أو فتح الشكل
type: docs
weight: 200
url: /ar/python-net/lock-or-unlock-shapes/
---

{{% alert color="primary" %}}

أحيانًا، تحتاج إلى حماية جميع الأشكال في بعض الأوراق لمنع تدميرها من قبل مواقف غير مرغوب فيها. في هذه الحالة، تحتاج إلى قفل جميع الأشكال في الورقة المحددة.

أحيانًا، تحتاج إلى تعديل بعض الأشكال في بعض الأوراق المحمية، في هذه الحالة، تحتاج إلى فتح هذه الأشكال.

سيقدم هذا المقال كيفية قفل وفتح الأشكال المحددة بالتفصيل.

{{% /alert %}}

## **حماية جميع الأشكال في ورقة عمل محددة**

لحماية جميع الأشكال في ورقة العمل المحددة، استخدم الأسلوب [Worksheet.Protect(type)](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/protect/#aspose.cells.ProtectionType)، كما هو موضح في الشيفرة المثالية التالية.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Lock-Or-Unlock-Shapes-1.py" >}}

## **فتح الأشكال المحددة في ورقة عمل محمية**

لفتح شكل معين في ورقة العمل المحمية، استخدم [shape.is_locked](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/is_locked/)، كما هو موضح في الشيفرة المثالية التالية.

ملاحظة: [shape.is_locked](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/is_locked/) له معنى فقط عندما تكون ورقة العمل محمية.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Lock-Or-Unlock-Shapes-2.py" >}}

{{< app/cells/assistant language="python-net" >}}
