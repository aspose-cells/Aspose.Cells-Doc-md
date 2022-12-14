---
title: Upptäck om arbetsbladet är lösenordsskyddat
type: docs
weight: 360
url: /sv/net/detect-if-worksheet-is-password-protected/
---
{{% alert color="primary" %}}

Det är möjligt att skydda arbetsböckerna och arbetsbladen separat. Ett kalkylblad kan till exempel innehålla ett eller flera kalkylblad som är lösenordsskyddade, men själva kalkylarket kan vara skyddat eller inte. Aspose.Cells API:er ger möjlighet att upptäcka om ett visst kalkylblad är lösenordsskyddat eller inte. Den här artikeln visar användningen av Aspose.Cells för .NET API för att uppnå samma sak.

{{% /alert %}}

 Aspose.Cells för .NET 8.7.0 har avslöjat[**Protection.IsProtectedWithPassword**](https://reference.aspose.com/cells/net/aspose.cells/protection/properties/isprotectedwithpassword) egenskap för att upptäcka om ett kalkylblad är lösenordsskyddat eller inte. boolesk typ[**Protection.IsProtectedWithPassword**](https://reference.aspose.com/cells/net/aspose.cells/protection/properties/isprotectedwithpassword) egendom returnerar**Sann** om[**Arbetsblad**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) är lösenordsskyddad och**falsk** om inte.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-CheckIfPasswordProtected-CheckIfPasswordProtected.cs" >}}
