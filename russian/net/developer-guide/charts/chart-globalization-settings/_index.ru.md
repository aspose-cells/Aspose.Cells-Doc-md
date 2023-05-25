---
title:  Использование класса ChartGlobalizationSettings для установки другого языка для компонента диаграммы
type: docs
weight: 2200
url: /ru/net/using-chartglobalizationsettings-class-to-set-different-language-for-chart-component/
---
##  **Возможные сценарии использования**

 Aspose.Cells API-интерфейсы раскрыли[**ChartGlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/) класс, чтобы иметь дело со сценариями, когда пользователь хочет установить компонент диаграммы на другой язык. настраиваемые метки для промежуточных итогов в электронной таблице.

##  **Введение в класс ChartGlobalizationSettings**

[**ChartGlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/)В настоящее время класс предлагает следующие 8 методов, которые можно переопределить в пользовательском классе для перевода, таких как имя AxisTitle, имя AxisUnit, имя ChartTitle и т. д., на другой язык.
1. [**GetAxisTitleName**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getaxistitlename/): получает имя заголовка для оси.
1. [**GetAxisUnitName**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getaxisunitname/): получает имя блока оси.
1. [**GetChartTitleName**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getcharttitlename/): получает имя заголовка диаграммы.
1. [**GetLegendDecreaseName**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getlegenddecreasename/): Получает имя Decrease для Legend.
1. [**GetLegendIncreaseName**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getlegendincreasename/): Получает имя увеличения для Легенды.
1. [**GetLegendTotalName**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getlegendtotalname/): получает имя Total для Legend.
1. [**GetOtherName**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getothername/): получает имя метки «Другие» для диаграммы.
1. [**GetSeriesName**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getseriesname/): получает имя серии на диаграмме.

###  **Пользовательский языковой перевод**
Здесь мы создадим каскадную диаграмму на основе следующих данных. Имена компонентов диаграммы будут отображаться на диаграмме на английском языке. Мы будем использовать пример турецкого языка, чтобы показать, как отображать заголовок диаграммы, имена увеличения/уменьшения легенды, общее имя и название оси на турецком языке.

![дело:image_alt_text](sample.png)

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
