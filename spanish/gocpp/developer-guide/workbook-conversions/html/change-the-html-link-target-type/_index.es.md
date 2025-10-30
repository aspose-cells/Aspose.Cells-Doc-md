---
title: Cambiar el tipo de destino del enlace HTML con Golang vía C++
linktitle: Cambiar el tipo de destino del enlace HTML
type: docs
weight: 320
url: /es/go-cpp/change-the-html-link-target-type/
description: Aprenda cómo cambiar el tipo de destino del enlace HTML usando Aspose.Cells for C++. Controle el atributo target en los enlaces HTML de forma programática.
---

{{% alert color="primary" %}}

Aspose.Cells te permite cambiar el tipo de destino del enlace HTML. El enlace HTML luce así

{{< highlight java >}}

 <a href="http://www.aspose.com/" target="_self">

{{< /highlight >}}

Como puedes ver, el atributo destino en el enlace HTML anterior es **_self**. Puedes controlar este atributo de destino usando la propiedad [**GetLinkTargetType()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getlinktargettype/). Esta propiedad toma la enumeración [**HtmlLinkTargetType**](https://reference.aspose.com/cells/cpp/aspose.cells/htmllinktargettype/) que tiene los siguientes valores.

- HtmlLinkTargetType::Blank
- HtmlLinkTargetType::Parent
- HtmlLinkTargetType::Self
- HtmlLinkTargetType::Top

{{% /alert %}}

El siguiente código ilustra el uso de la propiedad [**GetLinkTargetType()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getlinktargettype/). Cambia el tipo de destino del enlace a **blank**. Por defecto, es **parent**.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ChangeTheHtmlLinkTargetType.go" >}}
