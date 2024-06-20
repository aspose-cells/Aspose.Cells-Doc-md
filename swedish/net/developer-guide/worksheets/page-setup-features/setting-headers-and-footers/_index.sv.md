---
title:  Inställa sidhuvuden och sidfötter 
type: docs
weight: 30
url: /sv/net/setting-headers-and-footers/
description: Den här artikeln förklarar hur man programmatiskt infogar en bild i sidhuvudet och sidfotet för Excel kalkylblad genom att ställa in sidhuvudet och sidfotet med skriptkommandon med hjälp av C# API et eller .NET biblioteket.
keywords: infoga bild i excel sidhuvud sidfot c#, ställ in excel sidhuvud sidfot skriptkommandon c#
---

{{% alert color="primary" %}}

Sidhuvuden och sidfötter är textrader som visas under övre marginalen eller ovanför den nedre marginalen. Det är möjligt att lägga till sidhuvuden och sidfötter i kalkylbladen också. Sidhuvuden och sidfötter kan användas för att visa användbar information som sidnummer, författarnamn, ämnesnamn eller datum och tid. Sidhuvuden och sidfötter hanteras med sidlayoutinställningarna.

{{% /alert %}}

## **Ställa in sidhuvuden och sidfötter**

Aspose.Cells möjliggör att lägga till sidhuvuden och sidfötter till kalkylblad vid körning, men vi rekommenderar att sidhuvuden och sidfötter ställs in manuellt i en fördesignad fil för utskrift. Du kan använda Microsoft Excel som ett GUI-verktyg för att ställa in sidhuvuden och sidfötter för att spara ansträngning och utvecklingstid. Aspose.Cells kan importera filen och spara inställningarna.

För att lägga till sidhuvuden och sidfötter vid körning tillhandahåller Aspose.Cells speciella API-anrop och skriptkommandon för att formatera sidhuvuden och sidfötter.

### **Skriptkommandon**

Skriptkommandon är speciella kommandon som tillåter dig att ställa in sidhuvud- och sidfotformatering.

|**Skriptkommandon**|**Beskrivning**|
| :- | :- |
|&P|Det nuvarande sidnumret|
|&G|En bild|
|&N|Det totala antalet sidor|
|&D|Aktuellt datum|
|&T|Aktuell tid|
|&A|Arbetsbladets namn|
|&F|Filnamnet utan dess sökväg|
|&"\<FontName>"|Representerar ett typsnittsnamn. Till exempel: &"Arial"|
|&"\<FontName>, \<FontStyle>"|Representerar typsnittsnamn med stil. Till exempel: &"Arial,Fetstil"|
|&\<FontSize>|Representerar teckensnittsstorlek. Till exempel: “&14abc”. Men om detta kommando följs av ett vanligt nummer som ska skrivas ut i sidhuvudet, ska detta separeras med ett mellanslag från teckensnittsstorleken. Till exempel: “&14 123”|

### **Ställ in headers och footers**

[**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup)-klassen tillhandahåller två metoder, [**SetHeader**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/methods/setheader) och [**SetFooter**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/methods/setfooter), som används för att lägga till en sidhuvud och sidfot till ett arbetsblad. Dessa metoder tar endast två parametrar:

- **Avsnitt** – avsnittet där sidhuvudet eller sidfoten ska placeras. Det finns tre avsnitt: vänster, mitten och höger, representerade av 0, 1 och 2 respektive.
- **Skript** – skriptet som ska användas för sidhuvudet eller sidfoten. Detta skript innehåller skriptkommandon för att formatera sidhuvuden eller sidfötter.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetHeadersAndFooters-1.cs" >}}

### **Infoga en bild i en sidhuvud eller sidfot**

[**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup)-klassen har två ytterligare metoder, [**SetHeaderPicture**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/methods/setheaderpicture) och [**SetFooterPicture**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/methods/setfooterpicture), som används för att lägga till bilder i sidhuvud och sidfot. Dessa metoder tar parametrarna:

- **Avsnitt** – avsnittet för sidhuvudet eller sidfoten där bilden ska placeras. Det finns tre avsnitt, vänster, mitten och höger, representerade av värdena 0, 1 och 2 respektive.
- **Byte-arrayer** – de grafiska data (de binära data ska skrivas in i bufferten i en byte-array).

Efter att ha utfört koden nedan och öppnat filen, kontrollera arbetsbladets sidhuvud genom:

1. På **Arkiv**-menyn väljer du **Sidlayout**. En dialogruta visas.
1. Välj fliken **Sidhuvud/Sidfot**.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-InsertImageInHeaderFooter-1.cs" >}}
