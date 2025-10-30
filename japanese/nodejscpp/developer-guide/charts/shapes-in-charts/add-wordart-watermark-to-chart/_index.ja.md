---  
title: Node.jsとC++を使って、ChartにWordArtウォーターマークを追加する方法  
linktitle: グラフにWordArtウォーターマークを追加する  
description: Microsoft ExcelのチャートにWordArtウォーターマークを追加する方法をAspose.Cells for Node.js via C++で学びましょう。ガイドは、WordArtウォーターマークの作成と配置を示し、チャートの視覚的魅力と独自性を高めます。  
keywords: Aspose.Cells for Node.js、WordArtウォーターマーク、チャートウォーターマーク、Microsoft Excel、視覚的魅力、チャートの独自性。  
type: docs  
weight: 50  
url: /ja/nodejs-cpp/add-wordart-watermark-to-chart/  
---  

{{% alert color="primary" %}}  

WordArtを使用して、スプレッドシートに特殊なテキスト効果を追加できます。たとえば、タイトルを伸ばしたり、テキストを飾ったり、テキストをプリセットされた形に合わせたり、チャートのプロットエリアに影響を及ぼすテキストを透かしとして適用したりできます。WordArtは移動したり配置したりしてスプレッドシートに装飾を追加できるオブジェクトになります。  

次の例は、グラフのプロットエリアにウォーターマークとしてWordArtシェイプを追加する方法を示しています。  

{{% /alert %}}  

次の例では、既存のチャートのプロットエリアにWordArt形状をウォーターマークとして追加する方法を示しています。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");

// Open the existing excel file.
const workbook = new AsposeCells.Workbook(filePath);

// Get the chart in the first worksheet.
const chart = workbook.getWorksheets().get(0).getCharts().get(0);

// Add a WordArt watermark (shape) to the chart's plot area.
const wordart = chart.getShapes().addTextEffectInChart(AsposeCells.MsoPresetTextEffect.TextEffect2,
"CONFIDENTIAL", "Arial Black", 66, false, false, 1200, 500, 2000, 3000);

// Get the shape's fill format.
const wordArtFormat = wordart.getFill();

// Set the transparency.
wordArtFormat.setTransparency(0.9);

// Get the line format.
const lineFormat = wordart.getLine();

// Set Line format to invisible.
lineFormat.setWeight(0.0);

// Save the excel file.
workbook.save(path.join(dataDir, "output_out.xlsx"));
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
