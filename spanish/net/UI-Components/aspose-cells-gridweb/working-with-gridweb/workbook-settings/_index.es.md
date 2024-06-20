---
title: Configuraciones para libro de trabajo
type: docs
weight: 250
url: /es/net/aspose-cells-gridweb/aspose-cells-gridweb/workbook-settings/
description: Este artículo describe la configuración del libro de trabajo en GridWeb.
keywords: GridWeb,configuración
---


Hay algunas configuraciones que podemos especificar mediante GridWorkbookSettings:


- [**GridWorkbookSettings**](https://reference.aspose.com/cells/net/aspose-cells-gridweb/aspose.cells.gridweb.data/GridWorkbookSettings)

|**Nombre** |**Descripción** |
| :- | :- |
|MaxIteration |Obtiene o establece el número máximo de iteraciones para resolver una referencia circular, el valor predeterminado es 100.
|Iteration | Obtiene o establece si se utiliza la iteración para resolver referencias circulares.
|ForceFullCalculate | Obtiene o establece si se calcula completamente cada vez que se desencadena un cálculo.
|CreateCalcChain | Obtiene o establece si se crea una cadena de fórmulas calculadas. El valor predeterminado es falso.
|ReCalculateOnOpen | Obtiene o establece si se vuelven a calcular todas las fórmulas al abrir el archivo.
|PrecisionAsDisplayed | Verdadero si los cálculos en este libro de trabajo se realizarán utilizando solo la precisión de los números tal como se muestran.
|Date1904 | Obtiene o establece un valor que representa si el libro de trabajo usa el sistema de fecha 1904.
|CheckCustomNumberFormat | Obtiene o establece si se comprueba el formato de número personalizado al configurar Style.Custom.
|Author | Obtiene y establece el autor del archivo.



Por ejemplo, el siguiente código establece ReCalculateOnOpen en falso para detener el cálculo al abrir el archivo:

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "GridWorkbookSettings-ReCalculateOnOpen.cs" >}}

 El siguiente código establece el autor para el archivo:

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "GridWorkbookSettings-Author.cs" >}}


