---
title: Converti Excel in dati Python
type: docs
weight: 30
url: /it/python-net/convert-excel-to-list/
description: Converti Excel in elenco utilizzando l API Aspose.Cells per Python via .NET.
keywords: Converti Excel in dizionario utilizzando la libreria Excel Python, Converti Workbook in dizionario utilizzando la libreria Excel Python, Converti oggetto Row in elenco utilizzando la libreria Excel Python, Come convertire ListObject in elenco, Converti oggetto Column in elenco utilizzando la libreria Excel Python, Converti Range in elenco usando la libreria Excel Python, Converti Worksheet in elenco utilizzando la libreria Excel Python.
---

{{% alert color="primary" %}}

Utilizzando l'API Aspose.Cells per Python via .NET, puoi convertire Workbook, Worksheet, Range, Row, Column e altri dati excel in elenco Python.

{{% /alert %}}

## **Come convertire il Workbook di Excel in un dizionario**
Ecco uno snippet di codice di esempio per dimostrare come esportare i dati di Excel in un dizionario utilizzando Aspose.Cells per Python via .NET:
1. Caricare il [file di esempio](sample_data.xlsx).
1. Attraversa tutti i fogli di lavoro e converti il workbook in un dizionario utilizzando la libreria Excel Python Aspose.Cells.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Workbook-to-Dictionary.py" >}}

Il risultato dell'output:
```
{'Sheet1': [['City', 'Region', 'Store'], ['Chicago', 'Central', 3055], ['New York', 'East', 3036], ['Detroit', 'Central', 3074]], 'Sheet2': [['City2', 'Region2', 'Store3'], ['Seattle', 'West', 3000], ['philadelph', 'East', 3082], ['Detroit', 'Central', 3074]], 'Sheet3': [['City3', 'Region3', 'Store3'], ['Seattle', 'West', 3166], ['New York', 'East', 3090], ['Chicago', 'Central', 3055]]}
```

## **Come convertire il Workbook di Excel in un elenco**
Ecco un esempio di codice per dimostrare come esportare i dati di Excel in una lista utilizzando Aspose.Cells per Python via .NET:
1. Caricare il [file di esempio](sample_data.xlsx).
1. Attraversa tutti i fogli di lavoro e converti il workbook in una lista utilizzando la libreria Excel di Aspose.Cells per Python.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Workbook-to-List.py" >}}

Il risultato dell'output:
```
[[['City', 'Region', 'Store'], ['Chicago', 'Central', 3055], ['New York', 'East', 3036], ['Detroit', 'Central', 3074]], 
[['City2', 'Region2', 'Store3'], ['Seattle', 'West', 3000], ['philadelph', 'East', 3082], ['Detroit', 'Central', 3074]], [['City3', 'Region3', 'Store3'], ['Seattle', 'West', 3166], ['New York', 'East', 3090], ['Chicago', 'Central', 3055]]] 
```

## **Come Convertire un Foglio di Lavoro in Lista**
Ecco un esempio di codice per dimostrare come esportare i dati del foglio di lavoro in una lista utilizzando Aspose.Cells per Python via .NET:
1. Caricare il [file di esempio](sample_data.xlsx).
1. Ottenere il primo foglio di lavoro.
1. Converti i dati del foglio di lavoro in una lista utilizzando la libreria Excel di Aspose.Cells per Python.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Worksheet-to-List.py" >}}

Il risultato dell'output:
```
[['City', 'Region', 'Store'], ['Chicago', 'Central', 3055], ['New York', 'East', 3036], ['Detroit', 'Central', 3074]]
```

## **Come Convertire un ListObject di Excel in Lista**
Ecco un esempio di codice per dimostrare come esportare i dati di ListObject in una lista utilizzando Aspose.Cells per Python via .NET:
1. Caricare il [file di esempio](sample_data.xlsx).
1. Ottenere il primo foglio di lavoro.
1. Crea l'oggetto ListObject.
1. Converti i dati di ListObject in una lista utilizzando la libreria Excel di Aspose.Cells per Python.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-ListObject-to-List.py" >}}

Il risultato dell'output:
```
[['City', 'Region', 'Store'], ['Chicago', 'Central', 3055], ['New York', 'East', 3036], ['Detroit', 'Central', 3074]]
```


## **Come Convertire una Riga di Excel in Lista**
Ecco un esempio di codice per dimostrare come esportare i dati di Riga in una lista utilizzando Aspose.Cells per Python via .NET:
1. Caricare il [file di esempio](sample_data.xlsx).
1. Ottenere il primo foglio di lavoro.
1. Ottieni l'oggetto riga per indice riga.
1. Converti i dati della riga in lista usando la libreria Aspose.Cells per Excel in Python.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Row-to-List.py" >}}

Il risultato dell'output:
```
['Detroit', 'Central', 3074]
```

## **Come convertire una colonna di Excel in lista**
Ecco un esempio di frammento di codice per dimostrare come esportare i dati della colonna in lista utilizzando Aspose.Cells per Python via .NET:
1. Caricare il [file di esempio](sample_data.xlsx).
1. Ottenere il primo foglio di lavoro.
1. Ottenere l'oggetto colonna tramite l'indice della colonna.
1. Converti i dati della colonna in lista usando la libreria Aspose.Cells per Excel in Python.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Column-to-List.py" >}}

Il risultato dell'output:
```
['Store', 3055, 3036, 3074]
```

## **Come convertire un intervallo di Excel in lista**
Ecco un esempio di frammento di codice per dimostrare come esportare i dati dell'intervallo in lista utilizzando Aspose.Cells per Python via .NET:
1. Caricare il [file di esempio](sample_data.xlsx).
1. Ottenere il primo foglio di lavoro.
1. Crea l'intervallo.
1. Converti i dati dell'intervallo in lista usando la libreria Aspose.Cells per Excel in Python.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Range-to-List.py" >}}

Il risultato dell'output:
```
[['Region', 'Store'], ['Central', 3055], ['East', 3036]]
```
{{< app/cells/assistant language="python-net" >}}
