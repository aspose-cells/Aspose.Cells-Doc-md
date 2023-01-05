---
title: Mostra l'apostrofo iniziale nelle celle
type: docs
weight: 70
url: /it/net/show-leading-apostrophe-in-cells/
---
 In Microsoft Excel, l'apostrofo iniziale nel valore della cella è nascosto. Aspose.Cells fornisce la funzione per visualizzare l'apostrofo per impostazione predefinita. Per questo, lo API fornisce[Workbook.Settings.QuotePrefixToStyle](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/quoteprefixtostyle) proprietà. Questa proprietà indica se impostare il[CitazionePrefisso](https://reference.aspose.com/cells/net/aspose.cells/style/properties/quoteprefix)proprietà quando si immette un valore stringa che inizia con un singolo apice nella cella. Impostazione del[Workbook.Settings.QuotePrefixToStyle](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/quoteprefixtostyle) proprietà a**falso**visualizzerà l'apostrofo iniziale nel file excel di output.

Lo screenshot seguente mostra il file excel di output con l'apostrofo visibile.

![cose da fare:immagine_alt_testo](show-leading-apostrophe-in-cells_1.jpg)

Il seguente frammento di codice lo dimostra aggiungendo i dati con i marcatori intelligenti nel file Excel di origine. I file excel di origine e di output sono allegati per riferimento.

[File sorgente](98107425.xlsx)

[File di uscita](98107426.xlsx)
## **Codice d'esempio**
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-AllowLeadingApostrophe-1.cs" >}}

L'implementazione di*Oggetto dati*la classe è riportata di seguito

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-AllowLeadingApostrophe-2.cs" >}}
