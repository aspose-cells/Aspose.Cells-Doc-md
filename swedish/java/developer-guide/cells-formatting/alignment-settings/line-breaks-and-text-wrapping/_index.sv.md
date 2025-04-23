---
title: Radbrytningar och textomslag
type: docs
weight: 10
url: /sv/java/line-breaks-and-text-wrapping/
---

{{% alert color="primary" %}}

För att säkerställa att texten i en cell kan läsas, kan explicita radbrytningar och textomslag appliceras. Textomslag gör att en rad blir flera i en cell, medan explicita radbrytningar sätts in precis där du vill ha dem.

{{% /alert %}}

## **För att omsluta text i en cell**

För att omsluta text i en cell, använd [**Aspose.Cells.Style.setTextWrapped**](https://reference.aspose.com/cells/java/com.aspose.cells/style#IsTextWrapped)-egenskapen.

Följande provkod visar hur man använder textradering och explicita radbrytningar i en cell.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-WrapTextinCell-1.java" >}}

## **För att använda explicita radbrytningar**

Du kan använda '\n' i Java för att infoga explicita radbrytningar i en cell.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-UseExplicitLineBreaks-UseExplicitLineBreaks.java" >}}
{{< app/cells/assistant language="java" >}}
