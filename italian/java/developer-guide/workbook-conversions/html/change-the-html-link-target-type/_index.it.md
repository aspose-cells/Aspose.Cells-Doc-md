---
title: Modificare il tipo di destinazione del collegamento HTML
type: docs
weight: 450
url: /it/java/change-the-html-link-target-type/
---
{{% alert color="primary" %}} 

Aspose.Cells consente di modificare il tipo di destinazione del collegamento HTML. HTML il link si presenta così:

{{< highlight "java" >}}

 <a href="http://www.aspose.com/" target="_self">

{{< /highlight >}}

Come puoi vedere, l'attributo target nel link HTML sopra è **_self**. Puoi controllare questo attributo di destinazione utilizzando la proprietà [HtmlSaveOptions.setLinkTargetType()](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#LinkTargetType). Questa proprietà accetta l'enumerazione [HtmlLinkTargetType](https://reference.aspose.com/cells/java/com.aspose.cells/HtmlLinkTargetType) che ha i seguenti valori.

- [VUOTO](https://reference.aspose.com/cells/java/com.aspose.cells/htmllinktargettype#BLANK)
- [GENITORE](https://reference.aspose.com/cells/java/com.aspose.cells/htmllinktargettype#PARENT)
- [SE STESSO](https://reference.aspose.com/cells/java/com.aspose.cells/htmllinktargettype#SELF)
- [SUPERIORE](https://reference.aspose.com/cells/java/com.aspose.cells/htmllinktargettype#TOP)

{{% /alert %}} 
## **Modificare il tipo di destinazione del collegamento HTML**
 Il codice seguente illustra l'utilizzo di[HtmlSaveOptions.setLinkTargetType()](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#LinkTargetType) proprietà. Cambia il tipo di destinazione del collegamento in**vuoto**. Per impostazione predefinita, è il**genitore** . Puoi ottenere il[file excel di origine](5472932.xlsx) da questo collegamento tuttavia è possibile utilizzare qualsiasi file excel che contenga al suo interno un collegamento ipertestuale HTML per eseguire questo codice.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ChangeHTMLLinkTargetType-ChangeHTMLLinkTargetType.java" >}}
