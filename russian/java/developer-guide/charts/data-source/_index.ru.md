---
title: Форматирование данных в диаграммах
linktitle: Источник данных
type: docs
weight: 50
url: /ru/java/data-formatting-in-charts/
---

{{% alert color="primary" %}}

В предыдущих темах мы уже предоставили множество примеров для демонстрации того, как можно установить источник данных для вашего графика, но в этой теме мы собираемся предоставить более подробную информацию о типах данных, которые можно установить для графика.

{{% /alert %}}

## **Установка данных графика**

При работе с графиками с использованием Aspose.Cells есть два типа данных, с которыми нужно работать, следующие:

- [Данные диаграммы](/cells/ru/java/data-formatting-in-charts/#chart-data).
- [Данные категории](/cells/ru/java/data-formatting-in-charts/#category-data).

### **Данные графика**

Данные диаграммы - это данные, которые мы используем в качестве источника данных для создания графиков. Мы можем добавить диапазон ячеек (содержащий данные диаграммы), вызвав метод [**Add**](https://reference.aspose.com/cells/java/com.aspose.cells/seriescollection#add-java.lang.Object-) объекта [**SeriesCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-SettingChartsData-SettingChartsData.java" >}}

### **Данные категорий**

Данные категории используются для маркировки данных диаграммы и могут быть добавлены к [**SeriesCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection) с помощью его метода [**setCategoryData**](https://reference.aspose.com/cells/java/com.aspose.cells/seriescollection#CategoryData).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-SettingCategoryData-SettingCategoryData.java" >}}

**Столбчатая диаграмма с данными диаграммы и категории** 

![todo:image_alt_text](data-formatting-in-charts_1.png)

## **Продвинутые темы**
- [Создание динамических диаграмм](/cells/ru/java/create-dynamic-charts/)
- [Простой способ настройки диаграммы с использованием метода Chart.setChartDataRange](/cells/ru/java/easy-way-for-chart-setup-using-chart-setchartdatarange-method/)
- [Найдите тип значений X и Y точек в серии графика](/cells/ru/java/find-type-of-x-and-y-values-of-points-in-chart-series/)
- [Установить код формата значений серии графика](/cells/ru/java/set-the-values-format-code-of-chart-series/)
{{< app/cells/assistant language="java" >}}
