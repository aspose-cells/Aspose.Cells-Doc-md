---
title: احفظ Html مع StreamProvider
type: docs
weight: 120
url: /ar/java/convert-excel-to-html-with-streamprovider/
---
{{% alert color="primary" %}}

عند تحويل ملفات Excel التي تحتوي على صور وأشكال إلى ملفات html ، فإننا نواجه المسألتين التاليتين:
1. أين يجب أن نحفظ الصور والأشكال عند حفظ ملف Excel في دفق html.
1. استبدل المسار الافتراضي بالمسار المستثنى.

 تشرح هذه المقالة كيفية التنفيذ[**IStreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/IStreamProvider) واجهة لتعيين[**HtmlSaveOptions.StreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#StreamProvider) منشأه. من خلال تنفيذ هذه الواجهة ، ستتمكن من حفظ الموارد التي تم إنشاؤها أثناء إنشاء HTML في مواقعك المحددة أو تدفقات الذاكرة.

{{% /alert %}}

## عينة من الرموز

 هذا هو الكود الرئيسي الذي يوضح استخدام[**HtmlSaveOptions.StreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#StreamProvider)منشأه

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-HtmlSaveOptions-HtmlSaveOptions.java" >}}

 هنا هو رمز*ExportStreamProvider* الطبقة التي تنفذ[**IStreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/IStreamProvider)الواجهة المستخدمة داخل الكود أعلاه.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ExportStreamProvider-ExportStreamProvider.java" >}}

