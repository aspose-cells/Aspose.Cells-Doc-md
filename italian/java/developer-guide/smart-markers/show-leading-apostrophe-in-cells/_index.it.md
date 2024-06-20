---
title: Mostra l apostrofo iniziale nelle celle
type: docs
weight: 20
url: /it/java/show-leading-apostrophe-in-cells/
---

## **Mostra apostrofo iniziale nelle celle**

In Microsoft Excel, l'apostrofo iniziale nel valore della cella è nascosto. Aspose.Cells fornisce la funzionalità per visualizzare l'apostrofo per impostazione predefinita. A tal fine, l'API fornisce la proprietà [**Workbook.Settings.QuotePrefixToStyle**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#QuotePrefixToStyle). Questa proprietà indica se impostare la proprietà [**QuotePrefix**](https://reference.aspose.com/cells/java/com.aspose.cells/Style#QuotePrefix) quando si inserisce un valore di stringa che inizia con un singolo apice nella cella. Impostando la proprietà [**Workbook.Settings.QuotePrefixToStyle**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#QuotePrefixToStyle) su **false** si visualizzerà l'apostrofo iniziale nel file excel di output.

Lo screenshot seguente mostra il file excel di output con l'apostrofo visibile.

![todo:image_alt_text](show-leading-apostrophe-in-cells_1.jpg)

Il seguente snippet di codice dimostra ciò aggiungendo dati con Smart Markers nel file excel di origine. Sono allegati i file excel di origine e di output per riferimento.

[File sorgente](AllowLeadingApostropheSample.xlsx)

[File di output](AllowLeadingApostropheSample_out.xlsx)

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-AllowLeadingApostrophe-1.java" >}}

L'implementazione della classe *DataObject* è riportata di seguito

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-HelperClasses-DataObject-1.java" >}}
