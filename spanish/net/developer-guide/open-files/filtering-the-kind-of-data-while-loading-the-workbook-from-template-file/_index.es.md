---
title: Filtrar el tipo de datos al cargar el libro desde el archivo de plantilla.
type: docs
weight: 400
url: /es/net/filtering-the-kind-of-data-while-loading-the-workbook-from-template-file/
---

{{% alert color="primary" %}}

A veces, desea especificar qué tipo de datos debe cargarse al construir el libro desde el archivo de plantilla. Filtrar los datos cargados puede mejorar el rendimiento para su propósito especial, especialmente al usar [API de LightCells](/cells/es/net/using-lightcells-api/). Por favor, utilice la propiedad [**LoadOptions.LoadFilter**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/properties/loadfilter) para este propósito.

{{% /alert %}}

El siguiente código de muestra carga solo objetos de forma al cargar el libro desde el [archivo de plantilla](5115552.xlsx) que puede descargar desde el enlace dado. La siguiente captura de pantalla muestra los contenidos del [archivo de plantilla](5115552.xlsx) y también explica que los datos de color rojo y fondo amarillo no se cargarán porque se ha ajustado la propiedad [**LoadOptions.LoadFilter**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/properties/loadfilter) a [**LoadDataFilterOptions.Shape**](https://reference.aspose.com/cells/net/aspose.cells/loaddatafilteroptions)

![todo:image_alt_text](filtering-the-kind-of-data-while-loading-the-workbook-from-template-file_1.png)

La siguiente captura de pantalla muestra el [PDF de salida](5115555.pdf) que puede descargar desde el enlace dado. Aquí puede ver que los datos de color rojo y fondo amarillo no están presentes pero todas las formas sí lo están.

![todo:image_alt_text](filtering-the-kind-of-data-while-loading-the-workbook-from-template-file_2.png)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FilterDataWhileLoadingWorkbook-1.cs" >}}
