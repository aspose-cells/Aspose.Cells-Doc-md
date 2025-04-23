---
title: Çalışma sayfasının Parola Korumalı Olup Olmadığını Algılama
type: docs
weight: 360
url: /tr/net/detect-if-worksheet-is-password-protected/
---

{{% alert color="primary" %}}

Çalışma kitaplarını ve çalışma sayfalarını ayrı ayrı korumak mümkündür. Örneğin, bir elektronik tablo, parola korumalı bir veya daha fazla çalışma sayfası içerebilir, ancak elektronik tablo kendisi korunmuş olabilir veya olmayabilir. Aspose.Cells API'ları, belirli bir çalışma sayfasının parola korumalı olup olmadığını algılamak için olanak sağlar. Bu makale, aynı işlemi gerçekleştirmek için Aspose.Cells for .NET API'nın kullanımını göstermektedir.

{{% /alert %}}

Aspose.Cells for .NET 8.7.0, bir çalışma sayfasının parola korumalı olup olmadığını algılamak için [**Protection.IsProtectedWithPassword**](https://reference.aspose.com/cells/net/aspose.cells/protection/properties/isprotectedwithpassword) özelliğini ortaya çıkarmıştır. Boole türünde [**Protection.IsProtectedWithPassword**](https://reference.aspose.com/cells/net/aspose.cells/protection/properties/isprotectedwithpassword) özelliği, [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) parola korumalıysa **true** ve değilse **false** döndürür.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-CheckIfPasswordProtected-CheckIfPasswordProtected.cs" >}}
{{< app/cells/assistant language="csharp" >}}
