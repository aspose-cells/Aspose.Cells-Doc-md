---
title: كسر الأسطر وتضمين النص
description: كيفية تطبيق التفاف النص والتفاف الكلمة باستخدام مكتبة Aspose.Cells for Python via .NET. باستخدام مكتبة Aspose.Cells for Python via .NET، يمكنك إدراج النص بسهولة في الخلايا وتعيين طريقة التفاف النص، مثل التفاف يدوي، التفاف الكلمة، إلخ. يوضح هذا المستند كيفية تنفيذ هذه الميزات ويوفر رمز نموذجياً لمرجعتك.
keywords: Aspose.Cells للبايثون via .NET، فواصل الأسطر، التفاف النص، تخطيط النص
type: docs
weight: 60
url: /ar/python-net/line-breaks-and-text-wrapping/
---

{{% alert color="primary" %}}

لضمان قراءة النص في خلية معينة يمكن تطبيق كسرات الأسطر الصريحة وتضمين النص. يحول تضمين النص سطرًا واحدًا إلى عدة أسطر داخل خلية، بينما تضع كسرات الأسطر الصريحة فواصل تمامًا حيث تريدها.

{{% /alert %}}

## **لتضمين النص في خلية**

لتضمين النص في خلية، استخدم الخاصية [**Style.is_text_wrapped**](https://reference.aspose.com/cells/python-net/aspose.cells/style/is_text_wrapped).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-LineBreakTextWrapping-WrapText-1.py" >}}

## **للاستخدام كسرات الأسطر الصريحة**

يمكنك استخدام ' \n' في C# و ' vbLf' في VB.NET لإدراج تقسيم الأسطر الصريحة في الخلية.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-LineBreakTextWrapping-UseExplicitLineBreaks-1.py" >}}

{{< app/cells/assistant language="python-net" >}}
