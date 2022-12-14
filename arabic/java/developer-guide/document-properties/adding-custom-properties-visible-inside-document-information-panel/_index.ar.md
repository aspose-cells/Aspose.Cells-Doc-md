---
title: إضافة خصائص مخصصة مرئية داخل لوحة معلومات المستند
type: docs
weight: 500
url: /ar/java/adding-custom-properties-visible-inside-document-information-panel/
---
{{% alert color="primary" %}}

يمكن استخدام Aspose.Cells لإضافة خصائص مخصصة داخل عنصر المصنف والتي تكون مرئية داخل لوحة معلومات المستند. يمكنك فتح لوحة معلومات المستند في Microsoft Excel باستخدام ملف> معلومات> خصائص> إظهار أوامر قائمة لوحة المستند.

 يرجى استخدام[**Workbook.getContentTypeProperties (). add ()**](https://reference.aspose.com/cells/java/com.aspose.cells/contenttypepropertycollection#add(java.lang.Object)) لإضافة خاصية مخصصة ستكون مرئية في لوحة معلومات المستند

{{% /alert %}}

## **مثال**

يضيف نموذج التعليمات البرمجية التالي خاصيتين مخصصتين. الخاصية الأولى بدون أي نوع والخاصية الثانية لها نوع التاريخ والوقت. بمجرد فتح ملف Excel الناتج الذي تم إنشاؤه بواسطة هذا الرمز ، سترى هاتين الخاصيتين داخل لوحة معلومات المستند.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-management-AddingCustomProperties-AddingCustomProperties.java" >}}

## **مقالات لها صلة**

{{% alert color="primary" %}}

- [استخدام أجزاء XML المخصصة في Aspose.Cells](/cells/ar/java/using-custom-xml-parts-in-aspose-cells/)

{{% /alert %}}
