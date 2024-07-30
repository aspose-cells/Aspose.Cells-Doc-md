---
title: Вычислить масштабирование настройки страницы
type: docs
weight: 300
url: /ru/python-net/calculate-page-setup-scaling-factor/
description: Эта статья содержит пример кода, объясняющий, как использовать Aspose.Cells для Python via .NET API для расчета коэффициента масштабирования настройки страницы, используя опцию Подогнать на n страниц в ширину и m в высоту в рабочем листе Excel программно.
keywords: Библиотека Excel для Python, настройка страницы подогнать на n страниц в ширину и m в высоту в Python, расчет коэффициента масштабирования настройки страницы в Python.
---

{{% alert color="primary" %}}

Когда вы устанавливаете масштабирование настройки страницы с помощью опции **Вписать на n страницы по ширине и m по высоте**, Microsoft Excel вычисляет масштабный коэффициент настроек страницы. Вы можете рассчитать то же самое, используя свойство [**SheetRender.page_scale**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender/page_scale). Это свойство возвращает значение double, которое можно преобразовать в процентное значение. Например, если оно возвращает 0,5, это означает, что коэффициент масштабирования составляет 50%.

{{% /alert %}}

В следующем примере кода показано, как рассчитать масштабный коэффициент настроек страницы, используя свойство [**SheetRender.page_scale**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender/page_scale).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-CalculateScalingFactor-CalculatePageSetupScalingFactor.py" >}}
