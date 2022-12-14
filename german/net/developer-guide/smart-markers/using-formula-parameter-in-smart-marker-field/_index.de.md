---
title: Verwenden des Formelparameters im Smart Marker-Feld
type: docs
weight: 40
url: /de/net/using-formula-parameter-in-smart-marker-field/
---
## **Mögliche Nutzungsszenarien**
Manchmal möchten Sie Formeln in das intelligente Markierungsfeld einbetten. In diesem Artikel wird beschrieben, wie Sie die verwenden*Formel*Parameter zum Einbetten der Formel in das intelligente Markierungsfeld.
## **Verwenden des Formelparameters im Smart Marker-Feld**
 Der folgende Beispielcode bettet die Formel in das intelligente Markierungsfeld mit dem Namen TestFormula ein, und sein Datenquellenname ist MyDataSource, sodass das vollständige Feld mit dem Formelparameter wie folgt aussieht: &=MyDataSource.TestFormula(formula) und nach der Ausführung des Codes die[Endgültige Excel-Ausgabedatei](46465047.xlsx) wird Formeln in Zellen von A1 bis A5 haben.
## **Beispielcode**
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-UsingFormulaParameterInSmartMarkerField.cs" >}}
