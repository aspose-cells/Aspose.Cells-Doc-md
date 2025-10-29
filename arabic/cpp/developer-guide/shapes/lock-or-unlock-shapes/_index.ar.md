---
title: قفل أو فتح الشكل
linktitle: قفل أو فتح الشكل
type: docs
weight: 200
url: /ar/cpp/lock-or-unlock-shapes/
---

{{% alert color="primary" %}}

أحيانًا، تحتاج إلى حماية جميع الأشكال في بعض الأوراق لمنع تدميرها من قبل مواقف غير مرغوب فيها. في هذه الحالة، تحتاج إلى قفل جميع الأشكال في الورقة المحددة.

أحيانًا، تحتاج إلى تعديل بعض الأشكال في بعض الأوراق المحمية، في هذه الحالة، تحتاج إلى فتح هذه الأشكال.

سيقدم هذا المقال كيفية قفل وفتح الأشكال المحددة بالتفصيل.

{{% /alert %}}

## **حماية جميع الأشكال في ورقة عمل محددة**

لحماية جميع الأشكال في صفحة العمل المحددة، استخدم طريقة [Worksheet.Protect(ProtectionType)](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/protect/)، كما هو موضح في الشيفرة العينية التالية.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Lock-Or-Unlock-Shapes-1.cpp" >}}

## **فتح الأشكال المحددة في ورقة عمل محمية**

لفتح الشكل المحدد في صفحة العمل المحمية، استخدم [shape.IsLocked](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/islocked/) و [shape.SetIsLocked](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/setislocked/)، كما هو موضح في الشيفرة العينية التالية.

ملاحظة: [shape.IsLocked](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/islocked/) و [shape.SetIsLocked](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/setislocked/) لهما معنى فقط عندما تكون الصفحة العمل محمية.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Lock-Or-Unlock-Shapes-2.cpp" >}}

{{< app/cells/assistant language="cpp" >}}
