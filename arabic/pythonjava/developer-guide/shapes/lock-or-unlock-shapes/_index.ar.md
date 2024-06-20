---
title: قفل أو فتح الشكل
linktitle: قفل أو فتح الشكل
type: docs
weight: 200
url: /ar/python-java/lock-or-unlock-shapes/
---

{{% alert color="primary" %}}

أحيانًا، تحتاج إلى حماية جميع الأشكال في بعض الأوراق لمنع تدميرها من قبل مواقف غير مرغوب فيها. في هذه الحالة، تحتاج إلى قفل جميع الأشكال في الورقة المحددة.

أحيانًا، تحتاج إلى تعديل بعض الأشكال في بعض الأوراق المحمية، في هذه الحالة، تحتاج إلى فتح هذه الأشكال.

سيقدم هذا المقال كيفية قفل وفتح الأشكال المحددة بالتفصيل.

{{% /alert %}}

## **حماية جميع الأشكال في ورقة عمل محددة**

لحماية جميع الأشكال في صفحة العمل المحددة، استخدم طريقة [Worksheet.Protect(type)](https://reference.aspose.com/cells/python-java/asposecells.api/worksheet#protect(int))، كما هو موضح في الشيفرة البرمجية العينية التالية.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Lock-Or-Unlock-Shapes-1.py" >}}

## **فتح الأشكال المحددة في ورقة عمل محمية**

لفتح الشكل المحدد في صفحة العمل المحمية، استخدم [shape.IsLocked](https://reference.aspose.com/cells/python-java/asposecells.api/shape#IsLocked)، كما هو موضح في الشيفرة البرمجية العينية التالية.

ملاحظة: [shape.IsLocked](https://reference.aspose.com/cells/python-java/asposecells.api/shape#IsLocked) معنوي فقط عندما تكون صفحة العمل محمية.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Lock-Or-Unlock-Shapes-2.py" >}}

