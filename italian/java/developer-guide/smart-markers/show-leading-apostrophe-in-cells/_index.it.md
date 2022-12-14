---
title: Mostra l'apostrofo iniziale nelle celle
type: docs
weight: 20
url: /it/java/show-leading-apostrophe-in-cells/
---
## **Mostra l'apostrofo iniziale nelle celle**

In Microsoft Excel, l'apostrofo iniziale nel valore della cella è nascosto. Aspose.Cells fornisce la funzione per visualizzare l'apostrofo per impostazione predefinita. Per questo, lo API fornisce[**Workbook.Settings.QuotePrefixToStyle**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#QuotePrefixToStyle)proprietà. Questa proprietà indica se impostare il[**CitazionePrefisso**](https://reference.aspose.com/cells/java/com.aspose.cells/Style#QuotePrefix)proprietà quando si immette un valore stringa che inizia con un singolo apice nella cella. Impostazione del[**Workbook.Settings.QuotePrefixToStyle**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#QuotePrefixToStyle)proprietà a**falso**visualizzerà l'apostrofo iniziale nel file excel di output.

Lo screenshot seguente mostra il file excel di output con l'apostrofo visibile.

![cose da fare:immagine_alt_testo](show-leading-apostrophe-in-cells_1.jpg)

Il seguente frammento di codice lo dimostra aggiungendo i dati con i marcatori intelligenti nel file Excel di origine. I file excel di origine e di output sono allegati per riferimento.

[File sorgente](AllowLeadingApostropheSample.xlsx)

[File di uscita](AllowLeadingApostropheSample_out.xlsx)

## **Codice di esempio**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-AllowLeadingApostrophe-1.java" >}}

L'implementazione di*Oggetto dati*la classe è riportata di seguito

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-HelperClasses-DataObject-1.java" >}}
