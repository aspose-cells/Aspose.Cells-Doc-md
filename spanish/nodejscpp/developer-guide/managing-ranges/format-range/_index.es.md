---  
title: Formatear Rangos con Node.js mediante C++  
linktitle: Formato de rangos  
type: docs  
weight: 105  
url: /es/nodejs-cpp/how-to-format-a-range/  
description: Aprende cómo formatear un rango de celdas en Excel usando Aspose.Cells for Node.js via C++.  
---  

## **Escenarios de uso posibles**  
Cuando necesitas aplicar un estilo a un rango, puedes usar el formato de rango.  

## **Cómo dar formato a un rango en Excel**  

Para dar formato a un rango de celdas en Excel, puedes usar las opciones de formato integradas proporcionadas por Excel. Así es como puedes dar formato a un rango de celdas directamente en Excel:  

1. Abre Excel y el libro que contiene el rango que deseas formatear.  

2. Selecciona el rango de celdas que deseas formatear. Puedes hacer clic y arrastrar para seleccionar el rango, o puedes usar atajos de teclado como Shift + Flechas para extender la selección.  

3. Una vez seleccionado el rango, haz clic derecho en el rango seleccionado y elige "Formato de celdas" en el menú contextual. Alternativamente, ve a la pestaña Inicio en la cinta de Excel, haz clic en el menú desplegable "Formato" en el grupo "Celdas", y selecciona "Formato de celdas".  

4. Aparecerá el cuadro de diálogo "Formato de celdas". Aquí, puedes elegir varias opciones de formato para aplicar al rango seleccionado. Por ejemplo, puedes cambiar el estilo de fuente, tamaño de fuente, color de fuente, formato de número, bordes, color de fondo, etc. Explora las distintas pestañas en el cuadro de diálogo para acceder a varias opciones de formato.  

5. Después de realizar los cambios de formato deseados, haz clic en el botón "Aceptar" para aplicar el formato al rango seleccionado.  

## **Cómo formatear un rango usando Node.js**  

Para formatear un rango usando Aspose.Cells for Node.js via C++, puedes usar los siguientes métodos:  
1. [Range.applyStyle(Estilo, Bandera)](https://reference.aspose.com/cells/nodejs-cpp/range/#applyStyle-style-styleflag-)  
2. [Range.setStyle(Estilo)](https://reference.aspose.com/cells/nodejs-cpp/range/#setStyle-style-)  
3. [Range.setStyle(Estilo)](https://reference.aspose.com/cells/nodejs-cpp/range/#setStyle-style-)  

## **Código de muestra**  
En este ejemplo, creamos un libro de Excel, agregamos algunos datos de muestra, accedemos a la primera hoja de trabajo y definimos dos rangos ("A1:C3" y "A4:C5"). Luego, creamos nuevos estilos, establecemos varias opciones de formato (por ej., color de fuente, negrita) y aplicamos el estilo al rango. Finalmente, guardamos el libro en un nuevo archivo.  
<br>  
![todo:image_alt_text](format-range.png)  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Create the workbook
const workbook = new AsposeCells.Workbook(filePath);
// Get the first worksheet
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

// Access the worksheet
const worksheet = workbook.getWorksheets().get(0);

// Define the range
const range = worksheet.getCells().createRange("A1:C3");

// Apply formatting to the range
const style = workbook.createStyle();
style.getFont().setColor(AsposeCells.Color.Red);
style.getFont().setIsBold(true);

const flag = new AsposeCells.StyleFlag();
flag.setFont(true);
range.applyStyle(style, flag);

// Define the range
const range2 = worksheet.getCells().createRange("A4:C5");

// Apply formatting to the range
const style2 = workbook.createStyle();
style2.getFont().setColor(AsposeCells.Color.Blue);
style2.getFont().setIsItalic(true);
range2.setStyle(style2);

// Save the modified workbook
workbook.save("output.xlsx");
```  

