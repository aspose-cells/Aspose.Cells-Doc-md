---
title: Radbrytningar och textbrytning
type: docs
weight: 60
url: /sv/net/line-breaks-and-text-wrapping/
---
{{% alert color="primary" %}}

För att säkerställa att text i en cell kan läsas kan explicita radbrytningar och textbrytning tillämpas. Textbrytning förvandlar en rad till flera i en cell, vilka explicita radbrytningar sätts i brytningar precis där du vill ha dem.

{{% /alert %}}

## **Att slå in text i en Cell**

 Om du vill radbryta text i en cell använder du[**Aspose.Cells.Style.IsTextWrapped**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/istextwrapped)fast egendom.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-LineBreakTextWrapping-WrapText-1.cs" >}}

## **Att använda explicita radbrytningar**

Du kan använda '\n' i C# och 'vbLf' i VB.NET för att infoga explicita radbrytningar i en cell.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-LineBreakTextWrapping-UseExplicitLineBreaks-1.cs" >}}
