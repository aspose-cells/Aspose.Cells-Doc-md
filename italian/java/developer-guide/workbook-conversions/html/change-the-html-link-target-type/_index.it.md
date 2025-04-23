---
title: Modifica il Tipo di Destinazione del Link HTML
type: docs
weight: 450
url: /it/java/change-the-html-link-target-type/
---

{{% alert color="primary" %}} 

Aspose.Cells ti consente di modificare il tipo di destinazione del link HTML. Il link HTML appare così :

{{< highlight java >}}

 <a href="http://www.aspose.com/" target="_self">

{{< /highlight >}}

Come si può vedere, l'attributo target nel link HTML sopra è **_self**. È possibile controllare questo attributo target utilizzando la proprietà [HtmlSaveOptions.setLinkTargetType()](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#LinkTargetType). Questa proprietà richiede l'enum [HtmlLinkTargetType](https://reference.aspose.com/cells/java/com.aspose.cells/HtmlLinkTargetType) che ha i seguenti valori.

- [BLANK](https://reference.aspose.com/cells/java/com.aspose.cells/htmllinktargettype#BLANK)
- [PARENT](https://reference.aspose.com/cells/java/com.aspose.cells/htmllinktargettype#PARENT)
- [SELF](https://reference.aspose.com/cells/java/com.aspose.cells/htmllinktargettype#SELF)
- [TOP](https://reference.aspose.com/cells/java/com.aspose.cells/htmllinktargettype#TOP)

{{% /alert %}} 
## **Modifica il Tipo di Destinazione del Link HTML**
Il seguente codice illustra l'uso della proprietà [HtmlSaveOptions.setLinkTargetType()](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#LinkTargetType). Cambia il tipo di destinazione del link in **vuoto**. Per impostazione predefinita è il **genitore**. È possibile ottenere il [file excel di origine](5472932.xlsx) da questo link, tuttavia è possibile utilizzare qualsiasi file excel che contiene un collegamento ipertestuale HTML al suo interno per eseguire questo codice.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ChangeHTMLLinkTargetType-ChangeHTMLLinkTargetType.java" >}}
{{< app/cells/assistant language="java" >}}
