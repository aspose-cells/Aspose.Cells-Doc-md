---
title: Utilizzando il parametro Formula nel campo Smart Marker
type: docs
weight: 40
url: /it/net/using-formula-parameter-in-smart-marker-field/
---
## **Possibili scenari di utilizzo**
A volte, vuoi incorporare la formula nel campo del marcatore intelligente. Questo articolo descrive come utilizzare il*Formula*parametro per incorporare la formula nel campo del marcatore intelligente.
## **Utilizzando il parametro Formula nel campo Smart Marker**
 Il seguente codice di esempio incorpora la formula nel campo dell'indicatore intelligente denominato TestFormula e il nome dell'origine dati è MyDataSource, quindi il campo completo con il parametro della formula è simile a &=MyDataSource.TestFormula(formula) e dopo l'esecuzione del codice, il[file Excel di output finale](46465047.xlsx) avrà formule nelle celle da A1 a A5.
## **Codice d'esempio**
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-UsingFormulaParameterInSmartMarkerField.cs" >}}
