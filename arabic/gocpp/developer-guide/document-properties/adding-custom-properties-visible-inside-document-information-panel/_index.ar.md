---
title: إضافة خصائص مخصصة تظهر داخل لوحة معلومات المستند مع Golang عبر C++
linktitle: إضافة خصائص مخصصة مرئية داخل لوحة معلومات المستند
type: docs
weight: 300
url: /ar/go-cpp/adding-custom-properties-visible-inside-document-information-panel/
description: تعلم كيفية إضافة خصائص مخصصة تظهر في لوحة معلومات المستند باستخدام Aspose.Cells مع Golang عبر C++.
---

## **إضافة خصائص مخصصة مرئية داخل لوحة معلومات الوثيقة**

يمكن استخدام Aspose.Cells لإضافة خصائص مخصصة داخل كائن جدول البيانات والتي يمكن رؤيتها داخل لوحة معلومات المستند. يمكنك فتح لوحة المعلومات المستندية في Microsoft Excel باستخدام أوامر قائمة الملف > معلومات > الخصائص > عرض قائمة معلومات المستند.

 يرجى استخدام طريقة [**Workbook.ContentTypeProperties.Add()**](https://reference.aspose.com/cells/go-cpp/contenttypepropertycollection/add_string_string/) لإضافة خاصية مخصصة ستكون مرئية في لوحة معلومات المستند.

 يضيف رمز النموذج التالي خاصيتين مخصصتين. الخاصية الأولى بدون نوع معين والخاصية الثانية من نوع تاريخ ووقت. بمجرد فتح ملف إكسل الناتج الذي تم إنشاؤه بواسطة هذا الرمز، سترى هاتين الخاصيتين داخل لوحة معلومات المستند.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AddingCustomPropertiesVisibleInsideDocumentInformationPanel.go" >}}
### **مقال ذو صلة**

{{% alert color="primary" %}}

- [استخدام أجزاء XML المخصصة في Aspose.Cells](/cells/ar/cpp/use-custom-xml-parts-in-aspose-cells/)

{{% /alert %}}
