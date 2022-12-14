---
title: Unione e separazione Cells in GridDesktop
linktitle: Fusione e Separazione Cells
type: docs
weight: 90
url: /it/net/merging-and-unmerging-cells-griddesktop/
---
{{% alert color="primary" %}} 

In questo argomento, discuteremo una funzionalità di utilità per unire e separare le celle di un foglio di lavoro. Questa funzione è utile nei casi in cui è necessario estendere alcune righe o colonne per migliorare la leggibilità dei dati.

{{% /alert %}} 
## **Fusione Cells**
Per unire le celle in un'unica cella grande, procedi nel seguente modo:

-  Accedi a qualsiasi desiderato**Foglio di lavoro**
-  Creare un**Gamma di Cells** da unire
- **Unisci** l'intervallo di cellule in una grande cella

 Puoi usare**Unisci** metodo di**Foglio di lavoro** per unire le celle. Tuttavia, è possibile definire un intervallo di celle utilizzando**CellRange** oggetto.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-MergingAndUnMergingCells-MergeCells.cs" >}}
## **Disaggregabile Cells**
Per separare una cella grande in più celle, procedi nel seguente modo:

-  Accedi a qualsiasi desiderato**Foglio di lavoro**
- Accedi alla cella unita che deve essere divisa
- **Separa** la cella grande in molte celle utilizzando la posizione della cella unita

 Puoi usare**Separa** metodo di**Foglio di lavoro** separare una cella usando la sua posizione.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-MergingAndUnMergingCells-UnMergeCells.cs" >}}

{{% alert color="primary" %}} 

Quando unisci le celle in una singola cella, le impostazioni di formattazione della cella in alto a sinistra (nell'intervallo di celle) vengono applicate alla cella unita, ma quando la cella viene separata, tutte le celle separate mantengono le loro impostazioni di formattazione.

{{% /alert %}}
