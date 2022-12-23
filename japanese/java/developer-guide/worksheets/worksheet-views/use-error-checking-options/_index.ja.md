---
title: エラー チェック オプションを使用する
type: docs
weight: 60
url: /ja/java/use-error-checking-options/
---
{{% alert color="primary" %}} 

Microsoft Excel では、ユーザーがエラー チェックのオプションとルールを定義できます。数式を作成するときにエラー チェックが表示されることがよくあります。セルに問題がある場合は、セルの右上隅にある小さな三角形が強調表示されます。 Excel は、ユーザーが一般的な問題を解決するのに役立つ情報を提供します。

{{% /alert %}} 
## **エラーの種類**
数式が結果を返せないことを意味するエラー (数値をゼロで割るなど) には、すぐに対処する必要があり、エラー値がセルに表示されます。緑色の三角形をクリックすると感嘆符が表示され、これをクリックするとオプションのリストが開きます。

エラーは、オプションを使用して解決するか、無視することができます。エラーを無視すると、それ以降のエラー チェックでそのエラーが表示されなくなります。

Aspose.Cells は、エラー チェック オプション機能を提供します。 ErrorCheckOptions クラスは、さまざまな種類のエラー チェックを管理します。たとえば、テキストとして格納された数値、数式の計算エラー、検証エラーなどです。 ErrorCheckType 列挙体を使用して、目的のエラー チェックを設定します。
## **Numbers テキストとして保存**
場合によっては、数値が書式設定され、テキストとしてセルに格納されることがあります。これにより、計算で問題が発生したり、混乱した並べ替え順序が生成されたりする可能性があります。テキストとして書式設定されている Numbers は、セル内で右揃えではなく左揃えになります。セルに対して算術演算を実行する数式が値を返さない場合は、数式が参照するセルの配置を確認してください。これらのセルの一部またはすべてが、テキストとして書式設定された数値である可能性があります。

エラー チェック オプションを使用して、テキストとして保存されている数値を実数にすばやく変換できます。 Microsoft Excel 2003:

1. 上で**ツール**メニュー、クリック**オプション**.
1. [エラー チェック] タブを選択します。
   **テキストとして保存された数値**オプションはデフォルトでチェックされています。
1. 無効にします。
 MS Excel のデータに対して緑色の三角形がどのように表示されるかについては、下の図を参照してください。

![todo:画像_代替_文章](use-error-checking-options_1.png)

次のサンプル コードは、Aspose.Cells API を使用して、テンプレート XLS ファイル内のワークシートのテキスト エラー チェック オプションとして格納されている数値を無効にする方法を示しています。

**Java**

{{< highlight "csharp" >}}

 //Create a workbook and opening a template spreadsheet

Workbook workbook = new Workbook("d:\\files\\Book1.xls");

//Get the first worksheet

Worksheet sheet = workbook.getWorksheets().get(0);

//Instantiate the error checking options

ErrorCheckOptionCollection opts = sheet.getErrorCheckOptions();

int index = opts.add();

ErrorCheckOption opt = opts.get(index);

//Disable the numbers stored as text option

opt.setErrorCheck(ErrorCheckType.TEXT_NUMBER, false);

//Set the range

opt.addRange(CellArea.createCellArea(0, 0, 65535, 255));

//Save the Excel file

workbook.save("d:\\files\\out_test.xls");



{{< /highlight >}}
