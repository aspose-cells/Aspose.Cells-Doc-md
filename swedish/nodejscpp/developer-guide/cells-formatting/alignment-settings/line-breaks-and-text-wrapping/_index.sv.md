---  
title: Radbrytningar och textomslag
linktitle: Radbrytningar och textomslag  
description: Hur man implementerar textwrapping och ordwrapping med Aspose.Cells biblioteket i Node.js via C++. Genom att använda Aspose.Cells bibliotek kan du enkelt infoga text i celler och ställa in metoden för textwrap, som manuell ordwrapping, ordwrap, etc. Denna dokumentation beskriver hur man implementerar dessa funktioner och ger exempel kod för din referens.  
keywords: Aspose.Cells, radbrytningar, textwraps, textlayout Node.js via C++  
type: docs  
weight: 60  
url: /sv/nodejs-cpp/line-breaks-and-text-wrapping/  
---  

{{% alert color="primary" %}}  
För att säkerställa att texten i en cell kan läsas, kan explicita radbrytningar och textomslag appliceras. Textomslag gör att en rad blir flera i en cell, medan explicita radbrytningar sätts in precis där du vill ha dem.  
{{% /alert %}}  

## **För att omsluta text i en cell**  
För att wrapa text i en cell, använd [**Aspose.Cells.Style.setIsTextWrapped(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/style/#setIsTextWrapped-boolean-)-metoden.  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-AlignSettings-WrapTextInCell.js" >}}


## **För att använda explicita radbrytningar**  
Du kan använda ‘\n’ i JavaScript för att infoga explicita radbrytningar i en cell.  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-AlignSettings-UseExplicitLineBreaks.js" >}}



{{< app/cells/assistant language="nodejs-cpp" >}}
