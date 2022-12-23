---
title: HTML Bağlantı Hedefi Türünü değiştirin
type: docs
weight: 320
url: /tr/net/change-the-html-link-target-type/
---
{{% alert color="primary" %}}

Aspose.Cells, HTML bağlantı hedefi türünü değiştirmenizi sağlar. HTML bağlantısı şuna benziyor

{{< highlight "java" >}}

 <a href="http://www.aspose.com/" target="_self">

{{< /highlight >}}

Yukarıdaki HTML bağlantısındaki hedef özniteliği görebileceğiniz gibi **_self** şeklindedir. [**HtmlSaveOptions.LinkTargetType**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/linktargettype) özelliğini kullanarak bu hedef niteliğini kontrol edebilirsiniz. Bu özellik, aşağıdaki değerlere sahip [**HtmlLinkTargetType**](https://reference.aspose.com/cells/net/aspose.cells/htmllinktargettype) sıralamasını alır.

- HtmlLinkTargetType.Blank
- HtmlLinkTargetType.Parent
- HtmlLinkTargetType.Self
- HtmlLinkTargetType.Top

{{% /alert %}}

 Aşağıdaki kod kullanımını göstermektedir[**HtmlSaveOptions.LinkTargetType**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/linktargettype) Emlak. Bağlantı hedefi türünü şu şekilde değiştirir:**boşluk**. Varsayılan olarak,**ebeveyn**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ChangeHtmlLinkTarget-1.cs" >}}
