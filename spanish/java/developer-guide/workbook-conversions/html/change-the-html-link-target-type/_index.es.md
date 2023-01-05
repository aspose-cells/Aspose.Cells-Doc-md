---
title: Cambiar el tipo de destino del enlace HTML
type: docs
weight: 450
url: /es/java/change-the-html-link-target-type/
---
{{% alert color="primary" %}} 

Aspose.Cells le permite cambiar el tipo de destino del enlace HTML. El enlace HTML se ve así:

{{< highlight "java" >}}

 <a href="http://www.aspose.com/" target="_self">

{{< /highlight >}}

Como puede ver, el atributo de destino en el enlace anterior HTML es **_self**. Puede controlar este atributo de destino mediante la propiedad [HtmlSaveOptions.setLinkTargetType()](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#LinkTargetType). Esta propiedad toma la enumeración [HtmlLinkTargetType](https://reference.aspose.com/cells/java/com.aspose.cells/HtmlLinkTargetType) que tiene los siguientes valores.

- [BLANCO](https://reference.aspose.com/cells/java/com.aspose.cells/htmllinktargettype#BLANK)
- [PADRE](https://reference.aspose.com/cells/java/com.aspose.cells/htmllinktargettype#PARENT)
- [SER](https://reference.aspose.com/cells/java/com.aspose.cells/htmllinktargettype#SELF)
- [PARTE SUPERIOR](https://reference.aspose.com/cells/java/com.aspose.cells/htmllinktargettype#TOP)

{{% /alert %}} 
## **Cambiar el tipo de destino del enlace HTML**
 El siguiente código ilustra el uso de[HtmlSaveOptions.setLinkTargetType()](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#LinkTargetType) propiedad. Cambia el tipo de destino del enlace a**blanco**. Por defecto, es el**padre** . Puedes obtener el[archivo fuente excel](5472932.xlsx) Sin embargo, desde este enlace puede usar cualquier archivo de Excel que contenga un hipervínculo HTML para ejecutar este código.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ChangeHTMLLinkTargetType-ChangeHTMLLinkTargetType.java" >}}
