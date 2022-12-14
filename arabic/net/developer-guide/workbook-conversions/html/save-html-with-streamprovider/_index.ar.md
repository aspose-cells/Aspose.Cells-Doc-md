---
title: احفظ Html مع StreamProvider
type: docs
weight: 80
url: /ar/net/convert-excel-to-html-with-streamprovider/
---
{{% alert color="primary" %}} 

عند تحويل ملفات Excel التي تحتوي على iamges والأشكال إلى ملفات html ، فإننا نواجه المسألتين التاليتين:
1. أين يجب أن نحفظ الصور والأشكال عند حفظ ملف Excel في دفق html.
1. استبدل المسار الافتراضي بالمسار المستثنى.

 تشرح هذه المقالة كيفية التنفيذ[IStreamProvider](https://reference.aspose.com/cells/net/aspose.cells/istreamprovider) واجهة لتعيين[HtmlSaveOptions.StreamProvider](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/streamprovider) منشأه. من خلال تنفيذ هذه الواجهة ، ستتمكن من حفظ الموارد التي تم إنشاؤها أثناء إنشاء HTML في مواقعك المحددة أو تدفقات الذاكرة.

{{% /alert %}} 

 هذا هو الكود الرئيسي الذي يوضح استخدام[HtmlSaveOptions.StreamProvider](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/streamprovider)منشأه



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithHTMLFormat-ImplementIStreamProvider-ImplementIStreamProvider.cs" >}}



 هنا هو رمز*ExportStreamProvider* الطبقة التي تنفذ[IStreamProvider](https://reference.aspose.com/cells/net/aspose.cells/istreamprovider)الواجهة المستخدمة داخل الكود أعلاه.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithHTMLFormat-ImplementIStreamProvider-ExportStreamProviderClass.cs" >}}

