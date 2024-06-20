---
title: Calcular Factor de Escala de Configuración de Página
type: docs
weight: 300
url: /es/net/calculate-page-setup-scaling-factor/
description: Este artículo proporciona un código de ejemplo que explica cómo usar la API de C# o la biblioteca .NET para calcular el factor de escala de configuración de página utilizando la opción Ajustar a n página(s) de ancho por m de alto de forma programática en una hoja de cálculo de Excel.
keywords: Ajustar a n páginas de ancho por m de alto en Excel con C#, calcular factor de escala de configuración de página con C#
---

{{% alert color="primary" %}}

Cuando se establece la Escala de Configuración de Página usando la opción **Ajustar a n página(s) de ancho por m de alto**, Microsoft Excel calcula el Factor de Escala de Configuración de Página. Puedes calcular lo mismo utilizando la propiedad [**SheetRender.PageScale**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender/properties/pagescale). Esta propiedad devuelve un valor double que se puede convertir a un valor porcentual. Por ejemplo, si devuelve 0.5, significa que el factor de escala es del 50%.

{{% /alert %}}

El siguiente código de ejemplo ilustra cómo calcular el factor de escala de configuración de página utilizando la propiedad [**SheetRender.PageScale**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender/properties/pagescale).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-CalculateScalingFactor-CalculatePageSetupScalingFactor.cs" >}}
