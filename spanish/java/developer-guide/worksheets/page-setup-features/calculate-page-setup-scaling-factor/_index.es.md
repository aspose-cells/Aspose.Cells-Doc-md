---
title: Calcular factor de escala de configuración de página
type: docs
weight: 260
url: /es/java/calculate-page-setup-scaling-factor/
---
{{% alert color="primary" %}} 

Cuando configura Ajuste de escala de página usando**Ajustar a n página(s) de ancho por m de alto** opción, Microsoft Excel calcula el factor de escala de configuración de página. Puedes calcular lo mismo usando[SheetRender.getPageScale()](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender#PageScale) propiedad. Esta propiedad devuelve un valor doble que se puede convertir en un valor porcentual. Por ejemplo, si devuelve 0,5079621076, significa que el factor de escala es del 51 %.

{{% /alert %}} 
## **Calcular factor de escala de configuración de página**
 El siguiente código de muestra ilustra cómo calcular el factor de escala de la configuración de la página usando[SheetRender.getPageScale()](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender#PageScale)propiedad.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CalculatePageSetupScalingFactor-CalculatePageSetupScalingFactor.java" >}}
## **Salida de consola**
Aquí está la salida de la consola del código de muestra anterior.

{{< highlight "java" >}}

 0.5079621076583862

{{< /highlight >}}
