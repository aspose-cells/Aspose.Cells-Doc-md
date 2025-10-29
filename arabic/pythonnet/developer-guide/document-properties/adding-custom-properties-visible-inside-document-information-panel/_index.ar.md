---
title: إضافة خصائص مخصصة مرئية داخل لوحة معلومات المستند
type: docs
weight: 300
url: /ar/python-net/adding-custom-properties-visible-inside-document-information-panel/
---

## **إضافة خصائص مخصصة مرئية داخل لوحة معلومات الوثيقة**

يمكن استخدام Aspose.Cells لـ Python via .NET لإضافة خصائص مخصصة داخل كائن المصنف والتي تكون مرئية داخل لوحة معلومات معلومات المستند. يمكنك فتح لوحة معلومات المستند في إكسل الخاص بك باستخدام أوامر قوائم ملف > معلومات > خصائص > عرض لوحة المستند.

يرجى استخدام الطريقة [**Workbook.content_type_properties.add()**](https://reference.aspose.com/cells/python-net/aspose.cells.properties/contenttypepropertycollection/add) لإضافة خاصية مخصصة ستكون مرئية في لوحة معلومات المستند

الكود النموذجي التالي يضيف خاصيتين مخصصتين. الخاصية الأولى بدون أي نوع والخاصية الثانية بنوع DateTime. عند فتح ملف الإكسل الناتج من هذا الكود، سترى هاتين الخاصيتين داخل لوحة معلومات المستند.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Document-Properties-AddingCustomPropertiesVisible-1.py" >}}

### **مقال ذو صلة**

{{% alert color="primary" %}}

- [استخدام أجزاء XML المخصصة في Aspose.Cells](/cells/ar/python-net/use-custom-xml-parts-in-aspose-cells/)

{{% /alert %}}
{{< app/cells/assistant language="python-net" >}}
