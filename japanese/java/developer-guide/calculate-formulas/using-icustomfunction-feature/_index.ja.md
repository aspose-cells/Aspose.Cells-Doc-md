---
title: ICustomFunction機能の使用
type: docs
weight: 890
url: /ja/java/how-to-calculate-custom-fuctions/
description: この記事では、Aspose.CellsライブラリのICustomFunction機能を使用してMicrosoft Excelでカスタム関数を作成する方法について説明します。既存のExcelファイルを読み込むか新しいExcelファイルを作成し、Aspose.Cellsが提供するメソッドを使用してカスタム関数を定義し登録し、結果を取得することができます。最後に、変更したExcelファイルをディスクに保存します。
keywords: Aspose.Cells、Excel、ICustomFunction機能、カスタム関数、カスタム関数の計算方法。
---

{{% alert color="primary" %}} 

この記事では、ICustomFunction機能を使用してAspose.Cells APIでカスタム関数を実装する方法について詳細に説明します。

ICustomFunctionインターフェースを使用すると、特定の要件を満たすためにAspose.Cellsのコア計算エンジンを拡張してカスタム形式計算関数を追加できます。この機能は、テンプレートファイルやコードでカスタム関数を定義し、Aspose.Cells APIを使用して通常のMicrosoft Excel関数と同様に実装および評価できるようにします。

ICustomFunctionインターフェースは[AbstractCalculationEngine](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationEngine)に置き換えられ、将来的に削除される予定です。新しいAPIに関する一部の技術記事/例は、[こちら](/cells/ja/java/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)および[こちら](/cells/ja/java/returning-a-range-of-values-using-abstractcalculationengine/)でご確認いただけます。

{{% /alert %}} {{% alert color="primary" %}} 

Aspose.Cells for JavaのAPIが初めての場合は、プロジェクトでAspose.Cells for Javaを取得および参照する方法を知るために[こちら](https://docs.aspose.com/cells/java/installation/)の記事をご覧ください。

{{% /alert %}} 
## **ユーザー定義関数の作成と評価**
この記事では、ICustomFunctionインタフェースの実装をデモし、スプレッドシートでカスタム関数を作成し、その結果を取得する方法を説明します。名前が **MyFunc** のカスタム関数を定義し、次の詳細を持つ2つのパラメーターを受け入れるカスタム関数を定義します。

- 1番目のパラメーターは単一のセルを参照します
- 2番目のパラメーターはセル範囲を参照します

カスタム関数は、指定された2番目のパラメーターからすべての値を追加し、1番目のパラメーターの値で結果を除算します。

calculateCustomFunctionメソッドの実装方法は次のとおりです。

**Java**

{{< highlight csharp >}}

 public class CustomFunction implements ICustomFunction

{

    @Override

    public Object calculateCustomFunction(String functionName, java.util.ArrayList paramsList, java.util.ArrayList contextObjects)

    {

        double result = 0f;

        double sum = 0;

        //Get the value of 1st parameter

        Object firstParamB1 = paramsList.get(0);

        if (firstParamB1 instanceof ReferredArea)

        {

            ReferredArea ra = (ReferredArea)firstParamB1;

            firstParamB1 = ra.getValue(0, 0);

        }

        //Get values of 2nd parameter

        Object secondParamC1C5 = paramsList.get(1);

        if (secondParamC1C5 instanceof ReferredArea)

        {

            ReferredArea ra = (ReferredArea)secondParamC1C5;

            for (int i = ra.getStartRow(); i <= ra.getEndRow(); i++)

            {

                //Add all values

                sum += (double)ra.getValue(i, 0);

            }

        }

        result = sum / (double)firstParamB1;

        // Return result of the function

        return result;

    }

}

{{< /highlight >}}

新しく定義された関数をスプレッドシートで使用する方法は次のとおりです。

**Java**

{{< highlight csharp >}}

 //Open the workbook

Workbook workbook = new Workbook();

//Obtaining the reference of the first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Adding a sample value to "A1" cell

worksheet.getCells().get("B1").putValue(5);

//Adding a sample value to "A2" cell

worksheet.getCells().get("C1").putValue(100);

//Adding a sample value to "A3" cell

worksheet.getCells().get("C2").putValue(150);

//Adding a sample value to "B1" cell

worksheet.getCells().get("C3").putValue(60);

//Adding a sample value to "B2" cell

worksheet.getCells().get("C4").putValue(32);

//Adding a sample value to "B2" cell

worksheet.getCells().get("C5").putValue(62);

//Adding custom formula to Cell A1

worksheet.getCells().get("A1").setFormula("=MyFunc(B1,C1:C5)");

//Calcualating Formulas

workbook.calculateFormula(false, new CustomFunction());

//Assign resultant value to Cell A1

worksheet.getCells().get("A1").putValue(worksheet.getCells().get("A1").getValue());

//Save the file

workbook.save(dir + "UsingICustomFunction.xls");

{{< /highlight >}}
## **概要**
Aspose.CellsのAPIは、対応するパラメーターが参照またはその計算結果が参照の場合、ReferredAreaオブジェクトを"paramsList"に挿入します。参照そのものが必要な場合は、直接ReferredAreaを使用できます。式の位置に応じて参照されたセルから単一のセルの値が必要な場合は、ReferredArea.getValue(rowOffset, int colOffset)メソッドを使用できます。領域全体のセル値配列が必要な場合は、ReferredArea.getValuesメソッドを使用できます。

Aspose.CellsのAPIが"paramsList"にReferredAreaを与えるため、「contextObjects」でのReferredAreaCollectionはもはや必要ありません(以前のバージョンでは、カスタム関数のパラメーターに常に1対1マップを提供することができなかったため、これが"contextObjects"から削除されました)。

{{< highlight java >}}

 public Object calculateCustomFunction(String functionName, ArrayList paramsList, ArrayList contextObjects)

{

    ...

    Object o = paramsList.get(i);

    if(o is ReferredArea) //fetch data from reference

    {

        ReferredArea ra = (ReferredArea)o;

        if(ra.isArea())

        {

            o = ra.getValues();

        }

        else

        {

            o = ra.getValue(0, 0);

        }

    }

    if (o is Array)

    {

        ...

    }

    else if...

    ...

}

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
