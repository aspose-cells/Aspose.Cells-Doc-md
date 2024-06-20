---
title: Вычислить масштабирование настройки страницы
type: docs
weight: 300
url: /ru/net/calculate-page-setup-scaling-factor/
description: В этой статье приведен примерный код, объясняющий, как использовать C# API или .NET библиотеку для программного расчета масштабного коэффициента настроек страницы с использованием опции Excel Вписать на n страниц(ы) по ширине и m по высоте .
keywords: Вписать на n страниц по ширине и m по высоте excel c#, рассчитать масштабный коэффициент настроек страницы c#
---

{{% alert color="primary" %}}

Когда вы устанавливаете масштабирование настройки страницы с помощью опции **Вписать на n страницы по ширине и m по высоте**, Microsoft Excel вычисляет масштабный коэффициент настроек страницы. Вы можете рассчитать то же самое, используя свойство [**SheetRender.PageScale**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender/properties/pagescale). Это свойство возвращает значение double, которое можно преобразовать в процентное значение. Например, если оно возвращает 0,5, это означает, что коэффициент масштабирования составляет 50%.

{{% /alert %}}

В следующем примере кода показано, как рассчитать масштабный коэффициент настроек страницы, используя свойство [**SheetRender.PageScale**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender/properties/pagescale).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-CalculateScalingFactor-CalculatePageSetupScalingFactor.cs" >}}
