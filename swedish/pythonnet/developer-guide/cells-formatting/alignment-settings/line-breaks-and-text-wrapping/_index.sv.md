---
title: Radbrytningar och textomslag
description: Hur man implementerar textbrytning och ordvikt med biblioteket Aspose.Cells för Python via .NET. Genom att använda biblioteket Aspose.Cells för Python via .NET kan du enkelt infoga text i celler och ställa in textbrytningsmetoden, såsom manuell ordvikt, automatisk ordvikt etc. Detta dokument förklarar hur man implementerar dessa funktioner och ger exempel på kod för referens.
keywords: Aspose.Cells för Python via .NET, radbrytningar, textbrytning, textrayout
type: docs
weight: 60
url: /sv/python-net/line-breaks-and-text-wrapping/
---

{{% alert color="primary" %}}

För att säkerställa att texten i en cell kan läsas, kan explicita radbrytningar och textomslag appliceras. Textomslag gör att en rad blir flera i en cell, medan explicita radbrytningar sätts in precis där du vill ha dem.

{{% /alert %}}

## **För att omsluta text i en cell**

För att omsluta text i en cell, använd [**Style.is_text_wrapped**](https://reference.aspose.com/cells/python-net/aspose.cells/style/is_text_wrapped)-egenskapen.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-LineBreakTextWrapping-WrapText-1.py" >}}

## **För att använda explicita radbrytningar**

Du kan använda '\n' i C# och 'vbLf' i VB.NET för att sätta in explicita radbrytningar i en cell.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-LineBreakTextWrapping-UseExplicitLineBreaks-1.py" >}}

