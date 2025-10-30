---
title: Importazione intelligente di dati Master e Dettagli in Excel con Smart Markers
type: docs
weight: 30
url: /it/net/how-to-use-master-and-details-with-smart-markers/
---

## **Possibili Scenari di Utilizzo**
A volte, si desidera generare report Excel dinamici, che includono una dashboard principale completa e più fogli di lavoro dettagliati di livello fine. Tra questi, una singola tabella principale presenta una panoramica, che può mostrare varie varianti di prodotto, e ciascun foglio dettagliato corrispondente fornisce dati specifici e approfonditi per una singola variante. Aspose.Cells può soddisfare perfettamente le tue esigenze attraverso master e dettagli con smart markers.


## **Parametri Smart Marker per Master e Dettagli**
Per importare dati master e dettagli in Excel, è necessario utilizzare i seguenti parametri smart marker:

| Parametro | Descrizione | Valori accettabili (Sintassi) | Restrizioni | Opzionale | Comportamento predefinito | Vincoli di Excel |
| --- | --- | --- | --- | --- | --- | --- |
| `DetailSheet` | Specifica il nome del foglio di lavoro dei dettagli memorizzato nel file modello. | Valore stringa | Il valore deve essere nullo o il nome del foglio di lavoro. Se nullo, si tratta di un foglio di dettaglio. Deve essere un valore stringa semplice. La variabile non è supportata. | Se omesso, non è un foglio principale o di dettaglio. | Foglio di lavoro normale, non principale o di dettaglio. | |
| `DetailTable` | Specifica il nome della tabella del foglio di lavoro dei dettagli nel file modello. | Valore stringa | | Se omesso, lo smart marker nel foglio dei dettagli dovrebbe essere simile a quello del foglio principale, altrimenti non riusciamo a trovare la fonte dati. | Se omesso, lo smart marker nel foglio dei dettagli dovrebbe essere simile a quello del foglio principale, altrimenti non riusciamo a trovare la fonte dati. | |
| `DetailSheetNewName` | Specifica il nome del nuovo foglio di lavoro dei dettagli creato. | Espressione simile a formula Excel | Deve essere una formula valida per Excel se sostituiamo la variabile ({a.bc}) con un valore semplice. | Se omesso, i nuovi fogli saranno Sheet1, Sheet2... | Se omesso, i nuovi fogli saranno Sheet1, Sheet2... | Il nome deve essere un nome valido di foglio di lavoro. |
| `DetailLink` | Indica se aggiungere collegamenti ipertestuali alla posizione dei dati importati. | | | Se omesso, non aggiungere collegamenti ipertestuali alla posizione dei dati importati. | Se omesso, non aggiungere collegamenti ipertestuali alla posizione dei dati importati. | |

## **Come usare Master e Dettagli quando Master e Dettagli sono in un'unica sezione di lavoro**
A volte, è necessario importare dati master e dettagli in Excel in SmartMarkers. Aspose.Cells rende possibile utilizzare i parametri master e dettagli nei SmartMarkers. Si prega di verificare [file modello](MasterDetailInOneSheet.xlsx), [file JSON](MasterDetailData.json) e lo screenshot del file excel di output generato con il seguente codice.

|**Il primo foglio del modello.xlsx.**|
| :- |
|![todo:image_alt_text](1.png)|

|**Il primo foglio del file excel di output.**|
| :- |
|![todo:image_alt_text](2.png)|

|**Il secondo foglio del file excel di output.**|
| :- |
|![todo:image_alt_text](3.png)|

Dati json come segue:
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
L'esempio seguente mostra come funziona.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "SmartMarkers-Using-Master-Details-InOneSheet.cs" >}}

## **Come usare Master e Dettagli quando Master e Dettagli sono su diversi fogli di lavoro**
A volte, è necessario importare dati master e dettagli in Excel in SmartMarkers. Aspose.Cells rende possibile utilizzare i parametri master e dettagli nei SmartMarkers. Si prega di verificare [file modello](MasterDetailInTwoSheets.xlsx), [file JSON](MasterDetailData.json) e lo screenshot del file excel di output generato con il seguente codice.

|**Il primo foglio di lavoro principale del template.xlsx.**|
| :- |
|![todo:image_alt_text](4.png)|

|**Il secondo foglio di lavoro principale del template.xlsx.**|
| :- |
|![todo:image_alt_text](5.png)|

|**Il foglio di lavoro dei dettagli di template.xlsx.**|
| :- |
|![todo:image_alt_text](6.png)|

|**Il primo foglio di lavoro principale del file excel di output.**|
| :- |
|![todo:image_alt_text](7.png)|

|**Il secondo foglio di lavoro principale del file excel di output.**|
| :- |
|![todo:image_alt_text](8.png)|

|**Il foglio di lavoro dei dettagli del primo foglio di lavoro principale nel file excel di output.**|
| :- |
|![todo:image_alt_text](9.png)|

|**Il primo foglio di dettagli del secondo foglio di lavoro principale nel file excel di output.**|
| :- |
|![todo:image_alt_text](10.png)|

|**Il secondo foglio di dettagli del secondo foglio di lavoro principale nel file excel di output.**|
| :- |
|![todo:image_alt_text](11.png)|

Dati json come segue:
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
L'esempio seguente mostra come funziona.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "SmartMarkers-Using-Master-Details-InDifferentSheets.cs" >}}
