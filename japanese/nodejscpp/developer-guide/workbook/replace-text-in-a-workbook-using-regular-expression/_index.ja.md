---  
title: Node.js経由でC++を使用し、正規表現を用いてワークブック内のテキストを置換  
linktitle: 正規表現を使用してブック内のテキストを置換する  
type: docs  
weight: 90  
url: /ja/nodejs-cpp/replace-text-in-a-workbook-using-regular-expression/  
description: Node.js経由でC++を使用し、正規表現を用いてワークブック内のテキストを置換。  
---  

Aspose.Cellsは、正規表現を用いたワークブック内のテキスト置換機能を提供します。これには、APIの [**ReplaceOptions**](https://reference.aspose.com/cells/nodejs-cpp/replaceoptions) クラスの [**ReplaceOptions.getRegexKey()**](https://reference.aspose.com/cells/nodejs-cpp/replaceoptions/#getRegexKey--) プロパティを使用します。[**ReplaceOptions.getRegexKey()**](https://reference.aspose.com/cells/nodejs-cpp/replaceoptions/#getRegexKey--) を **true** に設定すると、検索キーが正規表現になることを示します。

次のコードスニペットは、[サンプルExcelファイル](101089318.xlsx)を使用して [**ReplaceOptions.getRegexKey()**](https://reference.aspose.com/cells/nodejs-cpp/replaceoptions/#getRegexKey--) プロパティの使用例を示しています。このコードによって生成された [出力ファイル](101089319.xlsx) を参考として添付しています。

## **サンプルコード**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");

// Output directory
const outputDir = path.join(__dirname, "output");

const filePath = path.join(sourceDir, "SampleRegexReplace.xlsx");
const workbook = new AsposeCells.Workbook(filePath);

const replace = new AsposeCells.ReplaceOptions();
replace.setCaseSensitive(false);
replace.setMatchEntireCellContents(false);
// Set to true to indicate that the searched key is regex
replace.setRegexKey(true);

workbook.replace("\\bKIM\\b", "^^^TIM^^^", replace);
workbook.save(path.join(outputDir, "RegexReplace_out.xlsx"));
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
