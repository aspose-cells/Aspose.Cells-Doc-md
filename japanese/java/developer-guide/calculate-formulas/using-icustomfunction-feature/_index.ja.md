---
title: ICustomFunction 機能の使用
type: docs
weight: 890
url: /ja/java/using-icustomfunction-feature/
---
{{% alert color="primary" %}} 

この記事では、ICustomFunction 機能を使用して Aspose.Cells API でカスタム関数を実装する方法について詳しく説明します。

ICustomFunction インターフェイスを使用すると、特定の要件を満たすために、Aspose.Cells のコア計算エンジンを拡張するカスタム数式計算関数を追加できます。この機能は、カスタム (ユーザー定義) 関数をテンプレート ファイルまたはコードで定義する場合に便利です。カスタム関数は、他の既定の Microsoft Excel 関数と同様に、Aspose.Cells API を使用して実装および評価できます。

このインターフェイスは、[AbstractCalculationEngine](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationEngine)将来的に削除されます。新しい API に関する技術記事/例:[ここ](/cells/ja/java/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)と[ここ](/cells/ja/java/returning-a-range-of-values-using-abstractcalculationengine/)

{{% /alert %}} {{% alert color="primary" %}} 

 Aspose.Cells for Java API を初めて使用する場合は、チェックしてください[これ](https://docs.aspose.com/cells/java/installation/)プロジェクトで Aspose.Cells for Java を取得して参照する方法については、この記事を参照してください。

{{% /alert %}} 
## **ユーザー定義関数の作成と評価**
この記事では、ICustomFunction インターフェイスを実装してカスタム関数を記述し、それをスプレッドシートで使用して結果を取得する方法を示します。カスタム関数を名前で定義します**MyFunc**これは、次の詳細を持つ 2 つのパラメーターを受け入れます。

- 最初のパラメータは単一のセルを参照します
- 番目のパラメーターは、セルの範囲を参照します

カスタム関数は、2 番目のパラメーターとして指定されたセル範囲からすべての値を追加し、結果を 1 番目のパラメーターの値で除算します。

これが calculateCustomFunction メソッドの実装方法です。

**Java**

{{< highlight "csharp" >}}

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

スプレッドシートで新しく定義された関数を使用する方法は次のとおりです

**Java**

{{< highlight "csharp" >}}

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
Aspose.Cells API は、対応するパラメーターが参照であるか、その計算結果が参照である場合、ReferredArea オブジェクトを「paramsList」に入れるだけです。参照自体が必要な場合は、ReferredArea を直接使用できます。数式の位置に対応する参照から単一セルの値を取得する必要がある場合は、ReferredArea.getValue(rowOffset, int colOffset) メソッドを使用できます。領域全体のセル値配列が必要な場合は、ReferredArea.getValues メソッドを使用できます。

Aspose.Cells API は "paramsList" で ReferredArea を提供するため、"contextObjects" での ReferredAreaCollection はもう必要ありません (古いバージョンでは、カスタム関数のパラメーターに常に 1 対 1 のマップを与えることができませんでした)。 「contextObjects」から削除されました。

{{< highlight "java" >}}

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
