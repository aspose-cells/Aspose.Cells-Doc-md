---
title: Öppna Excel fil utan dialogruta för Öppna Spara Avbryt med C++
linktitle: Öppna Excel fil utan dialogrutan Öppna Spara Avbryt
type: docs
weight: 150
url: /sv/cpp/opening-excel-file-without-open-save-cancel-dialog-box/
description: Lär dig hur du öppnar en Microsoft Excel fil i en webbläsare utan att visa dialogrutan Öppna Spara Cancel med Aspose.Cells for C++.
---

{{% alert color="primary" %}} 

Dokumentet förklarar hur man öppnar en Microsoft Excel-fil i en webbläsare utan att visa dialogrutan Öppna-Spara-Avbryt. 

Det bör noteras att begränsningen av säkerheten som inte tillåter direkt nedladdning av en fil upprätthålls av Microsoft (eller andra webbläsartillverkare), inte av Aspose. Det införs för att blockera och begränsa potentiellt skadliga filer från att laddas ned till lokala datorer. 

Det är riskabelt för klientens lokala system att tillåta nedladdning utan att visa dialogrutan Öppna-Spara-Avbryt för nedladdning. Det finns ingen möjlighet eller lösning från Aspose eftersom det skulle vara en mycket stor säkerhetsrisk.

{{% /alert %}} 

## **Varför en säkerhetsrisk?**
Bilden nedan visar dialogrutan Öppna-Spara-Avbryt som visas av Internet Explorer när du försöker ladda ner en fil.

|**Dialogrutan Öppna-Spara-Avbryt**|
| :- |
|![todo:image_alt_text](opening-excel-file-without-open-save-cancel-dialog-box_1.png)|

Som förklarats ovan utgör det en säkerhetsrisk att låta en fil öppnas eller köras på ditt system utan att först bekräfta att du verkligen vill det. Vissa filer innehåller virus och vissa webbplatser försöker ladda ner skadliga filer till din dator utan att meddela dig. Det rekommenderas därför inte att tillåta nedladdning av filer utan nedladdningsprompten, så att användare måste verifiera filen och dess källa innan de laddar ner eller kör den. Att inaktivera dialogrutan för nedladdning gör systemet sårbart för virus, trojaner och hackare som kan påverka ditt system utan att du märker det. 

## **Öppna en fil utan dialogrutan Öppna-Spara-Avbryt**
Även om det är en stor säkerhetsrisk så tillhandahåller Microsoft fortfarande inställningar för Internet Explorer som gör att användare kan inaktivera dialogrutan Öppna-Spara-Avbryt för nedladdning av filer. 

I Windows Utforskaren:

1. På menyn **Verktyg**, välj **Mappalternativ**.
1. Klicka på fliken Filtyper i dialogrutan Mappalternativ.
1. Välj filtypen XLS.
1. Klicka på **Avancerat**. 
   En dialogruta visas. Den har tre alternativ längst ned.
1. Avmarkera **Bekräfta öppning efter nedladdning**.
1. Välj det tredje alternativet - **Bläddra i samma fönster** - för att visa Excel-filen i Internet Explorer utan att starta separat Excel. 

|**Redigera filtypsalternativ**|
| :- |
|![todo:image_alt_text](opening-excel-file-without-open-save-cancel-dialog-box_2.png)|

Denna inställning gör det möjligt för filer att köras direkt i webbläsaren, utan att dialogrutan Öppna-Spara-Avbryt visas vid nedladdning eller öppning av filen.
{{< app/cells/assistant language="cpp" >}}
