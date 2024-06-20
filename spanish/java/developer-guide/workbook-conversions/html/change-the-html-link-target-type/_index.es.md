---
title: Cambiar el tipo de destino del enlace HTML
type: docs
weight: 450
url: /es/java/change-the-html-link-target-type/
---

{{% alert color="primary" %}} 

Aspose.Cells te permite cambiar el tipo de destino del enlace HTML. El enlace HTML se ve así:

{{< highlight java >}}

 <a href="http://www.aspose.com/" target="_self">

{{< /highlight >}}

Como puedes ver, el atributo de destino en el enlace HTML anterior es **_self**. Puedes controlar este atributo de destino utilizando la propiedad [HtmlSaveOptions.setLinkTargetType()](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#LinkTargetType). Esta propiedad toma el enum [HtmlLinkTargetType](https://reference.aspose.com/cells/java/com.aspose.cells/HtmlLinkTargetType) que tiene los siguientes valores:

- [BLANK](https://reference.aspose.com/cells/java/com.aspose.cells/htmllinktargettype#BLANK)
- [PARENT](https://reference.aspose.com/cells/java/com.aspose.cells/htmllinktargettype#PARENT)
- [SELF](https://reference.aspose.com/cells/java/com.aspose.cells/htmllinktargettype#SELF)
- [TOP](https://reference.aspose.com/cells/java/com.aspose.cells/htmllinktargettype#TOP)

{{% /alert %}} 
## **Cambiar el tipo de destino del enlace HTML**
El siguiente código ejemplifica el uso de la propiedad [HtmlSaveOptions.setLinkTargetType()](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#LinkTargetType). Cambia el tipo de destino del enlace a **blanco**. De forma predeterminada, es **padre**. Puedes obtener el [archivo de Excel fuente](5472932.xlsx) desde este enlace, sin embargo, puedes usar cualquier archivo de Excel que contenga un hipervínculo HTML en su interior para ejecutar este código.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ChangeHTMLLinkTargetType-ChangeHTMLLinkTargetType.java" >}}
