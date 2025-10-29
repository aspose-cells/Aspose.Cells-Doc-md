---
title: Установка источника данных для диаграммы с Golang через C++
linktitle: Источник данных
type: docs
weight: 10
url: /ru/go-cpp/data-formatting-in-charts/
description: Узнайте о различных поддерживаемых источниках данных в Aspose.Cells for C++. Наш гид проведет вас по различным типам источников данных и покажет, как подключаться к ним и получать данные для заполнения ваших листов.
keywords: Aspose.Cells for C++, построение графиков, форматирование данных, метки, цвета, шрифты, внешний вид, удобство.
---

В наших предыдущих темах мы уже предоставили много примеров, показывающих, как установить источник данных для вашего графика. В этой теме мы предоставим больше деталей о типах данных, которые могут быть установлены для графика.

## **Установка данных графика**

При работе с графиками с использованием Aspose.Cells есть два типа данных, с которыми нужно работать, следующие:

- Данные графика.
- Данные категорий.

### **Данные графика**

Данные графика - это данные, которые мы используем в качестве источника данных для построения наших графиков. Мы можем добавить диапазон ячеек (содержащих данные графика), вызвав метод [**Add**](https://reference.aspose.com/cells/go-cpp/seriescollection/add/) объекта [**SeriesCollection**](https://reference.aspose.com/cells/go-cpp/seriescollection/).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DataSource.go" >}}
### **Данные категорий**

Данные категорий используются для маркировки данных графика и могут быть добавлены к [**SeriesCollection**](https://reference.aspose.com/cells/go-cpp/seriescollection/) с использованием его свойства [**GetCategoryData()**](https://reference.aspose.com/cells/go-cpp/seriescollection/getcategorydata/). Приведен ниже полный пример для демонстрации использования данных графика и категорий. После выполнения приведенного выше примера кода на лист будет добавлена столбчатая диаграмма, как показано ниже.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DataSource-1.go" >}}
## **Дополнительные темы**
- [Изменение источника данных диаграммы на целевой лист при копировании строк или диапазона](/cells/ru/cpp/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/)
- [Создание динамических диаграмм](/cells/ru/cpp/create-dynamic-charts/)
- [Простой способ настройки диаграммы с использованием метода Chart.SetChartDataRange](/cells/ru/cpp/easy-way-for-chart-setup-using-chart-setchartdatarange-method/)
- [Найдите тип значений X и Y точек в серии графика](/cells/ru/cpp/find-type-of-x-and-y-values-of-points-in-chart-series/)
