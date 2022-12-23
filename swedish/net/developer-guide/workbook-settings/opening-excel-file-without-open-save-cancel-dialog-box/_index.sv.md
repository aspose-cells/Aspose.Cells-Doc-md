---
title: Öppna Excel-fil utan dialogrutan Öppna Spara Avbryt
type: docs
weight: 150
url: /sv/net/opening-excel-file-without-open-save-cancel-dialog-box/
---
{{% alert color="primary" %}} 

Det här dokumentet förklarar hur man öppnar en Microsoft Excel-fil i en webbläsare utan att visa dialogrutan Öppna-Spara-Avbryt.

 Det bör noteras här att säkerhetsbegränsningen som inte tillåter direkt nedladdning av en fil upprätthålls av Microsoft (eller andra webbläsarleverantörer), inte av Aspose. Den är införd för att blockera och begränsa potentiellt skadliga filer från att laddas ner till lokala maskiner .

Det är riskabelt för klientens lokala system att tillåta nedladdning utan att visa dialogrutan Öppna-Spara-Avbryt för att uppmana till nedladdning. Det finns inget alternativ eller en lösning tillgänglig från Aspose eftersom det kommer att vara en mycket stor säkerhetsrisk.

{{% /alert %}} 
## **Varför en säkerhetsrisk?**
Följande bild visar dialogrutan Öppna-Spara-Avbryt som visas av Internet Explorer när du försöker ladda ner en fil.

|**Dialogrutan Öppna-Spara-Avbryt**|
|:- |
|![todo:image_alt_text](opening-excel-file-without-open-save-cancel-dialog-box_1.png)|
Som förklarats ovan är det en säkerhetsrisk att låta en fil öppnas eller köras på ditt system utan att bekräfta att du verkligen vill att den ska göra det. Vissa filer innehåller virus, och vissa webbplatser kommer att försöka ladda ner skadliga filer till din maskin utan att uppmana dig. Det rekommenderas därför inte att du tillåter nedladdning av filer utan nedladdningsuppmaningen så att användarna måste verifiera filen och dess källa kan verifieras innan de laddas ner eller körs. Om du inaktiverar nedladdningsdialogrutan blir systemet sårbart för virus, trojaner och hackare som kan påverka ditt system i tysthet.
## **Öppna en fil utan dialogrutan Öppna-Spara-Avbryt**
 Även om det är ett stort säkerhetsproblem, tillhandahåller Microsoft fortfarande Internet Explorer-inställningar som tillåter användare att inaktivera öppna-spara-avbryt-prompten för filnedladdning.

I Windows Explorer:

1.  På**Verktyg** menyn, välj**Mappalternativ**.
1. Klicka på fliken Filtyper i dialogrutan Mappalternativ.
1. Välj filtypen XLS.
1.  Klick**Avancerad**. 
En dialogruta visas. Den har tre alternativ längst ner.
1.  Avmarkera**Bekräfta öppning efter nedladdning**.
1.  Välj det tredje alternativet -**Bläddra i samma fönster** - för att visa Excel-filen i Internet Explorer utan att starta Microsoft Excel fristående.

|**Redigera filtypsalternativ**|
|:- |
|![todo:image_alt_text](opening-excel-file-without-open-save-cancel-dialog-box_2.png)|
Den här inställningen tillåter att filer körs direkt i webbläsaren, utan att dialogrutan Öppna-Spara-Avbryt visas när du laddar ner eller öppnar filen.
