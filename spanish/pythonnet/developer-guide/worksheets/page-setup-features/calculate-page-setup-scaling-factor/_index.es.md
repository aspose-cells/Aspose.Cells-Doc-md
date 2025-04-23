---
title: Calcular Factor de Escala de Configuración de Página
type: docs
weight: 300
url: /es/python-net/calculate-page-setup-scaling-factor/
description: Este artículo proporciona código de ejemplo que explica cómo usar las APIs de Aspose.Cells para Python via .NET para calcular el factor de escala del Configuración de Página usando la opción Ajustar a n páginas de ancho por m de alto de la hoja de Excel.
keywords: Biblioteca de Excel para Python, Ajustar a n páginas de ancho por m de alto en Python, calcular el factor de escala de la configuración de página en Python.
---

{{% alert color="primary" %}}

Cuando se establece la Escala de Configuración de Página usando la opción **Ajustar a n página(s) de ancho por m de alto**, Microsoft Excel calcula el Factor de Escala de Configuración de Página. Puedes calcular lo mismo utilizando la propiedad [**SheetRender.page_scale**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender/page_scale). Esta propiedad devuelve un valor double que se puede convertir a un valor porcentual. Por ejemplo, si devuelve 0.5, significa que el factor de escala es del 50%.

{{% /alert %}}

El siguiente código de ejemplo ilustra cómo calcular el factor de escala de configuración de página utilizando la propiedad [**SheetRender.page_scale**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender/page_scale).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-CalculateScalingFactor-CalculatePageSetupScalingFactor.py" >}}
