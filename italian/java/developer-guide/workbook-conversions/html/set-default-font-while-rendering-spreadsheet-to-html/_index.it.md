---
title: Imposta il carattere predefinito durante il rendering del foglio di calcolo su HTML
type: docs
weight: 830
url: /it/java/set-default-font-while-rendering-spreadsheet-to/
---
{{% alert color="primary" %}} 

 Aspose.Cells consente di impostare il carattere predefinito durante il rendering del foglio di calcolo su HTML. Utilizzare il[HtmlSaveOptions.DefaultFontName](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#DefaultFontName)per questo scopo. Questa proprietà è utile quando in un foglio di calcolo sono presenti alcune celle con caratteri non validi o inesistenti. Quindi quelle celle verranno visualizzate in un carattere specificato con[HtmlSaveOptions.DefaultFontName](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#DefaultFontName) proprietà.

{{% /alert %}} 
## **Imposta il carattere predefinito durante il rendering del foglio di calcolo su HTML**
Il seguente codice di esempio crea una cartella di lavoro e aggiunge del testo nella cella B4 del primo foglio di lavoro e ne imposta il carattere su un carattere sconosciuto/inesistente. Quindi salva la cartella di lavoro in HTML impostando diversi nomi di caratteri predefiniti come Courier New, Arial, Times New Roman, ecc.

 Lo screenshot mostra l'effetto dell'impostazione di diversi nomi di font predefiniti tramite[HtmlSaveOptions.DefaultFontName](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#DefaultFontName)proprietà.

![cose da fare:immagine_alt_testo](set-default-font-while-rendering-spreadsheet-to-html_1.png)

 Il codice genera il file[uscita file HTML con Corriere Nuovo](5472568) , il[uscita HTML con Arial](5472567) e il[output HTML file con Times New Roman](5472565).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-files-utility-SetDefaultFontWhileRenderingSpreadsheetToHTML-.java" >}}
