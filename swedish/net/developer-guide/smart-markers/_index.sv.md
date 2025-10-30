---
title: Smart import och placering av data med Smart Markers
linktitle: Smarta markörer
type: docs
weight: 190
url: /sv/net/using-smart-markers/
description: Smartt importera och placera data enligt mallexcelfiler med Aspose.Cells biblioteket.
---

## **Varför importera data till Excel med Smart Markers**
Med Smart Markers för import av data till Excel förenklas dataintegration genom att kombinera mallbaserad design med dynamisk data-bindning. Denna metod är särskilt värdefull i verktyg som Aspose.Cells, där markörer fungerar som platshållare i mallar för att automatiskt fylla på data från olika källor. Nedan följer huvudskälen för att anta denna metod:

1. Effektivitet vid repetitiv rapportering: Upprepad användning av mallar, fördesignade Excel-mallar med inbäddade markörer (t.ex., &=$VariabelNamn, &=Datakälla.Fält) kan återanvändas för flera datamängder, vilket eliminerar manuella omarbetningar. Till exempel kräver finansiella rapporter eller lagerblad endast uppdatering av datakällan, inte ombyggnad av layouten. Automatiserad datainbindning, Smart Markers länkar direkt till datakällor (t.ex., databaser, JavaBeans, arrayer). Ändringar i källan reflekteras automatiskt i utdatafils Excel efter bearbetning, vilket minskar fel vid kopiera och klistra in.

2. Stöd för komplexa datastrukturer: Flera datakällor, En enda mall kan sammanfoga data från olika källor (t.ex., variabler, arrayer, ResultSets). Hierarkisk databehandling, Nestade data (t.ex., grupperade poster) kan behandlas med markörer som &=subtotal9:Person.id för att generera sammanfattningar (summeringar, genomsnitt) per grupp direkt i Excel.

3. Bevarande av Excelfunktionalitet: Smart Markers samexisterar med Excelfunktioner som formler, villkorsstyrd formatering och diagram. Till exempel: Dynamiska beräkningar med &==C{r}*D{r} tillämpar rad-specifika formler under datainjiceringsprocessen. Mallar behåller fördefinierade stilar (t.ex., rubriker, cellfärger), vilket säkerställer konsekvens utan efterimportjusteringar.

4. Avancerade automatiseringsmöjligheter: Anpassad datakällaintegration, Utvecklare kan implementera gränssnitt som ICellsDataTable (i .NET) för att mappa proprietära datastrukturer till markörer. Denna flexibilitet stödjer realtidsdata från API:er eller sensorer. Batchbearbetning, Verktyg som Aspose.Cells’ WorkbookDesigner möjliggör massoperationer (t.ex., generera 1000+ fakturor i ett kör) genom loopning genom datamängder.

5. Minskat utvecklings- och underhållsarbete: Separation av logik och design, Designer hanterar mallar i Excel (utan kodning), medan utvecklare sköter datalogiken. Denna indelning snabbar på iterationer. Felreducering, Automatisk datamappning minimerar risker för manuell datainmatning. Till exempel kan sensorvärden analyseras i VC++ och fyllas automatiskt i Excel-mallar via objektgränssnitt, vilket undviker transkriptionsfel.

## **Exempel på kod för att importera DataTable med Smart Markers**
Följande exempel har en datakälla med 6 poster. Vi vill visa endast 3 poster i ett kalkylblad, sedan flyttas resten automatiskt till det andra kalkylbladet. Observera att det andra kalkylbladet också ska ha samma smarta markörtag och du måste kalla [WorkbookDesigner.Process(sheetIndex, isPreserved)](https://reference.aspose.com/cells/net/aspose.cells.workbookdesigner/process/methods/2) metod för båda bladen. Se gärna [utdata Excel-fil](SmartMarkerDataTableToExcel.xlsx) som genereras av koden som referens.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "SmartMarkers-ImportDataTableToExcel.cs" >}}

## **Exempelkod för att importera JSON-data med Smart Markers**
Aspose.Cells for .NET stöder JSON-data i smarta markörer. Exempelkoden laddar en mall för tabell, importerar intelligent JSON-data för ifyllning, och beräknar sedan tabellens data. Vänligen kontrollera [mallfil](table.xlsx), [json-fil](table.json) och skärmbilden av den genererade excelfilen med följande kod.

|**Det första arbetsbladet i filen table.xlsx som visar smarta markörer.**|
| :- |
|![todo:image_alt_text](tabletemplate.png)|

|**Skärmbild av utdata Excel-fil.**|
| :- |
|![todo:image_alt_text](tableresult.png)|

Json-data enligt följande:
```json data
{
	"Items" : [
		{
			"ItemName" : "A123",
			"Description" : "Peonies",
			"Qty" : "55",
			"UnitPrice" : "3.05"			
		},
		{
			"ItemName" : "B456",
			"Description" : "Tulips",
			"Qty" : "45",
			"UnitPrice" : "2.66",
		},
		{
			"ItemName" : "K789",
			"Description" : "Buttercup",
			"Qty" : "68",
			"UnitPrice" : "8.35",
		}
	]
}
```
Exemplet nedan visar hur detta fungerar.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "SmartMarkers-ImportJsonToTable.cs" >}}

## **Exempelkod för att importera inbäddade objekt med Smart Markers**
Aspose.Cells stödjer inbäddade objekt i smarta markörer, de inbäddade objekten bör vara enkla. Vi använder en enkel mallfil. Se den designer-kalkylblad som innehåller några inbäddade smarta markörer.

|**Det första kalkylbladet i filen SM_NestedObjects.xlsx som visar inbäddade smarta markörer.**|
| :- |
|![todo:image_alt_text](using-smart-markers_7.png)|
Exemplet nedan visar hur detta fungerar.


{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-UsingNestedObjects-1.cs" >}}


## **Fortsatta ämnen**
- [Smart Marker-parametrar](/cells/sv/net/smart-marker-parameters/)
- [Lägg till anonymt eller anpassat objekt i SmartMarkers](/cells/sv/net/adding-anonymous-or-custom-object-into-smartmarkers/)
- [Automatiskt fylla i Smart Marker-data till andra kalkylblad om datan är för stor](/cells/sv/net/auto-populate-smart-marker-data-to-other-worksheets-if-data-is-too-large/)
- [Formatering av Smart Markers](/cells/sv/net/formatting-smart-markers/)
- [Få meddelanden när data sammanfogas med smarta markörer](/cells/sv/net/getting-notifications-while-merging-data-with-smart-markers/)
- [Ange anpassad datakälla för WorkbookDesigner](/cells/sv/net/set-custom-datasource-for-workbookdesigner/)
- [Visa ledande apostrofer i celler](/cells/sv/net/show-leading-apostrophe-in-cells/)
- [Använda Formelparameter i Smart Marker-fält](/cells/sv/net/using-formula-parameter-in-smart-marker-field/)
- [Smart import av arrayelement efter index till Excel med Smart Markers](/cells/sv/net/how-to-import-array-element-by-index-with-smart-markers/)
- [Smart import av arrayelement via slicer till Excel med Smart Markers](/cells/sv/net/how-to-import-array-element-by-slicer-with-smart-markers/)
- [Smart import av JSON till Excel med Smart Markers](/cells/sv/net/how-to-import-json-into-excel-with-smart-markers/)
- [Smart import av inbäddade objekt till Excel med Smart Markers](/cells/sv/net/how-to-import-nested-objects-with-smart-markers/)
- [Smart import av variablaarrayer till Excel med Smart Markers](/cells/sv/net/how-to-import-variable-arrays-with-smart-markers/)
- [Hur man använder bildmarkörer i Smart Markers](/cells/sv/net/how-to-use-image-markers-in-smart-markers/)
- [Hur man grupperar data i Smart Markers](/cells/sv/net/how-to-group-data-in-smart-markers/)

{{< app/cells/assistant language="csharp" >}}
