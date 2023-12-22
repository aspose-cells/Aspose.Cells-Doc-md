---
title: Applicare la formattazione condizionale nei fogli di lavoro
description: Come utilizzare la libreria Aspose.Cells in C# per applicare la formattazione condizionale nei fogli di lavoro. Modificando questi criteri, hai un maggiore controllo sull'aspetto e sulla visualizzazione delle celle.
keywords: Aspose.Cells, Conditional Formatting, C#, Worksheet, Formatting
type: docs
weight: 130
url: /it/net/apply-conditional-formatting-in-worksheets/
---
{{% alert color="primary" %}}

Questo articolo è progettato per fornire una comprensione dettagliata di come aggiungere la formattazione condizionale a un intervallo di celle in un foglio di lavoro.

La formattazione condizionale è una funzionalità avanzata di Microsoft Excel che consente di applicare formati a un intervallo di celle e di modificare la formattazione in base al valore della cella o al valore di una formula. Ad esempio, lo sfondo di una cella potrebbe essere rosso per evidenziare un valore negativo oppure il colore del testo potrebbe essere verde per un valore positivo. Quando il valore della cella soddisfa la condizione del formato, viene applicato il formato. Se il valore della cella non soddisfa la condizione di formattazione, viene utilizzata la formattazione predefinita della cella.

È possibile applicare la formattazione condizionale con Microsoft Office Automation ma ciò ha i suoi svantaggi. Ci sono diverse ragioni e questioni coinvolte: ad esempio, sicurezza, stabilità, scalabilità e velocità. Il motivo principale per cui abbiamo trovato un'altra soluzione è che lo stesso Microsoft sconsiglia vivamente l'automazione di Office per le soluzioni software.

Questo articolo mostra come creare un'applicazione console, aggiungere la formattazione condizionale sulle celle con poche semplici righe di codice utilizzando Aspose.Cells API.

{{% /alert %}}

##  **Utilizzo di Aspose.Cells per applicare la formattazione condizionale basata sul valore Cell**

1. *Scarica e installa Aspose.Cells**.
 1. Scarica Aspose.Cells for .NET.
1. Installalo sul tuo computer di sviluppo.
 Tutti i componenti Aspose, una volta installati, funzionano in modalità di valutazione. La modalità di valutazione non ha limiti di tempo e inserisce solo filigrane nei documenti prodotti.
1. *Crea un progetto**.
 Avvia Visual Studio.NET e crea una nuova applicazione console. In questo esempio viene creata un'applicazione console C#, ma è possibile utilizzare anche VB.NET.
1. *Aggiungi riferimenti**.
 Aggiungi un riferimento a Aspose.Cells al tuo progetto, ad esempio aggiungi un riferimento a ….\Programmi\Aspose\Aspose.Cells\Bin\Net1.0\Aspose.Cells.dll
1. *Applica la formattazione condizionale in base al valore della cella.
Di seguito è riportato il codice utilizzato per eseguire l'attività. Applico la formattazione condizionale su una cella.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ApplyConditionalFormatting-ApplyConditionalFormattingCellValue-1.cs" >}}

Quando viene eseguito il codice precedente, la formattazione condizionale viene applicata alla cella "A1" nel primo foglio di lavoro del file di output (output.xls). La formattazione condizionale applicata ad A1 dipende dal valore della cella. Se il valore della cella A1 è compreso tra 50 e 100, il colore di sfondo è rosso a causa della formattazione condizionale applicata.

##  **Utilizzo di Aspose.Cells per applicare la formattazione condizionale basata sulla formula**

1. Applicazione della formattazione condizionale in base alla formula (snippet di codice)
 Di seguito è riportato il codice per eseguire l'attività. Applica la formattazione condizionale su B3.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ApplyConditionalFormatting-ApplyConditionalFormattingFormula-1.cs" >}}

Quando viene eseguito il codice precedente, la formattazione condizionale viene applicata alla cella "B3" nel primo foglio di lavoro del file di output (output.xls). La formattazione condizionale applicata dipende dalla formula che calcola il valore di "B3" come somma di B1 e B2.
