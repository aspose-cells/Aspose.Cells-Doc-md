---
title: Calcular Factor de Escala de Configuración de Página
type: docs
weight: 260
url: /es/java/calculate-page-setup-scaling-factor/
---

{{% alert color="primary" %}} 

Cuando estableces el Escalado de la Configuración de Página usando la opción **Ajustar a n página(s) de ancho por m alto**, Microsoft Excel calcula el Factor de Escalado de la Configuración de Página. Puedes calcular lo mismo usando la propiedad [SheetRender.getPageScale()](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender#PageScale). Esta propiedad retorna un valor doble que puede convertirse a un valor porcentual. Por ejemplo, si retorna 0.5079621076, significa que el factor de escalado es del 51%.

{{% /alert %}} 
## **Calcular Factor de Escalado de la Configuración de Página**
El siguiente código de muestra ilustra cómo calcular el factor de escalado de la configuración de página usando la propiedad [SheetRender.getPageScale()](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender#PageScale).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CalculatePageSetupScalingFactor-CalculatePageSetupScalingFactor.java" >}}
## **Salida de la consola**
Aquí está la salida en consola del código de muestra anterior.

{{< highlight java >}}

 0.5079621076583862

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
