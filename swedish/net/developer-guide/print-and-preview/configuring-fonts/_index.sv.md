---
title: Konfigurera teckensnitt för rendering av kalkylblad
type: docs
weight: 10
url: /sv/net/configuring-fonts-for-rendering-spreadsheets/
---

## **Möjliga användningsscenario**

Aspose.Cells API: er tillhandahåller möjlighet att rendera kalkylbladen i bildformat samt konvertera dem till PDF- och XPS-format. För att maximera konversionsfideliteten är det nödvändigt att teckensnitten som används i kalkylbladet bör finnas i operativsystemets standardteckensnittkatalog. Om de nödvändiga teckensnitten inte är närvarande kommer Aspose.Cells API: er att försöka ersätta de nödvändiga teckensnitten med de som finns tillgängliga.

## **Val av teckensnitt**

Nedan är processen som Aspose.Cells API: er följer bakom scenen.

1. API försöker hitta teckensnitten på filsystemet som matchar det exakta teckensnittsnamnet som används i kalkylbladet.
1. Om API inte kan hitta teckensnitten med det exakta namnet försöker det använda standardteckensnittet som anges under arbetsbokens [**DefaultStyle.Font**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font) egenskap.
1. Om API inte kan hitta teckensnittet som definieras under arbetsbokens [**DefaultStyle.Font**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font) egenskap försöker det använda teckensnittet som anges under [**PdfSaveOptions.DefaultFont**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/defaultfont) eller [**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/defaultfont) egenskap.
1. Om API inte kan hitta teckensnittet som definieras under [**PdfSaveOptions.DefaultFont**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/defaultfont) eller [**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/defaultfont) egenskap försöker den använda teckensnittet som anges under [**FontConfigs.DefaultFontName**](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/properties/defaultfontname) egenskap.
1. Om API inte kan hitta teckensnittet som definieras under [**FontConfigs.DefaultFontName**](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/properties/defaultfontname) egenskapen försöker det välja de mest lämpliga teckensnitten från alla tillgängliga teckensnitt.
1. Slutligen, om API inte hittar några teckensnitt på filsystemet, renderar den kalkylbladet med Arial.

## **Ange anpassade typsnittsmappar**

Aspose.Cells API:er söker igenom operativsystemets standardmapp för teckensnitt efter de krävda teckensnitten. Om de krävda teckensnitten inte finns tillgängliga i systemets teckensnittmapp söker API:erna igenom anpassade (användardefinierade) mappar. Klassen [**FontConfigs**](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs) har exponerat ett antal sätt att ange anpassade teckensnittsmapar som detaljeras nedan.

1. [**FontConfigs.SetFontFolder**](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/setfontfolder): Metoden är användbar om det endast finns en mapp att ange.
1. [**FontConfigs.SetFontFolders**](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/setfontfolders): Metoden är användbar när typsnitten finns i flera mappar och användaren vill ange alla mapparna separat istället för att kombinera alla typsnitt i en enda mapp.
1. [**FontConfigs.SetFontSources**](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/setfontsources): Mekanismen är användbar när användaren vill ladda typsnitt från flera mappar eller en enda typsnittsfil eller typsnittsdata från en byte-array.

{{% alert color="primary" %}}

Både [**FontConfigs.SetFontFolder**](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/setfontfolder) och [**FontConfigs.SetFontFolders**](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/setfontfolders) metoder accepterar en Boolean typ som andra parameter. Att passera **true** som andra parameter kommer att dirigera Aspose.Cells API:erna att söka igenom undermapparna efter teckensnittsfilerna.

{{% /alert %}}

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-SetCustomFontFolders-1.cs" >}}

{{% alert color="primary" %}}

Använd gärna någon av ovan nämnda metoder i början av applikationen, det vill säga; innan du anropar några andra objekt i Aspose.Cells API:erna.

{{% /alert %}} {{% alert color="primary" %}}

Om alla ovan nämnda metoder används för att ställa in teckensnittskällor, kommer endast de senaste inställningarna att träda i kraft.

{{% /alert %}}

## **Mekanism för typsnittsutbyte**

Aspose.Cells APIs ger också möjlighet att ange ersättning för teckensnitt för renderingsändamål. Denna mekanism är användbar när ett nödvändigt teckensnitt inte är tillgängligt på den maskin där omvandlingen måste ske. Användare kan ange en lista med teckensnittsnamn som ett alternativ till det ursprungligen nödvändiga teckensnittet. För att uppnå detta har Aspose.Cells APIs exponerat [**FontConfigs.SetFontSubstitutes**](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/setfontsubstitutes)-metoden som accepterar 2 parametrar. Den första parametern är av typ **string**, som ska vara namnet på det teckensnitt som behöver ersättas. Den andra parametern är en array av typ **string**. Användare kan ange en lista med teckensnittsnamn som en ersättning för det ursprungliga teckensnittsnamnet (anges i den första parametern).

Här är ett enkelt användningsscenario.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-SetCustomFontFolders-FontSubstitution.cs" >}}

## **Informationssamling**

Förutom de ovan nämnda metoderna har Aspose.Cells API:erna även medel för att samla information om vilka källor och ersättningar som har angetts.

1. [**FontConfigs.GetFontSources**](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/getfontsources)-metoden returnerar en array av typ [**FontSourceBase**](https://reference.aspose.com/cells/net/aspose.cells/fontsourcebase) som innehåller listan över angivna teckensnittskällor. Om inga källor har ställts in kommer [**FontConfigs.GetFontSources**](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/getfontsources)-metoden att returnera en tom array.
1. [**FontConfigs.GetFontSubstitutes**](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/getfontsubstitutes)-metoden tar emot en parameter av typ **string** som tillåter att specifiera teckensnittsnamnet för vilket ersättning har ställts in. Om ingen ersättning har ställts in för det angivna teckensnittsnamnet kommer [**FontConfigs.GetFontSubstitutes**](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/getfontsubstitutes)-metoden att returnera null.

## **Fortsatta ämnen**
- [Ange standardtypsnitt vid rendering av kalkylark till bilder](/cells/sv/net/set-default-font-while-rendering-spreadsheet-to-images/)
- [Ställ in egenskapen DefaultFont för PdfSaveOptions och ImageOrPrintOptions för att prioritera](/cells/sv/net/set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority/)
- [Stödda teckensnittsformat](/cells/sv/net/supported-font-formats/)
- [Kalkylblad till bild - Ställ in pixelformat för den renderade bilden](/cells/sv/net/worksheet-to-image-set-pixel-format-for-the-rendered-image/)
