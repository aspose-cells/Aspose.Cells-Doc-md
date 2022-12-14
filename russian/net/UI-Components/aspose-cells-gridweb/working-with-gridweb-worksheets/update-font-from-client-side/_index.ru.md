---
title: Обновите настройки шрифта со стороны клиента
type: docs
weight: 170
url: /ru/net/update-font-from-client-side/
---
{{% alert color="primary" %}}

В этом разделе обсуждается изменение параметров шрифта на стороне клиента в элементе управления Aspose.Cells.GridWeb.

{{% /alert %}}

Aspose.Cells GridWeb теперь поддерживает изменение настроек шрифта на стороне клиента. Для этого API предоставляет следующие функции

- **обновлениеCellFontStyle**: Params - r/i/b/ib для обычного/курсивного/жирного/курсивного и&жирного
- **updateCellFontSize**: Params — имя шрифта и т. д. «Система»
- **updateCellFontName**: Params - размер шрифта и т.д. '12pt'
- **обновитьCellFontColor**: Params - none/u/l/ul/ для none/underline/strikout/underline&&strikout
- **обновлениеCellFontLine**: Params - цвет html, например #aa22ee, или известное название цвета, например, зеленый, красный,...
- **обновитьCellBackGroundColor**: Params - цвет html, например #aa22ee, или известное название цвета, например, зеленый, красный,...

В следующем фрагменте кода показано изменение параметров шрифта на стороне клиента в GridWeb.

## Образец кода

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples.GridWeb-CSharp-Worksheets-UpdateFontFromClientSide.aspx" >}}
