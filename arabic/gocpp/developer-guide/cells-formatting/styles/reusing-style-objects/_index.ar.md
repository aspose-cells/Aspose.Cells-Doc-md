---
title: إعادة استخدام كائنات النمط مع Golang عبر C++
linktitle: إعادة استخدام كائنات النمط
description: في Aspose.Cells for C++، يمكنك من خلال إنشاء واستخدام كائنات نمط قابلة لإعادة الاستخدام تبسيط إدارة الأنماط وتحسين كفاءة الكود. ستساعدك دليلاتنا على استغلال مزايا الكائنات النمطية المعاد استخدامها وتنفيذها في تطبيقك.
keywords: Aspose.Cells for C++، إعادة استخدام كائنات النمط، إدارة النمط، كفاءة الكود، أنماط قابلة لإعادة الاستخدام، تطوير التطبيقات، مرجع API، كود نموذجي، تحميل، دعم.
type: docs
weight: 3000
url: /ar/go-cpp/reusing-style-objects/
---

{{% alert color="primary" %}}

يمكن لإعادة استخدام كائنات النمط توفير الذاكرة وجعل البرنامج أسرع.

{{% /alert %}}

لتطبيق بعض التنسيق على مجموعة كبيرة من الخلايا في ورقة العمل:

1. إنشاء كائن النمط.
1. تحديد السمات.
1. تطبيق النمط على الخلايا في النطاق.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ReusingStyleObjects.go" >}}
{{% alert color="primary" %}}

نظرًا لأن النهج [**Cell.GetStyle**](https://reference.aspose.com/cells/go-cpp/cell/getstyle/)/[**Cell.SetStyle**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/setstyle/) يستخدم أقل من الذاكرة بكثير، وهو كفء، تمت إزالة خاصية Cell.Style القديمة التي كانت تستهلك الكثير من الذاكرة غير الضرورية مع إصدار Aspose.Cells 7.1.0.

{{% /alert %}}
