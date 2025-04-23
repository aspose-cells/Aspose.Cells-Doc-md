---
title: Rimuovere gli Stili Non Utilizzati all interno del Workbook
type: docs
weight: 340
url: /it/python-net/remove-unused-styles-inside-the-workbook/
---

{{% alert color="primary" %}}

Gli stili non utilizzati nel file Excel non solo occupano spazio, ma causano anche problemi di prestazioni durante la conversione in formati diversi come PDF, HTML, ecc. Aspose.Cells per Python via .NET fornisce il metodo [**Workbook.remove_unused_styles()**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/remove_unused_styles) per rimuovere tutti gli stili non utilizzati all’interno del workbook.

{{% /alert %}}

Il codice seguente spiega l'utilizzo di [**Workbook.remove_unused_styles()**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/remove_unused_styles). Il codice carica il [file excel di modello](5115520.xlsx) che puoi scaricare dal link fornito. Contiene uno stile non utilizzato chiamato **AsposeStyle**, questo stile e tutti gli altri stili non utilizzati verranno rimossi dopo l'esecuzione del codice.

![todo:image_alt_text](remove-unused-styles-inside-the-workbook_1.png)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Workbook-RemoveUnusedStyles-1.py" >}}

