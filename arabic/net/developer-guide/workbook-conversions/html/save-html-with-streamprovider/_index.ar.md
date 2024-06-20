---
title: حفظ Html باستخدام StreamProvider
type: docs
weight: 80
url: /ar/net/convert-excel-to-html-with-streamprovider/
---

{{% alert color="primary" %}} 

عند تحويل ملفات Excel التي تحتوي على صور وأشكال إلى ملفات HTML، نواجه في كثير من الأحيان المشاكل الاتية:
1.أين يجب أن نحفظ الصور والأشكال عند حفظ ملف Excel إلى تدفق HTML.
1. استبدال المسار الافتراضي بالمسار المتوقع.

يشرح هذا المقال كيفية تنفيذ واجهة [IStreamProvider](https://reference.aspose.com/cells/net/aspose.cells/istreamprovider) لضبط خاصية [HtmlSaveOptions.StreamProvider](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/streamprovider). من خلال تنفيذ هذه الواجهة، ستتمكن من حفظ الموارد التي تم إنشاؤها أثناء توليد صفحات HTML إلى مواقعك المحددة أو تدفقات الذاكرة الداخلية.

{{% /alert %}} 

هذا هو الرمز الرئيسي الذي يظهر استخدام [HtmlSaveOptions.StreamProvider](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/streamprovider) كخاصية



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithHTMLFormat-ImplementIStreamProvider-ImplementIStreamProvider.cs" >}}



فيما يلي الرمز لفئة *ExportStreamProvider* التي تنفذ [IStreamProvider](https://reference.aspose.com/cells/net/aspose.cells/istreamprovider) المستخدمة داخل الرمز المذكور أعلاه.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithHTMLFormat-ImplementIStreamProvider-ExportStreamProviderClass.cs" >}}

