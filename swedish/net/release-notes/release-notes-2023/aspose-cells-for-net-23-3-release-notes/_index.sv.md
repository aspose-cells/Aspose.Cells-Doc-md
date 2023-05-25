---
title: Aspose.Cells for .NET 23.3 Release Notes
type: docs
weight: 10
url: /sv/net/aspose-cells-for-net-23-3-release-notes/
---
{{% alert color="primary" %}}

 Den här sidan innehåller release notes för[Aspose.Cells for .NET 23.3](https://www.nuget.org/packages/Aspose.Cells/23.3.0).

{{% /alert %}}

|**Nyckel**|**Sammanfattning**|**Kategori**|
| :- | :- | :- |
|CELLSNET-52857|Stöd för att ställa in/läsa/spara ENCODEURL-funktion|
|CELLSNET-52921|Stöd för att ställa in/läsa/spara LET-funktion|
|CELLSNET-52605|Stödberoende av System.Drawing.Common från 6.0.0 för net6 och net7|
|CELLSNET-52840|Uppdatera beräknad kolumnformel vid kopiering|
|CELLSNET-52742|Textskuggeffekt försvinner när du sparar fil till pdf|
|CELLSNET-52802|Teckensnittsfärgen för smart art ska vara svart|
|CELLSNET-52634| SUBTOTAL och andra aggregerade funktioner fungerar inte korrekt i en dynamisk matrisformel|
|CELLSNET-52752|Felaktigt värde returneras vid beräkning av SWITCH-sats Array Formula|
|CELLSNET-52771|Problem med att beräkna matrisformler med externa länkar med INDIREKTA funktioner|
|CELLSNET-52858| Formelfel vid konvertering av xlsx till xls|
|CELLSNET-52770|Saknade axelticketiketter vid konvertering av diagram till bild i NetCore-projekt|
|CELLSNET-52888|Att exportera bild från diagram är inte samma sak som visas i Excel|
|CELLSNET-52565| Github demo: datakälla bindningsexempel fungerar inte|
|CELLSNET-52861|Att ställa in redigerbart område påverkar inte i GridWeb|
|CELLSNET-52890|Github-demo: GridWebs SessionModes fungerar inte|
|CELLSNET-44789|Felaktiga marginaler för konverteringar av xlsx till pdf|
|CELLSNET-52340|Textrutan är inte synlig när du konverterar xlsx till pdf|
|CELLSNET-52759|Sammanfogat område saknar kant när du sparar fil till pdf|
|CELLSNET-52801|Zorder respekterades inte när du sparade PDF om objektet täcker mer än en sida|
|CELLSNET-52897|XLS till PDF: Bilden i diagram EMF har inte renderats|
|CELLSNET-49337|HTML till XLSX: Vissa stilar visas inte korrekt|
|CELLSNET-52019| Excel till HTML konvertering - vissa datakolumner flyttas och formateringen är trasig|
|CELLSNET-52501|Att kopiera intervall från källa till målarbetsbok kopierar inte data/objekt korrekt|
|CELLSNET-52730|PNG bilder inuti celler konverteras inte till utdata PDF|
|CELLSNET-52736|Innehåll förlorat efter att Excel-filen har sparats på nytt|
|CELLSNET-52749|Att använda resize-metoden resulterar i en skadad utdatafil|
|CELLSNET-52788|Bredden på kopierade kommentarer är fel|
|CELLSNET-52792|Filkorruption efter att ha angett bildtyp när excel sparas till bild|
|CELLSNET-52822|Inställningarna för kommentarmarginalen ändras från Automatisk till Fast|
|CELLSNET-52824|Startpositionen, teckensnittet och teckenavståndet för textrutans teckensträng ändras|
|CELLSNET-52834|Den kopierade tabellen är skadad vid kopiering av intervall från ett annat ark.|
|CELLSNET-52839|Xls-filen är skadad om diagramtiteln är en konstant formel|
|CELLSNET-52871| Utöka tabeller och flytta andra tabeller under den|
|CELLSNET-52873|XLSB till HTML: Tabellformat behålls inte vid konvertering|
|CELLSNET-52896|Ett undantag bör göras när du flyttar delen av bordet.|
|CELLSNET-52917|Resultatfilen kraschar när Range ovanför Tabell infogas|
|CELLSNET-52922|Enhetstyp för Y-axeln ska vara synlig när diagrammet omvandlas till pdf.|
|CELLSNET-52901| Diagramtitel saknas för trädkarta|
|CELLSNET-52741|Form till bild Fel när filen sparades till pdf efter kopiering av arbetsbok|
|CELLSNET-52828|Null referens undantag vid kopiering av ett intervall|
|CELLSNET-52829|Undantag görs vid rendering av ODS filförhandsgranskning med valfritt OnePagePerSheet|
|CELLSNET-52830|Undantag för att spara och få förhandsgranskning|

##  **Offentlig API och bakåtinkompatibla ändringar**

Följande är en lista över alla ändringar som gjorts för allmänheten API, såsom tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts till Aspose.Cells for .NET. Om du har frågor om någon ändring som anges, vänligen ta upp den på supportforumet Aspose.Cells.

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

