---
title: Intelligentes Importieren von Array Elementen über Slicer in Excel mit Smart Markers
type: docs
weight: 30
url: /de/net/how-to-import-array-element-by-slicer-with-smart-markers/
---

## **Warum Zugriff auf Array-Elemente über Slicer**
Im Smart Marker von FastReport ermöglicht der Zugriff auf Array-Elemente mithilfe eines Slicers (z.B. [array[1..3]]) eine prägnante, effiziente Arbeit mit Teilmengen der Daten.

1. Vereinfachte Datenauswertung: Das manuelle Durchlaufen großer Arrays erfordert Schleifen und komplexe Syntax. Slicer lassen das Extrahieren von Bereichen (Teilarrays) in einer Zeile zu. Beispiel: [Products[1..5].Name] ruft die Namen der ersten 5 Produkte ab.
2. Dynamische Berichte: Erstellen Sie Berichte für variable Datenbereiche (z.B. „Top N Elemente“, paginierte Ansichten). Beispiel: [Sales[0..{PageNo*10}]] lädt dynamisch Datenabschnitte für mehrseitige Berichte.
3. Leistungsoptimierung: Vermeiden Sie das Laden ganzer Arrays in den Speicher. Laden Sie nur die benötigten Elemente. Beispiel: [Logs[^10..^1]] ruft effizient die letzten 10 Einträge ab.
4. Deklarative Syntax: Drücke Absichten direkt in Vorlagenmarkierungen aus. Beispiel: [Employees[3..7].Department] wählt eindeutig Abteilungen von Einträgen 3 bis 7 aus.
5. Integration mit Datenquellen: Funktioniert mit Arrays aus Datenbanken, JSON oder Code. Beispiel: Bind Invoice.Items[0..2], um die ersten 3 Posten anzuzeigen.
6. Slicer in Smart Markers reduzieren die Codekomplexität, verbessern die Lesbarkeit und optimieren die Datenverarbeitung für Array-Teilmengen. Verwenden Sie sie, wenn Sie schnellen, range-basierten Zugriff benötigen – ideal für Paginierung, Top-N-Listen oder fensterbasierte Datenansichten. 

## **Wie man Array-Elemente mit Slicern in Excel mit Smart Markers importiert**
Aspose.Cells unterstützt den Zugriff auf Array-Elemente durch Slicer in Smart Markers. Bitte überprüfen Sie [Vorlagendatei](ElementBySlicer.xlsx), [json-Datei](ElementBySlicer.json) und den Screenshot der Ausgabedatei im Excel-Format, die mit folgendem Code generiert wurde.

|**Das erste Arbeitsblatt der Datei smartmarker.xlsx zeigt Smart Marker.**|
| :- |
|![todo:image_alt_text](ElementBySlicer1.png)|

|**Screenshot der Ausgabedatei im Excel-Format.**|
| :- |
|![todo:image_alt_text](ElementBySlicer2.png)|

Die JSON-Daten sind wie folgt:
```json data
{
  "EntityCin": "EntityCin Test",
  "EntityName": "EntityName Test",
  "FirstName": "FirstName Test",
  "MiddleName": "MiddleName Test",
  "LastName": "LastName Test",
  "DOB": "2025-02-08",
  "SSN": "11111111",
  "Directors": [
    {
      "id": "director id 1",
      "FirstName": "director first 1",
      "MiddleName": "director middle 1",
      "LastName": "director last 1",
      "Reportees": [
        {
          "id": "aaa",
          "FirstName": "first aaa",
          "MiddleName": "middle aaa",
          "LastName": "last aaa",
          "Department": "aaa department",
          "City": "aaa city",
          "GST": "Yes",
          "ITR": "No"
        },
        {
          "id": "bbb",
          "FirstName": "first bbb",
          "MiddleName": "middle bbb",
          "LastName": "last bbb",
          "Department": "bbb department",
          "City": "bbb city",
          "GST": "Yes",
          "ITR": "Yes"
        },
        {
          "id": "ccc",
          "FirstName": "first ccc",
          "MiddleName": "middle ccc",
          "LastName": "last ccc",
          "Department": "ccc department",
          "City": "ccc city",
          "GST": "No",
          "ITR": "No"
        }
      ]
    },
    {
      "id": "director id 2",
      "FirstName": "director first 2",
      "MiddleName": "director middle 2",
      "LastName": "director last 2",
      "Reportees": [
        {
          "id": "eee",
          "FirstName": "first eee",
          "MiddleName": "middle eee",
          "LastName": "last eee",
          "Department": "eee department",
          "City": "eee city",
          "GST": "Yes",
          "ITR": "No"
        },
        {
          "id": "fff",
          "FirstName": "first fff",
          "MiddleName": "middle fff",
          "LastName": "last fff",
          "Department": "fff department",
          "City": "fff city",
          "GST": "No",
          "ITR": "No"
        }
      ]
    },
    {
      "id": "director id 3",
      "FirstName": "director first 2",
      "MiddleName": "director middle 2",
      "LastName": "director last 2",
      "Reportees": [
        {
          "id": "eee3",
          "FirstName": "first eee3",
          "MiddleName": "middle eee3",
          "LastName": "last eee3",
          "Department": "eee department3",
          "City": "eee city3",
          "GST": "Yes",
          "ITR": "No"
        },
        {
          "id": "fff3",
          "FirstName": "first fff3",
          "MiddleName": "middle fff3",
          "LastName": "last fff3",
          "Department": "fff department3",
          "City": "fff city",
          "GST": "No",
          "ITR": "No"
        }
      ]
    },
    {
      "id": "director id 4",
      "FirstName": "director first 4",
      "MiddleName": "director middle 4",
      "LastName": "director last 4",
      "Reportees": [
        {
          "id": "eee4",
          "FirstName": "first eee4",
          "MiddleName": "middle eee4",
          "LastName": "last eee4",
          "Department": "eee department4",
          "City": "eee city4",
          "GST": "Yes",
          "ITR": "No"
        },
        {
          "id": "fff4",
          "FirstName": "first fff4",
          "MiddleName": "middle fff4",
          "LastName": "last fff4",
          "Department": "fff department4",
          "City": "fff city4",
          "GST": "No",
          "ITR": "No"
        }
      ]
    }
  ]
}
```
Das folgende Beispiel zeigt, wie dies funktioniert.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "SmartMarkers-AccessElementBySlicer.cs" >}}

{{< app/cells/assistant language="csharp" >}}
