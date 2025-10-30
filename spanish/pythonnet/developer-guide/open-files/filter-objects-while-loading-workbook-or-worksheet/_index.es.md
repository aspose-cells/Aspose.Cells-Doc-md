---
title: Filtrar objetos al cargar el libro o la hoja de trabajo
type: docs
weight: 330
url: /es/python-net/filter-objects-while-loading-workbook-or-worksheet/
---

## **Escenarios de uso posibles**
Usa la propiedad [LoadOptions.load_filter](https://reference.aspose.com/cells/python-net/aspose.cells/loadoptions/load_filter) al filtrar datos del libro. Pero si quieres filtrar datos de hojas individuales, tendrás que sobrescribir el método [LoadFilter.start_sheet](https://reference.aspose.com/cells/python-net/aspose.cells/loadfilter/start_sheet). Proporciónale un valor apropiado del enumerado [LoadDataFilterOptions](https://reference.aspose.com/cells/python-net/aspose.cells/loaddatafilteroptions) al crear o trabajar con [LoadFilter](https://reference.aspose.com/cells/python-net/aspose.cells/loadfilter).

El enumerado [LoadDataFilterOptions](https://reference.aspose.com/cells/python-net/aspose.cells/loaddatafilteroptions) tiene los siguientes valores posibles.

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
## **Objetos de Filtro al cargar el Libro**
El siguiente código de ejemplo ilustra cómo filtrar gráficos del libro. Por favor, revise el [archivo de Excel de ejemplo](5115258.xlsx) utilizado en este código y el [PDF de salida](5115257.pdf) generado por él. Como se puede ver en el PDF de salida, todos los gráficos han sido filtrados fuera del libro.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-FilteringObjectsAtLoadTime-FilteringObjects.py" >}}

{{< app/cells/assistant language="python-net" >}}
