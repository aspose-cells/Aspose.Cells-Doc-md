---
title: Intelligentes Importieren von Master und Detaildaten in Excel mit Smart Markern
type: docs
weight: 30
url: /de/net/how-to-use-master-and-details-with-smart-markers/
---

## **Mögliche Verwendungsszenarien**
Manchmal möchten Sie dynamische Excel-Berichte erstellen, die ein umfassendes Hauptdashboard und mehrere fein granular aufgegliederte Arbeitsblätter enthalten. Darunter präsentiert eine einzelne Haupttabelle eine Übersicht, die verschiedene Produktvarianten zeigen kann, während jedes entsprechende Detail-Arbeitsblatt spezifische und tiefgehende Daten für eine einzelne Variante bietet. Aspose.Cells kann Ihre Anforderungen perfekt erfüllen durch Master- und Detaildaten mit Smart Markern.


## **Smart Marker-Parameter für Master- und Detaildaten**
Um Master- und Detaildaten in Excel zu importieren, verwenden Sie die folgenden Smart Marker-Parameter:

| Parameter | Beschreibung | Akzeptierte Werte (Syntax) | Einschränkungen | Optional | Standardverhalten | Excel-Beschränkungen |
| --- | --- | --- | --- | --- | --- | --- |
| `DetailSheet` | Legen Sie den Namen des Detail-Arbeitsblatts in der Vorlagendatei fest. | Stringwert | Der Wert muss null sein oder den Namen des Arbeitsblatts haben. Wenn null, ist es ein Detailblatt. Es sollte ein einfacher String-Wert sein. Variablen werden nicht unterstützt. | Wenn ausgelassen, kein Master- oder Detailblatt. | Normales Arbeitsblatt, kein Master- oder Detailblatt. | |
| `DetailTable` | Legen Sie den Tabellennamen des Detail-Arbeitsblatts in der Vorlagendatei fest. | Stringwert | | Wenn ausgelassen, sollte der Smart Marker im Detailblatt dem des Masterblatts ähnlich sein, sonst können wir die Datenquelle nicht finden. | Wenn ausgelassen, sollte der Smart Marker im Detailblatt dem des Masterblatts ähnlich sein, sonst können wir die Datenquelle nicht finden. | |
| `DetailSheetNewName` | Legen Sie den Namen des neu erstellten Detail-Arbeitsblatts fest. | Excel-Formel-ähnliche Expression | Es sollte eine gültige Formel für Excel sein, wenn wir Variable ({a.bc}) durch einen einfachen Wert ersetzen. | Wenn ausgelassen, werden die neuen Blätter Sheet1, Sheet2... heißen | Wenn ausgelassen, werden die neuen Blätter Sheet1, Sheet2... heißen | Der Name muss ein gültiger Name eines Arbeitsblatts sein. |
| `DetailLink` | Zeigt an, ob Hyperlinks zum Standort der importierten Daten hinzugefügt werden sollen. | | |Wenn ausgelassen, keine Hyperlinks zum Standort der importierten Daten hinzufügen. | Wenn ausgelassen, keine Hyperlinks zum Standort der importierten Daten hinzufügen. | |

## **So verwenden Sie Master und Details, wenn Master- und Detaildaten in einem Arbeitsblatt sind**
Manchmal müssen Sie Master- und Detaildaten in SmartMarkers in Excel importieren. Aspose.Cells macht es möglich, Master- und Detailparameter in SmartMarkers zu verwenden. Bitte prüfen Sie die [Vorlagendatei](MasterDetailInOneSheet.xlsx), [JSON-Datei](MasterDetailData.json) und den Screenshot der erzeugten Ausgabedatei in Excel mit folgendem Code.

|**Das erste Arbeitsblatt der template.xlsx.**|
| :- |
|![todo:image_alt_text](1.png)|

|**Das erste Arbeitsblatt der Ausgabedatei in Excel.**|
| :- |
|![todo:image_alt_text](2.png)|

|**Das zweite Arbeitsblatt der Ausgabedatei in Excel.**|
| :- |
|![todo:image_alt_text](3.png)|

Die JSON-Daten sind wie folgt:
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
Das folgende Beispiel zeigt, wie dies funktioniert.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "SmartMarkers-Using-Master-Details-InOneSheet.cs" >}}

## **So verwenden Sie Master und Details, wenn Master und Details in verschiedenen Arbeitsblättern sind**
Manchmal müssen Sie Master- und Detaildaten in SmartMarkers in Excel importieren. Aspose.Cells ermöglicht die Verwendung von Master- und Detailparametern in SmartMarkers. Bitte prüfen Sie [Vorlagendatei](MasterDetailInTwoSheets.xlsx), [JSON-Datei](MasterDetailData.json) und den Screenshot der erzeugten Excel-Ausgabe mit folgendem Code.

|**Das erste Master-Arbeitsblatt der Vorlage.xlsx.**|
| :- |
|![todo:image_alt_text](4.png)|

|**Das zweite Master-Arbeitsblatt der Vorlage.xlsx.**|
| :- |
|![todo:image_alt_text](5.png)|

|**Das Detail-Arbeitsblatt der Vorlage.xlsx.**|
| :- |
|![todo:image_alt_text](6.png)|

|**Das erste Master-Arbeitsblatt der Ausgabedatei.**|
| :- |
|![todo:image_alt_text](7.png)|

|**Das zweite Master-Arbeitsblatt der Ausgabedatei.**|
| :- |
|![todo:image_alt_text](8.png)|

|**Das Detail-Arbeitsblatt des ersten Master-Arbeitsblatts in der Ausgabedatei.**|
| :- |
|![todo:image_alt_text](9.png)|

|**Das erste Detail-Arbeitsblatt des zweiten Master-Arbeitsblatts in der Ausgabedatei.**|
| :- |
|![todo:image_alt_text](10.png)|

|**Das zweite Detail-Arbeitsblatt des zweiten Master-Arbeitsblatts in der Ausgabedatei.**|
| :- |
|![todo:image_alt_text](11.png)|

Die JSON-Daten sind wie folgt:
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
Das folgende Beispiel zeigt, wie dies funktioniert.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "SmartMarkers-Using-Master-Details-InDifferentSheets.cs" >}}
