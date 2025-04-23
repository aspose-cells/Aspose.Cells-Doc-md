---
title: Установить источник данных для графика
description: Узнайте о различных источниках данных, поддерживаемых Aspose.Cells for .NET. Наш руководство покажет вам различные типы доступных источников данных и покажет, как подключиться и извлечь данные из них для заполнения ваших листов.
keywords: Aspose.Cells for .NET, построение графиков, форматирование данных, метки, цвета, шрифты, внешний вид, удобство использования.
linktitle: Источник данных
type: docs
weight: 10
url: /ru/net/data-formatting-in-charts/
---

В предыдущих темах мы уже предоставили множество примеров для демонстрации того, как можно установить источник данных для вашего графика, но в этой теме мы собираемся предоставить более подробную информацию о типах данных, которые можно установить для графика.

## **Установка данных графика**

При работе с графиками с использованием Aspose.Cells есть два типа данных, с которыми нужно работать, следующие:

- Данные графика.
- Данные категорий.

### **Данные графика**

Данные графика - это данные, которые мы используем в качестве источника данных для построения наших графиков. Мы можем добавить диапазон ячеек (содержащих данные графика), вызвав метод [**Add**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection/methods/add) объекта [**SeriesCollection**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingChartsData-1.cs" >}}

### **Данные категорий**

Данные категорий используются для маркировки данных графика и могут быть добавлены к [**SeriesCollection**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection) с использованием его свойства [**CategoryData**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection/properties/categorydata). Приведен ниже полный пример для демонстрации использования данных графика и категорий. После выполнения приведенного выше примера кода на лист будет добавлена столбчатая диаграмма, как показано ниже.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingCategoryData-1.cs" >}}

## **Продвинутые темы**
- [Изменение источника данных диаграммы на целевой лист при копировании строк или диапазона](/cells/ru/net/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/)
- [Создание динамических диаграмм](/cells/ru/net/create-dynamic-charts/)
- [Простой способ настройки диаграммы с использованием метода Chart.SetChartDataRange](/cells/ru/net/easy-way-for-chart-setup-using-chart-setchartdatarange-method/)
- [Найдите тип значений X и Y точек в серии графика](/cells/ru/net/find-type-of-x-and-y-values-of-points-in-chart-series/)
{{< app/cells/assistant language="csharp" >}}
