---
title: Диаграмма в изображение
description: Узнайте, как использовать Aspose.Cells for .NET для преобразования диаграммы в графический формат, такой как JPEG или PNG. Наш руководство продемонстрирует, как экспортировать диаграмму из Microsoft Excel и сохранить её как самостоятельное изображение для дальнейшего использования и обработки.
keywords: Aspose.Cells for .NET, Диаграмма в изображение, Microsoft Excel, Преобразование изображения, Экспорт, Самостоятельное изображение.
linktitle: Диаграмма в изображение
type: docs
weight: 46
url: /ru/net/chart-to-image/
---

## **Диаграммы отображения**

API Aspose.Cells поддерживает преобразование диаграмм Excel в графические форматы без необходимости дополнительных инструментов или приложений. Для предоставления поддержки рендеринга класс [**Chart**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart) предоставляет методы [**ToImage**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/toimage/index) с различными перегрузками, чтобы оптимально подходить для требований приложения.

### **Отображение диаграмм в изображения**

Метод [**Chart.ToImage**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/toimage/index) имеет различные перегрузки для поддержки простого и расширенного рендеринга. Если требуется отобразить диаграмму в её стандартных размерах, мы предлагаем использовать метод [**Chart.ToImage**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/toimage/index), как показано ниже.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ChartRendering-ChartRenderingChartToImage.cs" >}}

Также возможно отображать диаграммы в изображения с расширенными настройками. API Aspose.Cells предоставляет перегрузку метода [**Chart.ToImage**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/toimage/index), который может принимать экземпляр [**ImageOrPrintOptions**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions), позволяя при этом указывать параметры, такие как разрешение, режим сглаживания, формат изображения и так далее.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ChartRendering-ChartRenderingChartToImageWithAdvancedOptions.cs" >}}

## **Поддерживаемые типы диаграмм для отображения**

Существует несколько видов диаграмм, которые в настоящее время не поддерживаются для рендеринга. Такие виды диаграмм содержат **N** в столбце **Поддерживаемые** в таблице ниже.

|Тип диаграммы|Подтип диаграммы|Поддерживается|
| :- | :- | :- |
|**Column**|Column|**Y**|
| |ColumnStacked|**Y**|
| |Column100PercentStacked|**Y**|
| |Column3DClustered|**Y**|
| |Column3DStacked|**Y**|
| |Column3D100PercentStacked|**Y**|
| |Column3D|**Y**|
|**Bar**|Bar|**Y**|
| |BarStacked|**Y**|
| |Bar100PercentStacked|**Y**|
| |Bar3DClustered|**Y**|
| |Bar3DStacked|**Y**|
| |Bar3D100PercentStacked|**Y**|
|**Line**|Line|**Y**|
| |LineStacked|**Y**|
| |Line100PercentStacked|**Y**|
| |LineWithDataMarkers|**Y**|
| |LineStackedWithDataMarkers|**Y**|
| |Line100PercentStackedWithDataMarkers|**Y**|
| |Line3D|**Y**|
|**Pie**|Pie|**Y**|
| |Pie3D|**Y**|
| |PiePie|**Y**|
| |PieExploded|**Y**|
| |Pie3DExploded|**Y**|
| |PieBar|**Y**|
|**Scatter**|Scatter|**Y**|
| |ScatterConnectedByCurvesWithDataMarker|**Y**|
| |ScatterConnectedByCurvesWithoutDataMarker|**Y**|
| |ScatterConnectedByLinesWithDataMarker|**Y**|
| |ScatterConnectedByLinesWithoutDataMarker|**Y**|
|**Area**|Area|**Y**|
| |AreaStacked|**Y**|
| |Area100PercentStacked|**Y**|
| |Area3D|**Y**|
| |Area3DStacked|**Y**|
| |Area3D100PercentStacked|**Y**|
|**Doughnut**|Doughnut|**Y**|
| |DoughnutExploded|**Y**|
|**Radar**|Radar|**Y**|
| |RadarWithDataMarkers|**Y**|
| |RadarFilled|**Y**|
|**Surface**|Surface3D|N|
| |SurfaceWireframe3D|N|
| |SurfaceContour|N|
| |SurfaceContourWireframe|N|
|**Bubble**|Bubble|**Y**|
| |Bubble3D|N|
|**Stock**|StockHighLowClose|**Y**|
| |StockOpenHighLowClose|**Y**|
| |StockVolumeHighLowClose|**Y**|
| |StockVolumeOpenHighLowClose|**Y**|
|**Cylinder**|Cylinder|**Y**|
| |CylinderStacked|**Y**|
| |Cylinder100PercentStacked|**Y**|
| |CylindricalBar|**Y**|
| |CylindricalBarStacked|**Y**|
| |CylindricalBar100PercentStacked|**Y**|
| |CylindricalColumn3D|**Y**|
|**Cone**|Cone|**Y**|
| |ConeStacked|**Y**|
| |Cone100PercentStacked|**Y**|
| |ConicalBar|**Y**|
| |ConicalBarStacked|**Y**|
| |ConicalBar100PercentStacked|**Y**|
| |ConicalColumn3D|**Y**|
|**Pyramid**|Pyramid|**Y**|
| |PyramidStacked|**Y**|
| |Pyramid100PercentStacked|**Y**|
| |PyramidBar|**Y**|
| |PyramidBarStacked|**Y**|
| |PyramidBar100PercentStacked|**Y**|
| |PyramidColumn3D|**Y**|
|**BoxWhisker**|BoxWhisker|Y|
|**Funnel**|Funnel|**Y**|
|**ParetoLine**|ParetoLine|**Y**|
|**Sunburst**|Sunburst|**Y**|
|**Treemap**|Treemap|**Y**|
|**Waterfall**|Waterfall|**Y**|
|**Histogram**|Histogram|Y|
|**Map**|Map|**N**|

{{% alert color="primary" %}}

В случае попытки отобразить не поддерживаемые типы диаграмм в изображения или PDF, можно получить изображения нулевого размера или пустой PDF.

{{% /alert %}}

## **Продвинутые темы**
- [Преобразовать диаграмму в PDF](/cells/ru/net/chart-to-pdf/)
{{< app/cells/assistant language="csharp" >}}
