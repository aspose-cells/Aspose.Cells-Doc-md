---
title: Ställa in sidhuvuden och sidfötter
type: docs
weight: 30
url: /sv/net/setting-headers-and-footers/
description: Den här artikeln förklarar hur du programmässigt infogar en bild i sidhuvudet och sidfoten i Excel-kalkylblad genom att ställa in sidhuvudet och sidfoten med skriptkommandon med hjälp av biblioteket C# API eller .NET.
keywords: insert image in excel header footer c#, set excel header footer script commands c#
---
{{% alert color="primary" %}}

Sidhuvuden och sidfötter är de textrader som visas under den övre marginalen respektive över den nedre marginalen. Det är möjligt att lägga till sidhuvuden och sidfötter till kalkylbladen också. Sidhuvuden och sidfötter kan användas för att visa användbar information som sidnummer, författarens namn, ämnesnamn eller datum och tid. Sidhuvuden och sidfötter hanteras med hjälp av sidinställningarna.

{{% /alert %}}

##  **Ställa in sidhuvuden och sidfötter**

Aspose.Cells låter dig lägga till sidhuvuden och sidfötter till kalkylblad under körning, men vi rekommenderar att du ställer in sidhuvuden och sidfötter manuellt i en fördesignad fil för utskrift. Du kan använda Microsoft Excel som ett GUI-verktyg för att ställa in sidhuvuden och sidfötter för att spara ansträngning och utvecklingstid. Aspose.Cells kan importera filen och spara inställningarna.

För att lägga till sidhuvuden och sidfötter under körning tillhandahåller Aspose.Cells speciella API-anrop och skriptkommandon för att formatera sidhuvuden och sidfötter.

###  **Skriptkommandon**

Skriptkommandon är speciella kommandon som låter dig ställa in sidhuvuds- och sidfotsformatering.

|**Skriptkommandon**|**Beskrivning**|
| :- | :- |
|&P|Aktuellt sidnummer|
|&G|En bild|
|&N|Det totala antalet sidor|
|&D|Det aktuella datumet|
|&T|Den aktuella tiden|
|&A|Kalkylbladets namn|
|&F|Filnamnet utan dess sökväg|
|&"\<FontName>"|Representerar ett teckensnittsnamn. Till exempel: &"Arial"|
|&"\<FontName>, \<FontStyle>"|Representerar teckensnittsnamn med stil. Till exempel: &"Arial,Fet"|
|&\<FontSize>|Representerar teckenstorlek. Till exempel: "&14abc". Men om detta kommando följs av ett vanligt nummer som ska skrivas ut i rubriken, bör detta separeras med ett mellanslag från teckenstorleken. Till exempel: "&14 123".|

###  **Ställ in sidhuvuden och sidfötter**

 De[**Utskriftsformat**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup) klass ger två metoder,[**SetHeader**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/methods/setheader) och[**SetFooter**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/methods/setfooter), används för att lägga till ett sidhuvud och en sidfot i ett kalkylblad. Dessa metoder tar bara två parametrar:

- **Sektion** – avsnittet där sidhuvudet eller sidfoten ska placeras. Det finns tre sektioner: vänster, mitten och höger, representerade av 0, 1 respektive 2.
- **Manus** – skriptet som ska användas för sidhuvudet eller sidfoten. Det här skriptet innehåller skriptkommandon för att formatera sidhuvuden eller sidfötter.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetHeadersAndFooters-1.cs" >}}

###  **Infoga en bild i en sidhuvud eller sidfot**

 De[**Utskriftsformat**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup) klass har ytterligare två metoder,[**SetHeaderPicture**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/methods/setheaderpicture) och[**SetFooterPicture**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/methods/setfooterpicture), används för att lägga till bilder i sidhuvudet och sidfoten. Dessa metoder tar parametrarna:

- **Sektion**– sidhuvudet eller sidfoten där bilden ska placeras. Det finns tre sektioner, vänster, mitten och höger, representerade av värdena 0, 1 respektive 2.
- **Byte array** – de grafiska data (de binära data bör skrivas in i bufferten för en byte-array).

Efter att ha kört koden nedan och öppnat filen, kontrollera rubriken på kalkylbladet genom att:

1.  På**Fil** menyn, välj *Sidinställningar**. En dialogruta kommer att visas.
1.  Välj**Sidhuvud/sidfot** flik.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-InsertImageInHeaderFooter-1.cs" >}}
