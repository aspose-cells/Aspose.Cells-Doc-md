---
title: Upptäck om arbetsbladet är lösenordsskyddat
type: docs
weight: 360
url: /sv/net/detect-if-worksheet-is-password-protected/
---

{{% alert color="primary" %}}

Det är möjligt att skydda arbetsböckerna och kalkylbladen separat. Till exempel kan ett kalkylblad innehålla ett eller flera kalkylblad som är lösenordsskyddade, dock kan kalkylbladet självt vara skyddat eller inte. Aspose.Cells API:er tillhandahåller medel för att upptäcka om ett visst kalkylblad är lösenordsskyddat eller inte. Den här artikeln visar användningen av Aspose.Cells for .NET API för att uppnå samma sak.

{{% /alert %}}

Aspose.Cells for .NET 8.7.0 har exponerat egenskapen [**Protection.IsProtectedWithPassword**](https://reference.aspose.com/cells/net/aspose.cells/protection/properties/isprotectedwithpassword) för att upptäcka om ett kalkylblad är lösenordsskyddat eller inte. Boolesk typ [**Protection.IsProtectedWithPassword**](https://reference.aspose.com/cells/net/aspose.cells/protection/properties/isprotectedwithpassword) returnerar **true** om [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) är lösenordsskyddat och **false** om inte.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-CheckIfPasswordProtected-CheckIfPasswordProtected.cs" >}}
{{< app/cells/assistant language="csharp" >}}
