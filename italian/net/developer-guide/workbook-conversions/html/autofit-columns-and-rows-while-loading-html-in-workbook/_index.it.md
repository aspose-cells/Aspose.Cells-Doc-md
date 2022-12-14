---
title: Adatta colonne e righe durante il caricamento dell'HTML nella cartella di lavoro
type: docs
weight: 120
url: /it/net/autofit-columns-and-rows-while-loading-html-in-workbook/
---
## **Possibili scenari di utilizzo**

Puoi adattare automaticamente colonne e righe durante il caricamento del file HTML all'interno dell'oggetto Cartella di lavoro. Si prega di impostare il**[HtmlLoadOptions.AutoFitColsAndRows](https://reference.aspose.com/cells/net/aspose.cells/htmlloadoptions/properties/autofitcolsandrows)** proprietà a**VERO**per questo scopo.

## **Adatta colonne e righe durante il caricamento dell'HTML nella cartella di lavoro**

 Il codice di esempio seguente carica innanzitutto l'HTML di esempio nella cartella di lavoro senza alcuna opzione di caricamento e lo salva in formato XLSX. Quindi carica nuovamente l'HTML di esempio nella cartella di lavoro, ma questa volta carica l'HTML dopo aver impostato il file**[HtmlLoadOptions.AutoFitColsAndRows](https://reference.aspose.com/cells/net/aspose.cells/htmlloadoptions/properties/autofitcolsandrows)** proprietà a**VERO**e lo salva in formato XLSX. Si prega di scaricare entrambi i file excel di output, ad es[File Excel di output senza AutoFitColsAndRows](outputWithout_AutoFitColsAndRows.xlsx) e[File Excel di output con AutoFitColsAndRows](outputWith_AutoFitColsAndRows.xlsx) . Lo screenshot seguente mostra l'effetto di**[HtmlLoadOptions.AutoFitColsAndRows](https://reference.aspose.com/cells/net/aspose.cells/htmlloadoptions/properties/autofitcolsandrows)**property su entrambi i file excel di output.

![cose da fare:immagine_alt_testo](autofit-columns-and-rows-while-loading-html-in-workbook_1.png)

## **Codice di esempio**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-AutoFitColumnsandRowsWhileLoadingHTMLInWorkbook-1.cs" >}}

