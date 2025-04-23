---
title: Verwenden des Formelparameters im Smart Marker Feld
type: docs
weight: 40
url: /de/net/using-formula-parameter-in-smart-marker-field/
---


## **Mögliche Verwendungsszenarien**
Manchmal möchten Sie eine Formel im Smart-Marker-Feld einbetten. Dieser Artikel beschreibt, wie der *Formel* -Parameter verwendet wird, um die Formel im Smart-Marker-Feld zu verwenden.
## **Verwenden des Formelparameters im Smart Marker-Feld**
Der folgende Beispielcode bindet die Formel im Smart-Marker-Feld namens TestFormula ein, und sein Datenquellenname ist MyDataSource. Das vollständige Feld mit Formelparameter sieht wie folgt aus &=MyDataSource.TestFormula(formula) und nach der Ausführung des Codes enthält die [endgültige Ausgabedatei Excel-Datei](46465047.xlsx) Formeln in Zellen von A1 bis A5.
## **Beispielcode**
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-UsingFormulaParameterInSmartMarkerField.cs" >}}
{{< app/cells/assistant language="csharp" >}}
