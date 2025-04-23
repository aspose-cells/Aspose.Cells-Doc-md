---  
title: Hur man roterar text i en cell
linktitle: Hur man roterar text i en cell  
type: docs  
weight: 80  
url: /sv/nodejs-cpp/how-to-rotate-text-of-cell/  
description: Lär dig hur man roterar text i en cell programmässigt med Aspose.Cells for Node.js via C++.  
keywords: Node.js rotera text i cell, Node.js programmering för att rotera text i cell i arbetsboken, programmera cellrotation i arbetsboken, Node.js hur man roterar text i cell i Excel.  
---  

## **Rotera Text i Cell i Aspose.Cells for Node.js via C++**

Aspose.Cells är ett kraftfullt Node.js-komponent som gör det möjligt för utvecklare att arbeta med Excel-kalkylblad programmatiskt. En av funktionerna i Aspose.Cells är möjligheten att rotera celler, vilket gör att du kan anpassa textens orientering och förbättra det visuella intrycket av dina data. I denna dokumentation utforskar vi hur man roterar celler med Aspose.Cells.

## **Hur man roterar text i cell i Excel**
För att rotera en cell i Excel kan du använda följande steg:
1. Öppna Excel och välj den cell eller det cellområde som du vill rotera.
1. Högerklicka på den markerade cellen/cellerna och välj "Formatera celler" i snabbmenyn. Alternativt kan du gå till fliken "Hem" i Excels menyflik, klicka på rullgardinsmenyn "Formatera" i gruppen "Celler" och välj "Formatera celler".
1. I dialogrutan "Formatera celler" navigerar du till fliken "Justering".
1. Under avsnittet "Orientering" ser du alternativen för att rotera texten. Du kan direkt ange önskad rotationsvinkel i grader i rutan "Grader". Positiva värden roterar texten moturs, och negativa värden roterar den medurs.
<br>
![todo:image_alt_text](alignment.png)
1. När du har valt önskad rotation klickar du på "OK" för att tillämpa ändringarna. Den valda cellen/cellerna kommer nu att vara roterade enligt din valda rotationsvinkel eller orientering.

## **Hur man roterar text i cell med hjälp av Aspose.Cells API**

[**Style.setRotationAngle(number)**](https://reference.aspose.com/cells/nodejs-cpp/style/#setRotationAngle-number-)-egenskapen gör det bekvämt att rotera celler. För att rotera celler i Aspose.Cells måste du följa dessa steg:
1. Läs in Excel-arbetsboken  
<br>
Först måste du läsa in Excel-arbetsboken med hjälp av Aspose.Cells. Du kan använda Workbook-klassen för att öppna en befintlig Excel-fil eller skapa en ny. 

1. Kom åt arbetsbladet  
<br>
När arbetsboken har lästs in måste du komma åt det arbetsblad där du vill rotera cellerna. Du kan antingen komma åt arbetsbladet genom dess index eller namn. 

1. Rotera texten i cellen  
<br>
Nu när du har åtkomst till arbetsbladet kan du rotera cellerna genom att ändra Style-objektet för de önskade cellerna. Style-objektet låter dig ställa in olika formateringsalternativ, inklusive rotation. 

1. Spara arbetsboken  
<br>
Efter att ha roterat cellerna kan du spara den modifierade arbetsboken till en fil eller ström med hjälp av Save -metoden.

## **Node.js exempelkod**

Se följande kod, den skapar ett arbetsboksobjekt och ställer in olika rotationsvinklar för flera celler. Skärmbilden visar resultatet efter körning av exemplet.
<br>
<img src="rotation.png" width=80% />

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-Styles-SetRotationOfCell.js" >}}


