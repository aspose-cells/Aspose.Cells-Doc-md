---
title: قم بتحميل Html إلى Excel باستخدام StreamProvider
type: docs
weight: 80
url: /ar/java/convert-html-to-excel-with-streamprovider/
---
{{% alert color="primary" %}} 

عند تحميل html الذي يحتوي على موارد خارجية ، فإننا نواجه مشكلتين التاليتين:
1. عند تحميل دفق html ، لا يمكن الحصول على الصور والموارد الخارجية المشار إليها بواسطة ملف html من خلال المسارات النسبية.
1. يجب تعيين مسارات الموارد الخارجية المشار إليها في ملفات html.

 تشرح هذه المقالة كيفية التنفيذ[**IStreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/IStreamProvider) واجهة لتعيين[**HtmlLoadOptions.StreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlloadoptions#StreamProvider) خاصية. من خلال تنفيذ هذه الواجهة ، ستتمكن من تحميل موارد خارجية أثناء تحميل تدفقات Html أو تكون هذه الموارد الخارجية نسبية.

{{% /alert %}} 

هذا هو الكود الرئيسي الذي يوضح استخدام[**HtmlLoadOptions.StreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlloadoptions#StreamProvider)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Load-Html-With-StreamProvider.java" >}}
