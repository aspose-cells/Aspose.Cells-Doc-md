---
title: Anpassa globaliseringsinställningarna för Pivot tabell
type: docs
weight: 50
url: /sv/net/customize-globalization-settings-for-pivot-table/
---

## **Möjliga användningsscenario**

Ibland vill du anpassa * Pivot Total, Sub Total, Grand Total, All Items, Multiple Items, Column Labels, Row Labels, Blank Values * -text enligt dina krav. Aspose.Cells tillåter dig att anpassa globaliseringsinställningarna för pivottabellen för att hantera sådana scenarier. Du kan också använda den här funktionen för att ändra etiketterna till andra språk som arabiska, hindi, polska, etc.

## **Anpassa globaliseringsinställningarna för Pivot-tabell**

Följande kodexempel förklarar hur du anpassar globaliseringsinställningarna för pivottabellen. Det skapar en klass * CustomPivotTableGlobalizationSettings * härledd från en grundklass [**PivotGlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells.settings/pivotglobalizationsettings/) och åsidosätter alla dess nödvändiga metoder. Dessa metoder returnerar den anpassade texten för * Pivot Total, Sub Total, Grand Total, All Items, Multiple Items, Column Labels, Row Labels, Blank Values *. Sedan tilldelar den objektet för denna klass till [**WorkbookSettings.GlobalizationSettings.PivotSettings**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/pivotsettings/) egendom. Koden laddar den [källa excel-filen](40468488.xlsx) som innehåller pivottabellen, uppdaterar och beräknar dess data och sparar den som [utmatnings-PD](40468487.pdf) fil. Följande skärmdump visar effekten av kodexemplet på utmatnings-PD:n. Som du kan se i skärmdumpen har olika delar av pivottabellen nu en anpassad text som returneras av de åsidosatta metoderna från [**PivotGlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells.settings/pivotglobalizationsettings/) klassen.

![todo:image_alt_text](customize-globalization-settings-for-pivot-table_1.png)

## **Exempelkod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-CustomizePivotTableGlobalSettings-CustomizePivotTableGlobalSettings.cs" >}}
