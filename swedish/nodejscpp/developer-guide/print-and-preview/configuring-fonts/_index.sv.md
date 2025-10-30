---
title: Konfigurera teckensnitt för rendering av kalkylblad med Node.js via C++
linktitle: Konfigurera teckensnitt för rendering av kalkylblad
type: docs
weight: 10
url: /sv/nodejs-cpp/configuring-fonts-for-rendering-spreadsheets/
description: Lär dig hur du konfigurerar teckensnitt för rendering av kalkylblad med Aspose.Cells for Node.js via C++. Säkerställ att teckensnitten är tillgängliga för optimal konverteringskvalitet.
---

## **Möjliga användningsscenario**

Aspose.Cells API:er ger möjlighet att rendera kalkylblad i bildformat samt konvertera dem till PDF- och XPS-format. För att maximera konverteringskvaliteten är det nödvändigt att de teckensnitt som används i kalkylbladet finns tillgängliga i operativsystemets standardfontkatalog. Om de nödvändiga teckensnitten inte finns, kommer Aspose.Cells API:er att försöka ersätta de nödvändiga teckensnitten med de tillgängliga.

## **Val av teckensnitt**

Nedan är processen som Aspose.Cells API: er följer bakom scenen.

1. API försöker hitta teckensnitten på filsystemet som matchar det exakta teckensnittsnamnet som används i kalkylbladet.
1. Om API inte kan hitta teckensnitten med det exakta namnet försöker det använda standardteckensnittet som anges under arbetsbokens [**DefaultStyle.getFont()**](https://reference.aspose.com/cells/nodejs-cpp/style/#getFont--) egenskap.
1. Om API inte kan hitta teckensnittet som definieras under arbetsbokens [**DefaultStyle.getFont()**](https://reference.aspose.com/cells/nodejs-cpp/style/#getFont--) egenskap försöker det använda teckensnittet som anges under [**PdfSaveOptions.getDefaultFont()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getDefaultFont--) eller [**ImageOrPrintOptions.getDefaultFont()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getDefaultFont--) egenskap.
1. Om API inte kan hitta teckensnittet som definieras under [**PdfSaveOptions.getDefaultFont()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getDefaultFont--) eller [**ImageOrPrintOptions.getDefaultFont()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getDefaultFont--) egenskap försöker den använda teckensnittet som anges under [**FontConfigs.getDefaultFontName()**](https://reference.aspose.com/cells/nodejs-cpp/fontconfigs/#getDefaultFontName--) egenskap.
1. Om API inte kan hitta teckensnittet som definieras under [**FontConfigs.getDefaultFontName()**](https://reference.aspose.com/cells/nodejs-cpp/fontconfigs/#getDefaultFontName--) egenskapen försöker det välja de mest lämpliga teckensnitten från alla tillgängliga teckensnitt.
1. Slutligen, om API inte hittar några teckensnitt på filsystemet, renderar den kalkylbladet med Arial.

## **Ange anpassade typsnittsmappar**

Aspose.Cells API söker i operativsystemets standardfontkatalog efter de nödvändiga teckensnitten. Om de inte finns där, söker API:erna i anpassade (användardefinierade) kataloger. Klassen [**FontConfigs**](https://reference.aspose.com/cells/nodejs-cpp/fontconfigs) har exponerat flera sätt att ange anpassade fontkataloger som beskrivs nedan.

1. [**FontConfigs.setFontFolder(string, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/fontconfigs/#setFontFolder-string-boolean-): Metoden är användbar om det endast finns en mapp att ange.
1. [**FontConfigs.setFontFolders(string[], boolean)**](https://reference.aspose.com/cells/nodejs-cpp/fontconfigs/#setFontFolders-stringarray-boolean-): Metoden är användbar när typsnitten finns i flera mappar och användaren vill ange alla mapparna separat istället för att kombinera alla typsnitt i en enda mapp.
1. [**FontConfigs.setFontSources(FontSourceBase[])**](https://reference.aspose.com/cells/nodejs-cpp/fontconfigs/#setFontSources-fontsourcebasearray-): Mekanismen är användbar när användaren vill ladda typsnitt från flera mappar eller en enda typsnittsfil eller typsnittsdata från en byte-array.

{{% alert color="primary" %}}

Både [**FontConfigs.setFontFolder(string, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/fontconfigs/#setFontFolder-string-boolean-) och [**FontConfigs.setFontFolders(string[], boolean)**](https://reference.aspose.com/cells/nodejs-cpp/fontconfigs/#setFontFolders-stringarray-boolean-) metoder accepterar en Boolean typ som andra parameter. Att passera **true** som andra parameter kommer att dirigera Aspose.Cells API:erna att söka igenom undermapparna efter teckensnittsfilerna.

{{% /alert %}}

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Defining string variables to store paths to font folders & font file
const fontFolder1 = path.join(dataDir, "Arial");
const fontFolder2 = path.join(dataDir, "Calibri");
const fontFile = path.join(dataDir, "arial.ttf"); 

// Setting first font folder with SetFontFolder method
// Second parameter directs the API to search the subfolders for font files
AsposeCells.FontConfigs.setFontFolder(fontFolder1, true);

// Setting both font folders with SetFontFolders method
// Second parameter prohibits the API to search the subfolders for font files
AsposeCells.FontConfigs.setFontFolders([fontFolder1, fontFolder2], false);

// Defining FolderFontSource
const sourceFolder = new AsposeCells.FolderFontSource(fontFolder1, false);

// Defining FileFontSource
const sourceFile = new AsposeCells.FileFontSource(fontFile);

// Defining MemoryFontSource
const sourceMemory = new AsposeCells.MemoryFontSource(require("fs").readFileSync(fontFile));

// Setting font sources
AsposeCells.FontConfigs.setFontSources([sourceFolder, sourceFile, sourceMemory]);
```

{{% alert color="primary" %}}

Använd gärna någon av ovan nämnda metoder i början av applikationen, det vill säga; innan du anropar några andra objekt i Aspose.Cells API:erna.

{{% /alert %}} {{% alert color="primary" %}}

Om alla ovan nämnda metoder används för att ställa in teckensnittskällor, kommer endast de senaste inställningarna att träda i kraft.

{{% /alert %}}

## **Mekanism för typsnittsutbyte**

Aspose.Cells API:er ger också möjlighet att specificera ersättningsteckensnitt för rendering. Denna mekanism är användbar när ett nödvändigt teckensnitt inte finns på maskinen där konverteringen sker. Användare kan ange en lista med teckensnittsnamn som ett alternativ till det ursprungliga nödvändiga teckensnittet. För att göra detta har Aspose.Cells API:er exponerat metoden [**FontConfigs.setFontSubstitutes(string, string[])**](https://reference.aspose.com/cells/nodejs-cpp/fontconfigs/#setFontSubstitutes-string-stringarray-) som tar emot 2 parametrar. Den första är av typen **string**, vilken är namnet på teckensnittet som ska ersättas. Den andra är en array av typen **string**, där användare kan ange en lista med teckensnittsnamn som ersättning för det ursprungliga teckensnittet (specificerat i den första parametern).

Här är ett enkelt användningsscenario.

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Substituting the Arial font with Times New Roman & Calibri
AsposeCells.FontConfigs.setFontSubstitutes("Arial", ["Times New Roman", "Calibri"]);
```

## **Informationssamling**

Förutom ovan nämnda metoder har Aspose.Cells API:er även tillhandahållit möjligheter att samla information om vilka källor och ersättningar som har ställts in.

1. [**FontConfigs.getFontSources()**](https://reference.aspose.com/cells/nodejs-cpp/fontconfigs/#getFontSources--) metoden returnerar en array av typen [**FontSourceBase**](https://reference.aspose.com/cells/nodejs-cpp/fontsourcebase) som innehåller listan över angivna fontkällor. Om inga källor har ställts in, returnerar metoden [**FontConfigs.getFontSources()**](https://reference.aspose.com/cells/nodejs-cpp/fontconfigs/#getFontSources--) en tom array.
1. [**FontConfigs.getFontSubstitutes(string)**](https://reference.aspose.com/cells/nodejs-cpp/fontconfigs/#getFontSubstitutes-string-) metoden tar emot en parameter av typen **string** för att specificera teckensnittnamnet för vilket ersättning har ställts in. Om ingen ersättning har ställts in för det angivna teckensnittet, returnerar metod [**FontConfigs.getFontSubstitutes(string)**](https://reference.aspose.com/cells/nodejs-cpp/fontconfigs/#getFontSubstitutes-string-) null.

## **Fortsatta ämnen**
- [Ange standardtypsnitt vid rendering av kalkylark till bilder](/cells/sv/nodejs-cpp/set-default-font-while-rendering-spreadsheet-to-images/)
- [Ställ in egenskapen DefaultFont för PdfSaveOptions och ImageOrPrintOptions för att prioritera](/cells/sv/nodejs-cpp/set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority/)
- [Stödda teckensnittsformat](/cells/sv/nodejs-cpp/supported-font-formats/)
- [Kalkylblad till bild - Ställ in pixelformat för den renderade bilden](/cells/sv/nodejs-cpp/worksheet-to-image-set-pixel-format-for-the-rendered-image/)
{{< app/cells/assistant language="nodejs-cpp" >}}
