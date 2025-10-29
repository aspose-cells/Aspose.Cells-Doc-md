---
title: تحديد إصدار المستند للملف باستخدام خصائص المستند المدمجة مع Golang عبر C++
linktitle: تحديد إصدار المستند
type: docs
weight: 20
url: /ar/go-cpp/specify-document-version-of-the-excel-file-using-builtin-document-properties/
description: تعلم كيفية تحديد إصدار مستند Excel باستخدام خصائص المستند المدمجة مع Aspose.Cells for C++.
---

## **سيناريوهات الاستخدام المحتملة**

يمكنك تغيير **رقم الإصدار** الخاص بملف Excel بالنقر بزر الماوس الأيمن على الملف ثم اختيار الخصائص > التفاصيل ثم تحرير حقل **رقم الإصدار**. يرجى استخدام خاصية [**BuiltInDocumentPropertyCollection.GetDocumentVersion()**](https://reference.aspose.com/cells/go-cpp/builtindocumentpropertycollection/getdocumentversion/) لتغييره برمجياً باستخدام واجهات برمجة التطبيقات Aspose.Cells.

## **تحديد إصدار المستند لملف الإكسل باستخدام خصائص المستند المضمنة**

يخلق الكود النموذجي التالي مصنفًا ويغير خصائص المستند المدمجة التي تشمل العنوان، والمؤلفين، ورقم الإصدار. يرجى مراجعة ملف الإكسل الناتج ([ملف الإكسل الناتج](64716811.xlsx)) الذي تم إنشاؤه بواسطة الكود، ولقطة الشاشة التي تظهر تعديل رقم الإصدار بواسطة خاصية [**BuiltInDocumentPropertyCollection.GetDocumentVersion()**](https://reference.aspose.com/cells/go-cpp/builtindocumentpropertycollection/getdocumentversion/).

![todo:image_alt_text](specify-document-version-of-the-excel-file-using-builtin-document-properties_1.png)

## **الكود المثالي**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SpecifyDocumentVersionOfTheExcelFileUsingBuiltinDocumentProperties.go" >}}
