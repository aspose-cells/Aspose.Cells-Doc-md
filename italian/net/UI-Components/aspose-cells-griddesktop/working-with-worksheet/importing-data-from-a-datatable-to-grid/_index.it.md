---
title: Importazione di dati da un DataTable alla griglia
type: docs
weight: 50
url: /it/net/importing-data-from-a-datatable-to-grid/
---
{{% alert color="primary" %}} 

Dal rilascio del Framework .NET, Microsoft ha fornito un modo eccellente per archiviare i dati in modalità offline sotto forma di un oggetto DataTable. Comprendendo le esigenze degli sviluppatori, Aspose.Cells.GridDesktop supporta anche l'importazione di dati da una tabella di dati. In questo argomento viene illustrato come eseguire questa operazione.

{{% /alert %}} 
## **Esempio**
Per importare il contenuto di una tabella dati utilizzando il controllo Aspose.Cells.GridDesktop:

1. Aggiungere il controllo Aspose.Cells.GridDesktop a un modulo.
1. Creare un oggetto DataTable che contenga i dati da importare.
1. Ottenere il riferimento di un foglio di lavoro desiderato.
1. Importa il contenuto della tabella dati nel foglio di lavoro.
1. Impostare le intestazioni di colonna del foglio di lavoro in base ai nomi delle colonne della tabella dati.
1. Imposta la larghezza delle colonne, se lo desideri/
1. Visualizza il foglio di lavoro.

Nell'esempio fornito di seguito, abbiamo creato un oggetto DataTable e lo abbiamo riempito con alcuni dati recuperati da una tabella di database denominata Products. Infine, abbiamo importato i dati da tale oggetto DataTable in un foglio di lavoro desiderato utilizzando Aspose.Cells.GridDesktop.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ImportDataFromDataTable-1.cs" >}}
