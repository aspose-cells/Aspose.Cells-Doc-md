---
title: ICustomFunction機能の使用
description: この記事では、Aspose.CellsライブラリのICustomFunction機能を使用してMicrosoft Excelでカスタム関数を作成する方法について説明します。既存のExcelファイルを読み込むか新しいExcelファイルを作成し、Aspose.Cellsが提供するメソッドを使用してカスタム関数を定義し登録し、結果を取得することができます。最後に、変更したExcelファイルをディスクに保存します。
keywords: Aspose.Cells、Excel、ICustomFunction機能、カスタム関数、カスタム関数の計算方法。
type: docs
weight: 30
url: /ja/net/how-to-calculate-custom-fuctions/
---

{{% alert color="primary" %}} 

この記事では、ICustomFunction機能を使用してAspose.Cells APIでカスタム関数を実装する方法について詳細に説明します。

ICustomFunctionインターフェースを使用すると、特定の要件を満たすためにAspose.Cellsのコア計算エンジンを拡張してカスタム形式計算関数を追加できます。この機能は、テンプレートファイルやコードでカスタム関数を定義し、Aspose.Cells APIを使用して通常のMicrosoft Excel関数と同様に実装および評価できるようにします。

このインターフェースは [AbstractCalculationEngine](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine/) に置き換えられ、将来的には削除されます。新しいAPIに関するいくつかの技術記事/例: [こちら](/cells/ja/net/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/) および [こちら](/cells/ja/net/returning-a-range-of-values-using-abstractcalculationengine/) 。

{{% /alert %}} 
## **ユーザー定義関数の作成と評価**
この記事では、ICustomFunctionインタフェースの実装をデモし、スプレッドシートでカスタム関数を作成し、その結果を取得する方法を説明します。名前が **MyFunc** のカスタム関数を定義し、次の詳細を持つ2つのパラメーターを受け入れるカスタム関数を定義します。

- 1番目のパラメーターは単一のセルを参照します
- 2番目のパラメーターはセル範囲を参照します

カスタム関数は、指定された2番目のパラメーターからすべての値を追加し、1番目のパラメーターの値で結果を除算します。

次は、CalculateCustomFunction メソッドの実装方法です。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-UsingICustomFunctionfeature-ICustomFunction.cs" >}}


新しく定義された関数をスプレッドシートで使用する方法は次のとおりです。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-UsingICustomFunctionfeature-UsingICustomFunctionFeature.cs" >}}
## **概要**
Aspose.Cells API は、対応するパラメータが参照またはその計算結果が参照の場合、「paramsList」に ReferredArea オブジェクトを置きます。参照自体が必要な場合は ReferredArea を直接使用できます。式の位置に対応する参照から単一のセルの値を取得する必要がある場合は、ReferredArea.GetValue(rowOffset, int colOffset) メソッドを使用できます。全体の範囲のセル値の配列が必要な場合は、ReferredArea.GetValues メソッドを使用できます。

Aspose.CellsのAPIが"paramsList"にReferredAreaを与えるため、「contextObjects」でのReferredAreaCollectionはもはや必要ありません(以前のバージョンでは、カスタム関数のパラメーターに常に1対1マップを提供することができなかったため、これが"contextObjects"から削除されました)。

{{< highlight java >}}

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
{{< app/cells/assistant language="csharp" >}}
