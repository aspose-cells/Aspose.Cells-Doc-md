---
title: إعادة استخدام كائنات النمط
description: في Aspose.Cells for .NET، من خلال إنشاء كائنات نمط قابلة لإعادة الاستخدام واستخدامها، يمكنك تبسيط إدارة الأنماط وتحسين كفاءة التعليمات البرمجية. سيساعدك دليلنا على الاستفادة من مزايا كائنات النمط القابلة لإعادة الاستخدام وتنفيذها في تطبيقك.
keywords: Aspose.Cells for .NET, Reusing Style Objects, Style Management, Code Efficiency, Reusable Styles, Application Development, API Reference, Example Code, Download, Support.
type: docs
weight: 3000
url: /ar/net/reusing-style-objects/
---
{{% alert color="primary" %}}

يمكن أن تؤدي إعادة استخدام كائنات النمط إلى توفير الذاكرة وجعل البرنامج أسرع.

{{% /alert %}}

لتطبيق بعض التنسيق على نطاق كبير من الخلايا في ورقة العمل:

1. إنشاء كائن نمط.
1. حدد السمات.
1. تطبيق النمط على الخلايا الموجودة في النطاق.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-StylingAndDataFormatting-ReusingStyleObjects-ReusingStyleObjects.cs" >}}

{{% alert color="primary" %}}

 بسبب ال[**Cell.GetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle)/[**Cell.SetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle) يستخدم الأسلوب ذاكرة أقل بكثير، وهو فعال، تمت إزالة خاصية Cell.Style الأقدم التي تستهلك الكثير من الذاكرة غير الضرورية، مع إصدار Aspose.Cells 7.1.0.

{{% /alert %}}
