---  
title: Determinare quale asse esiste nel grafico con Node.js tramite C++  
linktitle: Determinare quale Asse esiste nel Grafico  
description: Impara come determinare quale asse esiste in un grafico creato utilizzando Aspose.Cells for Node.js via C++. La nostra guida ti aiuterà a identificare e accedere ai diversi assi in un grafico, inclusi assi categoria, valore e secondari.  
keywords: Aspose.Cells per Node.js, grafico, asse, esistenza, categoria, valore, secondario.  
type: docs  
weight: 140  
url: /it/nodejs-cpp/determine-which-axis-exists-in-the-chart/  
---  

{{% alert color="primary" %}}  
A volte, l'utente ha bisogno di sapere se un determinato asse esiste nel grafico. Per esempio, vogliono sapere se esiste un asse secondario dei valori all'interno del grafico o meno. Alcuni grafici come Pie, PieExploded, PiePie, PieBar, Pie3D, Pie3DExploded, Doughnut, DoughnutExploded, ecc. non hanno un asse.  

Aspose.Cells fornisce il metodo [**Chart.hasAxis(axisType, isPrimary)**](https://reference.aspose.com/cells/nodejs-cpp/chart/#hasAxis-AxisType-boolean-) per determinare se il grafico ha un particolare asse o meno.  
{{% /alert %}}  

Il seguente esempio di codice dimostra l'uso di [**Chart.hasAxis(axisType, isPrimary)**](https://reference.aspose.com/cells/nodejs-cpp/chart/#hasAxis-AxisType-boolean-) per determinare se il grafico di esempio ha assi di categoria e valore primari e secondari.  

## Codice Node.js per determinare quale asse esiste nel grafico  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "source.xlsx");
// Create workbook object
const workbook = new AsposeCells.Workbook(filePath);

// Access the first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Check if there are any charts before accessing
const charts = worksheet.getCharts();
if (charts.getCount() === 0) {
console.log("No charts found in the worksheet.");
return;
}

// Access the chart
const chart = charts.get(0);

// Determine which axis exists in chart
let ret = chart.hasAxis(AsposeCells.AxisType.Category, true);
console.log("Has Primary Category Axis: " + ret);

ret = chart.hasAxis(AsposeCells.AxisType.Category, false);
console.log("Has Secondary Category Axis: " + ret);

ret = chart.hasAxis(AsposeCells.AxisType.Value, true);
console.log("Has Primary Value Axis: " + ret);

ret = chart.hasAxis(AsposeCells.AxisType.Value, false);
console.log("Has Secondary Value Axis: " + ret);
```  

## Output della console generato dall'esempio di codice  

L'output della console del codice mostrato di seguito, che visualizza true per gli assi principali di categoria e valore e false per gli assi secondari di categoria e valore.  

{{< highlight java >}}  
Has Primary Category Axis: True  
Has Secondary Category Axis: False  
Has Primary Value Axis: True  
Has Secondary Value Axis: False  
{{< /highlight >}}  
{{< app/cells/assistant language="nodejs-cpp" >}}
