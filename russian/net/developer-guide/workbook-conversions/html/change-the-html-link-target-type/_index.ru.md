---
title: Изменить тип HTML ссылки
type: docs
weight: 320
url: /ru/net/change-the-html-link-target-type/
---

{{% alert color="primary" %}}

Aspose.Cells позволяет вам изменять тип целевой ссылки HTML. HTML-ссылка выглядит так

{{< highlight java >}}

 <a href="http://www.aspose.com/" target="_self">

{{< /highlight >}}

Как видно из атрибута target в указанной выше HTML-ссылке **_self**. Вы можете контролировать этот атрибут target, используя свойство [**HtmlSaveOptions.LinkTargetType**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/linktargettype). Это свойство принимает перечисление [**HtmlLinkTargetType**](https://reference.aspose.com/cells/net/aspose.cells/htmllinktargettype), которое имеет следующие значения.

- HtmlLinkTargetType.Blank
- HtmlLinkTargetType.Parent
- HtmlLinkTargetType.Self
- HtmlLinkTargetType.Top

{{% /alert %}}

Приведенный ниже код иллюстрирует использование свойства [**HtmlSaveOptions.LinkTargetType**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/linktargettype). Он изменяет тип целевой ссылки на **blank**. По умолчанию это **parent**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ChangeHtmlLinkTarget-1.cs" >}}
