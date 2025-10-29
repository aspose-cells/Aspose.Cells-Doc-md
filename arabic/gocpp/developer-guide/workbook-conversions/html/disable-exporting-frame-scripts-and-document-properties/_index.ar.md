---
title: تعطيل تصدير نصوص الإطار وخصائص المستند باستخدام Golang عبر C++
type: docs
weight: 310
url: /ar/go-cpp/disable-exporting-frame-scripts-and-document-properties/
description: تعطيل تصدير نصوص الإطار وخصائص المستند باستخدام Aspose.Cells مع Golang عبر C++.
---

{{% alert color="primary" %}}

يقوم Aspose.Cells بتصدير برامج الإطار وخصائص المستند أثناء تحويل دفتر العمل إلى HTML. الإصدار 8.6.0 من Aspose.Cells for C++ يوفر خيارًا يتيح لك تعطيل تصدير برامج الإطار وخصائص المستند بشكل اختياري. يرجى استخدام الخاصية HtmlSaveOptions.ExportFrameScriptsAndProperties لتعطيل التصدير.

{{% /alert %}}

## **تعطيل تصدير الإطارات النصية وخصائص المستند**

الشيفرة النموذجية التالية تتيح لك تعطيل تصدير الإطارات النصية وخصائص المستند. بمجرد تحويل دفتر العمل إلى HTML، لن يحتوي الملف الناتج على أي إطارات نصية أو خصائص مستند.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DisableExportingFrameScriptsAndDocumentProperties.go" >}}
