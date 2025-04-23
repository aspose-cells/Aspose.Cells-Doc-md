---
title: Precedentes y Dependientes con Node.js vía C++
linktitle: Precedentes y Dependientes
type: docs
weight: 230
url: /es/nodejs-cpp/precedents-and-dependents/
description: Aprenda a rastrear celdas precedentes y dependientes en hojas de cálculo usando Aspose.Cells for Node.js via C++. Entienda cómo identificar celdas enlazadas en hojas de cálculo financieras complejas.
---

{{% alert color="primary" %}} 

Las hojas de cálculo financieras complejas, especialmente aquellas desarrolladas en colaboración, pueden ocultar los errores más vergonzosos. Verificar la precisión de las fórmulas y encontrar la fuente de un error puede ser difícil cuando la fórmula utiliza celdas precedentes y celdas dependientes.

{{% /alert %}} 
## **Introducción**
- **Celdas precedentes** son celdas a las que hace referencia una fórmula en otra celda. Por ejemplo, si la celda D10 contiene la fórmula =B5, la celda B5 es precedente a la celda D10.
- **Celdas dependientes** contienen fórmulas que hacen referencia a otras celdas. Por ejemplo, si la celda D10 contiene la fórmula =B5, la celda D10 depende de la celda B5.

Para que la hoja de cálculo sea fácil de leer, es posible que desees mostrar claramente qué celdas en una hoja de cálculo se utilizan en una fórmula. Del mismo modo, es posible que desees extraer las celdas dependientes de otras celdas.

Aspose.Cells te permite rastrear celdas y averiguar cuáles están vinculadas.
## **Rastreo de celdas precedentes y dependientes: Microsoft Excel**
Las fórmulas pueden cambiar en función de las modificaciones realizadas por un cliente. Por ejemplo, si la celda C1 depende de C3 y C4 que contienen una fórmula, y se cambia C1 (por lo que se anula la fórmula), C3 y C4, u otras celdas, necesitan cambiar para equilibrar la hoja de cálculo según las reglas empresariales.

De manera similar, suponga que C1 contiene la fórmula "=(B1*22)/(M2*N32)". Quiero encontrar las celdas de las que depende C1, es decir, las celdas precedentes B1, M2 y N32.

Es posible que necesite rastrear la dependencia de una celda particular respecto a otras celdas. Si las reglas empresariales están incrustadas en fórmulas, nos gustaría averiguar la dependencia y ejecutar algunas reglas basadas en ella. De manera similar, si se modifica el valor de una celda en particular, ¿qué celdas en la hoja de cálculo se ven afectadas por ese cambio?

Microsoft Excel permite a los usuarios rastrear las celdas precedentes y dependientes.

1. En la **Barra de herramientas Ver**, seleccione **Revisión de Fórmulas**. Se mostrará el cuadro de diálogo Revisión de Fórmulas.
1. Rastrear precedentes:
   1. Selecciona la celda que contiene la fórmula de la cual deseas encontrar las celdas precedentes.
   1. Para mostrar una flecha rastreadora a cada celda que proporciona datos directamente a la celda activa, haz clic en **Rastrear precedentes** en la barra de herramientas **Auditoría de fórmulas**.
1. Rastrear fórmulas que hacen referencia a una celda en particular (dependientes)
   1. Selecciona la celda de la que deseas identificar las celdas dependientes.
   1. Para mostrar una flecha rastreadora a cada celda que depende de la celda activa, haga clic en **Rastrear Dependientes** en la barra de herramientas de Auditoría de Fórmulas.
## **Rastreo de celdas precedentes y dependientes: Aspose.Cells**
### **Rastreo de Precedentes**
Aspose.Cells facilita obtener celdas precedentes. No solo puede recuperar celdas que proporcionan datos a predecesores de fórmulas simples, sino que también puede encontrar celdas que proporcionan datos a predecesores de fórmulas complejas con rangos nombrados.

En el ejemplo a continuación, se utiliza un archivo de plantilla de Excel, Book1.xls. La hoja de cálculo tiene datos y fórmulas en la primera hoja de trabajo.

Aspose.Cells proporciona el método [Cell.getPrecedents()](https://reference.aspose.com/cells/nodejs-cpp/cell/#getPrecedents--) de la clase [Cell](https://reference.aspose.com/cells/nodejs-cpp/cell) utilizado para rastrear los precedentes de una celda. Devuelve una colección de áreas referidas. Como se muestra arriba, en Book1.xls, la celda B7 contiene la fórmula "=SUM(A1:A3)". Por lo tanto, A1:A3 son las celdas precedentes de B7. El siguiente ejemplo demuestra la función de rastrear precedentes usando el archivo plantilla Book1.xls.


```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);
const cells = workbook.getWorksheets().get(0).getCells();
const cell = cells.get("B4");
// Check if the cell object is not null before proceeding
if (cell) 
{
const ret = cell.getPrecedents();
if (!ret.isNull() && ret.getCount() > 0)
{
const area = ret.get(0);
console.log(area.getSheetName());
console.log(AsposeCells.CellsHelper.cellIndexToName(area.getStartRow(), area.getStartColumn()));
console.log(AsposeCells.CellsHelper.cellIndexToName(area.getEndRow(), area.getEndColumn()));
}
else
{
console.error("No precedents found for the cell.");
}
} 
else 
{
console.error("Cell B4 is null.");
}
```
### **Rastreo de Dependientes**
Aspose.Cells le permite obtener las celdas dependientes en hojas de cálculo. Aspose.Cells no solo puede recuperar las celdas que proporcionan datos respecto a una fórmula simple, sino también encontrar las celdas que proporcionan datos a dependientes de fórmulas complejas con rangos con nombre.

Aspose.Cells proporciona el método [Cell.getDependents(boolean)](https://reference.aspose.com/cells/nodejs-cpp/cell/#getDependents-boolean-) de la clase [Cell](https://reference.aspose.com/cells/nodejs-cpp/cell) utilizado para rastrear las dependientes de una celda. Por ejemplo, en Book1.xlsx hay fórmulas: "=A1+20" y "=A1+30" en las celdas B2 y C2 respectivamente. El siguiente ejemplo demuestra cómo rastrear los dependientes de la celda A1 usando el archivo plantilla Book1.xlsx.


```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);
const cells = workbook.getWorksheets().get(0).getCells();
const cell = cells.get("B2");
// Ensure dependents is an array
const dependents = cell.getDependents(true);

if (Array.isArray(dependents)) 
{
for (const c of dependents) 
{
console.log(c.getName());
}
} 
else 
{
console.error("Dependents is not an array");
}
```
### **Rastreo de celdas precedentes y dependientes según la cadena de cálculo**
Las API anteriores para rastrear precedentes y dependientes son según la propia expresión de fórmula. Proporcionan simplemente una forma conveniente para que los usuarios rastreen las dependencias mutuas de unas pocas fórmulas. Si hay una gran cantidad de fórmulas en el libro de trabajo y el usuario necesita rastrear precedentes y dependientes para cada celda, tendrán un rendimiento pobre. Para tal situación, el usuario debería considerar usar los métodos [Cell.getPrecedentsInCalculation()](https://reference.aspose.com/cells/nodejs-cpp/cell/#getPrecedentsInCalculation--) y [Cell.getDependentsInCalculation(boolean)](https://reference.aspose.com/cells/nodejs-cpp/cell/#getDependentsInCalculation-boolean-). Estos dos métodos rastrean dependencias de acuerdo con la cadena de cálculo. Entonces, para usarlos, primero debe habilitar la cadena de cálculo mediante [FormulaSettings.getEnableCalculationChain()](https://reference.aspose.com/cells/nodejs-cpp/formulasettings/#getEnableCalculationChain--). Luego, debe realizar un cálculo completo del libro con [Workbook.calculateFormula()](https://reference.aspose.com/cells/nodejs-cpp/workbook/#calculateFormula--). Después de eso, puede rastrear precedentes o dependientes para todas esas celdas que necesita.

Para algunas fórmulas, los precedentes resultantes pueden ser diferentes para getPrecedents y getPrecedentsInCalculation, y los dependientes resultantes pueden ser diferentes para getDependents y getDependentsInCalculation. Por ejemplo, si la fórmula de la celda A1 es "=IF(TRUE,B2,C3)", getPrecedents proporcionará B2 y C3 como predecesores de A1. En consecuencia, B2 y C3 tienen a A1 como dependiente al verificar con getDependents. Sin embargo, para el cálculo de esta fórmula, es obvio que solo B2 puede afectar el resultado calculado. Por lo tanto, getPrecedentsInCalculation no proporcionará C3 para A1, y getDependentsInCalculation no proporcionará A1 para C3. Algunas veces, los usuarios solo necesitan rastrear esas interdependencias que realmente afectan el resultado calculado de las fórmulas según los datos actuales del libro, y en ese caso, también deben usar getDependentsInCalculation/getPrecedentsInCalculation en lugar de getDependents/getPrecedents.

El siguiente ejemplo demuestra cómo rastrear los precedentes y dependientes según la cadena de cálculo para las celdas:


```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");
// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);
const cells = workbook.getWorksheets().get(0).getCells();
cells.get("A1").setFormula("=B1+SUM(B1:B10)+[Book1.xls]Sheet1!B2");
cells.get("A2").setFormula("=IF(TRUE,B2,B1)");
workbook.getSettings().getFormulaSettings().setEnableCalculationChain(true);
workbook.calculateFormula();

let en = cells.get("B1").getDependentsInCalculation(false);
console.log("B1's calculation dependents:");
for (var cell of en) {
console.log(cell.getName());
}


en = cells.get("B2").getDependentsInCalculation(false);
console.log("B2's calculation dependents:");
for (var cell of en) {
console.log(cell.getName());
}

en = cells.get("A1").getPrecedentsInCalculation();
console.log("A1's calculation precedents:");
for (var area of en) {
console.log(area.toString());
}


en = cells.get("A2").getPrecedentsInCalculation();
console.log("A2's calculation precedents:");
for (var area of en) {
console.log(area.toString());
}
```
