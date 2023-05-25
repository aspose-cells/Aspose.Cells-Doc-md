---
title: Aspose.Cells for Node.js via Java 23.3 Release Notes
type: docs
weight: 10
url: /sv/nodejs-java/aspose-cells-for-node-js-via-java-23-3-release-notes/
---
{{% alert color="primary" %}}

 Den här sidan innehåller release notes för[Aspose.Cells for Node.js via Java 23.3](https://downloads.aspose.com/cells/nodejs/new-releases/aspose.cells-for-node.js-via-java-23.3/).

{{% /alert %}}

|**Nyckel**|**Sammanfattning**|**Kategori**|
| :- | :- | :- |
|CELLSJAVA-45149|Ändra logiken för att generera ett "gruppobjekt" från smartart-objektet|
|CELLSJAVA-45172|Stöd loadoption för GridWeb|
|CELLSJAVA-45173| Stöd marginaler för img-taggen när du laddar html|
|CELLSJAVA-45110|Konverterad bild är inte samma som MS Excel.|
|CELLSJAVA-45190|Beräknade fältvärden hämtas inte av funktionen getCalculatedValue() .|
|CELLSJAVA-45056|Diagram till bild - tecken och förklaringshöjd renderade inte korrekt|
|CELLSJAVA-45089|Konverterad PDF visar diagrametiketter på olika platser och felaktiga axelpunkter|
|CELLSJAVA-45141| Dataetiketter saknas i diagrammet i kopierad arbetsbok i v23|
|CELLSJAVA-45178|När du konverterar xlsx till html kommer programmet att fråga om att startcellen i diagramobjektet har ogiltigt '}'-innehåll|
|CELLSJAVA-45195|Serielinje saknas i ett punktdiagram|
|CELLSJAVA-45054|Kan inte byta kalkylblad för den angivna filen från kunden|
|CELLSJAVA-45143|CSV-filen är inte samma som WPS-fil|
|CELLSJAVA-45072|Den konverterade PDF till Aspose.Cells från MS Excel-filen kunde inte läsas normalt med iText|
|CELLSJAVA-45200|Visar "#" för siffror i den konverterade PDF|
|CELLSJAVA-45159|Texten är inte mittjusterad vid rendering till png-bild|
|CELLSJAVA-41794|HTML är fel när vissa rader är dolda|
|CELLSJAVA-45189|Välj pivotdatafält för en pivottabell att tillämpa format på|
|CELLSJAVA-45197|Formateringsproblem i HTML till Excel-konvertering|
|CELLSJAVA-45051| Lösenordet fungerar inte när du öppnar LibreOffice Calc-fil (ODS)|
|CELLSJAVA-44070|Undantag "Ogiltigt slutradindex" i renderingen CSV till PDF|
|CELLSJAVA-45107|Ett undantag IllegalArgumentException genereras vid export av filer till html|

##  **Offentlig API och bakåtinkompatibla ändringar**

Följande är en lista över alla ändringar som gjorts för allmänheten API, såsom tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts till Aspose.Cells for Java. Om du har frågor om någon ändring som anges, vänligen ta upp den på supportforumet Aspose.Cells.

###  **Lägger till egenskapen CalculationOptions.LinkedDataSources**

Tillåter användaren att ställa in länkade datakällor för externa länkar som används i formeln för beräkning.

###  **Föråldrad SvgSaveOptions-klass**

Använd klassen ImageSaveOptions istället.

###  **Föråldrade SvgSaveOptions()-konstruktorn**

Använd ImageSaveOptions(SaveFormat.Svg) istället och ställ in ImageSaveOptions.ImageOrPrintOptions.OnePagePerSheet till true.

###  **Föråldrade SvgSaveOptions.SheetIndex-egenskapen**

Använd ImageSaveOptions.ImageOrPrintOptions.SheetSet istället.

###  **Lägger till StyleModifyFlag.FontVerticalText enum**

Anger om texten är vertikaljusterad.

###  **Lägger till WarningType.InvalidOperator enum**

Representerar den ogiltiga varningsoperatören vid drift av Excel-filer.

###  **Stöder inställning av Row.GroupLevel och Column.GroupLevel egenskaper**

Stöder inställning av gruppnivå för rader och kolumner.

###  **Föråldrar HtmlLoadOptions.ConvertFormulasData och lägger till HtmlLoadOptions.HasFormula-egenskaper**

Använd HtmlLoadOptions.HasFormula istället.

###  **Föråldrar PivotGlobalizationSettings.GetTextOfProtection() och lägger till PivotGlobalizationSettings.GetTextOfProtectedName(String)-metoder**

Använd PivotGlobalizationSettings.GetTextOfProtectedName(String) istället.

###  **Lägger till metoden Chart.IsReferedByChart(Int32,Int32).**

Indikerar om denna cell refereras av diagrammet.

###  **Lägger till egenskapen PasteOptions.IgnoreLinksToOriginalFile**

Länka inte till originalfilen när du kopierar intervall.

###  **Lägger till PivotArea,PivotTableSelectionType och PivotTable.Format(Pivot.PivotArea,Style)**

Välj området och formatera det i pivottabellen.

###  **Lägger till egenskapen SheetSet.Active**

Får en uppsättning med aktivt ark av arbetsboken.
