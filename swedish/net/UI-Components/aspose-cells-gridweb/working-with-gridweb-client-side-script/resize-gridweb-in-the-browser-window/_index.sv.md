---
title: Ändra storlek på GridWeb i webbläsarfönstret
type: docs
weight: 40
url: /sv/net/resize-gridweb-in-the-browser-window/
---
## **Möjliga användningsscenarier**
Ibland vill du att Aspose.Cells.GridWeb ska ändra storlek på sig själv i enlighet med webbläsarfönstret. Du kanske behöver GridWeb bör alltid justera sin storlek (höjd, bredd) och kompatibel med webbläsarfönstrets storlek. Aspose.Cells.GridWeb tillhandahåller klientsidan*ändra storlek()* funktion för ändamålet. Dessutom kan du till och med ändra storlek på GridWeb-kontrollen i webbläsarfönstret. Du kan till exempel använda det nedre högra handtaget (via mus) för att anpassa dess bredd/höjd i fönstret. Du måste också inkludera/specificera jquery Javascript-filer för att få det att fungera i sidkällan i ditt projekt.
## **Använder GridWebs storleksändringsmetod**
Följande kod kommer att kontrollera om storleksändring sker var 100:e millisekund. När det inte finns någon åtgärd för att ändra storlek, tror den att storleksändringen är klar nu. Vi använder en exempelmallfil som importeras till GridWeb. Vi använder kod på klientsidan för att ändra storlek på GridWeb. Skärmdumpen visar att GridWeb ändrar storleken på sig själv när den ändrar storlek på webbläsarfönstret.

![todo:image_alt_text](resize-gridweb-in-the-browser-window_1.png)
### **Exempelkod**
{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-WorkingWithGridWebClientSideScript-ResizeGridWebUsingResizeMethod" >}}


## **Göra GridWeb storleksändringsbar med hjälp av jquery ui-funktionen**
Följande kod gör att GridWeb-kontrollen kan ändras i storlek i webbläsarfönstret. Du kan till exempel använda det nedre högra handtaget för att anpassa storleken på GridWeb i fönstret. Vi använder samma mallfil som först importeras till GridWeb. Vi använder jquery-skript för att göra GridWeb storleksanpassbar. Skärmdumpen visar att storleken på GridWeb har ändrats med sitt nedre högra handtag i webbläsarfönstret.

![todo:image_alt_text](resize-gridweb-in-the-browser-window_2.png)
### **Exempelkod**
{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-WorkingWithGridWebClientSideScript-MakingGridWebResizableUsingResizablejQueryUiFeature" >}}
