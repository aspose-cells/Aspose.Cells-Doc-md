---
title: Вычислить коэффициент масштабирования параметров страницы
type: docs
weight: 300
url: /ru/net/calculate-page-setup-scaling-factor/
description: В этой статье представлен пример кода, объясняющий, как использовать библиотеку C# API или .NET для расчета коэффициента масштабирования параметров страницы с помощью параметра «Подогнать до n страниц по ширине на m в высоту» рабочего листа Excel программным путем.
keywords: Fit to n page wide by m tall excel c#, calculate page setup scaling factor c#
---
{{% alert color="primary" %}}

 Когда вы устанавливаете Масштабирование параметров страницы с помощью**Вместить до n страниц в ширину и m в высоту** опция, Microsoft Excel вычисляет коэффициент масштабирования параметров страницы. Вы можете рассчитать то же самое, используя[**SheetRender.PageScale**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender/properties/pagescale)свойство. Это свойство возвращает двойное значение, которое можно преобразовать в процентное значение. Например, если он возвращает 0,5, это означает, что коэффициент масштабирования равен 50%.

{{% /alert %}}

 В следующем примере кода показано, как рассчитать коэффициент масштабирования параметров страницы с помощью[**SheetRender.PageScale**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender/properties/pagescale) свойство.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-CalculateScalingFactor-CalculatePageSetupScalingFactor.cs" >}}
