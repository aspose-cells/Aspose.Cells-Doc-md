---
title: Cambiar el tipo de destino del enlace HTML
type: docs
weight: 320
url: /es/net/change-the-html-link-target-type/
---

{{% alert color="primary" %}}

Aspose.Cells te permite cambiar el tipo de destino del enlace HTML. El enlace HTML luce así

{{< highlight java >}}

 <a href="http://www.aspose.com/" target="_self">

{{< /highlight >}}

Como puedes ver, el atributo destino en el enlace HTML anterior es **_self**. Puedes controlar este atributo de destino usando la propiedad [**HtmlSaveOptions.LinkTargetType**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/linktargettype). Esta propiedad toma la enumeración [**HtmlLinkTargetType**](https://reference.aspose.com/cells/net/aspose.cells/htmllinktargettype) que tiene los siguientes valores.

- HtmlLinkTargetType.Blank
- HtmlLinkTargetType.Parent
- HtmlLinkTargetType.Self
- HtmlLinkTargetType.Top

{{% /alert %}}

El siguiente código ilustra el uso de la propiedad [**HtmlSaveOptions.LinkTargetType**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/linktargettype). Cambia el tipo de destino del enlace a **blank**. Por defecto, es **parent**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ChangeHtmlLinkTarget-1.cs" >}}
