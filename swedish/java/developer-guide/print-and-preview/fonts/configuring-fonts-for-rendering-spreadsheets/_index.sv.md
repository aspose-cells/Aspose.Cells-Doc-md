---
title: Konfigurera teckensnitt för rendering av kalkylblad
type: docs
weight: 10
url: /sv/java/configuring-fonts-for-rendering-spreadsheets/
---
## **Möjliga användningsscenarier**

Aspose.Cells API:er ger möjlighet att rendera kalkylbladen i bildformat samt konvertera dem till PDF- och XPS-format. För att maximera omvandlingstroheten är det nödvändigt att teckensnitten som används i kalkylarket är tillgängliga i operativsystemets standardtypsnittskatalog. Om de nödvändiga typsnitten inte finns kommer API:erna Aspose.Cells att försöka ersätta de nödvändiga typsnitten med de tillgängliga.

## **Val av teckensnitt**

Nedan är processen som Aspose.Cells API:er följer bakom scenen.

1. API försöker hitta teckensnitten i filsystemet som matchar det exakta teckensnittsnamnet som används i kalkylarket.
1.  Om API inte kan hitta typsnitten med exakt samma namn, försöker den använda standardteckensnittet som anges under arbetsbokens[**DefaultStyle.Font**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Font) fast egendom.
1.  Om API inte kan hitta teckensnittet som definierats under arbetsbokens[**DefaultStyle.Font**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Font) egenskapen försöker den använda typsnittet som anges under[**PdfSaveOptions.DefaultFont**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveoptions#DefaultFont) eller[**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions#DefaultFont) fast egendom.
1.  Om API inte kan hitta teckensnittet som definieras under[**PdfSaveOptions.DefaultFont**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveoptions#DefaultFont) eller[**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions#DefaultFont) egenskapen försöker den använda typsnittet som anges under[**FontConfigs.DefaultFontName**](https://reference.aspose.com/cells/java/com.aspose.cells/FontConfigs#DefaultFontName) fast egendom.
1.  Om API inte kan hitta teckensnittet som definieras under[**FontConfigs.DefaultFontName**](https://reference.aspose.com/cells/java/com.aspose.cells/FontConfigs#DefaultFontName) egenskapen försöker den välja de mest lämpliga typsnitten från alla tillgängliga typsnitt.
1. Slutligen, om API inte kan hitta några teckensnitt i filsystemet, renderar den kalkylarket med Arial.

{{% alert color="primary" %}}

 Aspose.Cells API:erna skannar alltid operativsystemets standardfontkatalog med ett undantag, det vill säga; när JVM argumenterar**-DAspose.Cells.FontDirExc="YourFontDir"** är inställda. I så fall kommer API:erna Aspose.Cells att hoppa över att skanna operativsystemets standardteckensnittskatalog och endast söka efter sökvägen som specificeras i de tidigare nämnda JVM-argumenten.

{{% /alert %}}

## **Ställ in anpassade teckensnittsmappar**

 Aspose.Cells API:er söker i operativsystemets standardtypsnittskatalog efter de nödvändiga teckensnitten. Om de nödvändiga typsnitten inte är tillgängliga i systemets teckensnittskatalog så söker API:erna igenom de anpassade (användardefinierade) katalogerna. De[**FontConfigs**](https://reference.aspose.com/cells/java/com.aspose.cells/FontConfigs)class har avslöjat ett antal sätt att ställa in anpassade teckensnittskataloger som beskrivs nedan.

1. [**FontConfigs.setFontFolder**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#setFontFolder(java.lang.String,%20boolean)): Denna metod är användbar om det bara finns en mapp att ställa in.
1. [**FontConfigs.setFontFolders**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#setFontFolders(java.lang.String[],%20boolean)): Denna metod är användbar när teckensnitten finns i flera mappar och användaren vill ställa in alla mappar separat istället för att kombinera alla teckensnitt i en enda mapp.
1. [**FontConfigs.setFontSources**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#setFontSources(com.aspose.cells.FontSourceBase[])): Denna mekanism är användbar när användaren vill ladda typsnitt från flera mappar eller en enskild typsnittsfil eller teckensnittsdata från en uppsättning byte.

{{% alert color="primary" %}}

 Både[**FontConfigs.setFontFolder**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#setFontFolder(java.lang.String,%20boolean)) & [**FontConfigs.setFontFolders**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#setFontFolders(java.lang.String[],%20boolean) ) metoder accepterar en andra parameter av boolesk typ. Godkänd**Sann**som andra parameter styr Aspose.Cells API:erna att söka i undermapparna efter teckensnittsfilerna.

{{% /alert %}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SetCustomFontFolders-SetCustomFontFolders.java" >}}

{{% alert color="primary" %}}

Använd någon av de ovan nämnda metoderna i början av ansökan, det vill säga; innan du anropar några andra objekt i Aspose.Cells API:er.

{{% /alert %}} {{% alert color="primary" %}}

Om mer än en av de ovan nämnda metoderna används för att ställa in teckensnittskällorna kommer endast de senaste inställningarna att träda i kraft.

{{% /alert %}}

## **Teckensnittsersättningsmekanism**

Aspose.Cells API:er ger också möjlighet att ange ersättningsteckensnittet för renderingsändamål. Denna mekanism är användbar när ett önskat teckensnitt inte är tillgängligt på maskinen där konvertering måste ske. Användare kan tillhandahålla en lista med teckensnittsnamn som ett alternativ till det ursprungligen önskade teckensnittet. För att uppnå detta har API:erna Aspose.Cells avslöjat metoden FontConfigs.setFontSubstitutes som accepterar 2 parametrar. Den första parametern är av typ**Sträng** , vilket ska vara namnet på teckensnittet som måste ersättas. Den andra parametern är en array av typ**Sträng**. Användare kan tillhandahålla en lista med teckensnittsnamn som ersättning för det ursprungliga teckensnittet (anges i den första parametern).

Här är ett enkelt användningsscenario.

{{< highlight "java" >}}

 //Substituting the Arial font with Times New Roman & Calibri

FontConfigs.setFontSubstitutes("Arial", new String[]{ "Times New Roman", "Calibri" });

{{< /highlight >}}

## **Informationsmöte**

Utöver de ovan nämnda metoderna har API:erna Aspose.Cells också tillhandahållit sätt att samla information om vilka källor och ersättningar som har ställts in.

1. [**FontConfigs.getFontSources**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#getFontSources() ): Denna metod returnerar en array av typ[**FontSourceBase**](https://reference.aspose.com/cells/java/com.aspose.cells/FileFontSource)som innehåller listan över specificerade teckensnittskällor. Om inga källor har angetts,[**FontConfigs.getFontSources**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#getFontSources()) returnerar en tom array.
1. [**FontConfigs.getFontSubstitutes**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#getFontSubstitutes(java.lang.String) ): Denna metod accepterar en parameter av typen**Sträng** gör det möjligt att ange teckensnittsnamnet för vilket ersättning har ställts in. Om det inte har ställts in någon ersättning för det angivna teckensnittsnamnet sedan[**FontConfigs.getFontSubstitutes**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#getFontSubstitutes(java.lang.String))-metoden returnerar null.
