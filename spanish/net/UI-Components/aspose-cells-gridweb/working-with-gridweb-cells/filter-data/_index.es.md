---
title: Filtrar Datos
type: docs
weight: 80
url: /es/net/aspose-cells-gridweb/filter-data/
keywords: GridWeb, filtro, filtrar datos, filtrado de datos
description: Este artículo introduce cómo filtrar datos en GridWeb.
---

{{% alert color="primary" %}} 

Aspose.Cells.GridWeb proporciona funciones de autofiltrado y filtrado personalizado de datos. Estas características te permiten seleccionar solo aquellos elementos en una hoja de cálculo que deseas mostrar en una lista. Además, puedes filtrar elementos en una lista de acuerdo con criterios establecidos. Filtra texto, números o fechas con las características de filtrado.

{{% /alert %}} 
## **Trabajar con filtros**
Utiliza el método AddAutoFilter de la hoja de cálculo para habilitar el autofiltro para una hoja de cálculo. Este método acepta los índices de fila, columna de inicio y fin.

Para habilitar el filtro personalizado, utiliza el método AddCustomFilter de la hoja de cálculo que acepta el índice de fila al cual se debe aplicar el filtro y los criterios de filtrado personalizado.

El siguiente ejemplo implementa tanto autofiltros como filtros de datos personalizados. En el ejemplo, se habilita la función de autofiltro y se buscan filas filtradas basadas en algunos criterios.

**Entrada: la lista de datos en la primera hoja de cálculo** 

![todo:image_alt_text](filter-data_1.jpg)

**Salida: habilitar la función de autofiltro** 

![todo:image_alt_text](filter-data_2.jpg)
### **Autofiltro**
{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-SetAutoFilter.aspx-SetAutoFilter.cs" >}}
### **Filtro de Datos Personalizado**
**Datos filtrados personalizados basados en los criterios** 

![todo:image_alt_text](filter-data_3.jpg)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-SetCustomFilter.aspx-SetCustomFilter.cs" >}}
