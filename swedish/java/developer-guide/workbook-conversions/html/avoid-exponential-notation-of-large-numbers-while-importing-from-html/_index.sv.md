---
title: Undvik exponentiell notation för stora tal vid import från HTML
type: docs
weight: 600
url: /sv/java/avoid-exponential-notation-of-large-numbers-while-importing-from/
---

{{% alert color="primary" %}} 

Ibland innehåller din HTML nummer som 1234567890123456 som är längre än 15 siffror, och när du importerar din HTML-fil till excelfilen konverteras dessa siffror till exponentiell notation som 1.23457E+15. Om du vill att ditt nummer ska importeras som det är och inte konverteras till exponentiell notation, använd då [HtmlLoadOptions.KeepPrecision](https://reference.aspose.com/cells/java/com.aspose.cells/htmlloadoptions#KeepPrecision)-egenskapen och ställ in den som **true** vid inläsning av din HTML.

{{% /alert %}} 
## **Undvik exponentiell notation för stora tal vid import från HTML**
Följande kodexempel förklarar användningen av [HtmlLoadOptions.KeepPrecision](https://reference.aspose.com/cells/java/com.aspose.cells/htmlloadoptions#KeepPrecision)-egenskapen. Den importerar numret som det är utan att omvandla det till exponentiell notation.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-KeepPrecisionOfLargeNumbers-1.java" >}}
{{< app/cells/assistant language="java" >}}
