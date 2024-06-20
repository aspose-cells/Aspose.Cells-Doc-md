---
title: إضافة خصائص مخصصة مرئية داخل لوحة معلومات المستند
type: docs
weight: 500
url: /ar/java/adding-custom-properties-visible-inside-document-information-panel/
---

{{% alert color="primary" %}}

يمكن استخدام Aspose.Cells لإضافة خصائص مخصصة داخل كائن جدول البيانات والتي يمكن رؤيتها داخل لوحة معلومات المستند. يمكنك فتح لوحة المعلومات المستندية في Microsoft Excel باستخدام أوامر قائمة الملف > معلومات > الخصائص > عرض قائمة معلومات المستند.

يرجى استخدام طريقة [**Workbook.getContentTypeProperties().add()**](https://reference.aspose.com/cells/java/com.aspose.cells/contenttypepropertycollection#add(java.lang.Object)) لإضافة خاصية مخصصة ستكون مرئية في لوح معلومات المستند

{{% /alert %}}

## **مثال**

الكود النموذجي التالي يضيف خاصيتين مخصصتين. الخاصية الأولى بدون أي نوع والخاصية الثانية بنوع DateTime. عند فتح ملف الإكسل الناتج من هذا الكود، سترى هاتين الخاصيتين داخل لوحة معلومات المستند.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-management-AddingCustomProperties-AddingCustomProperties.java" >}}

## **مقال ذو صلة**

{{% alert color="primary" %}}

- [استخدام أجزاء XML المخصصة في Aspose.Cells](/cells/ar/java/using-custom-xml-parts-in-aspose-cells/)

{{% /alert %}}
