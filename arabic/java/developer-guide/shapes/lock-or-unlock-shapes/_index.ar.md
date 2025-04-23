---
title: قفل أو فتح الشكل
linktitle: قفل أو فتح الشكل
type: docs
weight: 200
url: /ar/java/lock-or-unlock-shapes/
---

{{% alert color="primary" %}}

أحيانًا، تحتاج إلى حماية جميع الأشكال في بعض الأوراق لمنع تدميرها من قبل مواقف غير مرغوب فيها. في هذه الحالة، تحتاج إلى قفل جميع الأشكال في الورقة المحددة.

أحيانًا، تحتاج إلى تعديل بعض الأشكال في بعض الأوراق المحمية، في هذه الحالة، تحتاج إلى فتح هذه الأشكال.

سيقدم هذا المقال كيفية قفل وفتح الأشكال المحددة بالتفصيل.

{{% /alert %}}

## **حماية جميع الأشكال في ورقة عمل محددة**

لحماية جميع الأشكال في ورقة عمل محددة، استخدم طريقة [Worksheet.protect(int type)](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet/#protect-int-). كما هو موضح في الشفرة البرمجية عينة التالية.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Lock-Or-Unlock-Shapes-1.java" >}}

## **فتح الأشكال المحددة في ورقة عمل محمية**

لفتح شكل محدد في ورقة عمل محمية، استخدم [shape.IsLocked](https://reference.aspose.com/cells/java/com.aspose.cells/shape/#isLocked--) و [shape.setLocked](https://reference.aspose.com/cells/java/com.aspose.cells/shape/#setLocked-boolean-). كما هو موضح في الشفرة البرمجية عينة التالية.

ملاحظة: [shape.IsLocked](https://reference.aspose.com/cells/java/com.aspose.cells/shape/#isLocked--) و [shape.setLocked](https://reference.aspose.com/cells/java/com.aspose.cells/shape/#setLocked-boolean-) ذات معنى فقط عندما تكون الورقة محمية.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Lock-Or-Unlock-Shapes-2.java" >}}

{{< app/cells/assistant language="java" >}}
