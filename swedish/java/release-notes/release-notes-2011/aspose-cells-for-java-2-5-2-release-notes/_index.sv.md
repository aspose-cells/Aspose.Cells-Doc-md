---
title: Aspose.Cells för Java 2.5.2 Release Notes
type: docs
weight: 70
url: /sv/java/aspose-cells-for-java-2-5-2-release-notes/
---
{{% alert color="primary" %}} 

 Den här sidan innehåller release notes för[Aspose.Cells för Java 2.5.2](https://downloads.aspose.com/cells/java/new-releases/aspose.cells-for-java-2.5.2/)

{{% /alert %}} 

 Vi är glada att kunna meddela Aspose.Cells för Java 2.5.2!

 Vad har ändrats:

- Stöder att läsa pivottabeller från mallfilerna.
 Lägger till LineShape i Excel 2007 XLSX-filer.
 Ger stöd för att ställa in serienamn när du ställer in diagrammets datakälla.
 Stöder för att få/ställa in Gridliness synlighet för olika arbetsblad i ODS-filer.
 Förbättring görs för att läsa Shapes från XLSX-filer.
 Förbättringar görs för funktionerna diagram-till-bild, ark-till-bild och Excel-till-PDF.
 Förbättring görs för att analysera formler.
 Förbättring är gjord för kopiering Cells.
31 korrigeringar och förbättringar.

 Problem lösta i Aspose.Cells för Java 2.5.2.





 Anmärkningsvärda förändringar för användarna:



 I gamla versioner användes FormatCondition.getStyle() för att få FormatConditions att behålla sitt eget Style-objekt. Ändring av det returnerade Style-objektet för getStyle() senare skulle ändra FormatConditions stil direkt.

Från den här versionen kommer FormatCondition att använda mer konkret stilklass DXFStyle (en underklass av Style, genom vilken vi kan tillhandahålla mer flexibla funktioner som ska stödjas i framtiden). Till exempel, nu kommer FormatCondition.getStyle() att returnera en kopia av DXFStyle-objektet istället för Style-objektet. Och vi rekommenderar användarna att använda DXFStyle-objektet för metoden FormatCondition.setStye(Style). Alla Style-objekt som är inställda på FormatCondition kommer att konverteras till DXFStyle och samlas till en global pool för arbetsboken. Således kommer FormatCondition endast att upprätthålla en DXFStyle-referens. Ändring av det returnerade DXFStyle-objektet för getStyle() senare kommer inte att ändra FormatConditions stil. För att ändringen ska träda i kraft måste användare anropa setStyle() för FormatCondition efter att stilen har ändrats.
