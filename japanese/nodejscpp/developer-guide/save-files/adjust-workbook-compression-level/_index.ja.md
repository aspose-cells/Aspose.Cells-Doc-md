---  
title: Workbookの圧縮レベルを調整する(Node.js経由のC++)で調整します。  
linktitle: Workbookの圧縮レベルを調整  
type: docs  
weight: 180  
url: /ja/nodejs-cpp/adjust-workbook-compression-level/  
description: Aspose.Cells for Node.js via C++でワークブックの圧縮レベルを調整する方法を学びます。  
---  

## **ワークブックの圧縮レベルを調整する**  

開発者は、大きなワークブックを扱う際に圧縮レベルを調整できます。開発者は、処理時間よりもファイルサイズの縮小を優先する場合や、その逆も選択できます。Aspose.Cells for Node.js via C++は、ワークブックの圧縮レベルを設定するための[**OoxmlCompressionType**](https://reference.aspose.com/cells/nodejs-cpp/ooxmlcompressiontype)列挙体を提供します。[**OoxmlCompressionType**](https://reference.aspose.com/cells/nodejs-cpp/ooxmlcompressiontype)列挙体には、次のメンバーが含まれます。  

- Level1：最速ですがあまり効果的でない圧縮。  
- Level2：少し遅くなりますが、Level1より優れています。  
- Level3：少し遅くなりますが、Level2より優れています。  
- Level4：少し遅くなりますが、Level3より優れています。  
- レベル5：レベル4よりもやや遅く、より効果的な圧縮。  
- レベル6：速度と圧縮効率の良いバランス。  
- Level7：かなり良い圧縮！  
- レベル8：レベル7よりも優れた圧縮！  
- Level9：「最良」の圧縮です。ここでの最良は入力データストリームのサイズを最も小さくすることを意味します。これはまた、最も遅い圧縮でもあります。  

次のコードスニペットは、[**OoxmlCompressionType**](https://reference.aspose.com/cells/nodejs-cpp/ooxmlcompressiontype)列挙型の使用を示し、Level1、Level6、Level9の変換時間を比較します。また、生成されたファイルのサイズを比較することもできます。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source and output directories
const sourceDir = path.join(__dirname, "data");
const outDir = path.join(__dirname, "output");

const filePath = path.join(sourceDir, "LargeSampleFile.xlsx");
const workbook = new AsposeCells.Workbook(filePath);
const options = new AsposeCells.XlsbSaveOptions();

options.setCompressionType(AsposeCells.OoxmlCompressionType.Level1);
let watch = process.hrtime();
workbook.saveAsync(path.join(outDir, "LargeSampleFile_level_1_out.xlsb"), options);
let elapsedMs = process.hrtime(watch);
console.log("Level 1 Elapsed Time: " + (elapsedMs[0] * 1e3 + elapsedMs[1] / 1e6));

watch = process.hrtime();
options.setCompressionType(AsposeCells.OoxmlCompressionType.Level6);
workbook.saveAsync(path.join(outDir, "LargeSampleFile_level_6_out.xlsb"), options);
elapsedMs = process.hrtime(watch);
console.log("Level 6 Elapsed Time: " + (elapsedMs[0] * 1e3 + elapsedMs[1] / 1e6));

watch = process.hrtime();
options.setCompressionType(AsposeCells.OoxmlCompressionType.Level9);
workbook.saveAsync(path.join(outDir, "LargeSampleFile_level_9_out.xlsb"), options);
elapsedMs = process.hrtime(watch);
console.log("Level 9 Elapsed Time: " + (elapsedMs[0] * 1e3 + elapsedMs[1] / 1e6));
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
