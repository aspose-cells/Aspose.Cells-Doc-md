---
title: Konfigurera teckensnitt för rendering av kalkylblad
type: docs
weight: 10
url: /sv/net/configuring-fonts-for-rendering-spreadsheets/
---
## **Möjliga användningsscenarier**

Aspose.Cells API:er ger möjlighet att rendera kalkylbladen i bildformat samt konvertera dem till PDF- och XPS-format. För att maximera omvandlingstroheten är det nödvändigt att teckensnitten som används i kalkylarket är tillgängliga i operativsystemets standardtypsnittskatalog. Om de nödvändiga typsnitten inte finns kommer API:erna Aspose.Cells att försöka ersätta de nödvändiga typsnitten med de tillgängliga.

## **Val av teckensnitt**

Nedan är processen som Aspose.Cells API:er följer bakom scenen.

1. API:n försöker hitta typsnitten i filsystemet som matchar det exakta teckensnittsnamnet som används i kalkylarket.
1.  Om API inte kan hitta typsnitten med exakt samma namn, försöker det använda standardteckensnittet som anges under arbetsbokens**[DefaultStyle.Font](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font)** fast egendom.
1.  Om API inte kan hitta typsnittet som definierats under arbetsbokens**[DefaultStyle.Font](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font)** egenskapen försöker den använda typsnittet som anges under**[PdfSaveOptions.DefaultFont](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/defaultfont)** eller**[ImageOrPrintOptions.DefaultFont](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/defaultfont)** fast egendom.
1. Om API inte kan hitta teckensnittet som definieras under**[PdfSaveOptions.DefaultFont](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/defaultfont)** eller**[ImageOrPrintOptions.DefaultFont](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/defaultfont)** egenskapen försöker den använda typsnittet som anges under**[FontConfigs.DefaultFontName](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/properties/defaultfontname)** fast egendom.
1. Om API inte kan hitta teckensnittet som definieras under**[FontConfigs.DefaultFontName](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/properties/defaultfontname)** egenskapen försöker den välja de mest lämpliga typsnitten från alla tillgängliga typsnitt.
1. Slutligen, om API inte kan hitta några teckensnitt i filsystemet, renderar det kalkylarket med Arial.

## **Ställ in anpassade teckensnittsmappar**

 Aspose.Cells API:er söker i operativsystemets standardtypsnittskatalog efter de nödvändiga teckensnitten. Om de nödvändiga typsnitten inte är tillgängliga i systemets teckensnittskatalog så söker API:erna igenom de anpassade (användardefinierade) katalogerna. De**[FontConfigs](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs)**class har avslöjat ett antal sätt att ställa in anpassade teckensnittskataloger som beskrivs nedan.

1. **[FontConfigs.SetFontFolder](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/setfontfolder)**: Den här metoden är användbar om det bara finns en mapp att ställa in.
1. **[FontConfigs.SetFontFolders](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/setfontfolders)**: Den här metoden är användbar när teckensnitten finns i flera mappar och användaren vill ställa in alla mappar separat istället för att kombinera alla teckensnitt i en enda mapp.
1. **[FontConfigs.SetFontSources](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/setfontsources)**: Den här mekanismen är användbar när användaren vill ladda teckensnitt från flera mappar eller en enda teckensnittsfil eller teckensnittsdata från en uppsättning byte.

{{% alert color="primary" %}}

 Både**[FontConfigs.SetFontFolder](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/setfontfolder)** & **[FontConfigs.SetFontFolders](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/setfontfolders)** metoder accepterar en andra parameter av boolesk typ. Godkänd**Sann** eftersom den andra parametern kommer att styra API:erna Aspose.Cells att söka i undermapparna efter teckensnittsfilerna.

{{% /alert %}}

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-SetCustomFontFolders-1.cs" >}}

{{% alert color="primary" %}}

Använd någon av de ovan nämnda metoderna i början av ansökan, det vill säga; innan du anropar några andra objekt i Aspose.Cells API:er.

{{% /alert %}} {{% alert color="primary" %}}

Om alla ovan nämnda metoder används för att ställa in teckensnittskällorna, kommer endast de senaste inställningarna att träda i kraft.

{{% /alert %}}

## **Teckensnittsersättningsmekanism**

 Aspose.Cells API:er ger också möjlighet att ange ersättningsteckensnittet för renderingsändamål. Denna mekanism är användbar när ett önskat teckensnitt inte är tillgängligt på maskinen där konvertering måste ske. Användare kan tillhandahålla en lista med teckensnittsnamn som ett alternativ till det ursprungligen önskade teckensnittet. För att uppnå detta har API:erna Aspose.Cells avslöjat**[FontConfigs.SetFontSubstitutes](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/setfontsubstitutes)** metod som accepterar 2 parametrar. Den första parametern är av typ**sträng** , vilket ska vara namnet på teckensnittet som måste ersättas. Den andra parametern är en array av typ**sträng**Användare kan tillhandahålla en lista med teckensnittsnamn som en ersättning till det ursprungliga teckensnittsnamnet (anges i den första parametern).

Här är ett enkelt användningsscenario.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-SetCustomFontFolders-FontSubstitution.cs" >}}

## **Informationsmöte**

Utöver de ovan nämnda metoderna har API:erna Aspose.Cells också tillhandahållit sätt att samla information om vilka källor och ersättningar som har ställts in.

1. **[FontConfigs.GetFontSources](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/getfontsources)** metod returnerar en array av typ**[FontSourceBase](https://reference.aspose.com/cells/net/aspose.cells/fontsourcebase)** som innehåller listan över angivna teckensnittskällor. Om inga källor har angetts,**[FontConfigs.GetFontSources](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/getfontsources)**metod returnerar en tom array.
1. **[FontConfigs.GetFontSubstitutes](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/getfontsubstitutes)** metod accepterar en parameter av typen**sträng** gör det möjligt att ange teckensnittsnamnet för vilket ersättning har ställts in. Om det inte har ställts in någon ersättning för det angivna teckensnittsnamnet sedan**[FontConfigs.GetFontSubstitutes](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/getfontsubstitutes)**metod returnerar null.

## **Förhandsämnen**
- [Ställ in standardteckensnitt när du renderar kalkylblad till bilder](/cells/sv/net/set-default-font-while-rendering-spreadsheet-to-images/)
- [Ställ in egenskapen DefaultFont för PdfSaveOptions och ImageOrPrintOptions att ha prioritet](/cells/sv/net/set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority/)
- [Typsnittsformat som stöds](/cells/sv/net/supported-font-formats/)
- [Arbetsblad till bild - Ställ in pixelformat för den renderade bilden](/cells/sv/net/worksheet-to-image-set-pixel-format-for-the-rendered-image/)
