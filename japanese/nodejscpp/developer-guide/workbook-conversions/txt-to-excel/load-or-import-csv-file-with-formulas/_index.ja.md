---  
title: Node.js を通じて数式を含む CSV ファイルを読み込みまたはインポートする  
linktitle: 数式を持つCSVファイルを読み込むまたはインポートする  
type: docs  
weight: 350  
url: /ja/nodejs-cpp/load-or-import-csv-file-with-formulas/  
description: Aspose.Cells for Node.js via C++ を使用して、数式を含む CSV ファイルを読み込み・取り込む方法を学びます。  
---  

{{% alert color="primary" %}}  

CSV ファイルはほとんどテキストデータで構成されており、数式は含まれません。しかしながら、時には CSV ファイルに数式も含まれる場合があります。そのような CSV ファイルをロードするには [TxtLoadOptions.getHasFormula()](https://reference.aspose.com/cells/nodejs-cpp/txtloadoptions/#getHasFormula--) を **true** に設定してください。このプロパティを **true** にすると、Aspose.Cells は数式を単純なテキストとして扱わず、数式として扱い、通常通り Aspose.Cells の数式計算エンジンが処理します。

{{% /alert %}}  

以下のコードは、数式を含む CSV ファイルのロードとインポートの例です。任意の CSV ファイルを使用できます。例として、[シンプルな CSV ファイル](5115034.csv) を使い、データを示します。ご覧の通り、数式を含んでいます。

{{< highlight javascript >}}  
const fs = require('fs');  
const AsposeCells = require('aspose.cells');  

let loadOptions = new AsposeCells.TxtLoadOptions();  
loadOptions.setHasFormula(true);  

let workbook = new AsposeCells.Workbook();  
workbook.open("path/to/your/file.csv", loadOptions);  
workbook.save("path/to/output.xlsx");  
{{< /highlight >}}  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.csv");

// TxtLoadOptions configuration
const opts = new AsposeCells.TxtLoadOptions();
opts.setSeparator(',');
opts.setHasFormula(true);

// Load your CSV file with formulas in a Workbook object
const workbook = new AsposeCells.Workbook(filePath, opts);

// You can also import your CSV file like this
// The code below is importing CSV file starting from cell D4
const worksheet = workbook.getWorksheets().get(0);
worksheet.getCells().importCSV(filePath, opts, 3, 3);

// Save your workbook in Xlsx format
workbook.save(path.join(dataDir, "output_out.xlsx"));
```  

まずCSVファイルを読み込み、その後セルD4に再度インポートします。最後に、ワークブックオブジェクトをXLSX形式で保存します。[出力されるXLSXファイル](5115052.xlsx)はこのようになります。ご覧のとおり、セルC3とF4に数式が含まれており、その結果は800です。

|![todo:image_alt_text](load-or-import-csv-file-with-formulas_1.png)|  
| :- |  


