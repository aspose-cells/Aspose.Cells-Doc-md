---
title: エラーチェックオプションを使用する
type: docs
weight: 60
url: /ja/java/use-error-checking-options/
---

{{% alert color="primary" %}} 

Microsoft Excelでは、ユーザーがエラーチェックオプションとルールを定義することができます。ユーザーが数式を作成する際にエラーチェックが表示されることがよくあります。セルの右上隅に小さな三角形が表示され、問題がある場合にこれが強調されます。Excelは、ユーザーが共通の問題を修正できる情報を提供します。

{{% /alert %}} 
## **エラーの種類**
数式が結果を返すことができないことを示すエラー（たとえばゼロで数値を割る）には、直ちに対処する必要があり、セルにエラー値が表示されます。緑色の三角形をクリックすると感嘆符が表示され、これをクリックするとオプションのリストが開きます。 

エラーはオプションを使用して解決したり、無視することができます。エラーを無視すると、以降のエラーチェックにそのエラーが表示されなくなります。

Aspose.Cellsはエラーチェックオプションの機能を提供します。ErrorCheckOptionsクラスは、例えばテキストとして保存された数値、数式の計算エラー、および検証エラーなど、異なる種類のエラーチェックを管理します。ErrorCheckType列挙型を使用して、望ましいエラーチェックを設定します。
## **テキストとして保存された数値**
時折、数値はセル内でテキストとしてフォーマットされ保存されることがあります。これは計算に問題を引き起こしたり、混乱する並び順を生むことがあります。テキストとしてフォーマットされた数値は、セル内で右寄せではなく左寄せになります。セル内で数学的演算を行うはずの式が値を返さない場合は、式が参照しているセルの配置を確認し、これらのいくつかまたはすべてのセルがテキストとして保存された数値である可能性があります。

テキストとして保存された数値を実際の数値に素早く変換するために、エラーチェックオプションを使用できます。Microsoft Excel 2003では:

1. **ツール** メニューで **オプション** をクリックします。
1. エラーチェックタブを選択します。
   **テキストとして保存された数値** オプションがデフォルトでチェックされています。 
1. 無効にします。
   MS Excelのデータに対して緑色の三角形が表示される例を以下の画像で確認してください。

![todo:image_alt_text](use-error-checking-options_1.png)

次のサンプルコードは、Aspose.CellsのAPIを使用してXLSファイルのワークシートにおいてテキストとして保存された数値のエラーチェックオプションを無効にする方法を示しています。 

**Java**

{{< highlight csharp >}}

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
{{< app/cells/assistant language="java" >}}
