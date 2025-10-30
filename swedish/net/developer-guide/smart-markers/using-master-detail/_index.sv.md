---
title: Smart import av master och detalldata till Excel med smartmarkörer
type: docs
weight: 30
url: /sv/net/how-to-use-master-and-details-with-smart-markers/
---

## **Möjliga användningsscenario**
Ibland vill du generera dynamiska Excel-rapporter, inklusive en omfattande huvuddashboard och flera finmaskiga detaljerade kalkylblad. Bland dem visar en huvudtabell en översikt, som kan visa olika produktvarianter, och varje tillhörande detaljblad ger specifika och djupgående data för en enskild variant. Aspose.Cells kan perfekt möta dina behov genom master- och detaljdata med smartmarkörer.


## **Smart Marker-parametrar för master och detaljer**
För att importera master- och detalldata till Excel behöver du använda följande smartmarkörparametrar:

| Parameter | Beskrivning | Godtagbara värden(syntax) | Begränsningar | Valfrihet | Standardbeteende | Excel-begränsningar |
| --- | --- | --- | --- | --- | --- | --- |
| `DetailSheet` | Ange namnet på detaljbladet som lagras i mallfilen. | Strängvärde | Värdet måste vara null eller bladets namn. Om null är detta ett detaljblad. Det bör vara ett enkelt strängvärde. Variabel stöds inte. | Om utelämnat, inte master- eller detaljblad. | Normalt blad, inte master- eller detaljblad. | |
| `DetailTable` | Ange tabellnamnet för detaljbladet i mallfilen. | Strängvärde | | Om utelämnat, bör smartmarkören i detaljbladet vara liknande som i huvudbladet, annars hittar vi inte datakällan. | Om utelämnat, bör smartmarkören i detaljbladet vara liknande som i huvudbladet, annars hittar vi inte datakällan. | |
| `DetailSheetNewName` | Ange namnet på det nyss skapade detaljbladet. | Excel-formel som liknar Expression | Det bör vara en giltig formel för Excel om vi ersätter variabeln ({a.bc}) med ett enkelt värde. | Om utelämnat, blir nya blad Sheet1, Sheet2... | Om utelämnat, blir nya blad Sheet1, Sheet2... | Namnet måste vara ett giltigt bladnamn. |
| `DetailLink` | Indikera om hyperlänkar ska läggas till till platsen för den importerade data. | | |Om utelämnat, lägg inte till hyperlänkar till platsen för den importerade data. | Om utelämnat, lägg inte till hyperlänkar till platsen för den importerade data. | |

## **Hur man använder master och detaljer när master och detaljer finns i ett blad**
Ibland behöver du importera master- och detalldata till Excel i SmartMarkers. Aspose.Cells gör det möjligt att använda master- och detaljparametrar i SmartMarkers. Vänligen kontrollera [mallfil](MasterDetailInOneSheet.xlsx), [json-fil](MasterDetailData.json) och skärmbilden av den utskrivna Excel-filen genererad med följande kod.

|**Det första arket i mall.xlsx.**|
| :- |
|![todo:image_alt_text](1.png)|

|**Det första arket i den utskrivna Excel-filen.**|
| :- |
|![todo:image_alt_text](2.png)|

|**Det andra arket i den utskrivna Excel-filen.**|
| :- |
|![todo:image_alt_text](3.png)|

Json-data enligt följande:
```json data
{
	"node": {
		"Styles1": [
			{
				"StyleID": "1style001",
				"StyleName": "StyleName1",
				"Quantity": 6,
				"UnitPrice": 18.45,
				"MaterialType":"Cotton"
			}
		],
		"Styles2": [
			{
				"StyleID": "2style001",
				"StyleName": "Cotton StyleName2",
				"Quantity": 6,
				"UnitPrice": 18.45,
				"MaterialType":"Cotton"
			},
			{
				"StyleID": "2style002",
				"StyleName": "Denim StyleName2",
				"Quantity": 8,
				"UnitPrice": 58.8,
				"MaterialType":"Denim"
			}
		]
	}
}
```
Exemplet nedan visar hur detta fungerar.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "SmartMarkers-Using-Master-Details-InOneSheet.cs" >}}

## **Hur man använder master och detaljer när master och detaljer finns i olika blad**
Ibland behöver du importera master- och detalldata till Excel i SmartMarkers. Aspose.Cells gör det möjligt att använda master- och detaljparametrar i SmartMarkers. Vänligen kontrollera [mallfil](MasterDetailInTwoSheets.xlsx), [json-fil](MasterDetailData.json) och skärmbilden av den utskrivna Excel-filen genererad med följande kod.

|**Den första huvudbladet i mall.xlsx.**|
| :- |
|![todo:image_alt_text](4.png)|

|**Det andra huvudbladet i mall.xlsx.**|
| :- |
|![todo:image_alt_text](5.png)|

|**Detaljbladet i mall.xlsx.**|
| :- |
|![todo:image_alt_text](6.png)|

|**Det första huvudbladet i utdata Excel-filen.**|
| :- |
|![todo:image_alt_text](7.png)|

|**Det andra huvudbladet i utdata Excel-filen.**|
| :- |
|![todo:image_alt_text](8.png)|

|**Detaljbladet för det första huvudbladet i utdata Excel-filen.**|
| :- |
|![todo:image_alt_text](9.png)|

|**Det första detaljbladet för det andra huvudbladet i utdata Excel-filen.**|
| :- |
|![todo:image_alt_text](10.png)|

|**Det andra detaljbladet för det andra huvudbladet i utdata Excel-filen.**|
| :- |
|![todo:image_alt_text](11.png)|

Json-data enligt följande:
```json data
{
	"node": {
		"Styles1": [
			{
				"StyleID": "1style001",
				"StyleName": "StyleName1",
				"Quantity": 6,
				"UnitPrice": 18.45,
				"MaterialType":"Cotton"
			}
		],
		"Styles2": [
			{
				"StyleID": "2style001",
				"StyleName": "Cotton StyleName2",
				"Quantity": 6,
				"UnitPrice": 18.45,
				"MaterialType":"Cotton"
			},
			{
				"StyleID": "2style002",
				"StyleName": "Denim StyleName2",
				"Quantity": 8,
				"UnitPrice": 58.8,
				"MaterialType":"Denim"
			}
		]
	}
}
```
Exemplet nedan visar hur detta fungerar.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "SmartMarkers-Using-Master-Details-InDifferentSheets.cs" >}}
