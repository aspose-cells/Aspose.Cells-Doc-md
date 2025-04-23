---
title: Установить источник данных для графика
description: Узнайте о различных источниках данных, поддерживаемых Aspose.Cells для Python via .NET. Наш гайд познакомит вас с различными типами источников данных и покажет, как подключаться и получать данные из них для заполнения ваших таблиц.
keywords: Aspose.Cells для Python via .NET, создание диаграмм, форматирование данных, метки, цвета, шрифты, внешний вид, удобство использования.
linktitle: Источник данных
type: docs
weight: 10
url: /ru/python-net/data-formatting-in-charts/
---

В предыдущих темах мы уже предоставили множество примеров для демонстрации того, как можно установить источник данных для вашего графика, но в этой теме мы собираемся предоставить более подробную информацию о типах данных, которые можно установить для графика.

## **Установка данных графика**

При работе с диаграммами в Aspose.Cells для Python via .NET существует два типа данных, с которыми нужно работать:

- Данные графика.
- Данные категорий.

### **Данные графика**

Данные графика - это данные, которые мы используем в качестве источника данных для построения наших графиков. Мы можем добавить диапазон ячеек (содержащих данные графика), вызвав метод [**add**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/seriescollection/add) объекта [**SeriesCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/seriescollection).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-SettingChartsData-1.py" >}}

### **Данные категорий**

Данные категорий используются для маркировки данных графика и могут быть добавлены к [**SeriesCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/seriescollection) с использованием его свойства [**category_data**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/seriescollection/category_data). Приведен ниже полный пример для демонстрации использования данных графика и категорий. После выполнения приведенного выше примера кода на лист будет добавлена столбчатая диаграмма, как показано ниже.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-SettingCategoryData-1.py" >}}

## **Продвинутые темы**
- [Изменение источника данных диаграммы на целевой лист при копировании строк или диапазона](/cells/ru/python-net/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/)
- [Создание динамических диаграмм](/cells/ru/python-net/create-dynamic-charts/)
- [Простой способ настройки диаграммы с использованием метода Chart.SetChartDataRange](/cells/ru/python-net/easy-way-for-chart-setup-using-chart-setchartdatarange-method/)
- [Найдите тип значений X и Y точек в серии графика](/cells/ru/python-net/find-type-of-x-and-y-values-of-points-in-chart-series/)
