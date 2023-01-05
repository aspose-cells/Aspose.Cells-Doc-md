---
title: Filtrar objetos al cargar el libro de trabajo o la hoja de trabajo
type: docs
weight: 1060
url: /es/java/filter-objects-while-loading-workbook-or-worksheet/
---
## **Posibles escenarios de uso**
 Por favor use[LoadOptions.LoadFilter](https://reference.aspose.com/cells/java/com.aspose.cells/loadoptions#LoadFilter) propiedad al filtrar datos del libro de trabajo. Pero si desea filtrar datos de hojas de trabajo individuales, tendrá que anular[LoadFilter.startSheet](https://reference.aspose.com/cells/java/com.aspose.cells/loadfilter#startSheet\(com.aspose.cells.Worksheet\) ) método. Proporcione el valor apropiado de la[LoadDataFilterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/LoadDataFilterOptions) enumeración al crear o trabajar con[Cargarfiltro](https://reference.aspose.com/cells/java/com.aspose.cells/loadfilter).

 Él[LoadDataFilterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/LoadDataFilterOptions)enumeración tiene los siguientes valores.

- [NINGUNO](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#NONE)
- [TODOS](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#ALL)
- [CELL_BLANK](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CELL_BLANK)
- [CELL_STRING](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CELL_STRING)
- [CELL_NUMERIC](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CELL_NUMERIC)
- [CELL_ERROR](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CELL_ERROR)
- [CELL_BOOL](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CELL_BOOL)
- [CELL_VALUE](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CELL_VALUE)
- [FÓRMULA](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#FORMULA)
- [DATOS_CELULARES](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CELL_DATA)
- [GRÁFICO](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CHART)
- [FORMA](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#SHAPE)
- [MERGED_AREA](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#MERGED_AREA)
- [FORMATO CONDICIONAL](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CONDITIONAL_FORMATTING)
- [VALIDACIÓN DE DATOS](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#DATA_VALIDATION)
- [TABLA DINÁMICA](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#PIVOT_TABLE)
- [MESA](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#TABLE)
- [HIPERVÍNCULOS](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#HYPERLINKS)
- [HOJA_AJUSTES](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#SHEET_SETTINGS)
- [HOJA_DATOS](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#SHEET_DATA)
- [CONFIGURACIÓN_LIBRO](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#BOOK_SETTINGS)
- [AJUSTES](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#SETTINGS)
- [XML_MAPA](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#XML_MAP)
- [ESTRUCTURA](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#STRUCTURE)
- [PROPIEDADES DEL DOCUMENTO](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#DOCUMENT_PROPERTIES)
- [DEFINED_NAMES](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#DEFINED_NAMES)
- [VBA](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#VBA)
- [ESTILO](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#STYLE)
## **Filtrar objetos al cargar el libro de trabajo**
 El siguiente código de ejemplo ilustra cómo filtrar gráficos del libro. Por favor, checa el[ejemplo de archivo de Excel](5472489.xlsx) utilizado en este código y el[salida PDF](5472488.pdf)generada por ella. Como puede ver en el resultado PDF, todos los gráficos se han filtrado del libro de trabajo.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-FilterObjectsLoadingWorkbook-FilterObjectsLoadingWorkbook.java" >}}
## **Filtrar objetos al cargar la hoja de trabajo**
 El siguiente código de ejemplo carga el[archivo fuente excel](5472492.xlsx) y filtra los siguientes datos de sus hojas de trabajo usando un filtro personalizado.

- Filtra gráficos de la hoja de trabajo denominada NoCharts.
- Filtra las formas de la hoja de trabajo denominada NoShapes.
- Filtra el formato condicional de la hoja de trabajo denominada NoConditionalFormatting.

 Una vez, carga el[archivo fuente excel](5472492.xlsx) con un filtro personalizado, toma las imágenes de todas las hojas de trabajo una por una. Aquí están las imágenes de salida para su referencia. Como puede ver, la primera imagen no tiene gráficos, la segunda imagen no tiene formas y la tercera imagen no tiene formato condicional.

- [NoGráficos.png](5472493.png)
- [Sin Formas.png](5472491.png)
- [Sin formato condicional.png](5472490.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-FilterObjectsLoadingWorksheets-1.java" >}}
