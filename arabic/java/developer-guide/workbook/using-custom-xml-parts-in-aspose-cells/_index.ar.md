---
title: استخدام أجزاء XML المخصصة في Aspose.Cells
type: docs
weight: 570
url: /ar/java/using-custom-xml-parts-in-aspose-cells/
---
{{% alert color="primary" %}} 

 أجزاء XML المخصصة هي بيانات XML التي يتم تخزينها بواسطة تطبيقات مختلفة مثل SharePoint وغيرها داخل ملف Excel. يتم استهلاك هذه البيانات من قبل التطبيقات المختلفة التي تحتاج إليها. Microsoft لا يستخدم Excel هذه البيانات لذلك لا توجد واجهة مستخدم رسومية لإضافتها. يمكنك عرض هذه البيانات عن طريق تغيير امتداد**.xlsx** داخل**.أَزِيز** ثم فتحه باستخدام**برنامج WinRAR** . البيانات موجودة داخل**customXml** مجلد كما هو موضح في هذه الصورة.

![ما يجب القيام به: image_بديل_نص](using-custom-xml-parts-in-aspose-cells_1.png)

 يمكنك إضافة أجزاء XML مخصصة باستخدام Aspose.Cells عبر ملف[Workbook.getContentTypeProperties (). add ()](https://reference.aspose.com/cells/java/com.aspose.cells/contenttypepropertycollection#add\(java.lang.Object\)) طريقة.

{{% /alert %}} 
## **استخدام أجزاء Xml المخصصة في Aspose.Cells**
 يستخدم نموذج التعليمات البرمجية التالي[Workbook.getContentTypeProperties (). add ()](https://reference.aspose.com/cells/java/com.aspose.cells/contenttypepropertycollection#add\(java.lang.Object\) ) ويضيف أسلوب**كتالوج الكتب Xml** واسمه**مكتبة لبيع الكتب**الصورة التالية تظهر نتيجة هذا الرمز. كما ترى ، تمت إضافة Book Catalog Xml داخل عقدة BookStore وهو اسم هذه الخاصية.

![ما يجب القيام به: image_بديل_نص](using-custom-xml-parts-in-aspose-cells_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-UsingCustomXmlParts-UsingCustomXmlParts.java" >}}
## **مقالات لها صلة**
{{% alert color="primary" %}} 

- [إضافة خصائص مخصصة مرئية داخل لوحة معلومات المستند](/cells/ar/java/adding-custom-properties-visible-inside-document-information-panel/)

{{% /alert %}}
