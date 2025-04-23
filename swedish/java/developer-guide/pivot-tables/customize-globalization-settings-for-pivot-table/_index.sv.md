---
title: Anpassa globaliseringsinställningarna för Pivot tabell
type: docs
weight: 20
url: /sv/java/customize-globalization-settings-for-pivot-table/
---

## **Möjliga användningsscenario**

Ibland vill du anpassa * Pivot Total, Sub Total, Grand Total, All Items, Multiple Items, Column Labels, Row Labels, Blank Values * -text enligt dina krav. Aspose.Cells tillåter dig att anpassa globaliseringsinställningarna för pivottabellen för att hantera sådana scenarier. Du kan också använda den här funktionen för att ändra etiketterna till andra språk som arabiska, hindi, polska, etc.

## **Anpassa globaliseringsinställningarna för Pivot-tabell**

Följande kodexempel förklarar hur du anpassar globaliseringsinställningar för pivot-tabell. Den skapar en klass *CustomPivotTableGlobalizationSettings* härledd från en bas klass [**GlobalizationSettings**](https://reference.aspose.com/cells/java/com.aspose.cells/GlobalizationSettings) och upphäver alla nödvändiga metoder. Dessa metoder returnerar den anpassade texten för *Pivot Total, Sub Total, Grand Total, All Items, Multiple Items, Column Labels, Row Labels, Blank Values*. Sedan tilldelar den objektet av denna klass till [**WorkbookSettings.GlobalizationSettings**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#GlobalizationSettings) egenskapen. Koden laddar [källa excel-filen](40468491.xlsx) som innehåller pivot-tabellen, uppdaterar och beräknar dess data och sparar den som [utdata PDF-fil](40468490.pdf). Följande skärmdump visar effekten av kodexemplet på utdata-PDF:en. Som du kan se på skärmdumpen har olika delar av pivot-tabellen nu en anpassad text som returneras av de upphävda metoderna från [**GlobalizationSettings**](https://reference.aspose.com/cells/java/com.aspose.cells/GlobalizationSettings)-klassen.

![todo:image_alt_text](customize-globalization-settings-for-pivot-table_1.png)

## **Exempelkod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-PivotTables-CustomizeGlobalizationSettingsforPivotTable-1.java" >}}
{{< app/cells/assistant language="java" >}}
