---
title: Imposta il carattere predefinito durante la conversione del foglio di calcolo in HTML
type: docs
weight: 830
url: /it/java/set-default-font-while-rendering-spreadsheet-to/
---

{{% alert color="primary" %}} 

Aspose.Cells ti consente di impostare il carattere predefinito durante la rendering del foglio di calcolo in HTML. Si prega di utilizzare [HtmlSaveOptions.DefaultFontName](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#DefaultFontName) per questo scopo. Questa proprietà è utile quando ci sono delle celle in un foglio di calcolo che hanno caratteri non validi o inesistenti. Quelle celle saranno quindi renderizzate con il carattere specificato dalla proprietà [HtmlSaveOptions.DefaultFontName](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#DefaultFontName).

{{% /alert %}} 
## **Imposta il carattere predefinito durante la rendering del foglio di calcolo in HTML**
Il seguente codice di esempio crea un workbook e aggiunge del testo nella cella B4 del primo foglio di lavoro e imposta il suo carattere su un font sconosciuto/inesistente. Quindi salva il workbook in HTML impostando diversi nomi di carattere predefinito come Courier New, Arial, Times New Roman, ecc.

Lo screenshot mostra l'effetto di impostare diversi nomi di carattere predefinito tramite la proprietà [HtmlSaveOptions.DefaultFontName](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#DefaultFontName).

![todo:image_alt_text](set-default-font-while-rendering-spreadsheet-to-html_1.png)

Il codice genera il [file HTML di output con Courier New](5472568), l'[output HTML con Arial](5472567) e il [file HTML di output con Times New Roman](5472565).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-files-utility-SetDefaultFontWhileRenderingSpreadsheetToHTML-.java" >}}
{{< app/cells/assistant language="java" >}}
