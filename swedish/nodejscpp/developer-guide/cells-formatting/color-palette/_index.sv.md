---  
title: Hur man använder färgpaletten
linktitle: Hur man använder färgpaletten  
type: docs  
weight: 80  
url: /sv/nodejs-cpp/excel-color-palette/  
description: Node.js kod för att lägga till anpassade färger till paletten och använda Excel färgpaletten med Aspose.Cells for Node.js via C++.  
keywords: node.js lägger till anpassade färger till paletten, node.js programmatisk användning av Excel färgpaletten, hur man använder färgpaletten i arbetsboken programmatisk, node.js hur man använder färgpaletten i Excel  
---  

## **Färger och Palett**  

En palett är antalet färger som är tillgängliga för att skapa en bild. Användningen av en standardiserad palett i en presentation gör att användaren kan skapa en enhetlig look. Varje Microsoft Excel (97-2003) fil har en palett med 56 färger som kan tillämpas på celler, teckensnitt, rutnät, grafiska objekt, fyllningar och linjer i en graf.  

Med Aspose.Cells for Node.js via C++ är det inte bara möjligt att använda palettens befintliga färger utan även anpassade färger. Innan du använder en anpassad färg, lägg till den till paletten först.  

Detta ämne diskuterar hur man lägger till anpassade färger i paletten.  

## **Lägg till anpassade färger i paletten**  

Aspose.Cells stöder Microsoft Excels 56-färgspalett. För att använda en anpassad färg som inte är definierad i paletten, lägg till färgen i paletten.  

Aspose.Cells tillhandahåller en klass, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook/), som representerar en Microsoft Excel-fil. [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook/)-klassen innehåller en [**changePalette(Color, number)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#changePalette-color-number-)-metod som tar följande parametrar för att lägga till en anpassad färg för att ändra paletten:  

- Anpassad färg, den anpassade färgen som ska läggas till.  
- Index, index för färgen i paletten som den anpassade färgen kommer att ersätta. Ska vara mellan 0-55.  

Exemplet nedan lägger till en anpassad färg (Orchid) i paletten innan den tillämpas på en font.  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-ColorPalette.js" >}}


{{% alert color="primary" %}}  

Paletten rymmer endast 56 färger. När du lägger till en anpassad färg i paletten ändras paletten och alla element i filen formaterade med den tidigare färgen ändras. Så, när du ändrar paletten, var mycket försiktig. Dessutom är detta begränsningen i XLS (Excel 97 - 2003) filformat endast då det inte finns någon sådan begränsning för XLSX eller andra avancerade MS Excel (2007/2010 eller 2013) filformat.  

{{% /alert %}}  

{{< app/cells/assistant language="nodejs-cpp" >}}
