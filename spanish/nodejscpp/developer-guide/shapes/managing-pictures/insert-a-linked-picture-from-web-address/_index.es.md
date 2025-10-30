---  
title: Insertar una imagen enlazada desde una dirección web con Node.js mediante C++  
linktitle: Insertar una imagen vinculada desde una dirección web  
type: docs  
weight: 450  
url: /es/nodejs-cpp/insert-a-linked-picture-from-web-address/  
description: Aprenda cómo insertar una imagen enlazada desde una dirección web en una hoja de cálculo mediante Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  
 A veces necesita insertar una imagen desde la web (http://) en una hoja de cálculo. Para ello, especifique la URL de la imagen y la imagen se descargará cada vez que se abra la hoja de cálculo en Excel. La imagen no está incrustada físicamente en el documento de Excel, sino que apunta a un recurso web.  
{{% /alert %}}  

## **Usar Microsoft Excel**  

En Microsoft Excel (por ejemplo, 2007):  

1. Haz clic en el menú **Insertar** y selecciona **Imagen**.  
1. Especifica la dirección web de la imagen en el cuadro de diálogo Insertar Imagen.  

## **Usando Aspose.Cells for Node.js via C++**  

Aspose.Cells for Node.js via C++ soporta agregar una imagen enlazada usando [**ShapeCollection.addLinkedPicture(upperLeftRow, upperLeftColumn, heightPixels, widthPixels, sourceFullName)**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addLinkedPicture-number-number-number-number-string-). El método devuelve un objeto [**Picture**](https://reference.aspose.com/cells/nodejs-cpp/picture).  

El siguiente ejemplo muestra cómo agregar una imagen vinculada desde una dirección web a una hoja de trabajo.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook();
// Insert a linked picture (from Web Address) to B2 Cell.
const pic = workbook.getWorksheets().get(0).getShapes().addLinkedPicture(1, 1, 100, 100, "http://www.aspose.com/Images/aspose-logo.jpg");
// Set the height and width of the inserted image.
pic.setHeightInch(1.04);
pic.setWidthInch(2.6);
// Save the Excel file.
workbook.save(path.join(dataDir, "outLinkedPicture.out.xlsx"));
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
