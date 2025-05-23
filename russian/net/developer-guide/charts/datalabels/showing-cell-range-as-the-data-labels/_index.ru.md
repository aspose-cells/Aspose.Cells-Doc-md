---
title: Отображение диапазона ячеек в качестве меток данных
description: Узнайте, как отображать диапазон ячеек в качестве меток данных на графиках, используя Aspose.Cells for .NET. Наше руководство продемонстрирует, как связать метки с вашим источником данных и форматировать их, чтобы обеспечить точную и значимую информацию на ваших графиках.
keywords: Aspose.Cells for .NET, построение графиков, метки данных, диапазон ячеек, источник данных, форматирование, точность, значимая информация.
type: docs
weight: 130
url: /ru/net/showing-cell-range-as-the-data-labels/
---

{{% alert color="primary" %}}

В Microsoft Excel 2013 вы можете отображать диапазон ячеек в качестве меток данных. Aspose.Cells поддерживает эту функцию.

{{% /alert %}}

## **Флажок для отображения диапазона ячеек в качестве меток данных**

Чтобы показать диапазон ячеек в качестве меток данных в Microsoft Excel:

1. Выберите метки данных ряда и щелкните правой кнопкой мыши, чтобы открыть контекстное меню.
1. Выберите **Формат меток данных**. Опции меток отображаются.
1. Выберите или снимите флажок у опции **Метка содержит - значение из ячеек**.

В приведенном ниже образце кода доступ к меткам данных серии графика и устанавливает свойство [**DataLabels.ShowCellRange**](https://reference.aspose.com/cells/net/aspose.cells.charts/datalabels/properties/showcellrange) в **true**, чтобы выбрать опцию **Метка содержит - значение из ячеек**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-ShowCellRangeAsDataLabels-ShowCellRangeAsDataLabels.cs" >}}
{{< app/cells/assistant language="csharp" >}}
