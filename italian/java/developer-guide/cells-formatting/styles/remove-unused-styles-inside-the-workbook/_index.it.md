---
title: Rimuovere gli Stili Non Utilizzati all interno del Workbook
type: docs
weight: 470
url: /it/java/remove-unused-styles-inside-the-workbook/
---

{{% alert color="primary" %}} 

Gli stili non utilizzati nel file di Excel non solo occupano spazio ma causano anche problemi di prestazioni durante la conversione in diversi formati come PDF, HTML, ecc. Aspose.Cells fornisce il [Workbook.removeUnusedStyles()](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#removeUnusedStyles\(\)) per rimuovere tutti gli stili non utilizzati all'interno del foglio di lavoro.

{{% /alert %}} 
## **Rimuovere gli stili non utilizzati all'interno del foglio di lavoro**
Il seguente codice spiega l'uso di [Workbook.removeUnusedStyles()](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#removeUnusedStyles\(\)). Il codice carica il [file Excel di modello](5473451.xlsx) che è possibile scaricare dal link fornito. Contiene uno stile non utilizzato chiamato **AsposeStyle**, questo stile e tutti gli altri stili non utilizzati verranno rimossi dopo l'esecuzione del codice. Si prega di vedere la seguente schermata per ulteriori illustrazioni.

![todo:image_alt_text](remove-unused-styles-inside-the-workbook_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-RemoveUnusedStyles-RemoveUnusedStyles.java" >}}
