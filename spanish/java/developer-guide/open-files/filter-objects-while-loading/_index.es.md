---
title: Filtrar objetos al cargar el libro o la hoja de trabajo
type: docs
weight: 1060
url: /es/java/filter-objects-while-loading-workbook-or-worksheet/
---

## **Escenarios de uso posibles**
Por favor, use la propiedad [LoadOptions.LoadFilter](https://reference.aspose.com/cells/java/com.aspose.cells/loadoptions#LoadFilter) al filtrar datos del libro. Pero si desea filtrar datos de hojas de trabajo individuales, entonces deberá anular el método [LoadFilter.startSheet](https://reference.aspose.com/cells/java/com.aspose.cells/loadfilter#startSheet\(com.aspose.cells.Worksheet\)). Por favor, proporcione el valor apropiado de la enumeración [LoadDataFilterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/LoadDataFilterOptions) al crear o trabajar con [LoadFilter](https://reference.aspose.com/cells/java/com.aspose.cells/loadfilter).

La enumeración [LoadDataFilterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/LoadDataFilterOptions) tiene los siguientes valores.

- [NINGUNO](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#NONE)
- [TODOS](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#ALL)
- [CELDA_VACÍA](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CELL_BLANK)
- [CELDA_TEXTO](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CELL_STRING)
- [CELDA_NUMÉRICA](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CELL_NUMERIC)
- [CELDA_ERROR](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CELL_ERROR)
- [CELDA_BOOL](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CELL_BOOL)
- [CELDA_VALOR](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CELL_VALUE)
- [FÓRMULA](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#FORMULA)
- [DATOS_CELDA](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CELL_DATA)
- [GRÁFICO](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CHART)
- [FORMA](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#SHAPE)
- [ÁREA_FUSIONADA](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#MERGED_AREA)
- [FORMATO_CONDICIONAL](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CONDITIONAL_FORMATTING)
- [VALIDACIÓN_DATOS](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#DATA_VALIDATION)
- [TABLA_PIVOTE](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#PIVOT_TABLE)
- [TABLA](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#TABLE)
- [HIPERVÍNCULOS](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#HYPERLINKS)
- [CONFIGURACIÓN_HOJA](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#SHEET_SETTINGS)
- [DATOS_HOJA](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#SHEET_DATA)
- [CONFIGURACIÓN_LIBRO](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#BOOK_SETTINGS)
- [CONFIGURACIONES](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#SETTINGS)
- [MAPA_XML](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#XML_MAP)
- [ESTRUCTURA](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#STRUCTURE)
- [PROPIEDADES_DOCUMENTO](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#DOCUMENT_PROPERTIES)
- [NOMBRES_DEFINIDOS](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#DEFINED_NAMES)
- [VBA](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#VBA)
- [ESTILO](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#STYLE)
## **Objetos de filtro mientras se carga el libro de trabajo**
El siguiente código de ejemplo ilustra cómo filtrar gráficos del libro de trabajo. Por favor, consulte el [archivo de Excel de ejemplo](5472489.xlsx) utilizado en este código y el [PDF de salida](5472488.pdf) generado por él. Como puede ver en el PDF de salida, todos los gráficos se han filtrado del libro de trabajo.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-FilterObjectsLoadingWorkbook-FilterObjectsLoadingWorkbook.java" >}}
## **Objetos de filtro mientras se carga la hoja de trabajo**
El siguiente código de ejemplo carga el [archivo de Excel de origen](5472492.xlsx) y filtra los siguientes datos de sus hojas de trabajo mediante un filtro personalizado.

- Filtra los gráficos de la hoja de trabajo llamada SinGráficos.
- Filtra las formas de la hoja de trabajo llamada SinFormas.
- Filtra el formato condicional de la hoja de trabajo llamada SinFormatoCondicional.

Una vez que carga el [archivo de Excel de origen](5472492.xlsx) con un filtro personalizado, toma las imágenes de todas las hojas de forma individual. Aquí están las imágenes de salida para su referencia. Como puede ver, la primera imagen no tiene gráficos, la segunda imagen no tiene formas y la tercera imagen no tiene formato condicional.

- [NoCharts.png](5472493.png)
- [NoShapes.png](5472491.png)
- [NoConditionalFormatting.png](5472490.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-FilterObjectsLoadingWorksheets-1.java" >}}
