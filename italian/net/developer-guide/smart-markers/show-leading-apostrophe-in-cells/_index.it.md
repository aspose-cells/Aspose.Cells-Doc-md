---
title: Mostra l apostrofo iniziale nelle celle
type: docs
weight: 70
url: /it/net/show-leading-apostrophe-in-cells/
---

In Microsoft Excel, l'apostrofo iniziale del valore della cella è nascosto. Aspose.Cells fornisce la funzionalità di visualizzare l'apostrofo per impostazione predefinita. A tal scopo, l'API fornisce la proprietà [Workbook.Settings.QuotePrefixToStyle](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/quoteprefixtostyle). Questa proprietà indica se impostare la proprietà [QuotePrefix](https://reference.aspose.com/cells/net/aspose.cells/style/properties/quoteprefix) quando si inserisce un valore di stringa che inizia con un singolo apostrofo nella cella. Impostando la proprietà [Workbook.Settings.QuotePrefixToStyle](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/quoteprefixtostyle) su **false** visualizzerà l'apostrofo iniziale nel file Excel di output.

Lo screenshot seguente mostra il file excel di output con l'apostrofo visibile.

![todo:image_alt_text](show-leading-apostrophe-in-cells_1.jpg)

Il seguente snippet di codice dimostra ciò aggiungendo dati con Smart Markers nel file excel di origine. Sono allegati i file excel di origine e di output per riferimento.

[File di origine](98107425.xlsx)

[File di output](98107426.xlsx)
## **Codice di Esempio**
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-AllowLeadingApostrophe-1.cs" >}}

L'implementazione della classe *DataObject* è riportata di seguito

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-AllowLeadingApostrophe-2.cs" >}}
