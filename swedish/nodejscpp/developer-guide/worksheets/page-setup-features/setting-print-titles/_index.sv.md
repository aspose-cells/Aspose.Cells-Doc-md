---  
title: Hur man ställer in utskriftstitlar med Node.js via C++  
linktitle: Hur man ställer in Utskriftsrubriker  
type: docs  
weight: 200  
url: /sv/nodejs-cpp/how-to-set-print-titles/  
description: Denna artikel visar hur du ställer in utskriftstitlar med hjälp av Aspose.Cells biblioteket för Node.js via C++.  
keywords: Skriv ut rader och kolumner upprepade gånger, Node.js Hur man ställer in utskriftstitlar, Sätt och ta bort utskriftstitlar med Node.js, Hur man tar bort utskriftstitlar i Node.js, Hur man lägger till utskriftstitlar med Node.js, Hur man tar bort utskriftstitlar med Node.js, Hur man ställer in utskriftstitlar i Excel, Hur man tar bort utskriftstitlar i Excel.  
---  

## **Möjliga användningsscenario**  

Att ställa in utskriftstitlar i Excel säkerställer att specifika rader eller kolumner upprepas på varje utskriven sida, vilket är särskilt användbart för stora kalkylblad som sträcker sig över flera sidor. Här är några anledningar till varför du kan ställa in utskriftstitlar:  

1. Förbättrad läsbarhet: Utskriftstitlar hjälper läsarna att förstå data genom att hålla rubriker synliga på alla sidor, vilket gör det lättare att tolka informationen på varje sida utan att behöva hänvisa tillbaka till första sidan.  

1. Professionell presentation: Att konsekvent visa rubriker eller etiketter på varje sida skapar ett mer polerat och professionellt utseende på utskrivna dokument.  

1. Förbättrad navigering: För dokument med omfattande data gör upprepning av rubriker på varje sida snabbare navigering och referens, vilket minskar behovet av att vända fram och tillbaka mellan sidor.  

1. Minskade fel: När rubriker är närvarande på varje sida minimeras missförstånd eller datainmatningsfel, eftersom användare lätt kan se sammanhanget för data.  

1. Konsekvens: Att säkerställa att viktig information, som kolumnrubriker eller radetiketter, alltid är synlig upprätthåller konsekvens och tydlighet genom hela dokumentet.  

## **Hur man ställer in utskriftstitlar i Excel**  

Följ dessa steg för att ställa in utskriftstitlar i Excel:  

1. Öppna fliken "Sidlayout": Klicka på "Sidlayout"-fliken i menyfliksområdet högst upp i Excel-fönstret.  
1. Få tillgång till Utskriftstitlar: I gruppen "Siduppställning" klickar du på "Utskriftstitlar".  
1. Ställ in rader att upprepa: I dialogrutan "Siduppställning" går du till fliken "Blad". I avsnittet "Utskriftstitlar" anger du de rader som ska upprepas överst genom att klicka på rutan bredvid "Rader att upprepa längst upp" och välja rad(er) du vill upprepa.  
1. Ställ in kolumner att upprepa (om behövs): På liknande sätt kan du ange de kolumner som ska upprepas längst till vänster genom att klicka på rutan bredvid "Kolumner att upprepa till vänster" och välja den eller de kolumner du vill upprepa.  
<br>  
<img src="3.png" width=60% />  

1. Bekräfta och skriv ut: Klicka på "OK" för att tillämpa inställningarna. När du skriver ut kalkylbladet kommer de angivna raderna eller kolumnerna att visas på varje utskriven sida.  

## **Hur man rensar utskriftstitlar i Excel**  

För att rensa utskriftstitlar i Excel måste du ta bort de rader eller kolumner som är inställda att upprepas på varje utskriven sida. Så här gör du:  

1. Öppna fliken "Sidlayout": Klicka på "Sidlayout"-fliken i menyfliksområdet högst upp i Excel-fönstret.  
1. Få tillgång till Utskriftstitlar: I gruppen "Siduppställning" klickar du på "Utskriftstitlar".  
1. Rensa utskriftstitlar: I dialogrutan "Siduppställning" går du till fliken "Blad". Radera texten i rutorna för "Rader att upprepa längst upp" och "Kolumner att upprepa till vänster" genom att ta bort innehållet i dem.  
<br>  
<img src="4.png" width=60% />  

1. Bekräfta och stäng: Klicka på "OK" för att tillämpa ändringarna.  

## **Hur man ställer in utskriftsrubriker med Aspose.Cells for Node.js via C++**  

För att ställa in utskriftstitlar i ett angivet kalkylblad: Ladda först [provfilen](input.xlsx), och du behöver sedan ändra egenskaperna [**Worksheet.getPageSetup()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getPageSetup--) och [**Worksheet.getPageSetup()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getPageSetup--) av [**PageSetup**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/)-objektet för det önskade kalkylbladet. Att ställa in dessa egenskaper till ett områdesträng kommer att ställa in utskriftstitlarna.  

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "input.xlsx");

// Load the workbook
const workbook = new AsposeCells.Workbook(filePath);

// Access the desired worksheet
const worksheet = workbook.getWorksheets().get(0);

// Set rows to repeat at the top (e.g., rows 1 and 2)
worksheet.getPageSetup().setPrintTitleRows("$1:$2");

// Set columns to repeat at the left (e.g., columns A and B)
worksheet.getPageSetup().setPrintTitleColumns("$A:$B");

// Save the workbook
workbook.save("set_print_titles.pdf");
```  

Utmatningsresultat:  
<br>  
<img src="1.png" width=60% />  

## **Hur man rensar utskriftsrubriker med Aspose.Cells for Node.js via C++**  

För att rensa utskriftstitlar i ett specificerat kalkylblad: Ladda först [provfilen](input.xlsx), och du behöver sedan ändra egenskaperna [**Worksheet.getPageSetup()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getPageSetup--) och [**Worksheet.getPageSetup()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getPageSetup--) av [**PageSetup**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/)-objektet för det önskade kalkylbladet. Att ställa in dessa egenskaper till en tom sträng rensar utskriftstitlarna.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "input.xlsx");
// Load the workbook
const workbook = new AsposeCells.Workbook(filePath);

// Access the desired worksheet
const worksheet = workbook.getWorksheets().get(0);

// Clear the rows and columns set to repeat
worksheet.getPageSetup().setPrintTitleRows("");
worksheet.getPageSetup().setPrintTitleColumns("");

// Save the workbook
workbook.save("clear_print_titles.pdf");
```  

Utmatningsresultat:  
<br>  
<img src="2.png" width=60% />  

{{< app/cells/assistant language="nodejs-cpp" >}}
