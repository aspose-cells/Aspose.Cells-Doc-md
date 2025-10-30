---
title: Konfigurera teckensnitt för rendering av kalkylblad
type: docs
weight: 10
url: /sv/python-net/configuring-fonts-for-rendering-spreadsheets/
---

## **Möjliga användningsscenario**

Aspose.Cells för Python via .NET API:erna ger möjlighet att rendera kalkylblad i bildformat samt konvertera dem till PDF- och XPS-format. För att optimera konverteringens kvalitet är det viktigt att typsnitten som används i kalkylbladet finns i operativsystemets standardtypsnitts-mapp. Om de nödvändiga typsnitten inte finns tillgängliga kommer Aspose.Cells för Python via .NET API:erna att försöka ersätta dessa med tillgängliga typsnitt.

## **Val av teckensnitt**

Nedanför följer processen som Aspose.Cells för Python via .NET API:erna utför bakom kulisserna.

1. API försöker hitta teckensnitten på filsystemet som matchar det exakta teckensnittsnamnet som används i kalkylbladet.
1. Om API inte kan hitta teckensnitten med det exakta namnet försöker det använda standardteckensnittet som anges under arbetsbokens [**DefaultStyle.font**](https://reference.aspose.com/cells/python-net/aspose.cells/style/font) egenskap.
1. Om API inte kan hitta teckensnittet som definieras under arbetsbokens [**DefaultStyle.font**](https://reference.aspose.com/cells/python-net/aspose.cells/style/font) egenskap försöker det använda teckensnittet som anges under [**PdfSaveOptions.default_font**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/default_font/) eller [**ImageOrPrintOptions.default_font**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/default_font) egenskap.
1. Om API inte kan hitta teckensnittet som definieras under [**PdfSaveOptions.default_font**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/default_font/) eller [**ImageOrPrintOptions.default_font**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/default_font) egenskap försöker den använda teckensnittet som anges under [**FontConfigs.default_font_name**](https://reference.aspose.com/cells/python-net/aspose.cells/fontconfigs/default_font_name) egenskap.
1. Om API inte kan hitta teckensnittet som definieras under [**FontConfigs.default_font_name**](https://reference.aspose.com/cells/python-net/aspose.cells/fontconfigs/default_font_name) egenskapen försöker det välja de mest lämpliga teckensnitten från alla tillgängliga teckensnitt.
1. Slutligen, om API inte hittar några teckensnitt på filsystemet, renderar den kalkylbladet med Arial.

## **Ange anpassade typsnittsmappar**

Aspose.Cells för Python via .NET API:erna söker i operativsystemets standardtypsnitts-mapp efter de nödvändiga typsnitten. Om de inte finns tillgängliga i systemets typsnittsmapp söker API:erna i anpassade (användardefinierade) kataloger. Klassen [**FontConfigs**](https://reference.aspose.com/cells/python-net/aspose.cells/fontconfigs) har flera sätt att ställa in egna typsnittskataloger, vilket beskrivs nedan.

1. [**FontConfigs.set_font_folder**](https://reference.aspose.com/cells/python-net/aspose.cells/fontconfigs/set_font_folder/): Metoden är användbar om det endast finns en mapp att ange.
1. [**FontConfigs.set_font_folders**](https://reference.aspose.com/cells/python-net/aspose.cells/fontconfigs/set_font_folders/): Metoden är användbar när typsnitten finns i flera mappar och användaren vill ange alla mapparna separat istället för att kombinera alla typsnitt i en enda mapp.
1. [**FontConfigs.set_font_sources**](https://reference.aspose.com/cells/python-net/aspose.cells/fontconfigs/set_font_sources/#list): Mekanismen är användbar när användaren vill ladda typsnitt från flera mappar eller en enda typsnittsfil eller typsnittsdata från en byte-array.

{{% alert color="primary" %}}

Både [**FontConfigs.set_font_folder**](https://reference.aspose.com/cells/python-net/aspose.cells/fontconfigs/set_font_folder/) och [**FontConfigs.set_font_folders**](https://reference.aspose.com/cells/python-net/aspose.cells/fontconfigs/set_font_folders/) metoderna accepterar en andra parameter av typen Boolean. Att skicka **true** som andra parameter kommer att dirigera Aspose.Cells för Python via .NET API:erna att söka igenom undermappar efter typsnittsfiler.

{{% /alert %}}

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-SetCustomFontFolders-1.py" >}}

{{% alert color="primary" %}}

Använd någon av ovan nämnda metoder i början av applikationen, det vill säga innan du anropar andra objekt i Aspose.Cells för Python via .NET API:erna.

{{% /alert %}} {{% alert color="primary" %}}

Om alla ovan nämnda metoder används för att ställa in teckensnittskällor, kommer endast de senaste inställningarna att träda i kraft.

{{% /alert %}}

## **Mekanism för typsnittsutbyte**

Aspose.Cells för Python via .NET API:erna ger också möjlighet att specificera ett ersättningstypsnitt för rendering. Denna mekanism är användbar när ett nödvändigt typsnitt inte finns tillgängligt på maskinen där konverteringen sker. Användare kan ange en lista med typsnittsnamn som alternativ till det ursprungligen nödvändiga typsnittet. För att åstadkomma detta har Aspose.Cells för Python via .NET API:erna tillgång till [**FontConfigs.set_font_substitutes**](https://reference.aspose.com/cells/python-net/aspose.cells/fontconfigs/set_font_substitutes/#str-list) metoden som tar emot 2 parametrar. Den första parametern är av typen **string**, vilket bör vara namnet på typsnittet som ska ersättas. Den andra parametern är en array av typen **string** där användare kan ange en lista med typsnittsnamn som ersättning för det ursprungliga typsnittet (specificerat i den första parametern).

Här är ett enkelt användningsscenario.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-SetCustomFontFolders-FontSubstitution.py" >}}

## **Informationssamling**

Förutom ovan nämnda metoder, har Aspose.Cells för Python via .NET också gjort det möjligt att samla information om vilka källor och ersättningar som har satts.

1. [**FontConfigs.get_font_sources**](https://reference.aspose.com/cells/python-net/aspose.cells/fontconfigs/get_font_sources/#)-metoden returnerar en array av typ [**FontSourceBase**](https://reference.aspose.com/cells/python-net/aspose.cells/fontsourcebase) som innehåller listan över angivna teckensnittskällor. Om inga källor har ställts in kommer [**FontConfigs.get_font_sources**](https://reference.aspose.com/cells/python-net/aspose.cells/fontconfigs/get_font_sources/#)-metoden att returnera en tom array.
1. [**FontConfigs.get_font_substitutes**](https://reference.aspose.com/cells/python-net/aspose.cells/fontconfigs/get_font_substitutes/#str)-metoden tar emot en parameter av typ **string** som tillåter att specifiera teckensnittsnamnet för vilket ersättning har ställts in. Om ingen ersättning har ställts in för det angivna teckensnittsnamnet kommer [**FontConfigs.get_font_substitutes**](https://reference.aspose.com/cells/python-net/aspose.cells/fontconfigs/get_font_substitutes/#str)-metoden att returnera null.

## **Fortsatta ämnen**
- [Ange standardtypsnitt vid rendering av kalkylark till bilder](/cells/sv/python-net/set-default-font-while-rendering-spreadsheet-to-images/)
- [Ställ in egenskapen DefaultFont för PdfSaveOptions och ImageOrPrintOptions för att prioritera](/cells/sv/python-net/set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority/)
- [Stödda teckensnittsformat](/cells/sv/python-net/supported-font-formats/)
- [Kalkylblad till bild - Ställ in pixelformat för den renderade bilden](/cells/sv/python-net/worksheet-to-image-set-pixel-format-for-the-rendered-image/)

{{< app/cells/assistant language="python-net" >}}
