---
title: قم بتحميل Html إلى Excel باستخدام StreamProvider
type: docs
weight: 80
url: /ar/net/convert-html-to-excel-with-streamprovider/
---
{{% alert color="primary" %}} 

عند تحميل ملفات html التي تحتوي على موارد خارجية ، فإننا نواجه مشكلتين التاليتين:
1. عند تحميل دفق html ، لا يمكن الحصول على الصور والموارد الخارجية المشار إليها بواسطة ملف html من خلال المسارات النسبية.
1. يجب تعيين مسارات الموارد الخارجية المشار إليها في ملفات html

 تشرح هذه المقالة كيفية التنفيذ[IStreamProvider](https://reference.aspose.com/cells/net/aspose.cells/istreamprovider) واجهة لتعيين[HtmlLoadOptions.StreamProvider](https://reference.aspose.com/cells/net/aspose.cells/htmlloadoptions/streamprovider/) منشأه. من خلال تنفيذ هذه الواجهة ، ستتمكن من تحميل موارد خارجية أثناء تحميل تدفقات Html أو تكون هذه الموارد الخارجية نسبية.

{{% /alert %}} 

 هذا هو الكود الرئيسي الذي يوضح استخدام[HtmlLoadOptions.StreamProvider](https://reference.aspose.com/cells/net/aspose.cells/htmlloadoptions/streamprovider/)منشأه



{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Load-Html-With-StreamProvider.cs" >}}
