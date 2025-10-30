---
title: Trabajando con el efecto de reflejo de Shape o Chart con Node.js mediante C++
linktitle: Trabajando con el Efecto de Reflexión de Forma o Gráfico
type: docs
weight: 210
url: /es/nodejs-cpp/working-with-the-reflection-effect-of-shape-or-chart/
description: Aprenda cómo trabajar con el efecto de reflejo de formas o gráficos usando Aspose.Cells for Node.js via C++. Establezca varias propiedades de reflexión para lograr los resultados deseados.
---

## **Escenarios de uso posibles**
Aspose.Cells for Node.js via C++ proporciona la propiedad [Shape.getReflection()](https://reference.aspose.com/cells/nodejs-cpp/shape/#getReflection--) junto con la clase [ReflectionEffect](https://reference.aspose.com/cells/nodejs-cpp/reflectioneffect) para trabajar con el efecto de reflexión de forma o gráfico. La clase [ReflectionEffect](https://reference.aspose.com/cells/nodejs-cpp/reflectioneffect) contiene las siguientes propiedades que se pueden ajustar para lograr diferentes resultados según los requisitos de la aplicación.

- [ReflectionEffect.getBlur()](https://reference.aspose.com/cells/nodejs-cpp/reflectioneffect/#getBlur--)
- [ReflectionEffect.getDirection()](https://reference.aspose.com/cells/nodejs-cpp/reflectioneffect/#getDirection--)
- [ReflectionEffect.getDistance()](https://reference.aspose.com/cells/nodejs-cpp/reflectioneffect/#getDistance--)
- [ReflectionEffect.getFadeDirection()](https://reference.aspose.com/cells/nodejs-cpp/reflectioneffect/#getFadeDirection--)
- [ReflectionEffect.getRotWithShape()](https://reference.aspose.com/cells/nodejs-cpp/reflectioneffect/#getRotWithShape--)
- [ReflectionEffect.getSize()](https://reference.aspose.com/cells/nodejs-cpp/reflectioneffect/#getSize--)
- [ReflectionEffect.getTransparency()](https://reference.aspose.com/cells/nodejs-cpp/reflectioneffect/#getTransparency--)
- [ReflectionEffect.getType()](https://reference.aspose.com/cells/nodejs-cpp/reflectioneffect/#getType--)

## **Trabajando con el Efecto de Reflexión de Forma o Gráfico**
El siguiente código de ejemplo carga el [archivo excel fuente](5115424.xlsx) y accede a la primera forma en la hoja de trabajo predeterminada. Establece diferentes propiedades de la clase [Shape.getReflection()](https://reference.aspose.com/cells/nodejs-cpp/shape/#getReflection--) y luego guarda el libro en [archivo excel de salida](5115423.xlsx).

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Load your source excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sample.xlsx"));

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access first shape
const shape = worksheet.getShapes().get(0);

// Set the reflection effect of the shape, set its Blur, Size, Transparency and Distance properties
const reflectionEffect = shape.getReflection();
reflectionEffect.setBlur(30);
reflectionEffect.setSize(90);
reflectionEffect.setTransparency(0);
reflectionEffect.setDistance(80);

// Save the workbook in xlsx format
workbook.save(path.join(dataDir, "output_out.xlsx"));
```
{{< app/cells/assistant language="nodejs-cpp" >}}
