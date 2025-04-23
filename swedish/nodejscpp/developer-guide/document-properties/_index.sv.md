---
title: Hantera dokumentegenskaper med Node.js via C++
linktitle: Dokumentegenskaper
type: docs
weight: 80
url: /sv/nodejs-cpp/managing-document-properties/
description: Lär dig hur du hanterar dokumentegenskaper genom Aspose.Cells for Node.js via C++ API er.
keywords: Hur man hanterar dokumentegenskaper i Node.js via C++, Hämta eller ställ in dokumentegenskaper med Node.js via C++, Lägg till eller ta bort dokumentegenskaper via Node.js via C++, Infoga eller ta bort dokumentegenskaper med Node.js via C++, Infoga eller ta bort dokumentegenskaper med Node.js via C++, Hur man får åtkomst till dokumentegenskaper med Aspose.Cells for Node.js via C++ API er.
---


## **Introduktion**

Microsoft Excel ger möjligheten att lägga till egenskaper i kalkylbladfiler. Dessa dokumentegenskaper förser användbar information och är uppdelade i 2 kategorier enligt detaljerna nedan.

- Systemdefinierade (inbyggda) egenskaper: Inbyggda egenskaper innehåller allmän information om dokumentet som dokumenttitel, författarnamn, dokumentstatistik och så vidare.
- Användardefinierade (anpassade) egenskaper: Anpassade egenskaper som definieras av användaren i form av namn-värdepar.

{{% alert color="primary" %}}

Det viktigaste att veta om inbyggda och anpassade egenskaper är att inbyggda egenskaper kan kommas åt och ändras, men inte skapas eller tas bort. Däremot kan anpassade egenskaper skapas och hanteras.

{{% /alert %}}

## **Hur man hanterar dokumentegenskaper med Microsoft Excel**

Microsoft Excel gör det möjligt att hantera dokumentegenskaper för Excel-filer på ett WYSIWYG-sätt. Följ stegen nedan för att öppna **Egenskaper**-dialogrutan i Excel 2016.

1. Välj **Info** i **Fil**-menyn.

|**Val av Info-meny**|
| :- |
|![todo:image_alt_text](managing-document-properties_1.png)|
2. Klicka på **Egenskaper** och välj "Avancerade egenskaper".

|**Klicka på Avancerad Val av egenskaper**|
| :- |
|![todo:image_alt_text](managing-document-properties_2.png)|
3. Hantera filens dokumentegenskaper.

|**Dialogruta Egenskaper**|
| :- |
|![todo:image_alt_text](managing-document-properties_3.png)|
I dialogrutan Egenskaper finns olika flikar, som Allmänt, Sammanfattning, Statistik, Innehåll och Anpassade. Varje flik hjälper till att konfigurera olika typer av information relaterad till filen. Anpassad flik används för att hantera anpassade egenskaper.

## **Hur man arbetar med dokumentegenskaper med Aspose.Cells**

Utvecklare kan dynamiskt hantera dokumentegenskaper med hjälp av Aspose.Cells API:er. Denna funktion hjälper utvecklarna att lagra användbar information tillsammans med filen, som när filen mottogs, bearbetades, tidsstämplades och så vidare.

{{% alert color="primary" %}}

Aspose.Cells for Node.js via C++ skriver direkt information om API och versionsnummer i utdatafiler. Till exempel, vid konvertering av dokument till PDF, fyller Aspose.Cells for Node.js via C++ i **Application**-fältet med värdet 'Aspose.Cells' och **PDF Producer**-fältet med värdet, t.ex. 'Aspose.Cells v17.9'.

Observera att du inte kan instruera Aspose.Cells for Node.js via C++ att ändra eller ta bort denna information från utdatafiler.

{{% /alert %}}

### **Hur man får åtkomst till dokumentegenskaper**

Aspose.Cells API:er stödjer båda typerna av dokumentegenskaper, inbyggda och anpassade. Aspose.Cells' [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)-klass representerar en Excel-fil och, precis som en Excel-fil, kan [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)-klassen innehålla flera kalkblad, var och ett representerat av [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)-klassen medan samlingen av kalkblad representeras av [**WorksheetCollection**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection)-klassen.

Använd [**WorksheetCollection**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection) för att komma åt filens dokumentegenskaper som beskrivs nedan.

- För att komma åt inbyggda dokumentegenskaper, använd [**WorksheetCollection.getBuiltInDocumentProperties()**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#getBuiltInDocumentProperties--).
- För att komma åt anpassade dokumentegenskaper, använd [**WorksheetCollection.getCustomDocumentProperties()**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#getCustomDocumentProperties--).

Både [**WorksheetCollection.getBuiltInDocumentProperties()**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#getBuiltInDocumentProperties--) och [**WorksheetCollection.getCustomDocumentProperties()**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#getCustomDocumentProperties--) returnerar instansen av [**Aspose.Cells.Properties.DocumentPropertyCollection**](https://reference.aspose.com/cells/nodejs-cpp/documentpropertycollection/). Denna samling innehåller [**Aspose.Cells.Properties.DocumentProperty**](https://reference.aspose.com/cells/nodejs-cpp/documentproperty/) objekt, var och ett som representerar en enkel inbyggd eller anpassad dokumentegenskap.

Det är upp till applikationskravet hur man får åtkomst till en egenskap, dvs. genom att använda index eller namn på egenskapen från [**DocumentPropertyCollection**](https://reference.aspose.com/cells/nodejs-cpp/documentpropertycollection/) som visas i exemplet nedan.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample-document-properties.xlsx");
// Instantiate a Workbook object
// Open an Excel file
const workbook = new AsposeCells.Workbook(filePath);

// Retrieve a list of all custom document properties of the Excel file
const customProperties = workbook.getCustomDocumentProperties();

// Accessing a custom document property by using the property name
const customProperty1 = customProperties.get("ContentTypeId");
console.log(`${customProperty1.getName()} ${customProperty1.getValue()}`);

// Accessing the same custom document property by using the property index
const customProperty2 = customProperties.get(0);
console.log(`${customProperty2.getName()} ${customProperty2.getValue()}`);
```

[**Aspose.Cells.Properties.DocumentProperty**](https://reference.aspose.com/cells/nodejs-cpp/documentproperty/)-klassen gör det möjligt att hämta namn, värde och typ för dokumentegenskapen:

- För att få egenskapens namn, använd [**DocumentProperty.getName()**](https://reference.aspose.com/cells/nodejs-cpp/documentproperty/#getName--).
- För att hämta egenskapens värde, använd [**DocumentProperty.getValue()**](https://reference.aspose.com/cells/nodejs-cpp/documentproperty/#getValue--). [**DocumentProperty.getValue()**](https://reference.aspose.com/cells/nodejs-cpp/documentproperty/#getValue--) returnerar värdet som ett objekt.
- För att hämta egenskapstypen, använd [**DocumentProperty.getType()**](https://reference.aspose.com/cells/nodejs-cpp/documentproperty/#getType--). Detta returnerar ett av [**PropertyType**](https://reference.aspose.com/cells/nodejs-cpp/propertytype/)-enumerationsvärdena. Efter att du har fått egenskapstypen, använd någon av **DocumentProperty.ToXXX**-metoderna för att erhålla värdet av lämplig typ istället för att använda [**DocumentProperty.getValue()**](https://reference.aspose.com/cells/nodejs-cpp/documentproperty/#getValue--). **DocumentProperty.ToXXX**-metoderna beskrivs i tabellen nedan.

{{% alert color="primary" %}}

 [**DocumentProperty**](https://reference.aspose.com/cells/nodejs-cpp/documentproperty/) -klassen ger också ett set av metoder som returnerar värden av andra datatyper.

{{% /alert %}}

|**Medlemsnamn**|**Beskrivning**|**ToXXX-metod**|
| :- | :- | :- |
|Boolean| Egenskapens datatyp är Boolean|ToBool|
|Date| Egenskapens datatyp är DateTime. Observera att Microsoft Excel endast lagrar <br>datumdelen, ingen tid kan lagras i en anpassad egenskap av denna typ|ToDateTime|
|Float| Egenskapens datatyp är Dubbel|ToDouble|
|Number| Egenskapens datatyp är Int32|ToInt|
|String|Typen av egenskapsdata är string|ToString|

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample-document-properties.xlsx");
// Instantiate a Workbook object
// Open an Excel file
const workbook = new AsposeCells.Workbook(filePath);

// Retrieve a list of all custom document properties of the Excel file
const customProperties = workbook.getCustomDocumentProperties();

// Accessing a custom document property
const customProperty1 = customProperties.get(0);

// Storing the value of the document property as an object
const objectValue = customProperty1.getValue();

// Accessing a custom document property
const customProperty2 = customProperties.get(1);

// Checking the type of the document property and then storing the value of the
// document property according to that type
if (customProperty2.getType() === AsposeCells.PropertyType.String) {
const value = customProperty2.getValue().toString();
console.log(`${customProperty2.getName()} : ${value}`);
}
```

### **Hur man lägger till eller tar bort anpassade dokumentegenskaper**

Som vi tidigare har beskrivit i början av detta ämne kan utvecklare inte lägga till eller ta bort inbyggda egenskaper eftersom dessa egenskaper är systemdefinierade men det är möjligt att lägga till eller ta bort anpassade egenskaper eftersom dessa är användardefinierade.

### **Hur man lägger till anpassade egenskaper**

Aspose.Cells API:er har exponerat [**add(string, string)**](https://reference.aspose.com/cells/nodejs-cpp/customdocumentpropertycollection/#add-string-string-)-metoden för [**CustomDocumentPropertyCollection**](https://reference.aspose.com/cells/nodejs-cpp/customdocumentpropertycollection/)-klassen för att lägga till anpassade egenskaper till samlingen. [**add(string, string)**](https://reference.aspose.com/cells/nodejs-cpp/customdocumentpropertycollection/#add-string-string-)-metoden lägger till egenskapen i excel-filen och returnerar en referens till den nya dokumentegenskapen som ett [**Aspose.Cells.Properties.DocumentProperty**](https://reference.aspose.com/cells/nodejs-cpp/documentproperty/)-objekt.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Instantiate a Workbook object
// Open an Excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sample-document-properties.xlsx"));

// Retrieve a list of all custom document properties of the Excel file
const customProperties = workbook.getCustomDocumentProperties();

// Adding a custom document property to the Excel file
customProperties.add("Publisher", "Aspose");

// Saving resultant spreadsheet
workbook.save(path.join(dataDir, "out_sample-document-properties.xlsx"));
```

### **Hur man konfigurerar egendom med länk till innehåll**

För att skapa en anpassad egenskap kopplad till innehållet i ett givet område, kalla på [**CustomDocumentPropertyCollection.addLinkToContent(string, string)**](https://reference.aspose.com/cells/nodejs-cpp/customdocumentpropertycollection/#addLinkToContent-string-string-)-metoden och passera egenskapens namn och källa. Du kan kontrollera om en egenskap är konfigurerad som kopplad till innehåll med hjälp av [**DocumentProperty.isLinkedToContent()**](https://reference.aspose.com/cells/nodejs-cpp/documentproperty/#isLinkedToContent--)-egenskapen. Dessutom är det också möjligt att få källområdet med hjälp av [**getSource()**](https://reference.aspose.com/cells/nodejs-cpp/documentproperty/#getSource--)-egenskapen i [**DocumentProperty**](https://reference.aspose.com/cells/nodejs-cpp/documentproperty/)-klassen.

Vi använder en enkel mall Microsoft Excel-fil i exemplet. Arbetsboken har en definierad namngiven område märkt **MyRange** som hänvisar till en cellvärde.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Instantiate an object of Workbook
// Open an Excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sample-document-properties.xlsx"));

// Retrieve a list of all custom document properties of the Excel file
const customProperties = workbook.getWorksheets().getCustomDocumentProperties();

// Add link to content.
customProperties.addLinkToContent("Owner", "MyRange");

// Accessing the custom document property by using the property name
const customProperty1 = customProperties.get("Owner");

// Check whether the property is linked to content
const isLinkedToContent = customProperty1.isLinkedToContent();

// Get the source for the property
const source = customProperty1.getSource();

// Save the file
workbook.save(path.join(dataDir, "out_sample-document-properties.xlsx"));
```

### **Hur man tar bort anpassade egenskaper**

För att ta bort anpassade egenskaper med Aspose.Cells, kalla på [**DocumentPropertyCollection.remove(string)**](https://reference.aspose.com/cells/nodejs-cpp/documentpropertycollection/#remove-string-)-metoden och passera namnet på dokumentegenskapen som ska tas bort.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Instantiate a Workbook object
// Open an Excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sample-document-properties.xlsx"));

// Retrieve a list of all custom document properties of the Excel file
const customProperties = workbook.getCustomDocumentProperties();

// Removing a custom document property
customProperties.remove("Publisher");

// Save the file
workbook.save(path.join(dataDir, "out_sample-document-properties.xlsx"));
```

## **Fortsatta ämnen**
- [Lägga till anpassade egenskaper synliga inuti dokumentinformationspanelen](/cells/sv/nodejs-cpp/adding-custom-properties-visible-inside-document-information-panel/)
- [Inställning av ScaleCrop och LinksUpToDate egenskaper för inbyggda dokumentegenskaper](/cells/sv/nodejs-cpp/setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties/)
- [Ange dokumentversionen för Excel-filen med hjälp av inbyggda dokumentegenskaper](/cells/sv/nodejs-cpp/specify-document-version-of-the-excel-file-using-builtin-document-properties/)
- [Ange språket för Excel-filen med hjälp av inbyggda dokumentegenskaper](/cells/sv/nodejs-cpp/specify-the-language-of-the-excel-file-using-builtin-document-properties/)
