---
title: Cómo agregar/insertar una Caja de Texto en la Hoja de Cálculo con Node.js vía C++
linktitle: Agregar cuadro de texto a la hoja de cálculo
type: docs
weight: 10
url: /es/nodejs-cpp/add-text-box-to-worksheet-in-aspose-cells/
description: Cómo agregar/insertar una Caja de Texto en la hoja de cálculo en Aspose.Cells for Node.js via C++.
keywords: agregar/insertar Texto en la Caja de Texto, Hoja de Cálculo, Excel, Aspose, Node.js vía C++
---

## Agregar cuadro de texto a la hoja de cálculo en Excel

En el programa de Excel (versión 07 y superior), hay dos lugares donde puede insertar cuadros de texto. Uno en "insertar-formas", el otro en la parte derecha del menú superior de la opción "Insertar".

### método uno:

![1](1.png)

### método dos:

![2](2.png)

## Cómo crear

Puedes crear cuadros de texto con texto horizontal o vertical.

- Seleccione la opción correspondiente (horizontal o vertical)
- Haz clic izquierdo en la página
- Mantén presionado el botón izquierdo y arrastra una distancia en la página
- Suelta el botón izquierdo

Ahora tienes un cuadro de texto.

## Agregar Caja de Texto a la Hoja de Cálculo en Aspose.Cells for Node.js via C++

Cuando necesite insertar en bloque TextBox en la hoja de cálculo, el método manual de inserción es claramente un desastre. Si esto le molesta, creo que este documento le ayudará. [Aspose.Cells](https://products.aspose.com/cells/) le proporciona una API para realizar inserciones masivas fácilmente en su código.

El siguiente código de ejemplo crea un cuadro de texto.

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create an object of the Workbook class
const workbook = new AsposeCells.Workbook();

// Access first worksheet from the collection
const sheet = workbook.getWorksheets().get(0);

// Add the TextBox to the worksheet
sheet.getTextBoxes().add(6, 10, 100, 200);

// Save. You can check your text box in this way.
workbook.save("result.xlsx", AsposeCells.SaveFormat.Xlsx);
```

Obtendrás un archivo similar a [archivo resultante](result.xlsx). En el archivo, verás lo siguiente:

![](52449.png)

{{< app/cells/assistant language="nodejs-cpp" >}}
