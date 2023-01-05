---
title: Изменить тип цели ссылки HTML
type: docs
weight: 320
url: /ru/net/change-the-html-link-target-type/
---
{{% alert color="primary" %}}

Aspose.Cells позволяет изменить тип цели ссылки HTML. HTML ссылка выглядит так

{{< highlight "java" >}}

 <a href="http://www.aspose.com/" target="_self">

{{< /highlight >}}

Как вы можете видеть, целевой атрибут в приведенной выше ссылке HTML — **_self**. Вы можете управлять этим целевым атрибутом с помощью свойства [**HtmlSaveOptions.LinkTargetType**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/linktargettype). Это свойство принимает перечисление [**HtmlLinkTargetType**](https://reference.aspose.com/cells/net/aspose.cells/htmllinktargettype), которое имеет следующие значения.

- HtmlLinkTargetType. Пусто
- HtmlLinkTargetType.Parent
- HtmlLinkTargetType.Self
- HtmlLinkTargetType.Top

{{% /alert %}}

 Следующий код иллюстрирует использование[**HtmlSaveOptions.LinkTargetType**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/linktargettype) имущество. Он изменяет тип цели ссылки на**пустой**. По умолчанию это**родитель**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ChangeHtmlLinkTarget-1.cs" >}}
