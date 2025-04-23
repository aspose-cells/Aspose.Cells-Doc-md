---
title: إعادة استخدام كائنات النمط
description: في Aspose.Cells Aspose.Cells for .NET، من خلال إنشاء واستخدام كائنات نمط قابلة لإعادة الاستخدام، يمكنك تبسيط إدارة الأنماط وتحسين كفاءة الكود. سيساعدك دليلنا على الاستفادة من مزايا كائنات النمط قابلة لإعادة الاستخدام وتنفيذها في تطبيقك.
keywords: Aspose.Cells for .NET, إعادة استخدام كائنات النمط, إدارة النمط, كفاءة الكود, أنماط قابلة لإعادة الاستخدام, تطوير التطبيقات, مرجع الواجهة البرمجية للتطبيقات, كود المثال, تنزيل, دعم.
type: docs
weight: 3000
url: /ar/net/reusing-style-objects/
---

{{% alert color="primary" %}}

يمكن لإعادة استخدام كائنات النمط توفير الذاكرة وجعل البرنامج أسرع.

{{% /alert %}}

لتطبيق بعض التنسيق على مجموعة كبيرة من الخلايا في ورقة العمل:

1. إنشاء كائن النمط.
1. تحديد السمات.
1. تطبيق النمط على الخلايا في النطاق.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-StylingAndDataFormatting-ReusingStyleObjects-ReusingStyleObjects.cs" >}}

{{% alert color="primary" %}}

نظرًا لأن النهج [**Cell.GetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle)/[**Cell.SetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle) يستخدم أقل من الذاكرة بكثير، وهو كفء، تمت إزالة خاصية Cell.Style القديمة التي كانت تستهلك الكثير من الذاكرة غير الضرورية مع إصدار Aspose.Cells 7.1.0.

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
