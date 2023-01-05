---
title: Calcular factor de escala de configuración de página
type: docs
weight: 300
url: /es/net/calculate-page-setup-scaling-factor/
---
{{% alert color="primary" %}}

Cuando configura Ajuste de escala de página usando**Ajustar a n página(s) de ancho por m de alto** opción, Microsoft Excel calcula el factor de escala de configuración de página. Puedes calcular lo mismo usando[**SheetRender.PageScale**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender/properties/pagescale) propiedad. Esta propiedad devuelve un valor doble que se puede convertir en un valor porcentual. Por ejemplo, si devuelve 0,5, significa que el factor de escala es del 50 %.

{{% /alert %}}

 El siguiente código de muestra ilustra cómo calcular el factor de escala de la configuración de la página usando[**SheetRender.PageScale**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender/properties/pagescale) propiedad.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-CalculateScalingFactor-CalculatePageSetupScalingFactor.cs" >}}
