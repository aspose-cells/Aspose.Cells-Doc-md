---  
title: Node.jsとC++を用いたエラー検査オプションの使用方法の解説記事  
linktitle: エラーチェックオプションを使用する  
type: docs  
weight: 140  
url: /ja/nodejs-cpp/use-error-checking-options/  
description: Aspose.Cells for Node.js via C++を使って、Excelワークシート内のエラー検出オプションをプログラム的に使用する方法を学びます。  
keywords: エラーがあり、数式が結果を返せない場合（ゼロ除算など）には、すぐに対処が必要で、セルにエラー値が表示されます。緑の三角マークをクリックすると感嘆符が表示され、そのオプションリストが開きます。  
---  

{{% alert color="primary" %}}  
Microsoft Excelでは、ユーザーはエラーチェックのオプションやルールを定義することができます。ユーザーが数式を作成する際にエラーチェックが表示されることがよくあり、セルの右上隅に小さな三角形が表示されます。Excelは、一般的な問題を修正するための情報を提供します。  
{{% /alert %}}  

## **エラーの種類**  

ゼロ除算など、結果を返せない数式を含むエラーは直ちに対処が必要であり、セルにエラー値が表示されます。緑の三角にマウスを合わせると感嘆符が表示され、それをクリックするとオプションのリストが開きます。  

このエラーはオプションで解決または無視できます。無視した場合、そのエラーは次回のエラー検査で表示されません。  

Aspose.Cellsはエラー検査機能を提供します。[**ErrorCheckOption**](https://reference.aspose.com/cells/nodejs-cpp/errorcheckoption)クラスは、数字をテキストとして保存するエラーや数式計算エラー、検証エラーなど、さまざまなタイプのエラー検査を管理します。[**ErrorCheckType**](https://reference.aspose.com/cells/nodejs-cpp/errorchecktype)列挙体を使用して、望ましいエラー検査を設定します。  

## **テキストとして保存された数値**  

時折、数値はセル内でテキストとしてフォーマットされ保存されることがあります。これは計算に問題を引き起こしたり、混乱する並び順を生むことがあります。テキストとしてフォーマットされた数値は、セル内で右寄せではなく左寄せになります。セル内で数学的演算を行うはずの式が値を返さない場合は、式が参照しているセルの配置を確認し、これらのいくつかまたはすべてのセルがテキストとして保存された数値である可能性があります。  

テキストとして保存された数値を実際の数値に素早く変換するために、エラーチェックオプションを使用できます。Microsoft Excel 2003では:  

1. **ツール** メニューで **オプション** をクリックします。  
1. エラーチェックタブを選択します。  
   **テキストとして保存された数値** オプションがデフォルトでチェックされています。  
1. 無効にします。  

次のサンプルコードは、Aspose.CellsのAPIを使用してXLSファイルのワークシートにおいてテキストとして保存された数値のエラーチェックオプションを無効にする方法を示しています。  

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Create a workbook and opening a template spreadsheet
const workbook = new AsposeCells.Workbook(filePath);

// Get the first worksheet
const sheet = workbook.getWorksheets().get(0);
// Instantiate the error checking options
const opts = sheet.getErrorCheckOptions();

const index = opts.add();
const opt = opts.get(index);
// Disable the numbers stored as text option
opt.setErrorCheck(AsposeCells.ErrorCheckType.NumberStoredAsText, false);
// Set the range
opt.addRange(AsposeCells.CellArea.createCellArea(0, 0, 1000, 50));

const outputFilePath = path.join(dataDir, "out_test.out.xlsx");
// Save the Excel file
workbook.save(outputFilePath);
```  
{{< app/cells/assistant language="nodejs-cpp" >}}
