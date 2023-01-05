---
title: Filtrar datos
type: docs
weight: 80
url: /es/net/filter-data/
---
{{% alert color="primary" %}} 

Aspose.Cells.GridWeb proporciona funciones de filtro automático y filtro de datos personalizado. Estas características le brindan una manera de seleccionar solo aquellos elementos en una hoja de trabajo que desea mostrar en una lista. Además, puede filtrar elementos en una lista de acuerdo con criterios establecidos. Filtre texto, números o fechas con las funciones de filtrado.

{{% /alert %}} 
## **Trabajar con filtros**
Utilice el método AddAutoFilter de la hoja de trabajo para habilitar el filtro automático para una hoja de trabajo. Este método acepta los índices de fila, inicio y final de columna.

Para habilitar el filtro personalizado, use el método AddCustomFilter de la hoja de trabajo que acepta el índice de fila al que se debe aplicar el filtro y los criterios de filtrado personalizados.

El siguiente ejemplo implementa filtros de datos automáticos y personalizados. En el ejemplo, la función de filtro automático está habilitada y las filas filtradas se buscan según algunos criterios.

**Entrada: la lista de datos en la primera hoja de trabajo** 

![todo:imagen_alternativa_texto](filter-data_1.jpg)

**Salida: habilitar la función de filtro automático** 

![todo:imagen_alternativa_texto](filter-data_2.jpg)
### **Auto-filtro**
{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-SetAutoFilter.aspx-SetAutoFilter.cs" >}}
### **Filtro de datos personalizado**
**Datos filtrados personalizados basados en los criterios** 

![todo:imagen_alternativa_texto](filter-data_3.jpg)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-SetCustomFilter.aspx-SetCustomFilter.cs" >}}
