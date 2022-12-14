---
title: إعداد خصائص ScaleCrop و LinksUpToDate لخصائص المستند المضمنة
type: docs
weight: 1050
url: /ar/java/setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties/
---
## **سيناريوهات الاستخدام الممكنة**
[ScaleCrop](https://reference.aspose.com/cells/java/com.aspose.cells/builtindocumentpropertycollection#ScaleCrop) و[الروابط](https://reference.aspose.com/cells/java/com.aspose.cells/builtindocumentpropertycollection#LinksUpToDate)نوعان من خصائص المستند المضمنة الممتدة المحددة داخل تنسيق OpenXml. الغرض من هذه الخصائص هو التالي
## **1) ScaleCrop**
 يشير هذا العنصر إلى وضع عرض مصغر المستند. اضبط هذا العنصر على**حقيقي** لتمكين تغيير حجم مصغر المستند إلى العرض. اضبط هذا العنصر على**خاطئة** لتمكين اقتصاص مصغر المستند لإظهار الأقسام التي تناسب العرض فقط.

يتم تحديد القيم المحتملة لهذا العنصر بواسطة نوع البيانات المنطقي W3C XML Schema.
## **2) LinksUpToDate**
 يشير هذا العنصر إلى ما إذا كانت الارتباطات التشعبية الموجودة في المستند محدثة أم لا. اضبط هذا العنصر على**حقيقي** للإشارة إلى تحديث الارتباطات التشعبية. اضبط هذا العنصر على**خاطئة**للإشارة إلى أن الارتباطات التشعبية قديمة.

يتم تحديد القيم المحتملة لهذا العنصر بواسطة نوع البيانات المنطقي W3C XML Schema.
## **لقطة شاشة تعرض هذه الخصائص داخل ملف app.xml**
![ما يجب القيام به: image_بديل_نص](setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties_1.png)
## **إعداد خصائص ScaleCrop و LinksUpToDate لخصائص المستند المضمنة**
 يعيّن نموذج التعليمات البرمجية التالي ملفات[ScaleCrop](https://reference.aspose.com/cells/java/com.aspose.cells/builtindocumentpropertycollection#ScaleCrop)و[الروابط](https://reference.aspose.com/cells/java/com.aspose.cells/builtindocumentpropertycollection#LinksUpToDate) خصائص المستند المضمنة الموسعة للمصنف. رجاء تاكد من[ملف اكسل الناتج](5472494.xlsx)تم إنشاؤه باستخدام هذا الرمز ، قم بتغيير امتداده إلى .zip واستخرج محتوياته واعرض ملف aap.xml كما هو موضح في لقطة الشاشة أعلاه.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SettingScaleCropLinksUpToDate-SettingScaleCropLinksUpToDate.java" >}}
