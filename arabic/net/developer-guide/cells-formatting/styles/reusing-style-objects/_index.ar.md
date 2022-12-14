---
title: إعادة استخدام كائنات النمط
type: docs
weight: 3000
url: /ar/net/reusing-style-objects/
---
{{% alert color="primary" %}}

يمكن أن تؤدي إعادة استخدام كائنات النمط إلى توفير الذاكرة وجعل البرنامج أسرع.

{{% /alert %}}

لتطبيق بعض التنسيقات على نطاق كبير من الخلايا في ورقة عمل:

1. قم بإنشاء كائن نمط.
1. حدد السمات.
1. قم بتطبيق النمط على الخلايا الموجودة في النطاق.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-StylingAndDataFormatting-ReusingStyleObjects-ReusingStyleObjects.cs" >}}

{{% alert color="primary" %}}

 بسبب ال[**Cell.GetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle)/[**Cell.SetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle) يستخدم الأسلوب ذاكرة أقل بكثير ، وهو فعال ، تمت إزالة خاصية النمط Cell الأقدم التي استهلكت الكثير من الذاكرة غير الضرورية ، مع إصدار Aspose.Cells 7.1.0.

{{% /alert %}}
