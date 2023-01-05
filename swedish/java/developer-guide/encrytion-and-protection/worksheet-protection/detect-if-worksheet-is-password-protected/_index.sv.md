---
title: Upptäck om arbetsbladet är lösenordsskyddat
type: docs
weight: 280
url: /sv/java/detect-if-worksheet-is-password-protected/
---
{{% alert color="primary" %}}

Det är möjligt att skydda arbetsböckerna och arbetsbladen separat. Ett kalkylblad kan till exempel innehålla ett eller flera kalkylblad som är lösenordsskyddade, men själva kalkylarket kan vara skyddat eller inte. Aspose.Cells API:er ger möjlighet att upptäcka om ett visst kalkylblad är lösenordsskyddat eller inte. Den här artikeln visar användningen av Aspose.Cells for Java API för att uppnå samma sak.

{{% /alert %}}

## **Upptäck om arbetsbladet är lösenordsskyddat**

Aspose.Cells for Java 8.7.0 har avslöjat[**Protection.isProtectedWithPassword**](https://reference.aspose.com/cells/java/com.aspose.cells/protection#IsProtectedWithPassword) egenskap för att upptäcka om ett kalkylblad är lösenordsskyddat eller inte. boolesk typ[**Protection.isProtectedWithPassword**](https://reference.aspose.com/cells/java/com.aspose.cells/protection#IsProtectedWithPassword) fältet returnerar**Sann** om[**Arbetsblad**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) är lösenordsskyddad och**falsk** om inte.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DetectWorksheetisPasswordProtected-DetectWorksheetisPasswordProtected.java" >}}
