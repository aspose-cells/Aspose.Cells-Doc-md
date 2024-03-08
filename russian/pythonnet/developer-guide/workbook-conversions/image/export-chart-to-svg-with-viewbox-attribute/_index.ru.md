---
title: Экспортировать диаграмму в номер SVG с атрибутом viewBox.
type: docs
weight: 280
url: /ru/python-net/export-chart-to-svg-with-viewbox-attribute/
description: Экспортируйте диаграмму в SVG с атрибутом viewBox, используя Aspose.Cells for Python via .NET API.
keywords: Python Export Chart to SVG with viewBox attribute, Export Chart to SVG with viewBox attribute in Python via NET, Python Convert Chart to SVG with viewBox attribute.
---
{{% alert color="primary" %}}

 По умолчанию, когда диаграмма экспортируется в формат SVG,**ViewBox** Атрибут не включен в его XML. Однако Aspose.Cells for Python via .NET обеспечивает[**ImageOrPrintOptions.svg_fit_to_view_port**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/svg_fit_to_view_port/) свойство, которое при установке на**истинный** экспортирует диаграмму в номер SVG с атрибутом viewBox.

{{% /alert %}}

##  Экспортировать диаграмму в номер SVG с атрибутом viewBox.

Следующий пример кода экспортирует диаграмму в формат SVG с атрибутом viewBox.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-ExportChartToSvgWithViewBox.py" >}}

{{% alert color="primary" %}}

 Если вы откроете номер диаграммы SVG в блокноте, вы увидите**ViewBox** атрибут, подобный этому.

{{< highlight "java" >}}

 <svg xmlns="http://www.w3.org/2000/svg"

     xmlns:xlink="http://www.w3.org/1999/xlink"

     width="100%" height="100%"

     viewBox="0 0 480 288">

{{< /highlight >}}

{{% /alert %}}
