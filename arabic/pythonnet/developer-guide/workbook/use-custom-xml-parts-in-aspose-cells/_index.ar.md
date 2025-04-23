---
title: استخدام أجزاء XML المخصصة في Aspose.Cells
type: docs
weight: 390
url: /ar/python-net/use-custom-xml-parts-in-aspose-cells/
---

## استخدام أجزاء XML مخصصة في Aspose.Cells لبايثون via .NET

أجزاء XML المخصصة هي بيانات XML يتم تخزينها بواسطة تطبيقات مختلفة مثل SharePoint وما إلى ذلك داخل ملف إكسل. يتم استخدام هذه البيانات بواسطة تطبيقات مختلفة تحتاج إليها. لا يقوم Microsoft Excel باستخدام هذه البيانات لذا لا توجد واجهة المستخدم الرسومية لإضافتها. يمكنك عرض هذه البيانات عن طريق تغيير امتداد **.xlsx** إلى **.zip** ثم فتحها باستخدام **WinZip**. يمكنك أيضًا فتح ملف ZIP باستخدام أي أداة ضغط ZIP خارجية لنظام Windows مثل WinRAR أو WinZip وما إلى ذلك. البيانات موجودة داخل مجلد **customXml**.

يمكنك إضافة أجزاء XML مخصصة باستخدام Aspose.Cells عبر طريقة [**Workbook.content_type_properties.add()**](https://reference.aspose.com/cells/python-net/aspose.cells.properties/contenttypepropertycollection/add/#str-str).

يستخدم مقتطف الكود التالي الطريقة [**Workbook.content_type_properties.add()**](https://reference.aspose.com/cells/python-net/aspose.cells.properties/contenttypepropertycollection/add/#str-str) ويضيف **فهرس كتب XML** واسمه **BookStore**. تُظهر الصورة التالية نتيجة هذا الكود. كما يمكنك رؤية فهرس كتب XML داخل عقدة BookStore وهو اسم هذه الخاصية.

![todo:image_alt_text](use-custom-xml-parts-in-aspose-cells_1.png)

![todo:image_alt_text](use-custom-xml-parts-in-aspose-cells_2.png)

## كود C# لاستخدام أجزاء XML مخصصة

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Workbook-UsingCustomXmlParts.py" >}}



