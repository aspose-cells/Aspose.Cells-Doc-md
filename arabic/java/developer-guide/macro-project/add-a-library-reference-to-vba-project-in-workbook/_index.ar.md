---
title: أضف مرجعًا إلى مشروع VBA في سجل العمل
type: docs
weight: 10
url: /ar/java/add-a-library-reference-to-vba-project-in-workbook/
description: تعلم كيفية إضافة اشارة مرجعية لمكتبة VBA إلى مشروع العمل من خلال API Aspose.Cells for Java.
keywords: كيفية إضافة اشارة مرجعية لمكتبة VBA إلى مشروع العمل في جافا، إدراج إشارة مرجعية لمكتبة VBA إلى مشروع العمل باستخدام جافا، تعيين اشارة مرجعية لمكتبة VBA إلى مشروع العمل باستخدام جافا. 
---

{{% alert color="primary" %}}

في برنامج Microsoft Excel، يمكنك إضافة إشارة مرجعية لمكتبة VBA إلى مشروع VBA عن طريق النقر فوق ** أدوات > مراجع... ** يدويا. سيفتح صندوق الحوار التالي الذي سيساعدك في اختيار المراجع الموجودة أو تصفح المكتبة بنفسك.

![todo:image_alt_text](add-a-library-reference-to-vba-project-in-workbook_1.png)

ولكن في بعض الأحيان، تحتاج إلى إضافة أو تسجيل مرجع المكتبة إلى المشروع VBA من خلال الشفرة. يمكنك القيام بذلك باستخدام طريقة Aspose.Cells [**VbaProject.getReferences().addRegisteredReference()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbaprojectreferencecollection#addRegisteredReference(java.lang.String,%20java.lang.String)).

{{% /alert %}}

## **كيفية إضافة اشارة مرجعية لمكتبة VBA إلى مشروع العمل**

الشيفرة الزمنية العينية التالية تضيف أو تسجل اثنين من مراجع المكتبات إلى مشروع VBA لسجل العمل باستخدام طريقة [**VbaProject.getReferences().addRegisteredReference()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbaprojectreferencecollection#addRegisteredReference(java.lang.String,%20java.lang.String)).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AddLibraryReference-AddLibraryReference.java" >}}
