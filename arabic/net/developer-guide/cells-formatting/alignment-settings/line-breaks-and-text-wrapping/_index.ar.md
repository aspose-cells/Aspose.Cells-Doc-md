---
title: كسر الأسطر وتضمين النص
description: كيفية تنفيذ تفصيل النص وتقسيم الكلمات باستخدام مكتبة Aspose.Cells في C#. من خلال استخدام مكتبة Aspose.Cells، يمكنك بسهولة إدراج نص في الخلايا وضبط طريقة تفصيل النص، مثل تفصيل النص اليدوي، تفصيل النص، إلخ. يوضح هذا المستند كيفية تنفيذ هذه الميزات ويوفر شيفرة نموذجية للرجوع إليها.
keywords: Aspose.Cells، تقسيم الأسطر، تفصيل النص، تخطيط النص
type: docs
weight: 60
url: /ar/net/line-breaks-and-text-wrapping/
---

{{% alert color="primary" %}}

لضمان قراءة النص في خلية معينة يمكن تطبيق كسرات الأسطر الصريحة وتضمين النص. يحول تضمين النص سطرًا واحدًا إلى عدة أسطر داخل خلية، بينما تضع كسرات الأسطر الصريحة فواصل تمامًا حيث تريدها.

{{% /alert %}}

## **لتضمين النص في خلية**

لتضمين النص في خلية، استخدم الخاصية [**Aspose.Cells.Style.IsTextWrapped**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/istextwrapped).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-LineBreakTextWrapping-WrapText-1.cs" >}}

## **للاستخدام كسرات الأسطر الصريحة**

يمكنك استخدام ' \n' في C# و ' vbLf' في VB.NET لإدراج تقسيم الأسطر الصريحة في الخلية.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-LineBreakTextWrapping-UseExplicitLineBreaks-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
