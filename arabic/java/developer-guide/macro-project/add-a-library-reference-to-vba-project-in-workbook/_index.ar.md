---
title: أضف مرجع مكتبة إلى مشروع VBA في المصنف
type: docs
weight: 10
url: /ar/java/add-a-library-reference-to-vba-project-in-workbook/
---
{{% alert color="primary" %}}

 في Microsoft Excel ، يمكنك إضافة مرجع مكتبة إلى مشروع VBA بالنقر فوق**أدوات> مراجع ...** يدويا. سيفتح مربع الحوار التالي الذي سيساعدك على الاختيار من بين المراجع الموجودة أو تصفح مكتبتك بنفسك.

![ما يجب القيام به: image_بديل_نص](add-a-library-reference-to-vba-project-in-workbook_1.png)

 لكن في بعض الأحيان ، تحتاج إلى إضافة مرجع المكتبة أو تسجيله إلى مشروع VBA من خلال التعليمات البرمجية. يمكنك القيام بذلك باستخدام Aspose.Cells[**VbaProject.getReferences (). addRegisteredReference ()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbaprojectreferencecollection#addRegisteredReference(java.lang.String,%20java.lang.String)) طريقة.

{{% /alert %}}

## **أضف مرجع مكتبة إلى مشروع VBA في المصنف**

 يقوم نموذج التعليمات البرمجية التالي بإضافة أو تسجيل مراجع مكتبة إلى مشروع VBA الخاص بالمصنف باستخدام[**VbaProject.getReferences (). addRegisteredReference ()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbaprojectreferencecollection#addRegisteredReference(java.lang.String,%20java.lang.String)) طريقة.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AddLibraryReference-AddLibraryReference.java" >}}
