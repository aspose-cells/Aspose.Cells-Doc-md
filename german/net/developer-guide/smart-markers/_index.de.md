---
title: Intelligentes Importieren und Platzieren von Daten mit Intelligenten Markern
linktitle: Intelligente Marker
type: docs
weight: 190
url: /de/net/using-smart-markers/
description: Intelligentes Importieren und Platzieren von Daten gemäß den Vorlagen Excel Dateien mit der Aspose.Cells Bibliothek.
---

## **Warum Daten mit Smart Markers in Excel importieren**
Durch die Verwendung von Smart Markers zum Importieren von Daten in Excel wird die Datenintegration durch die Kombination eines templatebasierten Designs mit dynamischer Datenbindung vereinfacht. Dieser Ansatz ist besonders wertvoll in Tools wie Aspose.Cells, bei denen Marker als Platzhalter in Templates dienen, um Daten aus verschiedenen Quellen automatisch zu füllen. Hier sind die wichtigsten Gründe für die Anwendung dieser Methode:

1. Effizienz bei wiederholtem Berichtswesen: Wiederverwendbarkeit von Templates, vorgefertigte Excel-Templates mit eingebetteten Markern (z.B. &=$VariableName, &=DataSource.Feld) können für mehrere Datensätze wiederverwendet werden, wodurch manuelles Neugestalten entfällt. Zum Beispiel müssen Finanzberichte oder Inventarlisten nur noch mit neuen Daten aktualisiert werden, nicht aber mit neuen Layouts. Automatisierte Datenbindung, Smart Markers sind direkt mit Datenquellen verbunden (z.B. Datenbanken, JavaBeans, Arrays). Änderungen an den Quelldaten spiegeln sich nach der Verarbeitung automatisch in der Ausgabedatei wider, was Copy-Paste-Fehler reduziert.

2. Unterstützung komplexer Datenstrukturen: Mehrquellen-Integration, Eine Vorlage kann Daten aus unterschiedlichen Quellen zusammenführen (z.B. Variablen, Arrays, ResultSets). Hierarchische Datenverwaltung, Verschachtelte Daten (z.B. gruppierte Datensätze) können mit Markern wie &=subtotal9:Person.id verarbeitet werden, um Zusammenfassungen (Summen, Durchschnitte) pro Gruppe direkt in Excel zu generieren.

3. Erhaltung der Excel-Funktionalität: Smart Markers arbeiten neben Funktionen wie Formeln, bedingter Formatierung und Diagrammen. Zum Beispiel: Dynamische Berechnungen mit &==C{r}*D{r} werden während der Dateninjektion auf Zeilenebene angewandt. Vorlagen behalten vordefinierte Stile (z.B. Kopfzeilen, Zellfarben) bei, wodurch Konsistenz auch nach dem Import gewährleistet ist.

4. Erweiterte Automatisierungsfähigkeiten: Anpassbare Datenquellenintegration, Entwickler können Schnittstellen wie ICellsDataTable (in .NET) implementieren, um proprietäre Datenstrukturen an Marker anzupassen. Diese Flexibilität ermöglicht Echtzeit-Daten von APIs oder Sensoren. Batch-Verarbeitung, Tools wie Aspose.Cells’ WorkbookDesigner erlauben Massenoperationen (z.B. mehr als 1.000 Rechnungen in einem Durchlauf erstellen), indem sie durch Datensätze iterieren.

5. Reduzierter Entwicklungs- und Wartungsaufwand: Trennung von Logik und Design, Designer verwalten Templates in Excel (ohne Programmierung), während Entwickler die Datenlogik übernehmen. Diese Trennung beschleunigt Iterationen. Fehlerreduktion, Automatisierte Datenzuordnung minimiert manuelle Eingabefehler. Zum Beispiel können Sensordaten, die in VC++ analysiert wurden, automatisch in Excel-Templates durch Objekt-Interfaces ausgefüllt werden, um Transkriptionsfehler zu vermeiden.

## **Beispielcode zum Importieren eines DataTable mit Smart Markers**
Der folgende Beispielcode verfügt über eine Datenquelle mit 6 Datensätzen. Wir möchten nur 3 Datensätze in einem Arbeitsblatt anzeigen, die restlichen Datensätze werden automatisch auf das zweite Arbeitsblatt verschoben. Bitte beachten Sie, dass das zweite Arbeitsblatt ebenfalls das gleiche Smart Marker-Tag haben sollte und Sie die Methode [WorkbookDesigner.Process(sheetIndex, isPreserved)](https://reference.aspose.com/cells/net/aspose.cells.workbookdesigner/process/methods/2) für beide Blätter aufrufen müssen. Sehen Sie sich die [Ausgabedatei Excel](SmartMarkerDataTableToExcel.xlsx) an, die vom Code generiert wurde, um eine Referenz zu erhalten.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "SmartMarkers-ImportDataTableToExcel.cs" >}}

## **Beispielcode zum Importieren von JSON-Daten mit Smart Markern**
Aspose.Cells for .NET unterstützt JSON-Daten in Smart Markern. Der Beispielcode lädt eine Tabellenvorlage, importiert intelligente JSON-Daten zur Befüllung und berechnet dann die Tabellendaten. Bitte prüfen Sie [Vorlagendatei](table.xlsx), [JSON-Datei](table.json) und den Screenshot der Ausgabedatei im Excel-Format, die mit folgendem Code generiert wurde.

|**Das erste Arbeitsblatt der Datei table.xlsx zeigt Smart Marker.**|
| :- |
|![todo:image_alt_text](tabletemplate.png)|

|**Screenshot der Ausgabedatei im Excel-Format.**|
| :- |
|![todo:image_alt_text](tableresult.png)|

Die JSON-Daten sind wie folgt:
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
Das folgende Beispiel zeigt, wie dies funktioniert.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "SmartMarkers-ImportJsonToTable.cs" >}}

## **Beispielcode zum Importieren verschachtelter Objekte mit Smart Markern**
Aspose.Cells unterstützt verschachtelte Objekte in Smart Markern, die verschachtelten Objekte sollten einfach sein. Wir verwenden eine einfache Vorlagendatei. Sehen Sie die Designer-Tabelle, die einige verschachtelte Smart Marker enthält.

|**Die erste Arbeitsmappe der SM_NestedObjects.xlsx Datei zeigt verschachtelte Smart Marker.**|
| :- |
|![todo:image_alt_text](using-smart-markers_7.png)|
Das folgende Beispiel zeigt, wie dies funktioniert.


{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-UsingNestedObjects-1.cs" >}}


## **Erweiterte Themen**
- [Smart Marker Parameter](/cells/de/net/smart-marker-parameters/)
- [Anonymes oder benutzerdefiniertes Objekt zu SmartMarkern hinzufügen](/cells/de/net/adding-anonymous-or-custom-object-into-smartmarkers/)
- [Automatisches Ausfüllen von Smart Marker-Daten in anderen Arbeitsblättern, wenn die Daten zu groß sind](/cells/de/net/auto-populate-smart-marker-data-to-other-worksheets-if-data-is-too-large/)
- [Formatierung von Smart Markers](/cells/de/net/formatting-smart-markers/)
- [Benachrichtigungen beim Zusammenführen von Daten mit Smart Markern erhalten](/cells/de/net/getting-notifications-while-merging-data-with-smart-markers/)
- [Benutzerdefinierte Datenquelle für WorkbookDesigner festlegen](/cells/de/net/set-custom-datasource-for-workbookdesigner/)
- [Führende Apostrophzeichen in Zellen anzeigen](/cells/de/net/show-leading-apostrophe-in-cells/)
- [Verwenden des Formelparameters im Smart Marker-Feld](/cells/de/net/using-formula-parameter-in-smart-marker-field/)
- [Intelligentes Importieren von Array-Elementen nach Index in Excel mit Smart Markern](/cells/de/net/how-to-import-array-element-by-index-with-smart-markers/)
- [Intelligentes Importieren von Array-Elementen via Slicer in Excel mit Smart Markern](/cells/de/net/how-to-import-array-element-by-slicer-with-smart-markers/)
- [Intelligentes Importieren von JSON in Excel mit Smart Markern](/cells/de/net/how-to-import-json-into-excel-with-smart-markers/)
- [Intelligentes Importieren verschachtelter Objekte nach Excel mit Smart Markern](/cells/de/net/how-to-import-nested-objects-with-smart-markers/)
- [Intelligentes Importieren variabler Arrays nach Excel mit Smart Markern](/cells/de/net/how-to-import-variable-arrays-with-smart-markers/)
- [So verwenden Sie Bildmarkierungen in Smart Markern](/cells/de/net/how-to-use-image-markers-in-smart-markers/)
- [Wie man Daten in Smart Markern gruppiert](/cells/de/net/how-to-group-data-in-smart-markers/)

{{< app/cells/assistant language="csharp" >}}
