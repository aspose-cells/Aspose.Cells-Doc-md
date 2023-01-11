﻿---
title: Aspose.Cells for .NET 22.11 Release Notes
type: docs
weight: 2
url: /sv/net/aspose-cells-for-net-22-11-release-notes/
---
{{% alert color="primary" %}}

 Den här sidan innehåller release notes för[Aspose.Cells for .NET 22.11](https://www.nuget.org/packages/Aspose.Cells/22.11.0).

{{% /alert %}}

|**Nyckel**|**Sammanfattning**|**Kategori**|
|:- |:- |:- |
|CELLSNET-52026|Stöd kopiering tidslinje|
|CELLSNET-52022|Skilj eller särskilj mellan CSE äldre matrisformel och normal matrisformel|
|CELLSNET-52156|Inaktivera sammanslagna tabellceller när du sparar XLSX till HTML|
|CELLSNET-52159|Stöd för att analysera kollapsad egendom vid konvertering av html till excel|
|CELLSNET-51939|XLSX till PDF: Innehållsfeljustering|
|CELLSNET-51940|XLS till PDF: Innehållsfeljustering i celler|
|CELLSNET-52068|XLSX till PDF: Former saknas/layout kollapsar|
|CELLSNET-52092|Teckenutskrift och mellanrum i figurerna i Excel skärs bort|
|CELLSNET-52186|Former/lådor är tomma vid konvertering av XLSX dokument till PDF|
|CELLSNET-52225|XLSX till PDF Tecken i textrutor omvända|
|CELLSNET-52086|Externa anslutningar skadade i den genererade filen|
|CELLSNET-52133|Excel-formler lindas med lockiga hängslen i den återsparade xlsb-filen|
|CELLSNET-52158|Felaktig cirkulär referensdetektering|
|CELLSNET-52174|Cell.IsArrayFormula är falskt för matrisformel efter att ha lästs från xlsb-mallfil|
|CELLSNET-52217|Uppslagsfunktioner beräknades felaktigt för vissa stora tal|
|CELLSNET-52221|Dynamisk matrisformel har inte spelats ut korrekt för XLOOKUP|
|CELLSNET-52232|Enstaka citattecken tas bort från den externa länkens arknamn|
|CELLSNET-52198|Överlappande problem vid konvertering av diagram som bildfiler|
|CELLSNET-52043|Problem vid beräkning av "PageSetup.Zoom" med HorizontalPageBreaks|
|CELLSNET-52157|Sidkanten överlappar text vid konvertering till pdf|
|CELLSNET-52118|Inkonsekvent resultat i olika format när html är inställt på cell i OpenOffice och LibreCalc|
|CELLSNET-52125|Index var utanför intervallet för range.copy med bild|
|CELLSNET-52143| Relationstypen för länken ändras när en XLS-fil konverteras till XLSM|
|CELLSNET-52144|XLS till XLSM konvertering ändrar länkrelationstyp|
|CELLSNET-52151|Att spara xlsb ersatte alla kommentarer med senaste kommentaren|
|CELLSNET-52152|Radhöjdsvärdet är felaktigt när AutoFit-radfunktionen tillämpas via Aspose.Cells|
|CELLSNET-52155|Villkorlig formatering förloras efter intervallkopiering|
|CELLSNET-52181|XLSX till HTML: Cells-intervallet har inte exporterats korrekt|
|CELLSNET-52214|Innehållet på sista raden trunkeras i den utgående Excel-filen|
|CELLSNET-52236| Smart markör (grupp:sammanfoga) fungerar inte för sammanslagna celler|
|CELLSNET-52241|Rutor (former) i dokumentet visas inte i utdata PDF|
|CELLSNET-52243|Ändring av VBA-projekt ger ett felmeddelande när arbetsboken sparas|

## **Offentlig API och bakåtinkompatibla ändringar**

Följande är en lista över alla ändringar som gjorts för allmänheten API, såsom tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts till Aspose.Cells for .NET. Om du har frågor om någon ändring som anges, vänligen ta upp den på supportforumet Aspose.Cells.

### **Lägger till egenskapen Cell.IsDynamicArrayFormula**

Anger om cellens formel är dynamisk matrisformel (sant) eller äldre matrisformel (falsk).

### **Föråldrade egendomen SparklineGroup.SparklineCollection och lägger till egendomen SparklineGroup.Sparklines**

Använd egenskapen SparklineGroup.Sparklines istället.

### **Föråldrade egendomen Worksheet.SparklineGroupCollection och lägger till egenskapen Worksheet.SparklineGroups**

Använd egenskapen Worksheet.SparklineGroups istället.