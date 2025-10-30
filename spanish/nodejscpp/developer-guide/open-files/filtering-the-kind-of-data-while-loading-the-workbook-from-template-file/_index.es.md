---  
title: Filtrar el tipo de datos al cargar el libro desde un archivo plantilla con Node.js vía C++  
linktitle: Filtrar el tipo de datos al cargar el libro desde el archivo de plantilla.  
type: docs  
weight: 400  
url: /es/nodejs-cpp/filtering-the-kind-of-data-while-loading-the-workbook-from-template-file/  
---  

{{% alert color="primary" %}}  
A veces, desea especificar qué tipo de datos se deben cargar al construir el libro desde el archivo plantilla. Filtrar los datos cargados puede mejorar el rendimiento para su propósito específico, especialmente al usar [LightCells APIs](/cells/es/nodejs-cpp/using-lightcells-api/). Por favor, utilice la propiedad [**LoadOptions.getLoadFilter()**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions/#getLoadFilter--) para este fin.  
{{% /alert %}}  

El siguiente código de ejemplo carga solo objetos de forma mientras carga el libro desde el [archivo plantilla](5115552.xlsx) que puede descargar desde el enlace proporcionado. La siguiente captura de pantalla muestra el contenido del [archivo plantilla](5115552.xlsx) y también explica que los datos en color rojo y fondo amarillo no se cargarán porque la propiedad [**LoadOptions.getLoadFilter()**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions/#getLoadFilter--) se ha establecido en [**Shape**](https://reference.aspose.com/cells/nodejs-cpp/shape/).  

![todo:image_alt_text](filtering-the-kind-of-data-while-loading-the-workbook-from-template-file_1.png)  

La siguiente captura de pantalla muestra el [PDF de salida](5115555.pdf) que puede descargar desde el enlace dado. Aquí puede ver que los datos de color rojo y fondo amarillo no están presentes pero todas las formas sí lo están.  

![todo:image_alt_text](filtering-the-kind-of-data-while-loading-the-workbook-from-template-file_2.png)  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");

// Output directory
const outputDir = path.join(__dirname, "output");

// Set the load options, we only want to load shapes and do not want to load data
const loadOptions = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Xlsx);            

loadOptions.setLoadFilter(new AsposeCells.LoadFilter(AsposeCells.LoadDataFilterOptions.All & ~AsposeCells.LoadDataFilterOptions.Chart));

// Create workbook object from sample excel file using load options
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "sampleFilterChars.xlsx"), loadOptions);

// Save the output in pdf format
workbook.save(outputDir + "sampleFilterChars_out.pdf", AsposeCells.SaveFormat.Pdf);
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
