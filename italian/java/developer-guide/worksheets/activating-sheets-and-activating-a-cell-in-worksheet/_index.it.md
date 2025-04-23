---
title: Attivazione di Fogli e Attivazione di una Cella nel Foglio di Lavoro
type: docs
weight: 5
url: /it/java/activating-sheets-and-activating-a-cell-in-worksheet/
---

{{% alert color="primary" %}}

A volte è necessario che un foglio di lavoro specifico sia attivo e visualizzato quando un utente apre un file di Microsoft Excel in Excel. Allo stesso modo, potresti voler attivare una cella specifica e impostare le barre di scorrimento per mostrare la cella attiva. Aspose.Cells è in grado di svolgere tutte queste attività come dimostrato di seguito.

- Un **foglio attivo** è un foglio su cui stai lavorando: il nome del foglio attivo sulla scheda è in grassetto per impostazione predefinita.
- Una **cella attiva** è una cella selezionata, la cella in cui vengono inseriti i dati quando si inizia a digitare. Solo una cella è attiva alla volta. La cella attiva è evidenziata da un bordo spesso.

{{% /alert %}}

## **Attivazione di Fogli e Attivazione di una Cella**

Aspose.Cells fornisce chiamate API specifiche per attivare un foglio e una cella. Ad esempio, la proprietà [**WorksheetCollection.ActiveSheetIndex**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#ActiveSheetIndex) è utile per impostare il foglio attivo in un workbook. Allo stesso modo, la proprietà [**Worksheet.ActiveCell**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#ActiveCell) può essere utilizzata per impostare e ottenere una cella attiva nel foglio di lavoro.

Per assicurarsi che le barre di scorrimento orizzontali o verticali siano nella posizione dell'indice di riga e colonna che si desidera mostrare dati specifici, utilizzare le proprietà [**Worksheet.FirstVisibleRow**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#FirstVisibleRow) e [**Worksheet.FirstVisibleColumn**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#FirstVisibleColumn).

Nell'esempio seguente viene mostrato come attivare un foglio di lavoro e rendere attiva una cella al suo interno. L'output seguente viene generato durante l'esecuzione del codice. Le barre di scorrimento sono scattate per rendere la 2ª riga e la 2ª colonna come la loro prima riga e colonna visibile.

**Impostare la cella B2 come una cella attiva**

![todo:image_alt_text](activating-sheets-and-activating-a-cell-in-worksheet_1.png)

## Codice Java per impostare un foglio di lavoro attivo in Excel

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ActivatingSheetsandActivatingCell-ActivatingSheetsandActivatingCell.java" >}}

{{% alert color="primary" %}}

In modalità di **valutazione**, cioè; senza impostare una licenza valida, il foglio di lavoro attivo sarà sempre quello contenente il watermark di valutazione. Questo comportamento può essere sovrascritto solo impostando la licenza all'avvio dell'applicazione.

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
