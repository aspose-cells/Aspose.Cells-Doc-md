---
title: Radbrytningar och textomslag
description: Hur man implementerar textomslag och ordomslag med hjälp av Aspose.Cells biblioteket i C#. Genom att använda Aspose.Cells biblioteket kan du enkelt infoga text i celler och ange textomslagsmetoden, såsom manuellt ordomslag, ordomslag, osv. Denna dokumentation beskriver hur man implementerar dessa funktioner och tillhandahåller exempelkod för din referens.
keywords: Aspose.Cells, radbrytningar, textomslag, textlayout
type: docs
weight: 60
url: /sv/net/line-breaks-and-text-wrapping/
---

{{% alert color="primary" %}}

För att säkerställa att texten i en cell kan läsas, kan explicita radbrytningar och textomslag appliceras. Textomslag gör att en rad blir flera i en cell, medan explicita radbrytningar sätts in precis där du vill ha dem.

{{% /alert %}}

## **För att omsluta text i en cell**

För att omsluta text i en cell, använd [**Aspose.Cells.Style.IsTextWrapped**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/istextwrapped)-egenskapen.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-LineBreakTextWrapping-WrapText-1.cs" >}}

## **För att använda explicita radbrytningar**

Du kan använda '\n' i C# och 'vbLf' i VB.NET för att sätta in explicita radbrytningar i en cell.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-LineBreakTextWrapping-UseExplicitLineBreaks-1.cs" >}}
