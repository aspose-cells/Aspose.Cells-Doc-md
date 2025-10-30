---  
title: Trabajar con ContentTypeProperties con Node.js a través de C++  
linktitle: Trabajando con ContentTypeProperties  
type: docs  
weight: 150  
url: /es/nodejs-cpp/working-with-contenttypeproperties/  
description: Aprende cómo trabajar con ContentTypeProperties personalizados en archivos de Excel usando Aspose.Cells for Node.js via C++.  
---  

Aspose.Cells proporciona el método [**Workbook.getContentTypeProperties()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getContentTypeProperties--) para agregar ContentTypeProperties personalizados a un archivo de Excel. También puedes hacer que la propiedad sea opcional configurando la propiedad [**ContentTypeProperty.isNillable()**](https://reference.aspose.com/cells/nodejs-cpp/contenttypeproperty/#isNillable--) a **true**. El siguiente fragmento de código demuestra cómo agregar propiedades ContentTypeProperties opcionales a un archivo de Excel. La siguiente imagen muestra ambas propiedades que fueron agregadas por el código de muestra.

![todo:image_alt_text](working-with-contenttypeproperties_1.jpg)

El archivo de salida generado por el código de ejemplo se adjunta para referencia.

[Archivo de Salida](95584314.xlsx)

## **Código de muestra**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

//source directory
const outputDir = path.join(__dirname, "output");

const workbook = new AsposeCells.Workbook(AsposeCells.FileFormatType.Xlsx);
let index = workbook.getContentTypeProperties().add("MK31", "Simple Data");
workbook.getContentTypeProperties().get(index).setIsNillable(false);
index = workbook.getContentTypeProperties().add("MK32", new Date().toISOString(), "DateTime");
workbook.getContentTypeProperties().get(index).setIsNillable(true);
workbook.save(path.join(outputDir, "WorkingWithContentTypeProperties_out.xlsx"));
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
