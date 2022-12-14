---
title: Stampa di cartelle di lavoro
type: docs
weight: 20
url: /it/java/printing-workbooks/
description: Come stampare fogli di lavoro e cartelle di lavoro utilizzando Java. Questo articolo fornisce il codice Java per stampare fogli di lavoro e cartelle di lavoro utilizzando Aspose.Cells for Java API.
keywords: printing workbooks, printing worksheets, printing workbook sheets, printing a workbook, printing workbook java, printing worksheets java, printing excel workbook java, print excel worksheet java, print workbook, print worksheet
---
{{% alert color="primary" %}}

Questo documento è progettato per fornire agli sviluppatori una comprensione (in modo compatto) su come stampare fogli di calcolo.

{{% /alert %}}

## Scenario di utilizzo

Dopo aver finito di creare il tuo foglio di calcolo, probabilmente vorrai stampare una copia cartacea del foglio per le tue necessità. Quando si stampa, MS Excel presuppone che si desideri stampare l'intera area del foglio di lavoro a meno che non si specifichi la selezione. Lo screenshot seguente mostra la finestra di dialogo per la stampa della cartella di lavoro con Excel.

![cose da fare:immagine_alt_testo](printing-workbooks_1.png)

**Figura:** Finestra di dialogo Stampa

## Stampa di cartelle di lavoro utilizzando Aspose.Cells

 Aspose.Cells for Java fornisce a[**toPrinter**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender#toPrinter(java.lang.String) ) metodo del[**FoglioRendering**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender) classe. Utilizzando il[**SheetRender.toPrinter**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender#toPrinter(java.lang.String)), è possibile fornire il nome della stampante oltre al nome del lavoro di stampa.

## Codice di esempio

### Stampa foglio di lavoro selezionato

Il seguente frammento di codice illustra l'uso di[**SheetRender.toPrinter**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender#toPrinter(java.lang.String)) per stampare il foglio di lavoro selezionato.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-PrintingSelectedWorksheet-PrintingSelectedWorksheet.java" >}}

### Stampa intera cartella di lavoro

 Puoi anche usare il[**WorkbookRender.toPrinter**](https://reference.aspose.com/cells/java/com.aspose.cells/workbookrender#toPrinter(java.lang.String) ) metodo per stampare l'intera cartella di lavoro. Il seguente frammento di codice illustra l'uso di[**WorkbookRender.toPrinter**](https://reference.aspose.com/cells/java/com.aspose.cells/workbookrender#toPrinter(java.lang.String)) metodo per stampare l'intera cartella di lavoro.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-PrintingWholeWorkbook-PrintingWholeWorkbook.java" >}}

## articoli Correlati

- [Specificare il nome del lavoro o del documento durante la stampa con Aspose.Cells](/cells/it/java/specify-job-or-document-name-while-printing-with-aspose-cells/)
