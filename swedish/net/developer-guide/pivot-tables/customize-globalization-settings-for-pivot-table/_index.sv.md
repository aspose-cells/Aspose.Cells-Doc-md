---
title: Anpassa globaliseringsinställningar för pivottabell
type: docs
weight: 50
url: /sv/net/customize-globalization-settings-for-pivot-table/
---
## **Möjliga användningsscenarier**

 Ibland vill du anpassa*Pivotsumma, Undersumma, Totalsumma, Alla artiklar, Flera artiklar, Kolumnetiketter, Radetiketter, Tomma värden*text enligt dina önskemål. Aspose.Cells låter dig anpassa globaliseringsinställningarna för pivottabellen för att hantera sådana scenarier. Du kan också använda den här funktionen för att ändra etiketterna till andra språk som arabiska, hindi, polska, etc.

## **Anpassa globaliseringsinställningar för pivottabell**

 Följande exempelkod förklarar hur du anpassar globaliseringsinställningarna för pivottabellen. Det skapar en klass*CustomPivotTableGlobalizationSettings* härledd från en basklass[**Globaliseringsinställningar**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings) och åsidosätter alla nödvändiga metoder. Dessa metoder returnerar den anpassade texten för*Pivotsumma, Undersumma, Totalsumma, Alla artiklar, Flera artiklar, Kolumnetiketter, Radetiketter, Tomma värden*. Sedan tilldelar den objektet för denna klass till[**WorkbookSettings.GlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/globalizationsettings) fast egendom. Koden laddar[källkod excel-fil](40468488.xlsx) som innehåller pivottabellen, uppdaterar och beräknar dess data och sparar den som[mata ut PDF](40468487.pdf)fil. Följande skärmdump visar effekten av exempelkoden på den utgående PDF-filen. Som du kan se på skärmdumpen har olika delar av pivottabellen nu en anpassad text som returneras av de åsidosatta metoderna för[**Globaliseringsinställningar**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings)klass.

![todo:image_alt_text](customize-globalization-settings-for-pivot-table_1.png)

## **Exempelkod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-CustomizePivotTableGlobalSettings-CustomizePivotTableGlobalSettings.cs" >}}
