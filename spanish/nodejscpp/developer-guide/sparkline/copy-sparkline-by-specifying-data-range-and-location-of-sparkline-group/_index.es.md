---  
title: Copiar Sparkline especificando el rango de datos y la ubicación del grupo de Sparkline con Node.js a través de C++  
linktitle: Copiar Sparkline especificando el rango de datos y la ubicación del grupo de sparkline  
type: docs  
weight: 300  
url: /es/nodejs-cpp/copy-sparkline-by-specifying-data-range-and-location-of-sparkline-group/  
description: Aprenda cómo copiar un rastro de línea en Excel especificando el rango de datos y la ubicación del grupo de líneas usando Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  
Microsoft Excel le permite copiar una sparkline especificando el rango de datos y la ubicación de un grupo de sparkline. Aspose.Cells soporta esta funcionalidad.  
{{% /alert %}}  

Para copiar una minigráfica en otras celdas en Microsoft Excel:  

1. Seleccione la celda que contiene la miniatura.  
1. Seleccione **Editar datos** en la sección de **Miniatura** de la pestaña **Diseño**.  
1. Seleccione **Editar ubicación y datos de grupo**.  
1. Especifique el rango de datos y la ubicación.  
1. Haz clic en **Aceptar**.  

Aspose.Cells proporciona el método `SparklineCollection.add(dataRange, row, column)` para especificar el rango de datos y la ubicación de un grupo de líneas. El siguiente código de ejemplo carga el archivo Excel de origen como se muestra en la captura de pantalla arriba, luego accede al primer grupo de líneas y agrega rangos de datos y ubicaciones en el grupo de líneas. Finalmente, escribe el archivo Excel de salida en disco, también mostrado en la captura de pantalla arriba.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Create workbook from source Excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "copy_sparkline.xlsx"));

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access the first sparkline group
const group = worksheet.getSparklineGroups().get(0);

// Add Data Ranges and Locations inside this sparkline group
group.getSparklines().add("Sheet1!D5:O5", 4, 15);
group.getSparklines().add("Sheet1!D6:O6", 5, 15);
group.getSparklines().add("Sheet1!D7:O7", 6, 15);
group.getSparklines().add("Sheet1!D8:O8", 7, 15);

// Save the workbook
workbook.save(path.join(dataDir, "output_out.xlsx"));
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
