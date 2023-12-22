---
title: Hur man roterar text till Cell
type: docs
weight: 80
url: /sv/net/how-to-rotate-text-of-cell/
description: C# kod för att rotera text av Cell med Aspose.Cells for .NET API
keywords: c# rotate text of Cell, c# programmatically rotate text of Cell in workbook, programmatically set cell rotation angle in workbook, c# how to rotate text of Cell in excel
---
##  **Rotera text från Cell till Aspose.Cells**

Aspose.Cells är en kraftfull .NET- och Java-komponent som gör det möjligt för utvecklare att arbeta med Excel-kalkylblad programmatiskt. En av funktionerna som tillhandahålls av Aspose.Cells är möjligheten att rotera celler, vilket gör att du kan anpassa orienteringen av text och förbättra den visuella presentationen av dina data. I det här dokumentet kommer vi att utforska hur man roterar celler med Aspose.Cells.

##  **Hur man roterar text av Cell i Excel**
För att rotera en cell i Excel kan du använda följande steg:
1. Öppna Excel och välj cellen eller cellintervallet som du vill rotera.
1. Högerklicka på de markerade cellerna och välj "Formatera Cells" från snabbmenyn. Alternativt kan du gå till fliken "Hem" i Excel-bandet, klicka på rullgardinsmenyn "Format" i gruppen "Cells" och välja "Format Cells."
1. I dialogrutan "Format Cells" navigerar du till fliken "Justering".
1. Under avsnittet "Orientering" ser du alternativen för att rotera texten. Du kan direkt mata in önskad rotationsvinkel i grader i rutan "Grader". Positiva värden roterar texten moturs och negativa värden roterar den medurs.
<br>
![todo:image_alt_text](alignment.png)
1. När du har valt önskad rotation klickar du på "OK" för att tillämpa ändringarna. Den/de valda cellen/cellerna kommer nu att roteras baserat på din valda rotationsvinkel eller orientering.

##  **Så här roterar du text till Cell med Aspose.Cells API**

[**Style.RotationAngle**](https://reference.aspose.com/cells/net/aspose.cells/style/rotationangle/) egenskap gör det bekvämt att rotera celler. För att rotera celler i Aspose.Cells måste du följa dessa steg:
1. Ladda Excel-arbetsboken
<br>
 Först måste du ladda Excel-arbetsboken med Aspose.Cells. Du kan använda klassen Workbook för att öppna en befintlig Excel-fil eller skapa en ny.

1. Gå till arbetsbladet
<br>
När arbetsboken har laddats måste du komma åt kalkylbladet där du vill rotera cellerna. Du kan antingen komma åt kalkylbladet genom dess index eller namn.

1. Rotera texten till Cell
<br>
 Nu när du har tillgång till kalkylbladet kan du rotera cellerna genom att ändra stilobjektet för de önskade cellerna. Style-objektet låter dig ställa in olika formateringsalternativ, inklusive rotation.

1. Spara arbetsboken
<br>
Efter att ha roterat cellerna kan du spara den ändrade arbetsboken tillbaka till en fil eller ström med hjälp av Spara-metoden.

##  **C# Provkod**

Se följande kod, den skapar ett arbetsboksobjekt och ställer in olika rotationsvinklar för flera celler. Skärmdumpen visar resultatet efter exekveringen av exempelkoden.
<br>
<img src="rotation.png" width=80% />



{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-rotate-text.cs" >}}
