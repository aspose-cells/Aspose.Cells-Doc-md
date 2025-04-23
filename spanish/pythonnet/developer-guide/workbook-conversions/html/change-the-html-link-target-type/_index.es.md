---
title: Cambiar el tipo de destino del enlace HTML
type: docs
weight: 320
url: /es/python-net/change-the-html-link-target-type/
description: Este tema le muestra cómo cambiar el tipo de destino de enlace HTML utilizando Aspose.Cells para Python via NET.
keywords: Cambiar el tipo de destino de enlace HTML, tipo de destino en blanco, tipo de destino padre, tipo de destino superior, tipo de destino propio.
---

{{% alert color="primary" %}}

Aspose.Cells para Python via NET le permite cambiar el tipo de destino de enlaces HTML. El enlace HTML se ve así

{{< highlight java >}}

 <a href="http://www.aspose.com/" target="_self">

{{< /highlight >}}

Como puedes ver, el atributo destino en el enlace HTML anterior es **_self**. Puedes controlar este atributo de destino usando la propiedad [**HtmlSaveOptions.link_target_type**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/link_target_type/). Esta propiedad toma la enumeración [**HtmlLinkTargetType**](https://reference.aspose.com/cells/python-net/aspose.cells/htmllinktargettype) que tiene los siguientes valores.

- HtmlLinkTargetType.BLANK
- HtmlLinkTargetType.PARENT
- HtmlLinkTargetType.SELF
- HtmlLinkTargetType.TOP

{{% /alert %}}

El siguiente código ilustra el uso de la propiedad [**HtmlSaveOptions.link_target_type**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/link_target_type/). Cambia el tipo de destino del enlace a **BLANK**. Por defecto, es el **PARENT**.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-ChangeHtmlLinkTarget-1.py" >}}
