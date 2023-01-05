---
title: Cambiar el tipo de destino del enlace HTML
type: docs
weight: 320
url: /es/net/change-the-html-link-target-type/
---
{{% alert color="primary" %}}

Aspose.Cells le permite cambiar el tipo de destino del enlace HTML. El enlace HTML se ve así

{{< highlight "java" >}}

 <a href="http://www.aspose.com/" target="_self">

{{< /highlight >}}

Como puede ver, el atributo de destino en el enlace anterior HTML es **_self**. Puede controlar este atributo de destino mediante la propiedad [**HtmlSaveOptions.LinkTargetType**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/linktargettype). Esta propiedad toma la enumeración [**HtmlLinkTargetType**](https://reference.aspose.com/cells/net/aspose.cells/htmllinktargettype) que tiene los siguientes valores.

- HtmlLinkTargetType.Blank
- HtmlLinkTargetType.Parent
- HtmlLinkTargetType.Self
- HtmlLinkTargetType.Top

{{% /alert %}}

 El siguiente código ilustra el uso de[**HtmlSaveOptions.LinkTargetType**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/linktargettype) propiedad. Cambia el tipo de destino del enlace a**blanco**. Por defecto, es el**padre**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ChangeHtmlLinkTarget-1.cs" >}}
