---
title: الكشف عما إذا كانت ورقة العمل محمية بكلمة مرور
type: docs
weight: 360
url: /ar/net/detect-if-worksheet-is-password-protected/
---

{{% alert color="primary" %}}

من الممكن حماية الدفاتر المحاسبية وأوراق العمل بشكل منفصل. على سبيل المثال ، قد تحتوي جدول بيانات على ورقة واحدة أو أكثر محمية بكلمة مرور ، ومع ذلك ، قد تكون جدول البيانات نفسه محميًا أو قد لا يكون محميًا. توفر واجهات برمجة التطبيقات في Aspose.Cells الوسيلة للكشف عما إذا كانت ورقة العمل المحددة محمية بكلمة مرور أم لا. يوضح هذا المقال استخدام واجهة برمجة التطبيقات Aspose.Cells for .NET لتحقيق الهدف نفسه.

{{% /alert %}}

قد قامت Aspose.Cells for .NET 8.7.0 بتعريض الخاصية [**Protection.IsProtectedWithPassword**](https://reference.aspose.com/cells/net/aspose.cells/protection/properties/isprotectedwithpassword) للكشف عما إذا كانت ورقة العمل محمية بكلمة مرور أم لا. تعيد الخاصية [**Protection.IsProtectedWithPassword**](https://reference.aspose.com/cells/net/aspose.cells/protection/properties/isprotectedwithpassword) من نوع بولياني **true** إذا كانت [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) محمية بكلمة مرور و **false** إذا لم تكن.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-CheckIfPasswordProtected-CheckIfPasswordProtected.cs" >}}
{{< app/cells/assistant language="csharp" >}}
