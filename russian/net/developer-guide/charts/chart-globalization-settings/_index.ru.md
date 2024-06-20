---
title: Используя класс ChartGlobalizationSettings для установки другого языка для компонента диаграммы 
description: Узнайте, как использовать класс ChartGlobalizationSettings в Aspose.Cells for .NET, чтобы устанавливать разные языки для компонентов диаграммы. Наше руководство поможет вам понять, как локализовать элементы диаграммы, метки и легенды на разных языках, что позволит вам представить данные в культурно адекватном виде.
keywords: Aspose.Cells for .NET, построение диаграмм, глобализация диаграмм, языки, локализация, ChartGlobalizationSettings, элементы, метки, легенды.
type: docs
weight: 2200
url: /ru/net/using-chartglobalizationsettings-class-to-set-different-language-for-chart-component/
---

## **Возможные сценарии использования**

API Aspose.Cells представило класс [**ChartGlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/), чтобы работать с ситуациями, когда пользователь хочет установить компонент диаграммы на другом языке. настраиваемые метки для промежуточных итогов в электронной таблице. 

## **Введение в класс ChartGlobalizationSettings**

Класс [**ChartGlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/) в настоящее время предлагает следующие 8 методов, которые могут быть переопределены в пользовательском классе для перевода, такие как название оси, название единицы оси, название диаграммы и т. д. на другой язык.
1. [**GetAxisTitleName**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getaxistitlename/): Получает название заголовка для оси.
1. [**GetAxisUnitName**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getaxisunitname/): Получает название единицы оси.
1. [**GetChartTitleName**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getcharttitlename/): Получает название заголовка диаграммы.
1. [**GetLegendDecreaseName**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getlegenddecreasename/): Получает название уменьшения для легенды.
1. [**GetLegendIncreaseName**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getlegendincreasename/): Получает название увеличения для легенды.
1. [**GetLegendTotalName**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getlegendtotalname/): Получает название итога для легенды.
1. [**GetOtherName**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getothername/): Получает название меток "Другие" для диаграммы.
1. [**GetSeriesName**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getseriesname/): Получает название серии в диаграмме.

### **Пользовательский перевод языка**
Здесь мы создадим водопадную диаграмму на основе следующих данных. Названия компонентов диаграммы будут отображаться на английском языке. Мы воспользуемся турецким примером, чтобы показать, как отображать заголовок диаграммы, наименования увеличения/уменьшения в легенде, общее наименование и заголовок оси на турецком языке.

![todo:image_alt_text](sample.png)

## **Образец кода**
В следующем образце кода загружается [образец файла Excel](waterfall.xlsx).

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "chartglobalizationsettings.cs" >}}

## Вывод, созданный образцовым кодом

Это вывод консоли вышеуказанного образца кода.

{{< highlight java >}}

Workbook chart title: Grafik Başlığı

Workbook chart legend: Artış

Workbook chart legend: Düşüş

Workbook chart legend: Toplam

Workbook category axis tile: Eksen Başlığı

{{< /highlight >}}
