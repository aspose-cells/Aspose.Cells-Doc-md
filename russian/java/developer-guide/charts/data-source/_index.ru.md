---
title: Форматирование данных в диаграммах
linktitle: Источник данных
type: docs
weight: 50
url: /ru/java/data-formatting-in-charts/
---
{{% alert color="primary" %}}

В наших предыдущих темах мы уже предоставили множество примеров, чтобы продемонстрировать, как вы можете установить источник данных для своей диаграммы, но в этой теме мы собираемся предоставить более подробную информацию о типах данных, которые можно установить для диаграммы.

{{% /alert %}}

## **Настройка данных диаграммы**

При работе с диаграммами с использованием Aspose.Cells необходимо иметь дело с двумя типами данных:

- [Данные диаграммы](/cells/ru/java/data-formatting-in-charts/#chart-data).
- [Данные категории](/cells/ru/java/data-formatting-in-charts/#category-data).

### **Данные диаграммы**

 Данные диаграммы — это данные, которые мы используем в качестве источника данных для построения наших диаграмм. Мы можем добавить диапазон ячеек (содержащих данные диаграммы), вызвав метод[**СерияКоллекция**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection) объекты[**Добавлять**](https://reference.aspose.com/cells/java/com.aspose.cells/seriescollection#add(java.lang.Object)) метод.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-SettingChartsData-SettingChartsData.java" >}}

### **Данные категории**

 Данные категории используются для маркировки данных диаграммы и могут быть добавлены в[**СерияКоллекция**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection) с помощью своего[**setCategoryData**](https://reference.aspose.com/cells/java/com.aspose.cells/seriescollection#CategoryData)метод.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-SettingCategoryData-SettingCategoryData.java" >}}

**Столбчатая диаграмма с данными диаграммы и категории** 

![дело:изображение_альтернативный_текст](data-formatting-in-charts_1.png)

## **Предварительные темы**
- [Создание динамических диаграмм](/cells/ru/java/create-dynamic-charts/)
- [Простой способ настройки диаграммы с использованием метода Chart.setChartDataRange](/cells/ru/java/easy-way-for-chart-setup-using-chart-setchartdatarange-method/)
- [Найдите тип значений X и Y точек в серии диаграмм](/cells/ru/java/find-type-of-x-and-y-values-of-points-in-chart-series/)
- [Установите код формата значений серии диаграммы](/cells/ru/java/set-the-values-format-code-of-chart-series/)
