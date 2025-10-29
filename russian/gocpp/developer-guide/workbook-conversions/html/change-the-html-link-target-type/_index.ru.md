---
title: Изменение типа целевого HTML ссылки с помощью Golang через C++
linktitle: Изменить тип HTML ссылки
type: docs
weight: 320
url: /ru/go-cpp/change-the-html-link-target-type/
description: Узнайте, как изменить тип назначения ссылки HTML с помощью Aspose.Cells for C++. Управляйте атрибутом target в HTML ссылках программно.
---

{{% alert color="primary" %}}

Aspose.Cells позволяет вам изменять тип целевой ссылки HTML. HTML-ссылка выглядит так

{{< highlight java >}}

 <a href="http://www.aspose.com/" target="_self">

{{< /highlight >}}

Как видно из атрибута target в указанной выше HTML-ссылке **_self**. Вы можете контролировать этот атрибут target, используя свойство [**GetLinkTargetType()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getlinktargettype/). Это свойство принимает перечисление [**HtmlLinkTargetType**](https://reference.aspose.com/cells/cpp/aspose.cells/htmllinktargettype/), которое имеет следующие значения.

- HtmlLinkTargetType::Blank
- HtmlLinkTargetType::Parent
- HtmlLinkTargetType::Self
- HtmlLinkTargetType::Top

{{% /alert %}}

Приведенный ниже код иллюстрирует использование свойства [**GetLinkTargetType()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getlinktargettype/). Он изменяет тип целевой ссылки на **blank**. По умолчанию это **parent**.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ChangeTheHtmlLinkTargetType.go" >}}
