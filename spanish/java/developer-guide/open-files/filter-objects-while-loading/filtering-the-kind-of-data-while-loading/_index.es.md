---
title: Filtrar el tipo de datos al cargar el libro desde el archivo de plantilla.
type: docs
weight: 680
url: /es/java/filtering-the-kind-of-data-while-loading-the-workbook-from-template-file/
---

{{% alert color="primary" %}} 

A veces, quieres especificar qué tipo de datos deben cargarse al construir el libro de trabajo a partir de un archivo de plantilla. Filtrar los datos cargados puede mejorar el rendimiento para tu propósito especial, especialmente al utilizar las [API de LightCells](/cells/es/java/using-lightcells-api/). Utiliza la propiedad [LoadOptions.getLoadFilter().setLoadDataFilterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/loadfilter#LoadDataFilterOptions) para este propósito.

{{% /alert %}} 
## **Filtrar el tipo de datos al cargar el libro de trabajo desde un archivo de plantilla**
El siguiente código de ejemplo carga solo objetos de forma al cargar el libro de trabajo desde el [archivo de plantilla](5472556.xlsx) que puedes descargar desde el enlace proporcionado.

La captura de pantalla siguiente muestra el contenido del [archivo de plantilla](5472556.xlsx) y también explica que los datos en color rojo y con fondo amarillo no se cargarán porque se ha establecido la propiedad [LoadOptions.getLoadFilter().setLoadDataFilterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/loadfilter#LoadDataFilterOptions) en [LoadDataFilterOptions.SHAPE](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#SHAPE).

![todo:image_alt_text](filtering-the-kind-of-data-while-loading-the-workbook-from-template-file_1.png)

La captura de pantalla siguiente muestra el [PDF de salida](5472554.pdf) que puedes descargar desde el enlace proporcionado. Aquí puedes ver que los datos en color rojo y con fondo amarillo no están presentes pero todas las formas sí lo están.

![todo:image_alt_text](filtering-the-kind-of-data-while-loading-the-workbook-from-template-file_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-FilterDataWhileLoadingWorkbook-1.java" >}}
{{< app/cells/assistant language="java" >}}
