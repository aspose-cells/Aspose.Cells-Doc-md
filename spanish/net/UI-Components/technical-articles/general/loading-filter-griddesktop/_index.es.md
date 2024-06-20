---
title: Filtrar objetos al cargar el libro de trabajo en GridDesktop
type: docs
weight: 1060
url: /es/net/aspose-cells-griddesktop/loading-filter
description: Este artículo describe cómo usar el filtro de carga en GridDesktop.
keywords: GridDesktop,loading,loading filter,filter
---

## **Escenarios de uso posibles**
Por favor, utilice la propiedad [GridDesktop.LoadDataFilter](https://reference.aspose.com/cells/net/aspose.cells.griddesktop/griddesktop/properties/loaddatafilter) al filtrar datos del libro de trabajo.

La enumeración [GridLoadDataFilterOptions](https://reference.aspose.com/cells/net/aspose.cells.griddesktop.data/gridloaddatafilteroptions) tiene los siguientes valores.
- Todo
- Configuraciones del libro
- Celda en blanco
- Celda booleana
- Datos de celda
- Error de celda
- Numérico de celda
- Cadena de celda
- Valor de celda
- Chart
- Formato condicional
- Validación de datos
- Nombres definidos
- Propiedades del documento
- Fórmula
- Hipervínculos
- Área fusionada
- Tabla Dinámica
- Configuración
- Forma
- Datos de Hoja
- Configuraciones de Hoja
- Estructura
- Estilo
- Tabla
- VBA
- MapaXml
## **Filtrar datos al cargar el libro de trabajo**
El siguiente código de muestra ilustra cómo filtrar dibujos del libro. Por favor, verifique el [archivo de Excel de muestra](5472489.xlsx). Como puede ver, todos los gráficos/formas/ imágenes han sido filtrados del libro.
![libro sin imagen](nodrawing.png)
### **Código de muestra**
{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "LoadingFilter.cs" >}}

