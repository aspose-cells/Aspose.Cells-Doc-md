---
title:  Использование класса ChartGlobalizationSettings для установки другого языка для компонента диаграммы
description: Узнайте, как использовать класс ChartGlobalizationSettings в Aspose.Cells for .NET, чтобы установить разные языки для компонентов диаграммы. Наше руководство поможет вам понять, как локализовать элементы диаграммы, метки и легенды на разных языках, что позволит вам представить данные в культурно приемлемом виде.
keywords: Aspose.Cells for .NET, charting, chart globalization, languages, localization, ChartGlobalizationSettings, elements, labels, legends.
type: docs
weight: 2200
url: /ru/net/using-chartglobalizationsettings-class-to-set-different-language-for-chart-component/
---
##  **Возможные сценарии использования**

 Aspose.Cells API раскрыли[**Настройки глобализации диаграммы**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/) класс, чтобы справиться со сценариями, когда пользователь желает установить для компонента диаграммы другой язык. пользовательские метки для промежуточных итогов в электронной таблице.

##  **Введение в класс ChartGlobalizationSettings**

[**Настройки глобализации диаграммы**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/)В настоящее время класс предлагает следующие 8 методов, которые можно переопределить в пользовательском классе для перевода, например, имени AxisTitle, имени AxisUnit, имени ChartTitle и т. д. на другой язык.
1. [**GetAxisTitleName**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getaxistitlename/): получает имя Title для оси.
1. [**GetAxisUnitName**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getaxisunitname/): получает имя устройства оси.
1. [**GetChartTitleName**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getcharttitlename/): получает имя заголовка диаграммы.
1. [**GetLegendDecreaseName**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getlegenddecreasename/): получает имя Decrease for Legend.
1. [**GetLegendIncreaseName**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getlegendincreasename/): получает имя увеличения для легенды.
1. [**GetLegendTotalName**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getlegendtotalname/): получает имя Total для Legend.
1. [**GetOtherName**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getothername/): получает имя метки «Другие» для диаграммы.
1. [**Получить имя серии**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getseriesname/): получает имя серии в диаграмме.

###  **Индивидуальный языковой перевод**
Здесь мы создадим каскадную диаграмму на основе следующих данных. Названия компонентов диаграммы будут отображаться на диаграмме на английском языке. Мы будем использовать пример на турецком языке, чтобы показать, как отображать заголовок диаграммы, имена увеличения/уменьшения легенды, общее имя и заголовок оси на турецком языке.

![задача: image_alt_text](sample.png)

##  **Образец кода**
 Следующий пример кода загружает[образец файла Excel](waterfall.xlsx).

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "chartglobalizationsettings.cs" >}}

##  Вывод, сгенерированный примером кода

Это консольный вывод приведенного выше примера кода.

{{< highlight "java" >}}

Workbook chart title: Grafik Başlığı

Workbook chart legend: Artış

Workbook chart legend: Düşüş

Workbook chart legend: Toplam

Workbook category axis tile: Eksen Başlığı

{{< /highlight >}}
