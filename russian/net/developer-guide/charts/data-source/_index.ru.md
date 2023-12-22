---
title: Установить источник данных для диаграммы
description: Узнайте о различных источниках данных, поддерживаемых номером Aspose.Cells for .NET. Наше руководство познакомит вас с различными типами доступных источников данных и покажет, как подключаться и получать из них данные для заполнения ваших рабочих листов.
keywords: Aspose.Cells for .NET, charting, data formatting, labels, colors, fonts, appearance, usability.
linktitle: Источник данных
type: docs
weight: 10
url: /ru/net/data-formatting-in-charts/
---
В наших предыдущих темах мы уже приводили множество примеров, демонстрирующих, как можно установить источник данных для диаграммы, но в этом разделе мы собираемся предоставить более подробную информацию о типах данных, которые можно установить для диаграммы.

##  **Настройка данных диаграммы**

При работе с диаграммами с использованием Aspose.Cells необходимо иметь дело с двумя типами данных:

- Данные диаграммы.
- Данные категории.

###  **Данные диаграммы**

 Данные диаграммы — это данные, которые мы используем в качестве источника данных для построения наших диаграмм. Мы можем добавить диапазон ячеек (содержащих данные диаграммы), вызвав метод[**СерияКоллекция**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection) объекты[**Добавлять**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection/methods/add)метод.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingChartsData-1.cs" >}}

###  **Данные категории**

 Данные категории используются для маркировки данных диаграммы и могут быть добавлены в[**СерияКоллекция**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection) используя свой[**КатегорияДанные**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection/properties/categorydata)свойство. Ниже приведен полный пример, демонстрирующий использование данных диаграммы и категорий. После выполнения приведенного выше примера кода на лист будет добавлена гистограмма, как показано ниже.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingCategoryData-1.cs" >}}

##  **Предварительные темы**
- [Изменение источника данных диаграммы на целевой лист при копировании строк или диапазона](/cells/ru/net/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/)
- [Создание динамических диаграмм](/cells/ru/net/create-dynamic-charts/)
- [Простой способ настройки диаграммы с использованием метода Chart.SetChartDataRange](/cells/ru/net/easy-way-for-chart-setup-using-chart-setchartdatarange-method/)
- [Найдите тип значений X и Y точек в серии диаграмм](/cells/ru/net/find-type-of-x-and-y-values-of-points-in-chart-series/)
