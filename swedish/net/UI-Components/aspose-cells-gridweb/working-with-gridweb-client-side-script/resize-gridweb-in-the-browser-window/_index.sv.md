---
title: Ändra GridWeb i webbläsarfönstret
type: docs
weight: 40
url: /sv/net/aspose-cells-gridweb/resize-gridweb-in-the-browser-window/
keywords: GridWeb, ändra storlek
description: Denna artikel introducerar hur man ändrar storlek i GridWeb.
---

## **Möjliga användningsscenario**
Ibland vill du att Aspose.Cells.GridWeb ska ändra storlek i enlighet med webbläsarfönstret. Du kanske behöver att GridWeb alltid anpassar sin storlek (höjd, bredd) och är kompatibel med webbläsarfönstrets storlek. Aspose.Cells.GridWeb tillhandahåller klientens sida *resize()* -funktion för detta ändamål. Dessutom kan du även göra GridWeb-kontrollen ändringsbar i webbläsarfönstret. Till exempel kan du använda det nedre högra handtaget (via musen) för att anpassa dess bredd/höjd i fönstret. Du måste också inkludera/ange jquery Javaskriptfiler för att få det att fungera i sidkällan i ditt projekt.
## **Använda GridWeb:s resizemetod**
Följande kod kommer att kontrollera om det har skett en ändringsåtgärd varje 100 millisekunder. När det inte längre finns någon ändringsåtgärd anser det att ändringsoperationen är avslutad nu. Vi använder en provmallfil som importeras i GridWeb. Vi använder klientens sidkod för att ändra storleken på GridWeb. Skärmbilden visar att GridWeb ändrar storlek i enlighet med ändringen av webbläsarfönstret.

![todo:image_alt_text](resize-gridweb-in-the-browser-window_1.png)
### **Exempelkod**
{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-WorkingWithGridWebClientSideScript-ResizeGridWebUsingResizeMethod" >}}


## **Göra GridWeb ändringsbar med hjälp av jQuery UI-funktionen resizable**
Följande kod kommer att göra GridWeb-kontrollen ändringsbar i webbläsarfönstret. Till exempel kan du använda det nedre högra handtaget för att anpassa storleken på GridWeb i fönstret. Vi använder samma mallfil som först importeras i GridWeb. Vi använder jquery-skript för att göra GridWeb ändringsbar. Skärmbilden visar att GridWeb har ändrats med hjälp av dess nedre högra handtag i webbläsarfönstret.

![todo:image_alt_text](resize-gridweb-in-the-browser-window_2.png)
### **Exempelkod**
{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-WorkingWithGridWebClientSideScript-MakingGridWebResizableUsingResizablejQueryUiFeature" >}}
