---
title: Configuraciones para el libro de trabajo
type: docs
weight: 250
url: /es/net/aspose-cells-gridweb/workbook-settings/
description: Este artículo describe la configuración del libro de trabajo para GridWeb.
keywords: settings
---
Hay algunas configuraciones que podemos especificar mediante set GridWorkbookSettings:

 
- **[Configuración de GridWorkbook](https://reference.aspose.com/cells/net/aspose.cells.gridweb.data/GridWorkbookSettings)**

|**Nombre** |**Descripción** |
|:- |:- |
| iteración máxima| Obtiene o establece el número máximo de iteraciones para resolver una referencia circular; el valor predeterminado es 100.|
| Iteración| Obtiene o establece si se usa la iteración para resolver las referencias circulares.|
| ForceFullCalculate| Obtiene o establece si se calcula completamente cada vez que se desencadena un cálculo.|
| CreateCalcChain|Obtiene o establece si se crea una cadena de fórmulas calculadas. El valor predeterminado es falso.|
| Recalcular al abrir| Obtiene o establece si se vuelven a calcular todas las fórmulas al abrir el archivo.|
| Precisión como se muestra| True si los cálculos en este libro de trabajo se realizarán usando solo la precisión de los números tal como se muestran|
| Fecha1904| Obtiene o establece un valor que representa si el libro usa el sistema de fechas de 1904.|
| Comprobar formato de número personalizado| Obtiene o establece si se comprueba el formato de número personalizado al configurar Style.Custom.|
| Autor| Obtiene y establece el autor del archivo.|
 


Por ejemplo, el siguiente código establece ReCalculateOnOpen en falso para detener el cálculo al abrir el archivo:

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "GridWorkbookSettings-ReCalculateOnOpen.cs" >}}

 el siguiente código establece el autor del archivo:

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "GridWorkbookSettings-Author.cs" >}}
 
 