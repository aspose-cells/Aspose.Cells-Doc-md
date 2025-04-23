---
title: Rimuovere gli Stili Non Utilizzati all interno del Workbook
type: docs
weight: 470
url: /it/java/remove-unused-styles-inside-the-workbook/
---

{{% alert color="primary" %}} 

Gli stili inutilizzati nel file Excel non solo occupano spazio ma causano anche problemi di prestazioni durante la conversione in diversi formati come PDF, HTML, ecc. Aspose.Cells fornisce il [Workbook.removeUnusedStyles()](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#removeUnusedStyles--) per rimuovere tutti gli stili inutilizzati all'interno del workbook.

{{% /alert %}} 
## **Rimuovere gli stili non utilizzati all'interno del foglio di lavoro**
Il seguente codice spiega l'uso di [Workbook.removeUnusedStyles()](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#removeUnusedStyles--). Il codice carica il [file Excel modello](5473451.xlsx) che puoi scaricare dal link fornito. Contiene uno stile inutilizzato chiamato **AsposeStyle**, questo stile e tutti gli altri stili inutilizzati verranno rimossi dopo l'esecuzione del codice. Consulta il seguente screenshot per ulteriori dettagli.

![todo:image_alt_text](remove-unused-styles-inside-the-workbook_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-RemoveUnusedStyles-RemoveUnusedStyles.java" >}}
{{< app/cells/assistant language="java" >}}
