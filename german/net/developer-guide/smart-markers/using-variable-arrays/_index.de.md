---
title: Intelligent Variablen Arrays in Excel mit Smart Markern importieren
type: docs
weight: 30
url: /de/net/how-to-import-variable-arrays-with-smart-markers/
---

## **Warum Variable Arrays für Smart Marker verwenden**
Variable arrays (e.g., <<products[0].name>> or <<foreach item in cart>>) enable dynamic handling of repeated data structures in templates. They solve limitations of flat/nested objects when dealing with lists, tables, or collections.

1. Dynamische Wiederholung ohne Hardcoding: Statische Marker funktionieren nicht bei variabler Länge (z.B. Bestellartikel, Benutzerberechtigungen). Arrays iterieren dynamisch. 
2. Vereinfachte Aggregation: Summen, Durchschnitte oder Filter direkt berechnen. Manuelle JavaScript-/C#-Logik in Vorlagen vermeiden.
3. Tabellarische/Listen-Datenrepräsentation: Natürliche Passform: Tabellen, Raster und Listen lassen sich inhärent auf Arrays abbilden.
4. Speichereffizienz: Arrays reduzieren die Komplexität der Vorlage und den Datenbindungsaufwand.
5. Integration mit APIs/Datenquellen: Passt zu JSON-/Array-zentrierten Daten (z.B. REST-APIs).

## **So importieren Sie variable Arrays mit Smart Markern**
Im folgenden Beispielcode wird gezeigt, wie Variable Arrays in Smart Markers verwendet werden. Wir platzieren einen Variablen-Array-Marker in Zelle A1 des ersten Arbeitsblatts der Arbeitsmappe dynamisch, der einen String von Werten enthält, die wir für den Marker festlegen, verarbeiten die Marker, um Daten in die Zellen gegen den Marker einzufügen. Schließlich speichern wir die Excel-Datei.


{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-UsingVariableArray-1.cs" >}}

## **So importieren Sie HTML-Eigenschaften mit Smart Markern**
The following sample code explains the use of HTML property of the Smart Markers. When it will be processed, it will show "World" in "Hello World" as bold because of HTML <b> tag.


{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-UsingHTMLProperty-1.cs" >}}

{{< app/cells/assistant language="csharp" >}}
