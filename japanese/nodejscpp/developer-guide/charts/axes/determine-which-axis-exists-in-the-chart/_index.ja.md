---  
title: どの軸がチャートに存在するかを判別します（Node.jsとC++を使用）  
linktitle: チャートにどの軸が存在するかを判断する  
description: Aspose.Cells for Node.js via C++を使用して作成したチャートにどの軸が存在するかを判断する方法を学びましょう。ガイドは、カテゴリ軸、値軸、二次軸を含む、チャート内のさまざまな軸を特定し、アクセスするのに役立ちます。  
keywords: Aspose.Cells for Node.js、チャート、軸、存在、カテゴリ、値、二次。  
type: docs  
weight: 140  
url: /ja/nodejs-cpp/determine-which-axis-exists-in-the-chart/  
---  

{{% alert color="primary" %}}  
時には、ユーザーは特定の軸がチャートに存在するかどうかを知る必要があります。例として、二次値軸がチャート内に存在するかどうかを知りたい場合などです。円グラフ、爆発円グラフ、パイパイ、パイバー、3Dパイ、3D爆発パイ、ドーナツ、爆発ドーナツなどの一部のグラフには軸がありません。  

Aspose.Cellsは、特定の軸がチャートに存在するかどうかを判断するための[**Chart.hasAxis(axisType, isPrimary)**](https://reference.aspose.com/cells/nodejs-cpp/chart/#hasAxis-AxisType-boolean-)メソッドを提供します。  
{{% /alert %}}  

次のサンプルコードは、[**Chart.hasAxis(axisType, isPrimary)**](https://reference.aspose.com/cells/nodejs-cpp/chart/#hasAxis-AxisType-boolean-)を使用してサンプルチャートにプライマリおよびセカンダリのカテゴリ軸と値軸が存在するかどうかを判断する例です。  

## Node.jsでチャートに存在する軸を判定するコード  

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

## サンプルコードによって生成されたコンソール出力  

コードのコンソール出力は以下の通りで、プライマリのカテゴリ軸と値軸にはtrue、セカンダリのカテゴリ軸と値軸にはfalseが表示されます。  

{{< highlight java >}}  
Has Primary Category Axis: True  
Has Secondary Category Axis: False  
Has Primary Value Axis: True  
Has Secondary Value Axis: False  
{{< /highlight >}}  
{{< app/cells/assistant language="nodejs-cpp" >}}
