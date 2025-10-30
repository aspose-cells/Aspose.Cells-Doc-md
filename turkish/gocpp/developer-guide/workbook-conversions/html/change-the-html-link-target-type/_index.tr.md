---
title: HTML Bağlantı Hedef Türünü Golang ve C++ ile değiştirme
linktitle: HTML Bağlantısı Hedef Türünü Değiştirme
type: docs
weight: 320
url: /tr/go-cpp/change-the-html-link-target-type/
description: Aspose.Cells for C++ kullanarak HTML bağlantı hedef türünü nasıl değiştireceğinizi öğrenin. Bağlantıların hedef özniteliğini programlı olarak kontrol edin.
---

{{% alert color="primary" %}}

Aspose.Cells, HTML bağlantı hedef türünü değiştirmenize olanak tanır. HTML bağlantısı şuna benzer

{{< highlight java >}}

 <a href="http://www.aspose.com/" target="_self">

{{< /highlight >}}

Yukarıdaki HTML bağlantısında hedef özniteliği **_self** olarak gösterilir. Bu hedef özniteliğini [**GetLinkTargetType()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getlinktargettype/) özelliğini kullanarak kontrol edebilirsiniz. Bu özellik, aşağıdakileri içeren [**HtmlLinkTargetType**](https://reference.aspose.com/cells/cpp/aspose.cells/htmllinktargettype/) enumunu alır.

- HtmlLinkTargetType::Blank
- HtmlLinkTargetType::Parent
- HtmlLinkTargetType::Self
- HtmlLinkTargetType::Top

{{% /alert %}}

Aşağıdaki kod, [**GetLinkTargetType()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getlinktargettype/) özelliğinin kullanımını gösterir. Bağlantı hedef türünü varsayılan olarak **parent** olarak değiştirir.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ChangeTheHtmlLinkTargetType.go" >}}
