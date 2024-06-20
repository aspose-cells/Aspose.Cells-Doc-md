---
title: Rimuovere gli Stili Non Utilizzati all interno del Workbook
type: docs
weight: 340
url: /it/net/remove-unused-styles-inside-the-workbook/
---

{{% alert color="primary" %}}

Gli stili non utilizzati nel file excel non solo occupano spazio ma causano anche problemi di prestazioni durante la conversione in formati diversi come PDF, HTML, ecc. Aspose.Cells fornisce il [**Workbook.RemoveUnusedStyles()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/removeunusedstyles) per rimuovere tutti gli stili non utilizzati all'interno del workbook.

{{% /alert %}}

Il codice seguente spiega l'utilizzo di [**Workbook.RemoveUnusedStyles()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/removeunusedstyles). Il codice carica il [file excel di modello](5115520.xlsx) che puoi scaricare dal link fornito. Contiene uno stile non utilizzato chiamato **AsposeStyle**, questo stile e tutti gli altri stili non utilizzati verranno rimossi dopo l'esecuzione del codice.

![todo:image_alt_text](remove-unused-styles-inside-the-workbook_1.png)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RemoveUnusedStyles-1.cs" >}}
