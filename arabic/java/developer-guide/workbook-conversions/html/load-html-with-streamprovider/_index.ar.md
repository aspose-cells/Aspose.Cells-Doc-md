---
title: تحميل HTML إلى Excel باستخدام StreamProvider
type: docs
weight: 80
url: /ar/java/convert-html-to-excel-with-streamprovider/
---

{{% alert color="primary" %}} 

عند تحميل HTML الذي يحتوي على موارد خارجية، نواجه غالبًا المشكلتين التاليتين:
1. عندما يتم تحميل تدفق HTML، لا يمكن الحصول على الصور والموارد الخارجية المشار إليها في ملف HTML من خلال المسارات النسبية.
1. يجب تعيين مسارات الموارد الخارجية المشار إليها في ملفات HTML.

يشرح هذا المقال كيفية تنفيذ واجهة [**IStreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/IStreamProvider) لضبط خاصية [**HtmlLoadOptions.StreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlloadoptions#StreamProvider). من خلال تنفيذ هذه الواجهة، ستكون قادرًا على تحميل الموارد الخارجية أثناء تحميل تيارات HTML أو أن تكون هذه الموارد الخارجية نسبية.

{{% /alert %}} 

هذا هو الكود الرئيسي الذي يظهر استخدام [**HtmlLoadOptions.StreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlloadoptions#StreamProvider)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Load-Html-With-StreamProvider.java" >}}
{{< app/cells/assistant language="java" >}}
