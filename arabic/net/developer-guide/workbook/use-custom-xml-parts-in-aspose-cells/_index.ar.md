---
title: استخدام أجزاء XML المخصصة في Aspose.Cells
type: docs
weight: 390
url: /ar/net/use-custom-xml-parts-in-aspose-cells/
---

## استخدام أجزاء XML المخصصة في Aspose.Cells

أجزاء XML المخصصة هي بيانات XML يتم تخزينها بواسطة تطبيقات مختلفة مثل SharePoint وما إلى ذلك داخل ملف إكسل. يتم استخدام هذه البيانات بواسطة تطبيقات مختلفة تحتاج إليها. لا يقوم Microsoft Excel باستخدام هذه البيانات لذا لا توجد واجهة المستخدم الرسومية لإضافتها. يمكنك عرض هذه البيانات عن طريق تغيير امتداد **.xlsx** إلى **.zip** ثم فتحها باستخدام **WinZip**. يمكنك أيضًا فتح ملف ZIP باستخدام أي أداة ضغط ZIP خارجية لنظام Windows مثل WinRAR أو WinZip وما إلى ذلك. البيانات موجودة داخل مجلد **customXml**.

يمكنك إضافة أجزاء XML مخصصة باستخدام Aspose.Cells عبر طريقة [**Workbook.ContentTypeProperties.Add()**](https://reference.aspose.com/cells/net/aspose.cells.properties/contenttypepropertycollection/methods/add/index).

يستخدم مقتطف الكود التالي الطريقة [**Workbook.ContentTypeProperties.Add()**](https://reference.aspose.com/cells/net/aspose.cells.properties/contenttypepropertycollection/methods/add/index) ويضيف **فهرس كتب XML** واسمه **BookStore**. تُظهر الصورة التالية نتيجة هذا الكود. كما يمكنك رؤية فهرس كتب XML داخل عقدة BookStore وهو اسم هذه الخاصية.

![todo:image_alt_text](use-custom-xml-parts-in-aspose-cells_1.png)

![todo:image_alt_text](use-custom-xml-parts-in-aspose-cells_2.png)

## كود C# لاستخدام أجزاء XML مخصصة

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UsingCustomXmlParts-UsingCustomXmlParts.cs" >}}

## مقال ذو صلة

- [إضافة خصائص مخصصة مرئية داخل لوحة معلومات الوثيقة](/cells/ar/net/adding-custom-properties-visible-inside-document-information-panel/)
