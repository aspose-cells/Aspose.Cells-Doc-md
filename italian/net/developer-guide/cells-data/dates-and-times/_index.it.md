---
title: Come gestire date e orari
type: docs
weight: 600
url: /it/net/how-to-manage-dates-and-times/
description: Scopri come gestire date e orari tramite lo Aspose.Cells for .NET API.
keywords: How to Manage Dates and Times, The 1900 date system, The 1904 date system, Set Dates and Times, Get Dates and Times, Manage Dates and Times, Store Dates and Times in Excel, Display Dates and Times in Cells.
---
##  **Come memorizzare date e orari in Excel**
Le date e le ore vengono archiviate nelle celle come numeri. Pertanto, i valori delle celle che contengono date e ore sono di tipo numerico. Un numero che specifica una data e un'ora è costituito dai componenti data (parte intera) e ora (parte frazionaria). La proprietà Cell.DoubleValue restituisce questo numero.

##  **Come visualizzare date e ore in Aspose.Cells**
Per visualizzare un numero come data e ora, applicare il formato di data e ora richiesto a una cella tramite[Stile.Numero](https://reference.aspose.com/cells/net/aspose.cells/style/number/) O[Stile.Personalizzato]() proprietà. La proprietà CellValue.DateTimeValue restituisce l'oggetto DateTime, che specifica la data e l'ora rappresentate dal numero contenuto in una cella.
<br>
<image src="1.png" width="70%" />

##  **Come cambiare due sistemi di data in Aspose.Cells**
MS-Excel memorizza le date come numeri chiamati valori seriali. Un valore seriale è un numero intero che rappresenta il numero di giorni trascorsi dal primo giorno nel sistema di data. Excel supporta i seguenti sistemi di data per i valori seriali:

1. Il sistema di data del 1900. La prima data è 1 gennaio 1900 e il relativo valore seriale è 1. L'ultima data è 31 dicembre 9999 e il relativo valore seriale è 2.958.465. Questo sistema di data viene utilizzato nella cartella di lavoro per impostazione predefinita.
1.  Il sistema di data del 1904. La prima data è 1 gennaio 1904 e il relativo valore seriale è 0. L'ultima data è 31 dicembre 9999 e il relativo valore seriale è 2.957.003. Per utilizzare questo sistema di data nella cartella di lavoro, impostare il file[Cartella di lavoro.Impostazioni.Data1904](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/date1904/) proprietà su true.


Questo esempio mostra che i valori seriali memorizzati nella stessa data in sistemi di data diversi sono diversi.
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-Datetime-1904.cs" >}}
Risultato dell'output:
```
A1 is Numeric Value: 45253
use The 1904 date system====================
A2 is Numeric Value: 43791
```

##  **Come impostare il valore DateTime in Aspose.Cells**
In questo esempio viene impostato un valore DateTime nelle celle A1 e A2, viene impostato il formato personalizzato di A1 e il formato numerico di A2, quindi vengono restituiti i tipi di valore.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-Set-Datetime.cs" >}}

Risultato dell'output:
```
A1 is Numeric Value: True
Cell A1 contains a DateTime value.
A2 is Numeric Value: True
Cell A2 contains a DateTime value.
```

##  **Come ottenere il valore DateTime in Aspose.Cells**
Questo esempio imposta un valore DateTime nelle celle A1 e A2, imposta il formato personalizzato di A1 e il formato numerico di A2, controlla i tipi di valore di due celle e quindi restituisce il valore DateTime e la stringa formattata.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-Get-Datetime.cs" >}}

Risultato dell'output:
```
A1 is Numeric Value: True
Cell A1 contains a DateTime value.
A1 DateTime Value: 11/23/2023 5:59:09 PM
A1 DateTime String Value: 11-23-23 17:59:09
A2 is Numeric Value: True
Cell A2 contains a DateTime value.
A2 DateTime Value: 11/23/2023 5:59:09 PM
A2 DateTime String Value: 11/23/2023 17:59
```
