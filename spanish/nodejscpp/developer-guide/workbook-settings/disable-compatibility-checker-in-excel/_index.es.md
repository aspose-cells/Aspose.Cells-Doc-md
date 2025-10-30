---  
title: Desactivar el verificador de compatibilidad en Excel con Node.js vía C++  
linktitle: Deshabilitar el Comprobador de Compatibilidad en Excel  
type: docs  
weight: 170  
url: /es/nodejs-cpp/disable-compatibility-checker-in-excel/  
description: Aprender cómo desactivar el verificador de compatibilidad a través de la API Aspose.Cells for Node.js via C++.  
keywords: Node.js Desactivar el verificador de compatibilidad, desactivar en Excel en Node.js vía C++, Desactivar compatibilidad en libro de trabajo.  
---  

## Desactivar verificador de compatibilidad en hojas de cálculo de Excel en Node.js  

{{% alert color="primary" %}}  
El Comprobador de compatibilidad de Microsoft Excel señala cuando guardar un archivo en un formato anterior podría causar problemas de funcionamiento o pérdida de fidelidad. El Comprobador de compatibilidad es una característica de Microsoft Office Excel 2007 y Microsoft Excel 2010.  

Al guardar un libro de trabajo en una versión anterior, Excel 97 a través de Excel 2003, desde Excel 2007 o Excel 2010, el Comprobador de Compatibilidad escanea el libro de trabajo para ver si contiene funciones que no son compatibles con la versión anterior. Para ayudarlo a tomar decisiones sobre cómo manejar problemas de compatibilidad, el Comprobador de Compatibilidad muestra cuadros de diálogo con opciones. También se puede utilizar para crear un informe sobre cualquier problema en el libro de trabajo o deshabilitar la función.  

A veces, necesitas desactivar el Comprobador de Compatibilidad para una hoja de cálculo en particular. Con las API de Aspose.Cells, puedes hacer esto programáticamente para que los usuarios no se frustren ni se confundan con la ventana de diálogo del Comprobador de Compatibilidad que aparece cuando vuelven a guardar el archivo manualmente en Microsoft Excel.  
{{% /alert %}}  

## **Cómo Deshabilitar el Comprobador de compatibilidad usando Microsoft Excel**  

Para deshabilitar el Comprobador de compatibilidad en Microsoft Excel (por ejemplo, Microsoft Excel 2007/2010):  

- (Excel 2007) En el botón de Office, haz clic en **Preparar**, luego en **Ejecutar Comprobador de compatibilidad**, y luego desmarca la opción **Comprobar compatibilidad al guardar este libro**.  
- (Excel 2010) En la pestaña **Archivo**, haz clic en **Información**, luego en **Buscar problemas**, haz clic en **Comprobar compatibilidad** y, finalmente, desmarca la opción **Comprobar compatibilidad al guardar este libro**.  

## **Cómo Deshabilitar el Comprobador de compatibilidad usando las API de Aspose.Cells**  

Establece la propiedad [**Workbook.getCheckCompatibility()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getCheckCompatibility--) en **falso** para desactivar el Comprobador de Compatibilidad de Microsoft Excel.  

### **Ejemplos de código**  

Los ejemplos de código que siguen muestran cómo desactivar el Comprobador de Compatibilidad con Aspose.Cells for Node.js via C++.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Open a template file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sample.xlsx"));

// Disable the compatibility checker
workbook.getSettings().setCheckCompatibility(false);

const outputFilePath = path.join(dataDir, "Output_BK_CompCheck.out.xlsx");
// Saving the Excel file
workbook.save(outputFilePath);
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
