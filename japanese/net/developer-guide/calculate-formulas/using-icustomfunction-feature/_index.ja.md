---
title: ICustomFunction 機能の使用
type: docs
weight: 30
url: /ja/net/using-icustomfunction-feature/
---
{{% alert color="primary" %}} 

この記事では、ICustomFunction 機能を使用して Aspose.Cells API でカスタム関数を実装する方法について詳しく説明します。

ICustomFunction インターフェイスを使用すると、特定の要件を満たすために、Aspose.Cells のコア計算エンジンを拡張するカスタム数式計算関数を追加できます。この機能は、カスタム (ユーザー定義) 関数をテンプレート ファイルまたはコードで定義する場合に便利です。カスタム関数は、他の既定の Microsoft Excel 関数と同様に、Aspose.Cells API を使用して実装および評価できます。

{{% /alert %}} 
## **ユーザー定義関数の作成と評価**
この記事では、ICustomFunction インターフェイスを実装してカスタム関数を記述し、それをスプレッドシートで使用して結果を取得する方法を示します。カスタム関数を名前で定義します**MyFunc**これは、次の詳細を持つ 2 つのパラメーターを受け入れます。

- 最初のパラメータは単一のセルを参照します
- 番目のパラメーターは、セルの範囲を参照します

カスタム関数は、2 番目のパラメーターとして指定されたセル範囲からすべての値を追加し、結果を 1 番目のパラメーターの値で除算します。

CalculateCustomFunction メソッドを実装する方法を次に示します。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-UsingICustomFunctionfeature-ICustomFunction.cs" >}}


スプレッドシートで新しく定義された関数を使用する方法は次のとおりです



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-UsingICustomFunctionfeature-UsingICustomFunctionFeature.cs" >}}
## **概要**
Aspose.Cells API は、対応するパラメーターが参照であるか、その計算結果が参照である場合、ReferredArea オブジェクトを「paramsList」に入れるだけです。参照自体が必要な場合は、ReferredArea を直接使用できます。数式の位置に対応する参照から単一のセルの値を取得する必要がある場合は、ReferredArea.GetValue(rowOffset, int colOffset) メソッドを使用できます。領域全体のセル値配列が必要な場合は、ReferredArea.GetValues メソッドを使用できます。

Aspose.Cells API は "paramsList" で ReferredArea を提供するため、"contextObjects" での ReferredAreaCollection はもう必要ありません (古いバージョンでは、カスタム関数のパラメーターに常に 1 対 1 のマップを与えることができませんでした)。 「contextObjects」から削除されました。

{{< highlight "java" >}}

 public object CalculateCustomFunction(string functionName, ArrayList paramsList, ArrayList contextObjects)

{

    ...

    object o = paramsList[i];

    if(o is ReferredArea) //fetch data from reference

    {

        ReferredArea ra = (ReferredArea)o;

        if(ra.IsArea)

        {

            o = ra.GetValues();

        }

        else

        {

            o = ra.GetValue(0, 0);

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
