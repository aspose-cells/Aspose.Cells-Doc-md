---
title: Konfigurera teckensnitt för rendering av kalkylblad
type: docs
weight: 10
url: /sv/java/configuring-fonts-for-rendering-spreadsheets/
---

## **Möjliga användningsscenario**

Aspose.Cells API: er tillhandahåller möjlighet att rendera kalkylbladen i bildformat samt konvertera dem till PDF- och XPS-format. För att maximera konversionsfideliteten är det nödvändigt att teckensnitten som används i kalkylbladet bör finnas i operativsystemets standardteckensnittkatalog. Om de nödvändiga teckensnitten inte är närvarande kommer Aspose.Cells API: er att försöka ersätta de nödvändiga teckensnitten med de som finns tillgängliga.

## **Val av teckensnitt**

Nedan är processen som Aspose.Cells API: er följer bakom scenen.

1. API försöker hitta teckensnitten på filsystemet som matchar det exakta teckensnittsnamnet som används i kalkylbladet.
1. Om API inte kan hitta teckensnitten med det exakta namnet försöker det använda standardteckensnittet som anges under arbetsbokens [**DefaultStyle.Font**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Font) egenskap.
1. Om API inte kan hitta teckensnittet som definieras under arbetsbokens [**DefaultStyle.Font**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Font) egenskap försöker det använda teckensnittet som anges under [**PdfSaveOptions.DefaultFont**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveoptions#DefaultFont) eller [**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions#DefaultFont) egenskap.
1. Om API inte kan hitta teckensnittet som definieras under [**PdfSaveOptions.DefaultFont**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveoptions#DefaultFont) eller [**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions#DefaultFont) egenskap försöker den använda teckensnittet som anges under [**FontConfigs.DefaultFontName**](https://reference.aspose.com/cells/java/com.aspose.cells/FontConfigs#DefaultFontName) egenskap.
1. Om API inte kan hitta teckensnittet som definieras under [**FontConfigs.DefaultFontName**](https://reference.aspose.com/cells/java/com.aspose.cells/FontConfigs#DefaultFontName) egenskapen försöker det välja de mest lämpliga teckensnitten från alla tillgängliga teckensnitt.
1. Slutligen, om API inte hittar några teckensnitt på filsystemet, renderar den kalkylbladet med Arial.

{{% alert color="primary" %}}

Generellt skannar Aspose.Cells API:erna standardfontkatalogerna för operativsystemet på Windows, Linux, MacOS som standard. Från och med [Aspose.Cells for Java 24.7](https://releases.aspose.com/cells/java/release-notes/2024/aspose-cells-for-java-24-7-release-notes/) skannar API:erna dessutom Office-cacheade molnfontkataloger som standard.

{{% /alert %}}

{{% alert color="primary" %}}

Aspose.Cells API:erna skannar alltid operativsystemets standardfontkatalog med ett undantag; när JVM-argumenten **-DAspose.Cells.FontDirExc="DinFontKatalog"** är inställda. I så fall hoppar Aspose.Cells API:erna över att skanna systemets standardfontkatalog och söker endast i den angivna sökvägen.

{{% /alert %}}

## **Ange anpassade typsnittsmappar**

Aspose.Cells API:er söker efter de nödvändiga typsnitten i operativsystemets standardtypsnittsmapp. Om de nödvändiga typsnitten inte finns i systemets typsnittsmapp, söker API:erna genom de användardefinierade (anpassade) mapparna. [**FontConfigs**](https://reference.aspose.com/cells/java/com.aspose.cells/FontConfigs) klassen har specificerat ett flertal sätt att ange anpassade typsnittsmappar enligt följande detaljerat.

1. [**FontConfigs.setFontFolder**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#setFontFolder-java.lang.String-boolean-): Metoden är användbar om det endast finns en mapp att ange.
1. [**FontConfigs.setFontFolders**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#setFontFolders-java.lang.String[]-boolean-): Metoden är användbar när typsnitten finns i flera mappar och användaren vill ange alla mapparna separat istället för att kombinera alla typsnitt i en enda mapp.
1. [**FontConfigs.setFontSources**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#setFontSources-com.aspose.cells.FontSourceBase[]-): Mekanismen är användbar när användaren vill ladda typsnitt från flera mappar eller en enda typsnittsfil eller typsnittsdata från en byte-array.

{{% alert color="primary" %}}

Både [**FontConfigs.setFontFolder**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#setFontFolder-java.lang.String-boolean-) och [**FontConfigs.setFontFolders**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#setFontFolders-java.lang.String[]-boolean-) metoder accepterar en parameter av typen boolean. Om sann (true) anges som andra parameter kommer Aspose.Cells API:erna att söka efter undermappar efter typsnittsfiler.

{{% /alert %}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SetCustomFontFolders-SetCustomFontFolders.java" >}}

{{% alert color="primary" %}}

Var god använd någon av de ovan nämnda metoderna i starten av programmet, dvs innan några objekt från Aspose.Cells API:erna anropas.

{{% /alert %}} {{% alert color="primary" %}}

Om fler än en av de ovan nämnda metoderna används för att ange typsnittskällor kommer endast de senaste inställningarna att ha effekt.

{{% /alert %}}

## **Mekanism för typsnittsutbyte**

Aspose.Cells API:erna ger också möjlighet att ange ersättningstypsnitt för presentationssyfte. Detta mekanism är användbar när ett nödvändigt typsnitt inte är tillgängligt på den maskin där konvertering ska ske. Användare kan ange en lista med typsnittsnamn som alternativ till det ursprungliga typsnittet. Aspose.Cells API:erna har exponerat metoden FontConfigs.setFontSubstitutes som accepterar två parametrar. Den första parametern är av typen String och ska vara namnet på det typsnitt som ska ersättas. Den andra parametern är en array av typen String. Användare kan ange en lista med typsnittsnamn som ersättningar för det ursprungliga typsnittet (specificerat i den första parametern).

Här är ett enkelt användningsscenario.

{{< highlight java >}}

 //Substituting the Arial font with Times New Roman & Calibri

FontConfigs.setFontSubstitutes("Arial", new String[] { "Times New Roman", "Calibri" });

{{< /highlight >}}

## **Informationssamling**

Förutom de ovan nämnda metoderna har Aspose.Cells API:erna även medel för att samla information om vilka källor och ersättningar som har angetts.

1. [**FontConfigs.getFontSources**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#getFontSources--): Denna metod returnerar en array av typen [**FontSourceBase**](https://reference.aspose.com/cells/java/com.aspose.cells/FileFontSource) innehållande listan över specificerade typsnittskällor. Om ingen källa har angetts returnerar metoden [**FontConfigs.getFontSources**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#getFontSources--) en tom array.
1. [**FontConfigs.getFontSubstitutes**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#getFontSubstitutes-java.lang.String-): Denna metod accepterar en parameter av typen String som låter användaren ange typsnittsnamnet för vilket ersättning har angetts. Om ingen ersättning har angetts för det angivna typsnittsnamnet returnerar metoden [**FontConfigs.getFontSubstitutes**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#getFontSubstitutes-java.lang.String-) null.
{{< app/cells/assistant language="java" >}}
