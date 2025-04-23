---
title: Filtrar el tipo de datos al cargar el libro desde el archivo de plantilla.
type: docs
weight: 400
url: /es/python-net/filtering-the-kind-of-data-while-loading-the-workbook-from-template-file/
---

{{% alert color="primary" %}}

A veces, quieres especificar qué tipo de datos se deben cargar al construir el libro desde el archivo de plantilla. Filtrar los datos cargados puede mejorar el rendimiento para tu propósito específico. Usa la propiedad [**LoadOptions.load_filter**](https://reference.aspose.com/cells/python-net/aspose.cells/loadoptions/load_filter) para este fin.

{{% /alert %}}

El siguiente código de muestra carga solo objetos de forma al cargar el libro desde el [archivo de plantilla](5115552.xlsx) que puede descargar desde el enlace dado. La siguiente captura de pantalla muestra los contenidos del [archivo de plantilla](5115552.xlsx) y también explica que los datos de color rojo y fondo amarillo no se cargarán porque se ha ajustado la propiedad [**LoadOptions.load_filter**](https://reference.aspose.com/cells/python-net/aspose.cells/loadoptions/load_filter) a [**LoadDataFilterOptions.SHAPE**](https://reference.aspose.com/cells/python-net/aspose.cells/loaddatafilteroptions/)

![todo:image_alt_text](filtering-the-kind-of-data-while-loading-the-workbook-from-template-file_1.png)

La siguiente captura de pantalla muestra el [PDF de salida](5115555.pdf) que puede descargar desde el enlace dado. Aquí puede ver que los datos de color rojo y fondo amarillo no están presentes pero todas las formas sí lo están.

![todo:image_alt_text](filtering-the-kind-of-data-while-loading-the-workbook-from-template-file_2.png)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-FilterDataWhileLoadingWorkbook-1.py" >}}

