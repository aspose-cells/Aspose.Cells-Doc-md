---
title: فواصل الأسطر والتفاف النص مع Golang عبر C++
description: كيفية تنفيذ التفاف النص وتغليف الكلمات باستخدام مكتبة Aspose.Cells في C++. من خلال استخدام مكتبة Aspose.Cells، يمكنك إدراج النص بسهولة في الخلايا وتعيين طريقة التفاف النص، مثل التفاف الكلمات اليدوي، والتفاف الكلمات، وغيرها. يوضح هذا المستند كيفية تنفيذ هذه الميزات ويقدم رمزًا نموذجيًا لمرجعك.
keywords: Aspose.Cells، تقسيم الأسطر، تفصيل النص، تخطيط النص
type: docs
weight: 60
url: /ar/go-cpp/line-breaks-and-text-wrapping/
---

{{% alert color="primary" %}}

لضمان قراءة النص في خلية معينة يمكن تطبيق كسرات الأسطر الصريحة وتضمين النص. يحول تضمين النص سطرًا واحدًا إلى عدة أسطر داخل خلية، بينما تضع كسرات الأسطر الصريحة فواصل تمامًا حيث تريدها.

{{% /alert %}}

## **لتضمين النص في خلية**

لتغليف النص في خلية، استخدم الخاصية [**Aspose.Cells.Style.IsTextWrapped**](https://reference.aspose.com/cells/go-cpp/style/istextwrapped/).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-LineBreaksAndTextWrapping.go" >}}
## **للاستخدام كسرات الأسطر الصريحة**

يمكنك استخدام ‘\n’ في C++ لإدراج فواصل أسطر صريحة داخل خلية.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-LineBreaksAndTextWrapping-1.go" >}}
