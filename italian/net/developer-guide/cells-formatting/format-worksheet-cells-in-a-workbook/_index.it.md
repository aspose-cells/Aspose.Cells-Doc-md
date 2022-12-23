---
title: Formattare il foglio di lavoro Cells in una cartella di lavoro
type: docs
weight: 2000
url: /it/net/format-worksheet-cells-in-a-workbook/
---
{{% alert color="primary" %}}

Questo articolo mostra come:

1. Usa gli stili per formattare rapidamente i dati.
1. Formatta le celle in righe e colonne.
1. Usa bordi e colori per enfatizzare i dati.
1. Applicare i formati numerici per enfatizzare i dati.
1. Usa caratteri e attributi per evidenziare i dati.
1. Formatta i dati in un intervallo denominato.
1. Modificare l'allineamento e l'orientamento dei dati.
1. Imposta l'altezza della riga e la larghezza della colonna.

 Il progetto di esempio esegue tutte queste attività e fornisce agli sviluppatori una descrizione dettagliata di come creare una cartella di lavoro, aggiungere dati e applicare la formattazione utilizzando[Aspose.Cells](https://products.aspose.com/cells/net/).

{{% /alert %}}

## **Formattazione dei dati**

La formattazione viene utilizzata per distinguere tra diversi tipi di informazioni e per visualizzare i dati in modo chiaro.

Un formato rappresenta uno stile ed è definito come un insieme di caratteristiche, come caratteri e dimensioni dei caratteri, formati numerici, bordi delle celle, ombreggiatura delle celle, rientro, allineamento e orientamento del testo. I bordi forniscono ulteriori modi per evidenziare le informazioni. Un bordo è una linea tracciata intorno a una cella o a un gruppo di celle.

Anche i formati numerici rendono i dati più significativi. Applicando diversi formati numerici, è possibile modificare l'aspetto dei numeri senza modificare il numero dietro l'aspetto.

Aspose.Cells ti consente di disegnare facilmente bordi attorno a celle e intervalli. Consente inoltre di applicare caratteri e ombreggiare le celle. Il componente è abbastanza efficiente da poter formattare una riga o colonna completa, impostare allineamenti, avvolgere e ruotare il testo nelle celle. Aspose.Cells supporta inoltre tutti i formati numerici supportati da Microsoft Excel.

Questo articolo illustra come creare un'applicazione console in Visual Studio.Net che genera un report annuale sulle vendite. La cartella di lavoro viene creata da zero, quindi i dati vengono inseriti e il foglio di lavoro viene formattato. Mostriamo come creare una semplice applicazione console che crea una cartella di lavoro Excel (puoi anche utilizzare un file modello), inserire i dati di vendita nel primo foglio di lavoro, formattare i dati e salvare un file Excel.

### **Processi**

Di seguito sono riportati i passaggi necessari per creare un foglio di calcolo e formattare celle diverse in righe e colonne diverse di un foglio di lavoro.

1. Scarica e installa Aspose.Cells:
   1. [Scaricamento](https://downloads.aspose.com/cells/net) Aspose.Cells for .NET.
 1. Installalo sul tuo computer di sviluppo.
1. Crea un progetto e aggiungi i riferimenti:
 1. Avviare Visual Studio.Net.
 1. Creare una nuova applicazione console.
 1. Aggiungere un riferimento a Aspose.Cells, ad esempio …\Program Files\Aspose\Aspose.Cells\Bin\Net1.0\Aspose.Cells.dll
1. Aggiungere il seguente codice al progetto:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FormatWorksheetCells-1.cs" >}}
