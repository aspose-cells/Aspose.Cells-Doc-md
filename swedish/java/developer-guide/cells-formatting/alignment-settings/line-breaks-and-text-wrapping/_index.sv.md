---
title: Radbrytningar och textbrytning
type: docs
weight: 10
url: /sv/java/line-breaks-and-text-wrapping/
---
{{% alert color="primary" %}}

För att säkerställa att text i en cell kan läsas kan explicita radbrytningar och textbrytning tillämpas. Textbrytning förvandlar en rad till flera i en cell, vilka explicita radbrytningar sätts i brytningar precis där du vill ha dem.

{{% /alert %}}

## **Att slå in text i en Cell**

 Om du vill radbryta text i en cell använder du[**Aspose.Cells.Style.setTextWrapped**](https://reference.aspose.com/cells/java/com.aspose.cells/style#IsTextWrapped)fast egendom.

Följande exempelkod visar hur man använder textbrytning och explicita radbrytningar i en cell.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-WrapTextinCell-1.java" >}}

## **Att använda explicita radbrytningar**

Du kan använda '\n' i Java för att infoga de explicita radbrytningarna i en cell.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-UseExplicitLineBreaks-UseExplicitLineBreaks.java" >}}
