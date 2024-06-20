---
title: حفظ Html باستخدام StreamProvider
type: docs
weight: 120
url: /ar/java/convert-excel-to-html-with-streamprovider/
---

{{% alert color="primary" %}}

عند تحويل ملفات إكسل التي تحتوي على صور وأشكال إلى ملفات HTML، نواجه غالبًا المشكلتين التاليتين:
1.أين يجب أن نحفظ الصور والأشكال عند حفظ ملف Excel إلى تدفق HTML.
1. استبدال المسار الافتراضي بالمسار المتوقع.

يشرح هذا المقال كيفية تنفيذ واجهة [**IStreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/IStreamProvider) لضبط خاصية [**HtmlSaveOptions.StreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#StreamProvider). من خلال تنفيذ هذه الواجهة، ستتمكن من حفظ الموارد التي تم إنشاؤها أثناء إنشاء HTML إلى مواقعك الخاصة أو تدفقات الذاكرة.

{{% /alert %}}

## كود عينة

هذا هو الكود الرئيسي الذي يظهر استخدام الخاصية [**HtmlSaveOptions.StreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#StreamProvider).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-HtmlSaveOptions-HtmlSaveOptions.java" >}}

إليك الكود للفئة *ExportStreamProvider* التي تنفذ واجهة [**IStreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/IStreamProvider) والتي يتم استخدامها داخل الكود أعلاه.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ExportStreamProvider-ExportStreamProvider.java" >}}

