---
title: Отображение диапазона ячеек в качестве меток данных
type: docs
weight: 110
url: /ru/java/showing-cell-range-as-the-data-labels/
---

## Показать диапазон ячеек в качестве меток данных в MS Excel

В Microsoft Excel 2013 можно отобразить диапазон ячеек в качестве меток данных. Этот вариант можно выбрать, следуя этим шагам

- Выберите Метки данных ряда и щелкните правой кнопкой мыши, чтобы открыть контекстное меню.
- Нажмите **Формат меток данных...**, и это покажет **Параметры меток**.
- Установите или снимите флажок **Метка содержит - Значение из ячеек**.

### **Флажок для отображения диапазона ячеек в качестве меток данных**

На следующем скриншоте выделено этот вариант для вашего справочного пособия.

![todo:image_alt_text](showing-cell-range-as-the-data-labels_1.png)

## Отображение диапазона ячеек в качестве меток данных с Aspose.Cells

Aspose.Cells предоставляет метод [**DataLabels.setShowCellRange()**](https://reference.aspose.com/cells/java/com.aspose.cells/datalabels#ShowCellRange) для установки или снятия флажка **Метка содержит - Значение из ячеек**, как показано на скриншоте выше.

## Код Java для отображения диапазона ячеек в качестве меток данных

Нижеприведенный образец кода получает доступ к меткам данных диаграммы и устанавливает метод [**DataLabels.setShowCellRange()**](https://reference.aspose.com/cells/java/com.aspose.cells/datalabels#ShowCellRange) в true, чтобы выбрать параметр **Метка содержит - Значение из ячеек**.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ShowCellRangeAsTheDataLabels-ShowCellRangeAsTheDataLabels.java" >}}
