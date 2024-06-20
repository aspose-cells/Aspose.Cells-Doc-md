---
title: Utilizzare il parametro Formula nel campo Smart Marker
type: docs
weight: 40
url: /it/net/using-formula-parameter-in-smart-marker-field/
---


## **Possibili Scenari di Utilizzo**
A volte si desidera incorporare una formula nel campo Smart Marker. Questo articolo descrive come utilizzare il parametro *Formula* per includere una formula nel campo Smart Marker
## **Utilizzo del parametro Formula nel campo di Smart Marker**
Il codice di esempio seguente incorpora la formula nel campo Smart Marker denominato TestFormula e il nome del relativo origine dati è MyDataSource, quindi il campo completo con il parametro formula appare come &=MyDataSource.TestFormula(formula) e dopo l'esecuzione del codice, il [file Excel di output finale](46465047.xlsx) presenterà le formule nelle celle da A1 ad A5
## **Codice di Esempio**
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-UsingFormulaParameterInSmartMarkerField.cs" >}}
