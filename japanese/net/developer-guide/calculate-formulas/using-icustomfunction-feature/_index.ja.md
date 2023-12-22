---
title: ICustomFunction 機能の使用
description: この記事では、Aspose.Cells ライブラリの ICustomFunction 機能を使用して、Microsoft Excel でカスタム関数を作成する方法について説明します。既存の Excel ファイルをロードするか、新しい Excel ファイルを作成することで、Aspose.Cells が提供するメソッドを使用してカスタム関数を定義および登録し、結果を取得できます。最後に、変更した Excel ファイルをディスクに保存します。
keywords: Aspose.Cells, Excel, ICustomFunction features, custom functions
type: docs
weight: 30
url: /ja/net/using-icustomfunction-feature/
---
{{% alert color="primary" %}} 

この記事では、ICustomFunction 機能を使用して Aspose.Cells API でカスタム関数を実装する方法について詳しく説明します。

ICustomFunction インターフェイスを使用すると、カスタム数式計算関数を追加して、特定の要件を満たすために Aspose.Cells のコア計算エンジンを拡張できます。この機能は、他の既定の Microsoft Excel 関数と同様に、Aspose.Cells API を使用してカスタム関数を実装および評価できるテンプレート ファイルまたはコードでカスタム (ユーザー定義) 関数を定義する場合に便利です。

このインターフェースは次のものに置き換えられていることに注意してください。[抽象的な計算エンジン](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine/)そして将来的には削除される予定です。新しい API に関するいくつかの技術記事/例:[ここ](/net/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)そして[ここ](/net/returning-a-range-of-values-using-abstractcalculationengine/)

{{% /alert %}} 
##  **ユーザー定義関数の作成と評価**
この記事では、カスタム関数を作成し、それをスプレッドシートで使用して結果を取得するための ICustomFunction インターフェイスの実装について説明します。カスタム関数を名前で定義します**マイファンク**これは、次の詳細を含む 2 つのパラメーターを受け入れます。

- 最初のパラメータは単一のセルを参照します
- 番目のパラメータはセル範囲を参照します

カスタム関数は、2 番目のパラメーターとして指定されたセル範囲のすべての値を加算し、結果を 1 番目のパラメーターの値で除算します。

CalculateCustomFunction メソッドを実装する方法を次に示します。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-UsingICustomFunctionfeature-ICustomFunction.cs" >}}


スプレッドシートで新しく定義した関数を使用する方法は次のとおりです。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-UsingICustomFunctionfeature-UsingICustomFunctionFeature.cs" >}}
##  **概要**
Aspose.Cells API は、対応するパラメーターが参照であるか、その計算結果が参照である場合に、ReferredArea オブジェクトを「paramsList」に入れるだけです。参照自体が必要な場合は、ReferredArea を直接使用できます。数式の位置に対応する参照から単一セルの値を取得する必要がある場合は、ReferredArea.GetValue(rowOffset, intcolOffset) メソッドを使用できます。エリア全体のセル値配列が必要な場合は、ReferredArea.GetValues メソッドを使用できます。

Aspose.Cells API は「paramsList」の ReferredArea を提供するため、「contextObjects」の ReferredAreaCollection は不要になります (古いバージョンでは、常にカスタム関数のパラメーターに 1 対 1 のマップを与えることができませんでした)。 「contextObjects」から削除されました。

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
