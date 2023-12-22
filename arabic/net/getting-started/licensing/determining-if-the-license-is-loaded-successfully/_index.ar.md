---
title: تحديد ما إذا تم تحميل الترخيص بنجاح
type: docs
weight: 260
url: /ar/net/determining-if-the-license-is-loaded-successfully/
description: تعرف على كيفية اكتشاف ما إذا تم تحميل الترخيص بنجاح من خلال Aspose.Cells لواجهات برمجة التطبيقات NET.
keywords: How to Detect if the License is loaded successfully in C#, Determine if the License is loaded successfully using C#, Check if the License is loaded successfully via C#, check the status of license.
---
{{% alert color="primary" %}}

 Aspose.Cells يوفر[**Workbook.IsLicensed**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/islicensed) الخاصية التي يمكنك استخدامها لتحديد ما إذا تم تحميل الترخيص بنجاح أم لا. إذا قمت بالوصول إلى هذه الخاصية قبل تعيين الترخيص، فسوف تعود**خطأ شنيع** وإذا قمت باستدعاء هذه الخاصية بعد تعيين الترخيص، فسوف تعود**حقيقي** يشير إلى أنه تم تحميل الترخيص بنجاح.

{{% /alert %}}

##  كود C# لتحديد ما إذا تم تحميل الترخيص بنجاح

 الكود التالي يصل إلى[**Workbook.IsLicensed**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/islicensed)الخاصية قبل تعيين الترخيص وترجع *خطأ**. ثم يقوم بتحميل الترخيص والوصول إلى الخاصية مرة أخرى والتي تُرجع الآن *true**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-DeterminingLicenseLoading-DeterminingLicenseLoading.cs" >}}

##  **إخراج وحدة التحكم**

فيما يلي إخراج وحدة التحكم (تصحيح الأخطاء) لنموذج التعليمات البرمجية أعلاه

{{< highlight "java" >}}

False

True

{{< /highlight >}}
