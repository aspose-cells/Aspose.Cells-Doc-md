---
title:  Inställa sidhuvuden och sidfötter 
type: docs
weight: 30
url: /sv/python-net/setting-headers-and-footers/
description: Denna artikel förklarar hur man programmatoriskt infogar en bild i sidhuvudet och sidfoten av Excel ark genom att ställa in sidhuvudet och sidfoten med skriptkommandon med hjälp av Aspose.Cells för Python via .NET API.
keywords: Python Excel Library, Python infoga bild i excelsidhuvudfot, ställa in excel sidhuvudfot skriptkommandon med Python.
---

{{% alert color="primary" %}}

Sidhuvuden och sidfötter är textrader som visas under övre marginalen eller ovanför den nedre marginalen. Det är möjligt att lägga till sidhuvuden och sidfötter i kalkylbladen också. Sidhuvuden och sidfötter kan användas för att visa användbar information som sidnummer, författarnamn, ämnesnamn eller datum och tid. Sidhuvuden och sidfötter hanteras med sidlayoutinställningarna.

{{% /alert %}}

## **Ställa in sidhuvuden och sidfötter**

Aspose.Cells för Python via .NET låter dig lägga till sidhuvuden och sidfotter i kalkylblad dynamiskt men vi rekommenderar att ställa in sidhuvuden och sidfotter manuellt i en fördesignad fil för utskrift. Du kan använda Microsoft Excel som ett GUI-verktyg för att ställa in sidhuvuden och sidfotter för att spara ansträngning och utvecklingstid. Aspose.Cells för Python via .NET kan importera filen och spara inställningarna.

För att lägga till sidhuvuden och sidfotter under körning tillhandahåller Aspose.Cells för Python via .NET särskilda API-anrop och skriptkommandon för att formatera sidhuvuden och sidfotter.

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

### **Hur man ställer in sidhuvuden och sidfötter**

[**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup)-klassen tillhandahåller två metoder, [**set_header**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/set_header/#int-str) och [**set_footer**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/set_footer/#int-str), som används för att lägga till en sidhuvud och sidfot till ett arbetsblad. Dessa metoder tar endast två parametrar:

- **Avsnitt** – avsnittet där sidhuvudet eller sidfoten ska placeras. Det finns tre avsnitt: vänster, mitten och höger, representerade av 0, 1 och 2 respektive.
- **Skript** – skriptet som ska användas för sidhuvudet eller sidfoten. Detta skript innehåller skriptkommandon för att formatera sidhuvuden eller sidfötter.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-SetHeadersAndFooters-1.py" >}}

### **Hur man infogar en bild i ett sidhuvud eller sidfot**

[**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup)-klassen har två ytterligare metoder, [**set_header_picture**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/set_header_picture/#int-bytes) och [**set_footer_picture**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/set_footer_picture/#int-bytes), som används för att lägga till bilder i sidhuvud och sidfot. Dessa metoder tar parametrarna:

- **Avsnitt** – avsnittet för sidhuvudet eller sidfoten där bilden ska placeras. Det finns tre avsnitt, vänster, mitten och höger, representerade av värdena 0, 1 och 2 respektive.
- **Byte-arrayer** – de grafiska data (de binära data ska skrivas in i bufferten i en byte-array).

Efter att ha utfört koden nedan och öppnat filen, kontrollera arbetsbladets sidhuvud genom:

1. På **Arkiv**-menyn väljer du **Sidlayout**. En dialogruta visas.
1. Välj fliken **Sidhuvud/Sidfot**.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-InsertImageInHeaderFooter-1.py" >}}
