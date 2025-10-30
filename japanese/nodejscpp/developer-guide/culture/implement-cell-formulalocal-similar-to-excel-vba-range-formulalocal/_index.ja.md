---
title: Node.jsを使ったC++経由で、Excel VBAのRange.FormulaLocalに類似したCell.FormulaLocalの実装
linktitle: Excel VBAのRange.FormulaLocalに類似したCell.FormulaLocalの実装
type: docs
weight: 30
url: /ja/nodejs-cpp/implement-cell-formulalocal-similar-to-excel-vba-range-formulalocal/
description: Aspose.Cells for Node.js via C++を使用して、Excel VBAのRange.FormulaLocalに類似したCell.FormulaLocalを実装する方法を学びましょう。 
---

## **可能な使用シナリオ**

Microsoft Excelの数式は、地域や言語によって異なる名前になっていることがあります。例えば、**SUM**関数はドイツ語では**SUMME**と呼ばれます。Aspose.Cellsは英語以外の関数名では動作しません。Microsoft Excel VBAには、その言語や地域に応じた関数名を返す**Range.FormulaLocal**プロパティがあります。Aspose.Cells for Node.js via C++もこの目的のために[**Cell.getFormulaLocal()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getFormulaLocal--)プロパティを提供しています。ただし、このプロパティは[**GlobalizationSettings.getLocalFunctionName(standardName)**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings/#getLocalFunctionName-string-)メソッドを実装したときにのみ機能します。

## **Excel VBAのRange.FormulaLocalと同様にCell.FormulaLocalを実装する**

次のサンプルコードは、[**GlobalizationSettings.getLocalFunctionName(standardName)**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings/#getLocalFunctionName-string-)メソッドを実装する方法を説明しています。このメソッドは、標準関数のローカル名を返します。標準関数が**SUM**の場合、**UserFormulaLocal_SUM**を返します。必要に応じてコードを変更し、正しいローカル関数名（例：ドイツ語では**SUMME**、ロシア語では**ТЕКСТ**）を返してください。以下に示すサンプルコードのコンソール出力も参照してください。

## **サンプルコード**

```javascript
const AsposeCells = require("aspose.cells.node");

class GS extends AsposeCells.GlobalizationSettings {
getLocalFunctionName(standardName) {
// Change the SUM function name as per your needs.
if (standardName === "SUM") {
return "UserFormulaLocal_SUM";
}

// Change the AVERAGE function name as per your needs.
if (standardName === "AVERAGE") {
return "UserFormulaLocal_AVERAGE";
}

return "";
}
}

function run() {
// Create workbook
const wb = new AsposeCells.Workbook();

// Assign GlobalizationSettings implementation class
wb.getSettings().setGlobalizationSettings(new GS());

// Access first worksheet
const ws = wb.getWorksheets().get(0);

// Access some cell
const cell = ws.getCells().get("C4");

// Assign SUM formula and print its FormulaLocal
cell.setFormula("SUM(A1:A2)");
console.log("Formula Local: " + cell.getFormulaLocal());

// Assign AVERAGE formula and print its FormulaLocal
cell.setFormula("=AVERAGE(B1:B2, B5)");
console.log("Formula Local: " + cell.getFormulaLocal());
}

// Call the run function
run();
```

## **コンソール出力**

{{< highlight javascript >}}

Formula Local: =UserFormulaLocal_SUM(A1:A2)

Formula Local: =UserFormulaLocal_AVERAGE(B1:B2,B5)

{{< /highlight >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
