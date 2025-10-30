---
title: Filtrar el tipo de datos al cargar el archivo de plantilla en formato de libro de trabajo con Golang a través de C++
linktitle: Filtrar datos al cargar un libro de Excel
type: docs
weight: 400
url: /es/go-cpp/filtering-the-kind-of-data-while-loading-the-workbook-from-template-file/
description: Aprenda a filtrar tipos de datos específicos al cargar un libro de trabajo desde un archivo de plantilla usando Aspose.Cells con Golang a través de C++.
---

{{% alert color="primary" %}}

A veces, desea especificar qué tipo de datos debe cargarse al construir el libro desde el archivo de plantilla. El filtrado de datos cargados puede mejorar el rendimiento para su propósito especial, especialmente al usar las API de [LightCells](/cells/es/cpp/using-lightcells-api/). Por favor, use la propiedad [**LoadOptions.GetLoadFilter()**](https://reference.aspose.com/cells/go-cpp/loadoptions/getloadfilter/) para este propósito.

{{% /alert %}}

El siguiente código de muestra carga solo objetos de forma al cargar el libro desde el [archivo de plantilla](5115552.xlsx) que puede descargar desde el enlace dado. La siguiente captura de pantalla muestra los contenidos del [archivo de plantilla](5115552.xlsx) y también explica que los datos de color rojo y fondo amarillo no se cargarán porque se ha ajustado la propiedad [**LoadOptions.GetLoadFilter()**](https://reference.aspose.com/cells/go-cpp/loadoptions/getloadfilter/) a [**LoadDataFilterOptions.Shape**](https://reference.aspose.com/cells/cpp/aspose.cells/loaddatafilteroptions/)

![todo:image_alt_text](filtering-the-kind-of-data-while-loading-the-workbook-from-template-file_1.png)

La siguiente captura de pantalla muestra el [PDF de salida](5115555.pdf) que puede descargar desde el enlace dado. Aquí puede ver que los datos de color rojo y fondo amarillo no están presentes pero todas las formas sí lo están.

![todo:image_alt_text](filtering-the-kind-of-data-while-loading-the-workbook-from-template-file_2.png)

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FilteringTheKindOfDataWhileLoadingTheWorkbookFromTemplateFile.go" >}}
