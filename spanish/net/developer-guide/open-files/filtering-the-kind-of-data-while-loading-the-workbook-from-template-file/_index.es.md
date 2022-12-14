---
title: Filtrado del tipo de datos al cargar el libro de trabajo desde el archivo de plantilla
type: docs
weight: 400
url: /es/net/filtering-the-kind-of-data-while-loading-the-workbook-from-template-file/
---
{{% alert color="primary" %}}

 A veces, desea especificar qué tipo de datos se deben cargar al crear el libro de trabajo a partir del archivo de plantilla. El filtrado de datos cargados puede mejorar el rendimiento para su propósito especial, especialmente cuando se usa[API de LightCells](/cells/es/net/using-lightcells-api/) . Por favor use el[**LoadOptions.LoadFilter**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/properties/loadfilter) propiedad para este fin.

{{% /alert %}}

El siguiente código de ejemplo carga solo objetos de forma mientras carga el libro de trabajo desde el[archivo de plantilla](5115552.xlsx) que se puede descargar desde el enlace dado. La siguiente captura de pantalla muestra la[archivo de plantilla](5115552.xlsx) contenido y también explica que los datos en color rojo y fondo amarillo no se cargarán porque[**LoadOptions.LoadFilter**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/properties/loadfilter)la propiedad se ha establecido en[**LoadDataFilterOptions.Forma**](https://reference.aspose.com/cells/net/aspose.cells/loaddatafilteroptions)

![todo:imagen_alternativa_texto](filtering-the-kind-of-data-while-loading-the-workbook-from-template-file_1.png)

 La siguiente captura de pantalla muestra la[PDF de salida](5115555.pdf) que se puede descargar desde el enlace dado. Aquí puede ver que los datos en color rojo y fondo amarillo no están presentes, pero todas las formas están ahí.

![todo:imagen_alternativa_texto](filtering-the-kind-of-data-while-loading-the-workbook-from-template-file_2.png)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FilterDataWhileLoadingWorkbook-1.cs" >}}
