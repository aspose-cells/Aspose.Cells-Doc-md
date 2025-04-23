---
title: Adattare automaticamente le righe per le celle unite
type: docs
weight: 120
url: /it/net/autofit-rows-for-merged-cells/
---

{{% alert color="primary" %}}

Microsoft Excel fornisce una funzione che consente di dimensionare automaticamente l'altezza di una cella in base al suo contenuto. La funzione si chiama adattamento automatico delle righe. Microsoft Excel non imposta l'operazione di adattamento automatico sulle celle unite in modo nativo. A volte la funzione diventa vitale per un utente che ha davvero bisogno di implementare l'adattamento automatico delle righe anche sulle celle unite.

{{% /alert %}}

## **Come utilizzare AutoFitMergedCellsType per l'adattamento automatico delle righe**
Aspose.Cells supporta questa funzionalità attraverso l'API [**AutoFitterOptions.AutoFitMergedCellsType**](https://reference.aspose.com/cells/net/aspose.cells/autofitmergedcellstype/). Utilizzando questa API, è possibile adattare automaticamente le righe in un foglio di lavoro, comprese le celle unite. Ecco un elenco di tutti i possibili tipi di adattamento automatico delle celle unite:

- Nessuna
- Prima riga
- Ultima riga
- Ogni riga

## **Autoadattamento righe per celle unite**

Si prega di vedere il seguente codice, crea un oggetto workbook e aggiungi più fogli di lavoro. Utilizzare metodi diversi per operazioni di autoadattamento in ciascun foglio di lavoro. La schermata mostra i risultati dopo l'esecuzione del codice di esempio.

<br>
<img src="result.png" width=80% />

## **Codice di esempio C#**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-AutoFitRowsMergedCells-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
