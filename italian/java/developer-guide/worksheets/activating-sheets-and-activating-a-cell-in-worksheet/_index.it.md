---
title: Attivazione di fogli e attivazione di un Cell nel foglio di lavoro
type: docs
weight: 5
url: /it/java/activating-sheets-and-activating-a-cell-in-worksheet/
---
{{% alert color="primary" %}}

A volte, è necessario che un foglio di lavoro specifico sia attivo e visualizzato quando un utente apre un file Excel Microsoft in Excel. Allo stesso modo, potresti voler attivare una cella specifica e impostare le barre di scorrimento per mostrare la cella attiva. Aspose.Cells è in grado di svolgere tutte queste attività come dimostrato di seguito.

-  Un**foglio attivo** è un foglio su cui stai lavorando: il nome del foglio attivo sulla scheda è in grassetto per impostazione predefinita.
-  Un**Cellula attiva** è una cella selezionata, la cella in cui vengono inseriti i dati quando inizi a digitare. È attiva solo una cella alla volta. La cella attiva è evidenziata da un bordo spesso.

{{% /alert %}}

## **Attivazione Fogli e Attivazione Cell**

Aspose.Cells prevede chiamate specifiche API per l'attivazione di un foglio e di una cella. Ad esempio, il[**WorksheetCollection.ActiveSheetIndex**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#ActiveSheetIndex)è utile per impostare il foglio attivo in una cartella di lavoro. Allo stesso modo, il[**Foglio di lavoro.Cella attiva**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#ActiveCell)La proprietà può essere utilizzata per impostare e ottenere una cella attiva nel foglio di lavoro.

Per assicurarti che le barre di scorrimento orizzontali o verticali si trovino nella posizione dell'indice di riga e colonna in cui desideri mostrare dati specifici, utilizza il[**Worksheet.FirstVisibleRow**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#FirstVisibleRow)e[**Foglio di lavoro.FirstVisibleColumn**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#FirstVisibleColumn)proprietà.

L'esempio seguente mostra come attivare un foglio di lavoro e creare una cella attiva al suo interno. Il seguente output viene generato durante l'esecuzione del codice. Le barre di scorrimento vengono fatte scorrere per rendere la seconda riga e la seconda colonna come prima riga e colonna visibili.

**Impostazione della cella B2 come cella attiva**

![cose da fare:immagine_alt_testo](activating-sheets-and-activating-a-cell-in-worksheet_1.png)

## Java codice per impostare un foglio di lavoro attivo in Excel

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ActivatingSheetsandActivatingCell-ActivatingSheetsandActivatingCell.java" >}}

{{% alert color="primary" %}}

 In**valutazione** modalità, cioè; senza impostare una licenza valida, il foglio di lavoro attivo sarà sempre quello contenente la filigrana di valutazione. Questo comportamento può essere ignorato solo impostando la licenza all'avvio dell'applicazione.

{{% /alert %}}
