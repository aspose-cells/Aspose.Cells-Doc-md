---
title: Adatta automaticamente le righe per l'unione Cells
type: docs
weight: 120
url: /it/net/autofit-rows-for-merged-cells/
---
{{% alert color="primary" %}}

Microsoft Excel fornisce una funzionalità che consente di ridimensionare automaticamente l'altezza di una cella in base al suo contenuto. La funzionalità è chiamata adattamento automatico delle righe. Microsoft Excel non imposta l'operazione di adattamento automatico sulle celle unite in modo nativo. A volte la funzionalità diventa vitale per un utente che ha davvero bisogno di implementare le righe di adattamento automatico anche sulle celle unite.

{{% /alert %}}

##  **Come utilizzare AutoFitMergedCellsType per l'adattamento automatico delle righe**
 Aspose.Cells supporta questa funzionalità tramite il[**AutoFitterOptions.AutoFitMergedCellsType**](https://reference.aspose.com/cells/net/aspose.cells/autofitmergedcellstype/)API. Utilizzando questo API, è possibile adattare automaticamente le righe in un foglio di lavoro includendo celle unite. Ecco un elenco di tutti i possibili tipi di celle unite con adattamento automatico:

- Nessuno
- Prima linea
- Ultima linea
- Ogni linea

##  **Adatta automaticamente le righe per l'unione Cells**

Consulta il codice seguente, crea un oggetto cartella di lavoro e aggiunge più fogli di lavoro. Utilizzare metodi diversi per le operazioni di adattamento automatico in ogni foglio di lavoro. Lo screenshot mostra i risultati dopo l'esecuzione del codice di esempio.

<br>
<img src="result.png" width=80% />

##  **C# Codice Campione**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-AutoFitRowsMergedCells-1.cs" >}}
