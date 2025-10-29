---
title: Использование класса ChartGlobalizationSettings для установки языка компонента диаграммы с Golang через C++
linktitle: Использование класса ChartGlobalizationSettings
description: Узнайте, как использовать класс ChartGlobalizationSettings в Aspose.Cells for C++ для задания разных языков для элементов графика. Наше руководство поможет вам понять, как локализовать элементы графика, метки и легенды на разные языки, чтобы представить ваши данные в культурно подходящей форме.
keywords: Aspose.Cells for C++, создание графиков, глобализация графиков, языки, локализация, ChartGlobalizationSettings, элементы, метки, легенды.
type: docs
weight: 2200
url: /ru/go-cpp/using-chartglobalizationsettings-class-to-set-different-language-for-chart-component/
---

## **Возможные сценарии использования**

API Aspose.Cells представило класс [**ChartGlobalizationSettings**](https://reference.aspose.com/cells/go-cpp/chartglobalizationsettings/), чтобы работать с ситуациями, когда пользователь хочет установить компонент диаграммы на другом языке. настраиваемые метки для промежуточных итогов в электронной таблице. 

## **Введение в класс ChartGlobalizationSettings**

Класс [**ChartGlobalizationSettings**](https://reference.aspose.com/cells/go-cpp/chartglobalizationsettings/) в настоящее время предлагает следующие 8 методов, которые можно переопределить в пользовательском классе для перевода таких элементов, как название оси, название единицы оси, название графика и так далее на разные языки.

1. [**GetAxisTitleName**](https://reference.aspose.com/cells/go-cpp/chartglobalizationsettings/getaxistitlename/): Получает название заголовка для оси.
1. [**GetAxisUnitName**](https://reference.aspose.com/cells/go-cpp/chartglobalizationsettings/getaxisunitname/): Получает название единицы оси.
1. [**GetChartTitleName**](https://reference.aspose.com/cells/go-cpp/chartglobalizationsettings/getcharttitlename/): Получает название заголовка диаграммы.
1. [**GetLegendDecreaseName**](https://reference.aspose.com/cells/go-cpp/chartglobalizationsettings/getlegenddecreasename/): Получает название уменьшения для легенды.
1. [**GetLegendIncreaseName**](https://reference.aspose.com/cells/go-cpp/chartglobalizationsettings/getlegendincreasename/): Получает название увеличения для легенды.
1. [**GetLegendTotalName**](https://reference.aspose.com/cells/go-cpp/chartglobalizationsettings/getlegendtotalname/): Получает название итога для легенды.
1. [**GetOtherName**](https://reference.aspose.com/cells/go-cpp/chartglobalizationsettings/getothername/): Получает название меток "Другие" для диаграммы.
1. [**GetSeriesName**](https://reference.aspose.com/cells/go-cpp/chartglobalizationsettings/getseriesname/): Получает название серии в диаграмме.

### **Пользовательский перевод языка**
Здесь мы создадим водопадную диаграмму на основе следующих данных. Названия компонентов диаграммы будут отображаться на английском языке. Мы воспользуемся турецким примером, чтобы показать, как отображать заголовок диаграммы, наименования увеличения/уменьшения в легенде, общее наименование и заголовок оси на турецком языке.

![todo:image_alt_text](sample.png)

## **Образец кода**
В следующем образце кода загружается [образец файла Excel](waterfall.xlsx).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ChartGlobalizationSettings.go" >}}
## Вывод, созданный образцовым кодом

Это вывод консоли вышеуказанного образца кода.

{{< highlight java >}}

Workbook chart title: Grafik Başlığı

Workbook chart legend: Artış

Workbook chart legend: Düşüş

Workbook chart legend: Toplam

Workbook category axis tile: Eksen Başlığı

{{< /highlight >}}
