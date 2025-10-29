---
title: استخدام أجزاء XML مخصصة في Aspose.Cells مع Golang عبر C++
linktitle: استخدام أجزاء XML مخصصة
type: docs
weight: 390
url: /ar/go-cpp/use-custom-xml-parts-in-aspose-cells/
description: تعلم كيفية استخدام أجزاء XML مخصصة في ملفات إكسل برمجيًا باستخدام Aspose.Cells مع Golang عبر C++.
---

## استخدام أجزاء XML المخصصة في Aspose.Cells

أجزاء XML المخصصة هي البيانات XML المخزنة بواسطة تطبيقات مختلفة مثل SharePoint داخل ملف إكسل. يتم استهلاك هذه البيانات بواسطة تطبيقات مختلفة تتطلبها. لا يستخدم Microsoft Excel هذه البيانات، لذلك لا يوجد واجهة رسومية لإضافتها. يمكنك عرض هذه البيانات بتغيير امتداد **.xlsx** إلى **.zip** ثم فتحه باستخدام **WinZip**. يمكنك أيضًا فتح ملف ZIP باستخدام أي أداة ضغط خارجية لنظام Windows مثل WinRAR أو WinZip. البيانات موجودة داخل مجلد **customXml**.

يمكنك إضافة أجزاء XML مخصصة باستخدام Aspose.Cells عبر طريقة [**Workbook.ContentTypeProperties.Add()**](https://reference.aspose.com/cells/go-cpp/contenttypepropertycollection/add_string_string/).

يستخدم الكود النموذجي التالي طريقة [**Workbook.ContentTypeProperties.Add()**](https://reference.aspose.com/cells/go-cpp/contenttypepropertycollection/add_string_string/) لإضافة **Book Catalog XML**، واسمه **BookStore**. يظهر الصورة التالية نتيجة هذا الكود. كما ترى، تم إضافة XML فهرس الكتب داخل عقدة BookStore، وهو اسم الخاصية تلك.

![todo:image_alt_text](use-custom-xml-parts-in-aspose-cells_1.png)

![todo:image_alt_text](use-custom-xml-parts-in-aspose-cells_2.png)

## كود C++ لاستخدام أجزاء XML مخصصة

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-UseCustomXmlPartsInAsposeCells.go" >}}
## مقال ذو صلة

- [إضافة خصائص مخصصة مرئية داخل لوحة معلومات المستند](/cells/ar/cpp/adding-custom-properties-visible-inside-document-information-panel/)
