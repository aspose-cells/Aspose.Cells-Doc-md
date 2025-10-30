---
title: Konfigurera teckensnitt för rendering av kalkylblad med C++
linktitle: Konfigurera teckensnitt för rendering av kalkylblad
type: docs
weight: 10
url: /sv/cpp/configuring-fonts-for-rendering-spreadsheets/
description: Lär dig hur du konfigurerar teckensnitt för rendering av kalkylblad till bilder, PDF och XPS format med hjälp av Aspose.Cells for C++.
---

## **Möjliga användningsscenario**

Aspose.Cells API:erna möjliggör rendering av kalkylblad i bildformat och konvertering till PDF och XPS. För att maximera konverteringskvaliteten är det nödvändigt att teckensnitten som används i kalkylbladet finns tillgängliga i operativsystemets standardteckensnittsmappar. Om de önskade teckensnitten inte finns närvarande kommer Aspose.Cells API att försöka ersätta de nödvändiga teckensnitten med tillgängliga.

## **Val av teckensnitt**

Nedan följer processen som Aspose.Cells API:erna använder i bakgrunden:

1. API försöker hitta teckensnitten på filsystemet som matchar det exakta teckensnittsnamnet som används i kalkylbladet.
1. Om API:n inte kan hitta teckensnitten med exakt samma namn, försöker det använda standardteckensnittet som anges under Workbook's [**DefaultStyle.Font**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getfont/)-egenskap.
1. Om API:n inte kan hitta teckensnittet definierat under arbetsbokens [**DefaultStyle.Font**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getfont/)-egenskap, försöker det använda det teckensnitt som anges under [**PdfSaveOptions.PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)**](https://reference.aspose.com/cells/cpp/aspose.cells/paginatedsaveoptions/~paginatedsaveoptions/) eller [**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getdefaultfont/)-egenskapen.
1. Om API:n inte kan hitta teckensnittet definierat under [**PdfSaveOptions.PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)**](https://reference.aspose.com/cells/cpp/aspose.cells/paginatedsaveoptions/~paginatedsaveoptions/) eller [**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getdefaultfont/)-egenskapen, försöker det använda teckensnittet som anges under [**FontConfigs.DefaultFontName**](https://reference.aspose.com/cells/cpp/aspose.cells/fontconfigs/getdefaultfontname/)-egenskapen.
1. Om API:n inte kan hitta teckensnittet definierat under [**FontConfigs.DefaultFontName**](https://reference.aspose.com/cells/cpp/aspose.cells/fontconfigs/getdefaultfontname/)-egenskapen, försöker det välja de mest lämpliga teckensnitten från alla tillgängliga teckensnitt.
1. Slutligen, om API:n inte kan hitta några teckensnitt på filsystemet, renderar det kalkylbladet med Arial.

## **Ange anpassade typsnittsmappar**

Aspose.Cells API:erna söker i operativsystemets standardteckensnittsmapp efter de nödvändiga teckensnitten. Om de nödvändiga teckensnitten inte finns tillgängliga i systemets teckensnittsmapp, söker API:erna i anpassade (användardefinierade) kataloger. Klassen [**FontConfigs**](https://reference.aspose.com/cells/cpp/aspose.cells/fontconfigs/) ger flera sätt att ställa in anpassade teckensnittsmappar, som beskrivs nedan:

1. [**FontConfigs.SetFontFolder**](https://reference.aspose.com/cells/cpp/aspose.cells/fontconfigs/setfontfolder/): Metoden är användbar om det endast finns en mapp att ange.
1. [**FontConfigs.SetFontFolders**](https://reference.aspose.com/cells/cpp/aspose.cells/fontconfigs/setfontfolders/): Denna metod är användbar när teckensnitten finns i flera mappar, och användaren vill sätta alla mappar separat snarare än att samla alla teckensnitt i en enda mapp.
1. [**FontConfigs.SetFontSources**](https://reference.aspose.com/cells/cpp/aspose.cells/fontconfigs/setfontsources/): Denna mekanism är användbar när användaren vill ladda fonter från flera mappar, en enda fontfil eller fontdata från en bytearray.

{{% alert color="primary" %}}

Både [**FontConfigs.SetFontFolder**](https://reference.aspose.com/cells/cpp/aspose.cells/fontconfigs/setfontfolder/) och [**FontConfigs.SetFontFolders**](https://reference.aspose.com/cells/cpp/aspose.cells/fontconfigs/setfontfolders/) metoder accepterar en andra parameter av typen Boolean. Att skicka **true** som andra parameter kommer att dirigera Aspose.Cells API:erna att söka efter fontfiler i undermappar.

{{% /alert %}}

```c++
#include <iostream>
#include <fstream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

Vector<uint8_t> GetDataFromFile(const U16String& file)
{
    std::string f = file.ToUtf8();
    // open a file 
    std::ifstream fileStream(f, std::ios::binary);

    if (!fileStream.is_open()) {
        std::cerr << "Failed to open the file." << std::endl;
        return 1;
    }

    // Get file size
    fileStream.seekg(0, std::ios::end);
    std::streampos fileSize = fileStream.tellg();
    fileStream.seekg(0, std::ios::beg);

    // Read file contents into uint8_t array
    uint8_t* buffer = new uint8_t[fileSize];
    fileStream.read(reinterpret_cast<char*>(buffer), fileSize);
    fileStream.close();

    Vector<uint8_t>data(buffer, fileSize);
    delete[] buffer;

    return data;
}

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String fontFolder1 = srcDir + u"Arial";
    U16String fontFolder2 = srcDir + u"Calibri";
    U16String fontFile = srcDir + u"arial.ttf";

    FontConfigs::SetFontFolder(fontFolder1, true);

    Vector<U16String> fontFolders{ fontFolder1 , fontFolder2 };

    FontConfigs::SetFontFolders(fontFolders, false);

    FolderFontSource sourceFolder(fontFolder1, false);
    FileFontSource sourceFile(fontFile);
    Vector<uint8_t> fontData = GetDataFromFile(fontFile);
    MemoryFontSource sourceMemory(fontData);

    Vector<FontSourceBase> fontSources{ sourceFolder ,sourceFile ,sourceMemory };

    FontConfigs::SetFontSources(fontSources);

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}

Var god använd någon av ovan nämnda metoder i början av applikationen, det vill säga innan du anropar andra objekt av Aspose.Cells API:er.

{{% /alert %}}

{{% alert color="primary" %}}

Om alla ovan nämnda metoder används för att ställa in teckensnittskällor, kommer endast de senaste inställningarna att träda i kraft.

{{% /alert %}}

## **Mekanism för typsnittsutbyte**

Aspose.Cells API:erna ger också möjligheten att specificera ersättningsfonter för rendering. Denna mekanism är användbar när en nödvändig font inte är tillgänglig på maskinen där konverteringen ska ske. Användare kan tillhandahålla en lista över fontsnamn som ett alternativ till den ursprungliga fonten. För att uppnå detta har Aspose.Cells API:erna exponerat [**FontConfigs.SetFontSubstitutes**](https://reference.aspose.com/cells/cpp/aspose.cells/fontconfigs/setfontsubstitutes/) metoden, vilken accepterar två parametrar. Den första är av typen **string**, vilket bör vara namnet på fonten som ska ersättas. Den andra är en array av typen **string**. Användare kan tillhandahålla en lista över fontnamn som en ersättning för det ursprungliga fontnamnet (specificerat i första parametern).

Här är ett enkelt användningsscenario:

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Substituting the Arial font with Times New Roman & Calibri
    Vector<U16String> substituteFonts{ u"Times New Roman", u"Calibri" };
    FontConfigs::SetFontSubstitutes(u"Arial", substituteFonts);

    Aspose::Cells::Cleanup();
}
```

## **Informationssamling**

Förutom ovan nämnda metoder tillhandahåller Aspose.Cells API:erna också verktyg för att samla information om vilka källor och ersättningar som har konfigurerats:

1. [**FontConfigs.GetFontSources**](https://reference.aspose.com/cells/cpp/aspose.cells/fontconfigs/getfontsources/) metoden returnerar en array av typen [**FontSourceBase**](https://reference.aspose.com/cells/cpp/aspose.cells/fontsourcebase/) som innehåller listan över angivna fontkällor. Om inga källor har konfigurerats, kommer [**FontConfigs.GetFontSources**](https://reference.aspose.com/cells/cpp/aspose.cells/fontconfigs/getfontsources/) metoden att returnera en tom array.
1. [**FontConfigs.GetFontSubstitutes**](https://reference.aspose.com/cells/cpp/aspose.cells/fontconfigs/getfontsubstitutes/) metoden accepterar en parameter av typen **string**, vilket tillåter dig att specificera fontnamnet för vilket ersättning har konfigurerats. Om ingen ersättning har konfigurerats för det angivna fontnamnet, returnerar [**FontConfigs.GetFontSubstitutes**](https://reference.aspose.com/cells/cpp/aspose.cells/fontconfigs/getfontsubstitutes/) metoden null.

## **Avancerade ämnen**
- [Ange standardtypsnitt vid rendering av kalkylark till bilder](/cells/sv/cpp/set-default-font-while-rendering-spreadsheet-to-images/)
- [Ställ in egenskapen DefaultFont för PdfSaveOptions och ImageOrPrintOptions för att prioritera](/cells/sv/cpp/set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority/)
- [Stödda teckensnittsformat](/cells/sv/cpp/supported-font-formats/)
{{< app/cells/assistant language="cpp" >}}
