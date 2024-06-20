---
title: Applicare la formattazione condizionale nei fogli di lavoro
description: Come utilizzare la libreria Aspose.Cells in C# per applicare la formattazione condizionale nei fogli di lavoro. Regolando questi criteri, si ha maggior controllo su come appaiono e appaiono le celle.
keywords: Aspose.Cells, Formattazione condizionale, C#, Foglio di lavoro, Formattazione
type: docs
weight: 130
url: /it/net/apply-conditional-formatting-in-worksheets/
---

{{% alert color="primary" %}}

Questo articolo è progettato per fornire una comprensione dettagliata di come aggiungere la formattazione condizionale a un intervallo di celle in un foglio di lavoro.

La formattazione condizionale è una funzionalità avanzata di Microsoft Excel che consente di applicare formati a un intervallo di celle e di far sì che la formattazione cambi a seconda del valore della cella o del valore di una formula. Ad esempio, lo sfondo di una cella può essere rosso per evidenziare un valore negativo, o il colore del testo potrebbe essere verde per un valore positivo. Quando il valore della cella soddisfa la condizione di formattazione, la formattazione viene applicata. Se il valore della cella non soddisfa la condizione di formattazione, viene utilizzata la formattazione predefinita della cella.

È possibile applicare la formattazione condizionale con la Automazione di Office di Microsoft ma ciò comporta alcuni svantaggi. Sono coinvolte diverse ragioni e problemi: ad esempio, sicurezza, stabilità, scalabilità e velocità. Il motivo principale per trovare un'altra soluzione è che Microsoft stessa sconsiglia vivamente l'Automazione di Office per le soluzioni software.

Questo articolo mostra come creare un'applicazione console, aggiungere la formattazione condizionale alle celle con poche semplici righe di codice utilizzando l'API di Aspose.Cells.

{{% /alert %}}

## **Utilizzare Aspose.Cells per Applicare la Formattazione Condizionale in Base al Valore della Cella**

1. **Scarica e installa Aspose.Cells**.
   1. Scarica Aspose.Cells for .NET.
1. Installalo sul tuo computer di sviluppo.
   Tutti i componenti Aspose, una volta installati, funzionano in modalità di valutazione. La modalità di valutazione non ha limiti di tempo e inserisce solo filigrane nei documenti prodotti.
1. **Crea un progetto**.
   Avvia Visual Studio.NET e crea una nuova applicazione console. Questo esempio crea un'applicazione console C#, ma è possibile utilizzare anche VB.NET.
1. **Aggiungi riferimenti**.
   Aggiungi un riferimento a Aspose.Cells al tuo progetto, ad esempio aggiungi un riferimento a ….\Program Files\Aspose\Aspose.Cells\Bin\Net1.0\Aspose.Cells.dll
1. *Applica formattazione condizionale in base al valore della cella.
   Di seguito è riportato il codice utilizzato per completare il compito. Si applica la formattazione condizionale a una cella.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ApplyConditionalFormatting-ApplyConditionalFormattingCellValue-1.cs" >}}

Quando il codice precedente viene eseguito, la formattazione condizionale viene applicata alla cella “A1” nel primo foglio di lavoro del file di output (output.xls). La formattazione condizionale applicata a A1 dipende dal valore della cella. Se il valore della cella di A1 è compreso tra 50 e 100, il colore di sfondo è rosso a causa della formattazione condizionale applicata.

## **Utilizzare Aspose.Cells per Applicare la Formattazione Condizionale in Base a una Formula**

1. Applicare la formattazione condizionale in base alla formula (Snippet di codice)
   Di seguito è riportato il codice per completare il compito. Si applica la formattazione condizionale su B3.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ApplyConditionalFormatting-ApplyConditionalFormattingFormula-1.cs" >}}

Quando il codice precedente viene eseguito, la formattazione condizionale viene applicata alla cella “B3” nel primo foglio di lavoro del file di output (output.xls). La formattazione condizionale applicata dipende dalla formula che calcola il valore di “B3” come somma di B1 e B2.
