---
title: Convertire Excel in NumPy
type: docs
weight: 30
url: /it/python-net/convert-excel-to-numpy/
description: Convertire Excel in NumPy utilizzando l API Aspose.Cells per Python via .NET.
keywords: Python Convert Excel to NumPy array, Export Workbook to NumPy array in Python via NET, Python Convert Row to NumPy array, Python Convert Table to NumPy array, Export ListObject to NumPy array in Python via NET, Python Convert Range to NumPy array, Column to NumPy array using Python.
---

## **Introduzione a NumPy**
NumPy (Numerical Python) è un'estensione open source per calcoli numerici di Python. Questo strumento può essere utilizzato per memorizzare e elaborare grandi matrici, molto più efficiente della struttura di liste nidificate di Python (che può anche essere utilizzata per rappresentare matrici). Supporta un gran numero di array dimensionali e operazioni su matrici e fornisce anche un gran numero di librerie di funzioni matematiche per operazioni su array. 

Le principali funzioni di NumPy:
1. Ndarray, un oggetto di array multidimensionale, è una struttura dati veloce, flessibile e di risparmio di spazio.
1. Operazioni di algebra lineare, inclusa la moltiplicazione di matrici, la trasposizione, l'inversione, ecc.
1. Trasformata di Fourier, esegue una trasformata di Fourier veloce su un array.
1. Operazione rapida di array in virgola mobile.
1. Integrare il codice del linguaggio C in Python per eseguirlo più velocemente.

Utilizzando Aspose.Cells per Python via .NET API, è possibile convertire Excel, TSV, CSV, Json e molti formati diversi in ndarra NumPy.

## **Come convertire un Workbook di Excel in un ndarray NumPy**
Ecco un esempio di snippet di codice per dimostrare come esportare i dati di Excel in un array NumPy utilizzando Aspose.Cells per Python via .NET:
1. Caricare il [file di esempio](sample_data.xlsx).
1. Attraversare i dati di Excel ed esportare i dati in un ndarray NumPy utilizzando Aspose.Cells per Python via .NET.


{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Workbook-to-NDArray.py" >}}

Il risultato dell'output:
```
[[['City' 'Region' 'Store']    
  ['Chicago' 'Central' '3055'] 
  ['New York' 'East' '3036']   
  ['Detroit' 'Central' '3074']]

 [['City2' 'Region2' 'Store3']
  ['Seattle' 'West' '3000']
  ['philadelph' 'East' '3082']
  ['Detroit' 'Central' '3074']]

 [['City3' 'Region3' 'Store3']
  ['Seattle' 'West' '3166']
  ['New York' 'East' '3090']
  ['Chicago' 'Central' '3055']]]
```

## **Come convertire un Foglio di lavoro in un ndarray NumPy**
Ecco un esempio di snippet di codice per dimostrare come esportare i dati del foglio di lavoro in un ndarray NumPy utilizzando Aspose.Cells per Python via .NET:
1. Caricare il [file di esempio](sample_data.xlsx).
1. Ottenere il primo foglio di lavoro.
1. Convertire i dati del foglio di lavoro in un ndarray NumPy utilizzando la libreria Excel Aspose.Cells per Python.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Worksheet-to-NDArray.py" >}}

Il risultato dell'output:
```
[['City' 'Region' 'Store']    
 ['Chicago' 'Central' '3055'] 
 ['New York' 'East' '3036']   
 ['Detroit' 'Central' '3074']]
```
## **Come convertire un intervallo di Excel in un ndarray NumPy**
Ecco un esempio di frammento di codice per dimostrare come esportare i dati dell'intervallo in un ndarray NumPy utilizzando Aspose.Cells per Python via .NET:
1. Caricare il [file di esempio](sample_data.xlsx).
1. Ottenere il primo foglio di lavoro.
1. Crea l'intervallo.
1. Converti i dati dell'intervallo in un ndarray NumPy utilizzando la libreria Excel Aspose.Cells per Python.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Range-to-NDArray.py" >}}

Il risultato dell'output:
```
[['Region' 'Store']
 ['Central' '3055']
 ['East' '3036']]
```

## **Come convertire un ListObject di Excel in un ndarray NumPy**
Ecco un esempio di frammento di codice per dimostrare come esportare i dati dell'ListObject in un ndarray NumPy utilizzando Aspose.Cells per Python via .NET:
1. Caricare il [file di esempio](sample_data.xlsx).
1. Ottenere il primo foglio di lavoro.
1. Crea l'oggetto ListObject.
1. Converti i dati dell'ListObject in un ndarray NumPy utilizzando la libreria Excel Aspose.Cells per Python.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-ListObject-to-NDArray.py" >}}

Il risultato dell'output:
```
[['City' 'Region' 'Store']
 ['Chicago' 'Central' '3055']
 ['New York' 'East' '3036']
 ['Detroit' 'Central' '3074']]
```

## **Come convertire una riga di Excel in un ndarray NumPy**
Ecco un esempio di frammento di codice per dimostrare come esportare i dati della riga in un ndarray NumPy utilizzando Aspose.Cells per Python via .NET:
1. Caricare il [file di esempio](sample_data.xlsx).
1. Ottenere il primo foglio di lavoro.
1. Ottieni l'oggetto riga per indice riga.
1. Convertire i dati della riga in un ndarray NumPy utilizzando la libreria Excel Aspose.Cells per Python.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Row-to-NDArray.py" >}}

Il risultato dell'output:
```
['Detroit' 'Central' '3074']
```

## **Come convertire una colonna di Excel in un ndarray NumPy.**
Ecco un esempio di snippet di codice per dimostrare come esportare i dati della colonna in un ndarray NumPy utilizzando Aspose.Cells per Python via .NET:
1. Caricare il [file di esempio](sample_data.xlsx).
1. Ottenere il primo foglio di lavoro.
1. Ottenere l'oggetto colonna tramite l'indice della colonna.
1. Convertire i dati della colonna in un ndarray NumPy utilizzando la libreria Excel Aspose.Cells per Python.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Column-to-NDArray.py" >}}

Il risultato dell'output:
```
['Store' '3055' '3036' '3074']
```
{{< app/cells/assistant language="python-net" >}}
