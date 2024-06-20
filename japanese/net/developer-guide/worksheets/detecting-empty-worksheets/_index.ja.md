---
title: 空のワークシートを検出する
type: docs
weight: 410
url: /ja/net/detecting-empty-worksheets/
description: この記事では、C# APIおよび.NETライブラリを使用してExcelワークブックの空のワークシートをプログラムで検出する方法について説明します。
keywords: C#で空のExcelワークシートを検出する
---

## **空の初期化されたセルのチェック**

ワークシートには、値が入力された1つ以上のセルがある場合があります。値は単純なもの（テキスト、数値、日付/時刻）または式または式に基づく値であることがあります。そのような場合、指定されたワークシートが空かどうかを検出することは簡単です。確認する必要があるのは、[**Cells.MaxDataRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdatarow)または[**Cells.MaxDataColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdatacolumn)プロパティのみです。上記のプロパティがゼロまたは正の値を返す場合、1つ以上のセルが埋められていることを意味します。ただし、これらのプロパティのいずれかが-1を返す場合、指定されたワークシートにセルが1つも埋められていないことを示します。

{{% alert color="primary" %}}

行と列のコレクションは0から始まるインデックスを持っています。そのため、行0および列0のセルは、ワークシート内の最初のセルであるA1を意味します。

{{% /alert %}}

## **空の初期化されたセルのチェック**

値が入力されたセルは自動的に初期化されますが、ワークシートには書式のみが適用されたセルが存在する可能性があります。このようなシナリオでは、[**Cells.MaxDataRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdatarow)または[**Cells.MaxDataColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdatacolumn)プロパティは-1を返すため、値は入力されていないものの初期化されたセルが検出されません。指定されたワークシートに空の初期化されたセルがあるかどうかを確認するには、[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) コレクションから取得した列挙子上でIEnumerator.MoveNextメソッドを使用することが推奨されています。IEnumerator.MoveNextメソッドが**true**を返す場合、指定されたワークシートに1つ以上の初期化されたセルが存在することを示します。

## **図形のチェック**

指定されたワークシートに値が入力されたセルがない場合でも、コントロール、グラフ、画像などの形状やオブジェクトが含まれている可能性があります。ワークシートに形状が含まれているかどうかを確認するには、[**ShapeCollection.Count**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection)プロパティを検査することができます。プラスの値が入力されている場合、ワークシートに形状が存在することを示します。

## **プログラミングサンプル**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-DetectEmptyWorksheets-DetectEmptyWorksheets.cs" >}}
