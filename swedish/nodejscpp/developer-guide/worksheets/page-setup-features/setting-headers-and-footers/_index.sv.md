---
title: Inställning av rubriker och sidfötter med Node.js via C++
linktitle:  Inställa sidhuvuden och sidfötter 
type: docs
weight: 30
url: /sv/nodejs-cpp/setting-headers-and-footers/
description: Denna artikel förklarar hur man programmässigt infogar en bild i rubrik och sidfötter i Excel arbetsblad med Aspose.Cells for Node.js via C++. 
keywords: infoga bild i excel rubrik sidfots Node.js via C++, sätt excel rubrik sidfot skriptkommandon Node.js via C++
---

{{% alert color="primary" %}}

Sidhuvuden och sidfötter är textrader som visas under övre marginalen eller ovanför den nedre marginalen. Det är möjligt att lägga till sidhuvuden och sidfötter i kalkylbladen också. Sidhuvuden och sidfötter kan användas för att visa användbar information som sidnummer, författarnamn, ämnesnamn eller datum och tid. Sidhuvuden och sidfötter hanteras med sidlayoutinställningarna.

{{% /alert %}}

## **Ställa in sidhuvuden och sidfötter**

Aspose.Cells for Node.js via C++ tillåter dig att lägga till rubriker och sidfötter till arbetsblad vid körning, men vi rekommenderar att du ställer in rubriker och sidfötter manuellt i en fördesignad fil för utskrift. Du kan använda Microsoft Excel som ett grafiskt användargränssnitt för att ställa in rubriker och sidfötter för att spara tid och ansträngning. Aspose.Cells kan importera filen och spara inställningarna.

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
|&&Text| Visar &Text. Till exempel: &&WO kommer att visas som &WO|
|&"\<FontName>"|Representerar ett typsnittsnamn. Till exempel: &"Arial"|
|&"\<FontName>, \<FontStyle>"|Representerar typsnittsnamn med stil. Till exempel: &"Arial,Fetstil"|
|&\<FontSize>|Representerar teckensnittsstorlek. Till exempel: “&14abc”. Men om detta kommando följs av ett vanligt nummer som ska skrivas ut i sidhuvudet, ska detta separeras med ett mellanslag från teckensnittsstorleken. Till exempel: “&14 123”|

### **Ställ in headers och footers**

Klass [**PageSetup**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup) erbjuder två metoder, [**setHeader(number, string)**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#setHeader-number-string-) och [**setFooter(number, string)**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#setFooter-number-string-), som används för att lägga till en rubrik och en sidfot till ett kalkylblad. Dessa metoder tar endast två parametrar:

- **Avsnitt** – avsnittet där sidhuvudet eller sidfoten ska placeras. Det finns tre avsnitt: vänster, mitten och höger, representerade av 0, 1 och 2 respektive.
- **Skript** – skriptet som ska användas för sidhuvudet eller sidfoten. Detta skript innehåller skriptkommandon för att formatera sidhuvuden eller sidfötter.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const excel = new AsposeCells.Workbook();

// Obtaining the reference of the PageSetup of the worksheet
const pageSetup = excel.getWorksheets().get(0).getPageSetup();

// Setting worksheet name at the left section of the header
pageSetup.setHeader(0, "&A");

// Setting current date and current time at the central section of the header
// and changing the font of the header
pageSetup.setHeader(1, "&\"Times New Roman,Bold\"&D-&T");

// Setting current file name at the right section of the header and changing the
// font of the header
pageSetup.setHeader(2, "&\"Times New Roman,Bold\"&12&F");

// Setting a string at the left section of the footer and changing the font
// of a part of this string ("123")
pageSetup.setFooter(0, "Hello World! &\"Courier New\"&14 123");

// Setting the current page number at the central section of the footer
pageSetup.setFooter(1, "&P");

// Setting page count at the right section of footer
pageSetup.setFooter(2, "&N");

// Save the Workbook.
excel.save("SetHeadersAndFooters_out.xls");
```

### **Infoga en bild i en sidhuvud eller sidfot**

Klass [**PageSetup**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup) har två ytterligare metoder, [**setHeaderPicture(number, number[])**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#setHeaderPicture-number-numberarray-) och [**setFooterPicture(number, number[])**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#setFooterPicture-number-numberarray-), som används för att lägga till bilder i rubriken och sidfoten. Dessa metoder tar parametrarna:

- **Avsnitt** – avsnittet för sidhuvudet eller sidfoten där bilden ska placeras. Det finns tre avsnitt, vänster, mitten och höger, representerade av värdena 0, 1 och 2 respektive.
- **Byte-arrayer** – de grafiska data (de binära data ska skrivas in i bufferten i en byte-array).

Efter att ha utfört koden nedan och öppnat filen, kontrollera arbetsbladets sidhuvud genom:

1. På **Arkiv**-menyn väljer du **Sidlayout**. En dialogruta visas.
1. Välj fliken **Sidhuvud/Sidfot**.

```javascript
const fs = require("fs");
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Creating a Workbook object
const workbook = new AsposeCells.Workbook();

// Creating a string variable to store the url of the logo/picture
const logoUrl = path.join(dataDir, "aspose-logo.jpg");

// Declaring a byte array
const binaryData = fs.readFileSync(logoUrl);

// Creating a PageSetup object to get the page settings of the first worksheet of the workbook
const pageSetup = workbook.getWorksheets().get(0).getPageSetup();

// Setting the logo/picture in the central section of the page header
pageSetup.setHeaderPicture(1, binaryData);

// Setting the script for the logo/picture
pageSetup.setHeader(1, "&G");

// Setting the Sheet's name in the right section of the page header with the script
pageSetup.setHeader(2, "&A");

// Saving the workbook
workbook.save(path.join(dataDir, "InsertImageInHeaderFooter_out.xls"));
```
{{< app/cells/assistant language="nodejs-cpp" >}}
