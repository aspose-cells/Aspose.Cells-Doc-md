---  
title: Establecer borde de rango con Node.js a través de C++  
linktitle: Establecer Borde de Rango  
type: docs  
weight: 600  
url: /es/nodejs-cpp/set-range-border/  
---  

## **Escenarios de uso posibles**  
Cuando deseas establecer el borde de un rango, no necesitas establecer cada celda individualmente. Puedes establecer el borde en todo el rango. Aspose.Cells for Node.js via C++ ofrece esta función.  
Este artículo proporciona un código de ejemplo que usa Aspose.Cells for Node.js via C++ para establecer el borde del rango.  

## **Establecer borde de rango en Excel**  
Para establecer el borde de un rango en Excel, puedes seguir estos pasos:  
1. Selecciona el rango de celdas al que deseas aplicarle el borde.  
2. En la pestaña "Inicio" de la cinta, busca el grupo "Fuente".  
3. Dentro del grupo "Fuente", haz clic en el botón desplegable "Bordes".  
<br>  
<img src="border.png" />  
4. Elige el tipo de borde que deseas aplicar de las opciones en el menú desplegable. Puedes elegir entre estilos de borde preestablecidos o personalizar tu propio borde.  
5. Una vez que hayas seleccionado el estilo de borde deseado, el borde se aplicará al rango seleccionado de celdas.  

## **Establecer borde de rango usando Aspose.Cells for Node.js via C++**  
Este ejemplo muestra cómo:  

1. Crear un libro de trabajo.  
2. Agregar datos a las celdas en la primera hoja de trabajo.  
3. Crear un [**Range**](https://reference.aspose.com/cells/nodejs-cpp/range).  
4. Establecer borde interior del rango.  
5. Establecer borde exterior del rango.  

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();
// Obtaining the reference of the newly added worksheet
const ws = workbook.getWorksheets().get(0);
const cells = ws.getCells();

// Setting the value to the cells
let cell = cells.get("A1");
cell.putValue("Fruit");
cell = cells.get("B1");
cell.putValue("Count");
cell = cells.get("C1");
cell.putValue("Price");

cell = cells.get("A2");
cell.putValue("Apple");
cell = cells.get("A3");
cell.putValue("Mango");
cell = cells.get("A4");
cell.putValue("Blackberry");
cell = cells.get("A5");
cell.putValue("Cherry");

cell = cells.get("B2");
cell.putValue(5);
cell = cells.get("B3");
cell.putValue(3);
cell = cells.get("B4");
cell.putValue(6);
cell = cells.get("B5");
cell.putValue(4);

cell = cells.get("C2");
cell.putValue(5);
cell = cells.get("C3");
cell.putValue(20);
cell = cells.get("C4");
cell.putValue(30);
cell = cells.get("C5");
cell.putValue(60);

// Create a range (A1:C5).
const range = cells.createRange("A1", "C5");

// set inner border of range
const innerColor = workbook.createCellsColor();
innerColor.setColor(AsposeCells.Color.Red);
range.setInsideBorders(AsposeCells.BorderType.Vertical, AsposeCells.CellBorderType.Thin, innerColor);
innerColor.setColor(AsposeCells.Color.Green);
range.setInsideBorders(AsposeCells.BorderType.Horizontal, AsposeCells.CellBorderType.Thin, innerColor);

// set outer border of range
const outerColor = workbook.createCellsColor();
outerColor.setColor(AsposeCells.Color.Blue);
range.setOutlineBorders(AsposeCells.CellBorderType.Thin, outerColor);

workbook.save("out.xlsx");
```  
{{< app/cells/assistant language="nodejs-cpp" >}}
