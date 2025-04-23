---  
title: Trabajar con el efecto brillo de una forma o gráfico con Node.js mediante C++  
linktitle: Trabajar con el efecto de resplandor de la forma o el gráfico  
type: docs  
weight: 240  
url: /es/nodejs-cpp/working-with-the-glow-effect-of-shape-or-chart/  
description: Aprende a trabajar con el efecto brillo de formas o gráficos en Node.js usando Aspose.Cells for Node.js via C++.  
---  

## **Escenarios de uso posibles**  
Aspose.Cells proporciona la propiedad [Shape.getGlow()](https://reference.aspose.com/cells/nodejs-cpp/shape/#getGlow--) junto con la clase [GlowEffect](https://reference.aspose.com/cells/nodejs-cpp/gloweffect/) para trabajar con el efecto brillo de la forma o gráfico. La clase [GlowEffect](https://reference.aspose.com/cells/nodejs-cpp/gloweffect/) contiene las siguientes propiedades que pueden establecerse para lograr diferentes resultados según las necesidades de la aplicación.  

- [GlowEffect.getSize()](https://reference.aspose.com/cells/nodejs-cpp/gloweffect/#getSize--)  
- [GlowEffect.getTransparency()](https://reference.aspose.com/cells/nodejs-cpp/gloweffect/#getTransparency--)  
- [GlowEffect.getColor()](https://reference.aspose.com/cells/nodejs-cpp/gloweffect/#getColor--)  

## **Trabajando con el Efecto de Resplandor de Forma o Gráfico**  
El siguiente código de ejemplo carga el [archivo excel fuente](5115407.xlsx) y accede a la primera forma en la primera hoja de trabajo y establece las subpropiedades de [Shape.getGlow()](https://reference.aspose.com/cells/nodejs-cpp/shape/#getGlow--) y luego guarda el libro en [archivo excel de salida](5115414.xlsx).  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Load your source excel file
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access first shape
const shape = worksheet.getShapes().get(0);

// Set the glow effect of the shape, Set its Size and Transparency properties
const glowEffect = shape.getGlow();
glowEffect.setSize(30);
glowEffect.setTransparency(0.4);

// Save the workbook in xlsx format
workbook.save(path.join(dataDir, "output_out.xlsx"));
```  
