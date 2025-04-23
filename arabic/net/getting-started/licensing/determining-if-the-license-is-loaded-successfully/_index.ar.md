---
title: تحديد ما إذا تم تحميل الترخيص بنجاح
type: docs
weight: 260
url: /ar/net/determining-if-the-license-is-loaded-successfully/
description: تعلم كيفية اكتشاف ما إذا تم تحميل الترخيص بنجاح من خلال Aspose.Cells for NET APIs.
keywords: كيفية اكتشاف ما إذا تم تحميل الترخيص بنجاح في C#، تحديد ما إذا تم تحميل الترخيص بنجاح باستخدام C#، التحقق مما إذا تم تحميل الترخيص بنجاح عبر C#، التحقق من حالة الترخيص.
---

{{% alert color="primary" %}}

توفر Aspose.Cells [**Workbook.IsLicensed**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/islicensed) خاصية يمكنك استخدامها لتحديد ما إذا تم تحميل الترخيص بنجاح أم لا. إذا قمت بالوصول إلى هذه الخاصية قبل تعيين الترخيص، ستعيد **false**، وإذا قمت بالاتصال بهذه الخاصية بعد تعيين الترخيص، ستعيد **true** مشيرة إلى أن الترخيص تم تحميله بنجاح.

{{% /alert %}}

## كود C# لتحديد ما إذا تم تحميل الترخيص بنجاح

يقوم الكود التالي بالوصول إلى الخاصية [**Workbook.IsLicensed**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/islicensed) قبل تعيين ترخيص ويعيد **false**. ثم يقوم بتحميل الترخيص ويوصل إلى الخاصية مرة أخرى التي تعيد **true** الآن.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-DeterminingLicenseLoading-DeterminingLicenseLoading.cs" >}}

## **مخرجات الوحدة**

هنا مخرجات الكونسول (التصحيح) للشيفرة العينية أعلاه

{{< highlight java >}}

False

True

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
