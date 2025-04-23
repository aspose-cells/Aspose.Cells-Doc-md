---  
title: Trabajando con el efecto de sombra de Shape o Chart con Node.js mediante C++  
linktitle: Trabajando con el Efecto de Sombra de Forma o Gráfico  
type: docs  
weight: 220  
url: /es/nodejs-cpp/working-with-the-shadow-effect-of-shape-or-chart/  
description: Aprenda cómo trabajar con el efecto de sombra de formas o gráficos usando Aspose.Cells for Node.js via C++.  
---  

## **Escenarios de uso posibles**  
Aspose.Cells for Node.js via C++ proporciona la propiedad [Shape.getShadowEffect()](https://reference.aspose.com/cells/nodejs-cpp/shape/#getShadowEffect--) junto con la clase [ShadowEffect](https://reference.aspose.com/cells/nodejs-cpp/shadoweffect) para trabajar con el efecto de sombra de forma o gráfico. La clase [ShadowEffect](https://reference.aspose.com/cells/nodejs-cpp/shadoweffect) contiene las siguientes propiedades que se pueden ajustar para lograr diferentes resultados según los requisitos de la aplicación.  

- [ShadowEffect.getAngle()](https://reference.aspose.com/cells/nodejs-cpp/shadoweffect/#getAngle--)  
- [ShadowEffect.getBlur()](https://reference.aspose.com/cells/nodejs-cpp/shadoweffect/#getBlur--)  
- [ShadowEffect.getColor()](https://reference.aspose.com/cells/nodejs-cpp/shadoweffect/#getColor--)  
- [ShadowEffect.getDistance()](https://reference.aspose.com/cells/nodejs-cpp/shadoweffect/#getDistance--)  
- [ShadowEffect.getPresetType()](https://reference.aspose.com/cells/nodejs-cpp/shadoweffect/#getPresetType--)  
- [ShadowEffect.getSize()](https://reference.aspose.com/cells/nodejs-cpp/shadoweffect/#getSize--)  
- [ShadowEffect.getTransparency()](https://reference.aspose.com/cells/nodejs-cpp/shadoweffect/#getTransparency--)  

## **Trabajar con el Efecto de Sombra de la Forma o Gráfico**  
El siguiente código de ejemplo carga el [archivo excel fuente](5115425.xlsx) y accede a la primera forma en la primera hoja de trabajo y ajusta las subpropiedades de la propiedad [Shape.getShadowEffect()](https://reference.aspose.com/cells/nodejs-cpp/shape/#getShadowEffect--) y luego guarda el libro en [archivo excel de salida](5115411.xlsx).  

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

// Set the shadow effect of the shape, set its Angle, Blur, Distance and Transparency properties
const shadowEffect = shape.getShadowEffect();
shadowEffect.setAngle(150);
shadowEffect.setBlur(4);
shadowEffect.setDistance(45);
shadowEffect.setTransparency(0.3);

// Save the workbook in xlsx format
workbook.save(path.join(dataDir, "output_out.xlsx"));
```  

