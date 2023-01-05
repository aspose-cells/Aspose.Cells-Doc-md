---
title: استخدم أجزاء XML المخصصة في Aspose.Cells
type: docs
weight: 390
url: /ar/net/use-custom-xml-parts-in-aspose-cells/
---
## استخدام أجزاء XML المخصصة في Aspose.Cells

أجزاء XML المخصصة هي بيانات XML التي يتم تخزينها بواسطة تطبيقات مختلفة مثل SharePoint وما إلى ذلك داخل ملف Excel. يتم استهلاك هذه البيانات من قبل التطبيقات المختلفة التي تحتاج إليها. Microsoft لا يستخدم Excel هذه البيانات لذلك لا توجد واجهة مستخدم رسومية لإضافتها. يمكنك عرض هذه البيانات عن طريق تغيير امتداد**.xlsx** داخل**.أَزِيز** ثم فتحه باستخدام**برنامج WinZip** . يمكنك أيضًا فتح ملف ZIP باستخدام أي أداة مضغوطة من الجزء الثالث Windows مثل WinRAR أو WinZip وما إلى ذلك. البيانات موجودة داخل**customXml** مجلد.

 يمكنك إضافة أجزاء XML مخصصة باستخدام Aspose.Cells عبر ملف[**Workbook.ContentTypeProperties.Add ()**](https://reference.aspose.com/cells/net/aspose.cells.properties/contenttypepropertycollection/methods/add/index)طريقة.

 يستخدم نموذج التعليمات البرمجية التالي[**Workbook.ContentTypeProperties.Add ()**](https://reference.aspose.com/cells/net/aspose.cells.properties/contenttypepropertycollection/methods/add/index) طريقة ويضيف**كتالوج الكتب XML** واسمه**مكتبة لبيع الكتب**. الصورة التالية تظهر نتيجة هذا الرمز. كما ترى ، تمت إضافة XML لـ Book Catalog داخل عقدة BookStore وهي اسم هذه الخاصية.

![ما يجب القيام به: image_بديل_نص](use-custom-xml-parts-in-aspose-cells_1.png)

![ما يجب القيام به: image_بديل_نص](use-custom-xml-parts-in-aspose-cells_2.png)

## C# كود لاستخدام أجزاء XML المخصصة

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UsingCustomXmlParts-UsingCustomXmlParts.cs" >}}

## مقالات لها صلة

- [إضافة خصائص مخصصة مرئية داخل لوحة معلومات المستند](/cells/ar/net/adding-custom-properties-visible-inside-document-information-panel/)
