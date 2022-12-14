---
title: Adatta colonne e righe durante il caricamento dell'HTML nella cartella di lavoro
type: docs
weight: 70
url: /it/java/autofit-columns-and-rows-while-loading-html-in-workbook/
---
## **Possibili scenari di utilizzo**

 Puoi adattare automaticamente colonne e righe mentre carichi il tuo file HTML all'interno del file**[Cartella di lavoro](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)** oggetto. Si prega di impostare il**[HtmlLoadOptions.AutoFitColsAndRows](https://reference.aspose.com/cells/java/com.aspose.cells/htmlloadoptions#AutoFitColsAndRows)** proprietà a**VERO**per questo scopo.

## **Adatta colonne e righe durante il caricamento dell'HTML nella cartella di lavoro**

 Il codice di esempio seguente carica innanzitutto l'HTML di esempio nella cartella di lavoro senza alcuna opzione di caricamento e lo salva in formato XLSX. Quindi carica nuovamente l'HTML di esempio nella cartella di lavoro, ma questa volta carica l'HTML dopo aver impostato il file**[HtmlLoadOptions.AutoFitColsAndRows](https://reference.aspose.com/cells/java/com.aspose.cells/htmlloadoptions#AutoFitColsAndRows)** proprietà a**VERO**e lo salva in formato XLSX. Si prega di scaricare entrambi i file excel di output, ad es[File Excel di output senza AutoFitColsAndRows](outputWithout_AutoFitColsAndRows.xlsx) e[File Excel di output con AutoFitColsAndRows](outputWith_AutoFitColsAndRows.xlsx) . Lo screenshot seguente mostra l'effetto di**[HtmlLoadOptions.AutoFitColsAndRows](https://reference.aspose.com/cells/java/com.aspose.cells/htmlloadoptions#AutoFitColsAndRows)**property su entrambi i file excel di output.

![cose da fare:immagine_alt_testo](autofit-columns-and-rows-while-loading-html-in-workbook_1.png)

## **Codice di esempio**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-AutoFitColumnsRowsLoadingHTML-1.java" >}}
