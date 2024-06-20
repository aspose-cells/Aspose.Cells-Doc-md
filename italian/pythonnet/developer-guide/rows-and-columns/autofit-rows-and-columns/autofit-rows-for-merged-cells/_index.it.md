---
title: Adattare automaticamente le righe per le celle unite
type: docs
weight: 120
url: /it/python-net/autofit-rows-for-merged-cells/
description: Questo articolo mostra come AutoFit righe per celle unite attraverso l API Aspose.Cells per Python via .NET.
keywords: Libreria Excel Python, Come utilizzare AutoFitMergedCellsType per adattare automaticamente le righe, Autofit righe per celle unite in Python.
---

{{% alert color="primary" %}}

Microsoft Excel fornisce una funzione che consente di dimensionare automaticamente l'altezza di una cella in base al suo contenuto. La funzione si chiama adattamento automatico delle righe. Microsoft Excel non imposta l'operazione di adattamento automatico sulle celle unite in modo nativo. A volte la funzione diventa vitale per un utente che ha davvero bisogno di implementare l'adattamento automatico delle righe anche sulle celle unite.

{{% /alert %}}

## **Come utilizzare AutoFitMergedCellsType per l'adattamento automatico delle righe**
Aspose.Cells per Python via .NET supporta questa funzione tramite l'API [**AutoFitterOptions.AutoFitMergedCellsType**](https://reference.aspose.com/cells/python-net/aspose.cells/autofitmergedcellstype/). Utilizzando questa API, è possibile auto-dimensionare le righe in un foglio di lavoro incluse le celle unite. Ecco un elenco di tutti i possibili tipi di adattamento automatico per le celle unite:

- NONE
- PRIMA RIGA
- ULTIMA RIGA
- OGNI RIGA

## **Autoadattamento righe per celle unite**

Si prega di vedere il seguente codice, crea un oggetto workbook e aggiungi più fogli di lavoro. Utilizzare metodi diversi per operazioni di autoadattamento in ciascun foglio di lavoro. La schermata mostra i risultati dopo l'esecuzione del codice di esempio.

<br>
<img src="result.png" width=80% />

## **Codice di esempio C#**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-AutoFitRowsMergedCells-1.py" >}}
