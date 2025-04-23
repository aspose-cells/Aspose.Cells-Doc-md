---
title: استخدام أجزاء XML المخصصة في Aspose.Cells
type: docs
weight: 570
url: /ar/java/using-custom-xml-parts-in-aspose-cells/
---

{{% alert color="primary" %}} 

تمثل أجزاء XML المخصصة البيانات XML المخزنة بواسطة تطبيقات مختلفة مثل SharePoint الخ. داخل ملف Excel. تستهلك هذه البيانات بواسطة تطبيقات مختلفة تحتاج إليها. لا يقوم Microsoft Excel باستخدام هذه البيانات لذا لا يوجد واجهة رسومية لإضافتها. يمكنك عرض هذه البيانات عن طريق تغيير امتداد **.xlsx** إلى **.zip** ثم فتحها باستخدام **WinRAR**. البيانات موجودة داخل مجلد **customXml** كما هو موضح في هذه الصورة.

![todo:image_alt_text](using-custom-xml-parts-in-aspose-cells_1.png)

يمكنك إضافة أجزاء XML مخصصة باستخدام Aspose.Cells عبر طريقة [Workbook.getContentTypeProperties().add()](https://reference.aspose.com/cells/java/com.aspose.cells/contenttypepropertycollection#add-java.lang.Object-)

{{% /alert %}} 
## **استخدام أجزاء XML المخصصة في Aspose.Cells**
يوضح الكود النموذجي التالي استخدام طريقة [Workbook.getContentTypeProperties().add()](https://reference.aspose.com/cells/java/com.aspose.cells/contenttypepropertycollection#add-java.lang.Object-) ويضيف **Book Catalog Xml** واسمه **BookStore**. تُظهر الصورة التالية ناتج هذا الكود. كما ترى، تم إضافة Book Catalog Xml داخل عقدة BookStore والتي هي اسم الخاصية تلك.

![todo:image_alt_text](using-custom-xml-parts-in-aspose-cells_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-UsingCustomXmlParts-UsingCustomXmlParts.java" >}}
## **مقال ذو صلة**
{{% alert color="primary" %}} 

- [إضافة خصائص مخصصة مرئية داخل لوحة معلومات الوثيقة](/cells/ar/java/adding-custom-properties-visible-inside-document-information-panel/)

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
