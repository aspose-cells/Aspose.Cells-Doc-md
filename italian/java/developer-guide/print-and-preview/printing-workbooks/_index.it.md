---
title: Stampa Fogli di lavoro
type: docs
weight: 20
url: /it/java/printing-workbooks/
description: Come stampare fogli di lavoro e workbook utilizzando Java. Questo articolo fornisce il codice Java per stampare fogli di lavoro e workbook utilizzando l API Aspose.Cells for Java.
keywords: stampare workbook, stampare worksheets, stampare fogli del workbook, stampare un workbook, stampare workbook java, stampare worksheets java, stampare workbook excel java, stampare foglio excel java, stampare workbook, stampare foglio di lavoro
---

{{% alert color="primary" %}}

Questo documento è progettato per fornire agli sviluppatori una comprensione (in modo compatto) su come stampare fogli di calcolo.

{{% /alert %}}

## Scenario d'uso

Dopo aver creato il tuo foglio di calcolo, probabilmente vorrai stampare una copia cartacea della scheda per le tue esigenze. Quando stai stampando, MS Excel presume che tu voglia stampare l'intera area del foglio di lavoro a meno che tu non specifichi la tua selezione. Nella seguente schermata viene mostrata la finestra di dialogo per la stampa del workbook con Excel.

![todo:image_alt_text](printing-workbooks_1.png)

**Figura:** Finestra di dialogo di stampa

## Stampare i fogli di lavoro con Aspose.Cells

Aspose.Cells for Java fornisce un metodo [**toPrinter**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender#toPrinter-java.lang.String-) della classe [**SheetRender**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender). Utilizzando il metodo [**SheetRender.toPrinter**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender#toPrinter-java.lang.String-), puoi fornire il nome della stampante e il nome del lavoro di stampa.

## Codice di esempio

### Stampare il foglio di lavoro selezionato

Il seguente frammento di codice dimostra l'uso del metodo [**SheetRender.toPrinter**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender#toPrinter-java.lang.String-) per stampare il foglio di lavoro selezionato.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-PrintingSelectedWorksheet-PrintingSelectedWorksheet.java" >}}

### Stampare l'intero workbook

Puoi anche utilizzare il metodo [**WorkbookRender.toPrinter**](https://reference.aspose.com/cells/java/com.aspose.cells/workbookrender#toPrinter-java.lang.String-) per stampare l'intero workbook. Il seguente frammento di codice dimostra l'uso del metodo [**WorkbookRender.toPrinter**](https://reference.aspose.com/cells/java/com.aspose.cells/workbookrender#toPrinter-java.lang.String-) per stampare l'intero workbook.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-PrintingWholeWorkbook-PrintingWholeWorkbook.java" >}}

## Articoli correlati

- [Specificare il nome del lavoro o del documento durante la stampa con Aspose.Cells](/cells/it/java/specify-job-or-document-name-while-printing-with-aspose-cells/)
{{< app/cells/assistant language="java" >}}
