---
title: Изменить тип HTML ссылки
type: docs
weight: 320
url: /ru/python-net/change-the-html-link-target-type/
description: В этой теме показано, как изменить тип цели ссылки HTML с помощью Aspose.Cells для Python via NET.
keywords: Изменить тип цели HTML ссылки, тип цели пустой, тип цели родитель, тип цели верхний, тип цели сам.
---

{{% alert color="primary" %}}

Aspose.Cells для Python via NET позволяет изменить тип цели ссылки HTML. HTML-ссылка выглядит так

{{< highlight java >}}

 <a href="http://www.aspose.com/" target="_self">

{{< /highlight >}}

Как видно из атрибута target в указанной выше HTML-ссылке **_self**. Вы можете контролировать этот атрибут target, используя свойство [**HtmlSaveOptions.link_target_type**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/link_target_type/). Это свойство принимает перечисление [**HtmlLinkTargetType**](https://reference.aspose.com/cells/python-net/aspose.cells/htmllinktargettype), которое имеет следующие значения.

- HtmlLinkTargetType.BLANK
- HtmlLinkTargetType.PARENT
- HtmlLinkTargetType.SELF
- HtmlLinkTargetType.TOP

{{% /alert %}}

В следующем коде показано использование свойства [**HtmlSaveOptions.link_target_type**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/link_target_type/). Оно изменяет тип цели ссылки на **BLANK**. По умолчанию это **PARENT**.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-ChangeHtmlLinkTarget-1.py" >}}
