---  
title: Node.jsとC++を利用してテンプレートファイルからワークブックを読み込むときにデータの種類をフィルタする例  
linktitle: テンプレートファイルからワークブックをロードする際にデータの種類をフィルタリングする  
type: docs  
weight: 400  
url: /ja/nodejs-cpp/filtering-the-kind-of-data-while-loading-the-workbook-from-template-file/  
---  

{{% alert color="primary" %}}  
時には、テンプレートファイルからワークブックを作成するときにどの種類のデータを読み込むかを指定したいことがあります。読み込みデータのフィルタは、特に[LightCells API](/cells/ja/nodejs-cpp/using-lightcells-api/)を使用している場合にパフォーマンスを向上させることができます。この目的には[**LoadOptions.getLoadFilter()**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions/#getLoadFilter--)プロパティを使用してください。  
{{% /alert %}}  

以下のサンプルコードは、ダウンロードリンクから取得したテンプレートファイル（5115552.xlsx）を読み込む際に、シェイプオブジェクトのみをロードします。スクリーンショットは、テンプレートファイルの内容と、赤色と黄色の背景のデータが[**LoadOptions.getLoadFilter()**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions/#getLoadFilter--)プロパティを[**Shape**](https://reference.aspose.com/cells/nodejs-cpp/shape/)に設定しているために読み込まれないことを示しています。  

![todo:image_alt_text](filtering-the-kind-of-data-while-loading-the-workbook-from-template-file_1.png)  

[指定されたリンク](5115555.pdf)からダウンロードできる出力PDFです。ここでは、赤色および黄色の背景のデータが存在しない一方、すべての形状が存在することが分かります。  

![todo:image_alt_text](filtering-the-kind-of-data-while-loading-the-workbook-from-template-file_2.png)  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");

// Output directory
const outputDir = path.join(__dirname, "output");

// Set the load options, we only want to load shapes and do not want to load data
const loadOptions = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Xlsx);            

loadOptions.setLoadFilter(new AsposeCells.LoadFilter(AsposeCells.LoadDataFilterOptions.All & ~AsposeCells.LoadDataFilterOptions.Chart));

// Create workbook object from sample excel file using load options
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "sampleFilterChars.xlsx"), loadOptions);

// Save the output in pdf format
workbook.save(outputDir + "sampleFilterChars_out.pdf", AsposeCells.SaveFormat.Pdf);
```  

