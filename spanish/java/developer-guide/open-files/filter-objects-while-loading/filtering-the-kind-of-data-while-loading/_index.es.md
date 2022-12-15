---
title: Filtrado del tipo de datos al cargar el libro de trabajo desde el archivo de plantilla
type: docs
weight: 680
url: /es/java/filtering-the-kind-of-data-while-loading-the-workbook-from-template-file/
---
{{% alert color="primary" %}} 

 A veces, desea especificar qué tipo de datos se deben cargar al crear el libro de trabajo a partir de un archivo de plantilla. El filtrado de datos cargados puede mejorar el rendimiento para su propósito especial, especialmente cuando se usa[API de LightCells](/cells/es/java/using-lightcells-api/) . Por favor use el[LoadOptions.getLoadFilter().setLoadDataFilterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/loadfilter#LoadDataFilterOptions) propiedad para este fin.

{{% /alert %}} 
## **Filtrar el tipo de datos al cargar el libro de trabajo desde un archivo de plantilla**
El siguiente código de ejemplo carga solo objetos de forma mientras carga el libro de trabajo desde el[archivo de plantilla](5472556.xlsx)que se puede descargar desde el enlace dado.

La siguiente captura de pantalla muestra la[archivo de plantilla](5472556.xlsx) contenido y también explica que los datos en color rojo y fondo amarillo no se cargarán porque el[LoadOptions.getLoadFilter().setLoadDataFilterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/loadfilter#LoadDataFilterOptions)la propiedad se ha establecido en[LoadDataFilterOptions.SHAPE](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#SHAPE).

![todo:imagen_alternativa_texto](filtering-the-kind-of-data-while-loading-the-workbook-from-template-file_1.png)

La siguiente captura de pantalla muestra la[PDF de salida](5472554.pdf) que se puede descargar desde el enlace dado. Aquí puede ver que los datos en color rojo y fondo amarillo no están presentes, pero todas las formas están ahí.

![todo:imagen_alternativa_texto](filtering-the-kind-of-data-while-loading-the-workbook-from-template-file_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-FilterDataWhileLoadingWorkbook-1.java" >}}
