---
title: إعادة استخدام كائنات النمط
description: في Aspose.Cells لبايثون via .NET، يمكنك تبسيط إدارة الأنماط وتحسين كفاءة الشفرة من خلال إنشاء واستخدام كائنات أنماط قابلة لإعادة الاستخدام. ستساعدك دليلنا على الاستفادة من مزايا هذه الكائنات وتنفيذها في تطبيقك.
keywords: Aspose.Cells لبايثون via .NET، إعادة استخدام كائنات النمط، إدارة الأنماط، كفاءة الشفرة، أنماط قابلة لإعادة الاستخدام، تطوير التطبيق، مرجع API، مثال على الشفرة، التحميل، الدعم
type: docs
weight: 3000
url: /ar/python-net/reusing-style-objects/
---

{{% alert color="primary" %}}

يمكن لإعادة استخدام كائنات النمط توفير الذاكرة وجعل البرنامج أسرع.

{{% /alert %}}

لتطبيق بعض التنسيق على مجموعة كبيرة من الخلايا في ورقة العمل:

1. إنشاء كائن النمط.
1. تحديد السمات.
1. تطبيق النمط على الخلايا في النطاق.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-ReusingStyleObjects.py" >}}

{{% alert color="primary" %}}

نظرًا لأن النهج [**Cell.get_style**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_style)/[**Cell.set_style**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/set_style) يستخدم أقل من الذاكرة بكثير، وهو كفء، تمت إزالة خاصية Cell.Style القديمة التي كانت تستهلك الكثير من الذاكرة غير الضرورية مع إصدار Aspose.Cells 7.1.0.

{{% /alert %}}
{{< app/cells/assistant language="python-net" >}}
