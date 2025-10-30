---
title: Wie man Range Parameter in SmartMarkers verwendet
type: docs
weight: 10
url: /de/net/how-to-use-range-parameter-in-smart-markers/
---

## **Warum der Einsatz des Range-Parameters in Smart Markern sinnvoll ist**
Der Range-Parameter in SmartMarkers wird verwendet, um genau zu steuern, wo und wie Daten in einer Excel-Vorlage platziert werden, wenn sie mit Daten aus einer Quelle (z.B. JSON, Datenbanken) gefüllt wird. Er hilft bei der Verwaltung dynamischer Datenausgaben, insbesondere bei variablen Array-Längen oder komplexen Gruppierungen.

1. Steuerung der Datenplatzierung und Vermeidung von Überschneidungen: Wenn Datenquellen dynamische Arrays enthalten (z.B. unterschiedliche Anzahl von Elementen pro Datensatz), sorgt der Range-Parameter dafür, dass Daten in einem definierten Excel-Bereich ausgefüllt werden, um Überlauf in benachbarte Zellen oder Abschnitte zu verhindern.

2. Umgang mit dynamischen Array-Formeln: Für Operationen wie das Transponieren dynamischer Arrays (z.B. &=TRANSPOSE(DataArray)) sorgt der Range-Parameter dafür, dass die Ausgabe sich an die tatsächliche Datenmenge anpasst, ohne Residualwerte (z.B. Nullen in leeren Feldern) aus vorherigen Operationen zu hinterlassen.

3. Unterstützung von Gruppierungen und hierarchischen Daten: Wenn Daten gruppiert werden sollen (z.B. verschachtelte JSON-Strukturen), hilft der Range-Parameter, hierarchische Ausgabebereiche zu definieren. Zum Beispiel, um Datensätze unter einer Elterngruppe zu gruppieren, ohne manuelle Zeilenanpassungen. Ohne einen definierten Bereich kann SmartMarkers möglicherweise verschachtelte Beziehungen nicht genau abbilden, insbesondere wenn Datenquellen keine expliziten Hierarchien enthalten.

4. Verbesserung des Vorlagendesigns und der Konsistenz: Durch die Angabe von Bereichen stellen Nutzer sicher, dass Formatierungen, Formeln und Rahmen konsequent auf den Ausgabebereich angewendet werden. Dies verhindert Probleme wie inkonsistentes Zellstyling oder defekte Formeln in generierten Berichten.

5. Leistungsoptimierung und Daten sortieren: Der Range-Parameter ermöglicht es Tools, Datenquellen vor dem Ausfüllen der Vorlagen vorzusortieren, sodass gruppierte Daten in der richtigen Reihenfolge erscheinen.

## **Wie man Range-Parameter in SmartMarkers verwendet**
Manchmal müssen Sie eine Range in SmartMarkers sortieren oder andere Operationen durchführen. Aspose.Cells macht es möglich, den Range-Parameter in SmartMarkers zu verwenden. Bitte prüfen Sie [Vorlagendatei](range.xlsx), [JSON-Datei](range.json) und den Screenshot der erzeugten Excel-Ausgabedatei mit folgendem Code.

|**Das erste Arbeitsblatt der range.xlsx-Datei zeigt Smart Markers.**|
| :- |
|![todo:image_alt_text](range_template.png)|

|**Screenshot der Ausgabedatei im Excel-Format.**|
| :- |
|![todo:image_alt_text](range_result.png)|

Die JSON-Daten sind wie folgt:
```json data
{
  "Groups": [
    {
      "Materials": [
        { 
	        "Name": "BBB", 
	        "DSSection": { "Name": "Item B" } 
	      },
        {
          "Name": "CCC",
          "DSSection": { "Name": "Item C" }
        },
        {
          "Name": "AAA",
          "DSSection": { "Name": "Item A" }
        },        
        {
          "Name": "BBB",
          "DSSection": { "Name": "Item A" }
        },
        {
          "Name": "CCC",
          "DSSection": { "Name": "Item A" }
        },
        {
          "Name": "BBB",
          "DSSection": { "Name": "Item A" }
        },
        { 
	        "Name": "AAA", 
	        "DSSection": { "Name": "Item C" } 
        }
      ]
    }
  ]
}
```
Das folgende Beispiel zeigt, wie dies funktioniert.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "SmartMarkers-Using-Range-Parameter.cs" >}}
{{< app/cells/assistant language="csharp" >}}
