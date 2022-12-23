---
title: Esporta uno stile del bordo simile quando lo stile del bordo non è supportato dai browser web
type: docs
weight: 70
url: /it/java/export-similar-border-style-when-border-style-is-not-supported-by-web-browsers/
---
## **Possibili scenari di utilizzo**

Microsoft Excel supporta alcuni tipi di bordi tratteggiati che non sono supportati dai browser Web. Quando si converte un file Excel di questo tipo in HTML utilizzando Aspose.Cells, tali bordi vengono rimossi. Tuttavia, Aspose.Cells può anche supportare la visualizzazione di bordi simili con[**HtmlSaveOptions.ExportSimilarBorderStyle**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExportSimilarBorderStyle)proprietà. Si prega di impostare il suo valore come**VERO**e anche i bordi non supportati verranno esportati nel file HTML.

## **Esporta uno stile del bordo simile quando lo stile del bordo non è supportato dai browser web**

Il codice di esempio seguente carica il file[esempio di file Excel](64716832.xlsx)che contiene alcuni bordi non supportati come mostrato nello screenshot seguente. Lo screenshot illustra ulteriormente l'effetto di[**HtmlSaveOptions.ExportSimilarBorderStyle**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExportSimilarBorderStyle)proprietà all'interno del[uscita HTML](64716831.zip).

![cose da fare:immagine_alt_testo](export-similar-border-style-when-border-style-is-not-supported-by-web-browsers_1.png)

## **Codice d'esempio**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "HTML-ExportSimilarBorderStyle.java" >}}
