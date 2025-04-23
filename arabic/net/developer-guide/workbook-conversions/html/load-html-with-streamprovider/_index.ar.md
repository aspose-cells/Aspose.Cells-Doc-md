---
title: تحميل HTML إلى Excel باستخدام StreamProvider
type: docs
weight: 80
url: /ar/net/convert-html-to-excel-with-streamprovider/
---

{{% alert color="primary" %}} 

عندما تحمل ملفات HTML التي تحتوي على موارد خارجية، نواجه غالبًا مشكلتين:
1. عندما يتم تحميل تدفق HTML، لا يمكن الحصول على الصور والموارد الخارجية المشار إليها في ملف HTML من خلال المسارات النسبية.
1. يجب تعيين مسارات الموارد الخارجية المشار إليها في ملفات HTML

يشرح هذا المقال كيفية تنفيذ واجهة البرمجة المساعدة [IStreamProvider](https://reference.aspose.com/cells/net/aspose.cells/istreamprovider) لضبط خاصية [HtmlLoadOptions.StreamProvider](https://reference.aspose.com/cells/net/aspose.cells/htmlloadoptions/streamprovider/) . من خلال تنفيذ هذه الواجهة، ستتمكن من تحميل الموارد الخارجية أثناء تحميل تدفقات Html أو أن يتم تحميل هذه الموارد الخارجية نسبيًا.

{{% /alert %}} 

هذا هو الكود الرئيسي الذي يظهر استخدام [HtmlLoadOptions.StreamProvider](https://reference.aspose.com/cells/net/aspose.cells/htmlloadoptions/streamprovider/) .



{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Load-Html-With-StreamProvider.cs" >}}
{{< app/cells/assistant language="csharp" >}}
