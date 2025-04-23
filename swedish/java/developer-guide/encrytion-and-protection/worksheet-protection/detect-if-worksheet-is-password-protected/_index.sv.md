---
title: Upptäck om arbetsbladet är lösenordsskyddat
type: docs
weight: 280
url: /sv/java/detect-if-worksheet-is-password-protected/
---

{{% alert color="primary" %}}

Det är möjligt att skydda arbetsböcker och arbetsblad separat. Till exempel kan en kalkylblad innehålla ett eller flera arbetsblad som är lösenordsskyddade, men kalkylbladet självt kan vara skyddat eller inte. Aspose.Cells API:er ger möjlighet att upptäcka om ett givet arbetsblad är lösenordsskyddat eller inte. Den här artikeln demonstrerar användningen av Aspose.Cells for Java API för att uppnå samma.

{{% /alert %}}

## **Upptäck om arbetsbladet är lösenordsskyddat**

Aspose.Cells for Java 8.7.0 har exponerat egenskapen [**Protection.isProtectedWithPassword**](https://reference.aspose.com/cells/java/com.aspose.cells/protection#IsProtectedWithPassword) för att upptäcka om ett arbetsblad är lösenordsskyddat eller inte. Boolesk typ [**Protection.isProtectedWithPassword**](https://reference.aspose.com/cells/java/com.aspose.cells/protection#IsProtectedWithPassword) fält returnerar **true** om [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) är lösenordsskyddat och **false** om inte.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DetectWorksheetisPasswordProtected-DetectWorksheetisPasswordProtected.java" >}}
{{< app/cells/assistant language="java" >}}
