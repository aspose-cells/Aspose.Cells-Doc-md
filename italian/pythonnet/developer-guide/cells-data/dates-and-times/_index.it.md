---
title: Come gestire le date e gli orari
type: docs
weight: 600
url: /it/python-net/how-to-manage-dates-and-times/
description: Impara come gestire date e orari attraverso l API Aspose.Cells for .NET.
keywords: Come gestire date e orari, Il sistema di data 1900, Il sistema di data 1904, Imposta date e orari, Ottieni date e orari, Gestisci date e orari, Archivia date e orari in Excel, Visualizza date e orari nelle celle.
---

## **Come archiviare date e orari in Excel**
Date e orari sono archiviati nelle celle come numeri. Quindi, i valori delle celle che contengono date e orari sono di tipo numerico. Un numero che specifica una data e un'ora è composto dalle componenti di data (parte intera) e ora (parte frazionaria). La proprietà Cell.DoubleValue restituisce questo numero.

## **Come visualizzare date e orari in Aspose.Cells**
Per visualizzare un numero come data e ora, applica il formato di data e ora richiesto a una cella tramite la proprietà [Style.Number](https://reference.aspose.com/cells/net/aspose.cells/style/number/) o [Style.Custom](). La proprietà CellValue.DateTimeValue restituisce l'oggetto DateTime, che specifica la data e l'ora rappresentate dal numero contenuto in una cella.
<br>
<image src="1.png" width="70%" />

## **Come passare da un sistema di date a un altro in Aspose.Cells**
MS-Excel archivia le date come numeri chiamati valori seriali. Un valore seriale è un intero che rappresenta il numero di giorni trascorsi dal primo giorno nel sistema di date. Excel supporta i seguenti sistemi di data per i valori seriali:

1. Il sistema di data 1900. La prima data è il 1 gennaio 1900 e il suo valore seriale è 1. L'ultima data è il 31 dicembre 9999 e il suo valore seriale è 2.958.465. Questo sistema di data è utilizzato nel foglio di lavoro per impostazione predefinita.
1. Il sistema di data 1904. La prima data è il 1 gennaio 1904 e il suo valore seriale è 0. L'ultima data è il 31 dicembre 9999 e il suo valore seriale è 2.957.003. Per utilizzare questo sistema di data nel foglio di lavoro, impostare la proprietà [Workbook.Settings.Date1904](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/date1904/) su true.


Questo esempio mostra che i valori seriali archiviati nella stessa data in sistemi di date diversi sono diversi.
{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-DatesAndTimes-Datetime-1904.py" >}}
Risultato in output:
```
A1 is Numeric Value: 45253
use The 1904 date system====================
A2 is Numeric Value: 43791
```

## **Come impostare il valore di data e ora in Aspose.Cells**
Questo esempio imposta un valore di data e ora nella cella A1 e A2, imposta il formato personalizzato di A1 e il formato numerico di A2, e quindi restituisce i tipi di valore.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-DatesAndTimes-Set-Datetime.py" >}}

Risultato in output:
```
A1 is Numeric Value: True
Cell A1 contains a DateTime value.
A2 is Numeric Value: True
Cell A2 contains a DateTime value.
```

## **Come ottenere il valore di data e ora in Aspose.Cells**
Questo esempio imposta un valore di data e ora nella cella A1 e A2, imposta il formato personalizzato di A1 e il formato numerico di A2, verifica i tipi di valore delle due celle, e quindi restituisce il valore di data e ora e la stringa formattata.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-DatesAndTimes-Get-Datetime.py" >}}

Risultato in output:
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
