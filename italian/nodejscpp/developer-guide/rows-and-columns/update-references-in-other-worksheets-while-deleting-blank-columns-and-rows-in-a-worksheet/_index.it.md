---
title: Aggiorna i riferimenti in altri fogli di lavoro mentre elimini colonne e righe vuote in un foglio di lavoro
linktitle: Aggiorna i riferimenti in altri fogli di lavoro mentre elimini colonne e righe vuote in un foglio di lavoro
type: docs
weight: 5000
url: /it/nodejs-cpp/update-references-in-other-worksheets-while-deleting-blank-columns-and-rows-in-a-worksheet/
description: Impara come mantenere i riferimenti in altri fogli di lavoro durante l eliminazione di colonne e righe vuote in un foglio di lavoro usando Aspose.Cells for Node.js via C++.
---

{{% alert color="primary" %}}

Quando elimini colonne e righe vuote in una tabella, i relativi riferimenti in altre tabelle diventano non validi. Se vuoi evitare questo comportamento e vuoi che quei riferimenti della tabella corrente in altre tabelle siano aggiornati, utilizza la proprietà [**DeleteOptions.getUpdateReference()**](https://reference.aspose.com/cells/nodejs-cpp/deleteoptions/#getUpdateReference--) e impostala su **true**.

{{% /alert %}}

## **Aggiorna i riferimenti in altri fogli di lavoro mentre elimini colonne e righe vuote in un foglio di lavoro**

Consulta il seguente esempio di codice e il suo output sulla console. La cella E3 nel secondo foglio di lavoro ha una formula =Sheet1!C3 che si riferisce alla cella C3 nel primo foglio di lavoro. Se imposterai la proprietà [**DeleteOptions.getUpdateReference()**](https://reference.aspose.com/cells/nodejs-cpp/deleteoptions/#getUpdateReference--) come **true**, questa formula verrà aggiornata e diventerà =Sheet1!A1 quando elimini colonne e righe vuote nel primo foglio di lavoro. Tuttavia, se imposti la proprietà [**DeleteOptions.getUpdateReference()**](https://reference.aspose.com/cells/nodejs-cpp/deleteoptions/#getUpdateReference--) come **false**, la formula nella cella E3 del secondo foglio di lavoro rimarrà =Sheet1!C3 e diventerà invalida.

### **Esempio di programmazione**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");

// Create workbook
const wb = new AsposeCells.Workbook();

// Add second sheet with name Sheet2
wb.getWorksheets().add("Sheet2");

// Access first sheet and add some integer value in cell C1
// Also add some value in any cell to increase the number of blank rows and columns
const sht1 = wb.getWorksheets().get(0);
sht1.getCells().get("C1").putValue(4);
sht1.getCells().get("K30").putValue(4);

// Access second sheet and add formula in cell E3 which refers to cell C1 in first sheet
const sht2 = wb.getWorksheets().get(1);
sht2.getCells().get("E3").setFormula("'Sheet1'!C1");

// Calculate formulas of workbook
wb.calculateFormula();

// Print the formula and value of cell E3 in second sheet before deleting blank columns and rows in Sheet1.
console.log("Cell E3 before deleting blank columns and rows in Sheet1.");
console.log("--------------------------------------------------------");
console.log("Cell Formula: " + sht2.getCells().get("E3").getFormula());
console.log("Cell Value: " + sht2.getCells().get("E3").getStringValue());

// If you comment DeleteOptions.UpdateReference property below, then the formula in cell E3 in second sheet will not be updated
const opts = new AsposeCells.DeleteOptions();
opts.setUpdateReference(true);

// Delete all blank rows and columns with delete options
sht1.getCells().deleteBlankColumns(opts);
sht1.getCells().deleteBlankRows(opts);

// Calculate formulas of workbook
wb.calculateFormula();

// Print the formula and value of cell E3 in second sheet after deleting blank columns and rows in Sheet1.
console.log("");
console.log("");
console.log("Cell E3 after deleting blank columns and rows in Sheet1.");
console.log("--------------------------------------------------------");
console.log("Cell Formula: " + sht2.getCells().get("E3").getFormula());
console.log("Cell Value: " + sht2.getCells().get("E3").getStringValue());
```

### **Output della console**

Questo è l'output sulla console del codice sopra quando la proprietà [**DeleteOptions.getUpdateReference()**](https://reference.aspose.com/cells/nodejs-cpp/deleteoptions/#getUpdateReference--) è stata impostata su **true**.

{{< highlight java >}}

 Cell E3 before deleting blank columns and rows in Sheet1.

\--------------------------------------------------------

Cell Formula: =Sheet1!C1

Cell Value: 4


Cell E3 after deleting blank columns and rows in Sheet1.

\--------------------------------------------------------

Cell Formula: =Sheet1!A1

Cell Value: 4

{{< /highlight >}}

Questo è l'output sulla console del codice sopra quando la proprietà [**DeleteOptions.getUpdateReference()**](https://reference.aspose.com/cells/nodejs-cpp/deleteoptions/#getUpdateReference--) è stata impostata su **false**. Come puoi vedere, la formula nella cella E3 del secondo foglio di lavoro non viene aggiornata e il suo valore di cella è ora 0 invece di 4, il che è invalido.

{{< highlight java >}}

 Cell E3 before deleting blank columns and rows in Sheet1.

\--------------------------------------------------------

Cell Formula: =Sheet1!C1

Cell Value: 4


Cell E3 after deleting blank columns and rows in Sheet1.

\--------------------------------------------------------

Cell Formula: =Sheet1!C1

Cell Value: 0

{{< /highlight >}}
