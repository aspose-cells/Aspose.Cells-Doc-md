---
title: ダイナミック チャートの作成
type: docs
weight: 200
url: /ja/java/create-dynamic-charts/
---
{{% alert color="primary" %}}

動的 (または対話型) グラフには、データの範囲を変更すると変化する機能があります。つまり、動的グラフは、データ ソースが変更されたときに変更を自動的に反映できます。データ ソースの変更をトリガーするには、Excel テーブルのフィルター オプションを使用するか、ComboBox やドロップダウン リストなどのコントロールを使用できます。

この記事では、Aspose.Cells for Java API を使用して、前述の両方のアプローチを使用して動的チャートを作成する方法を示します。

{{% /alert %}}

## **Excel テーブルの使用**

{{% alert color="primary" %}}

Excel テーブルは Aspose.Cells' パースペクティブでは ListObjects と呼ばれるため、明確にするために「テーブル」ではなく「ListObject」という用語を使用します。詳しい方法をお読みください[ListObject を作成する](/cells/ja/java/creating-a-list-object/)Aspose.Cells for .NET API で。

{{% /alert %}}

ListObjects は、ユーザーの操作に基づいてデータを並べ替えおよびフィルター処理する組み込み機能を提供します。 ListObject のヘッダー行に自動的に追加されるドロップダウン リストから、並べ替えとフィルタリングの両方のオプションが提供されます。これらの機能 (並べ替えとフィルタリング) により、ListObject は動的グラフのデータ ソースとして機能するのに最適な候補のようです。 ListObject の状態。

デモンストレーションを理解しやすくするために、ワークブックを最初から作成し、以下に概説するように段階的に進めます。

1. 空のワークブックを作成します。
1. ワークブックの最初のワークシートの Cells にアクセスします。
1. セルにデータを挿入します。
1. 挿入されたデータに基づいて ListObject を作成します。
1. ListObject のデータ範囲に基づいて Chart を作成します。
1. 結果をディスクに保存します。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-UsingExcelTables-UsingExcelTables.java" >}}

## **動的数式の使用**

ListObjects をダイナミック チャートのデータ ソースとして使用したくない場合は、Excel 関数 (または数式) を使用してデータのダイナミック レンジを作成し、コントロール (ComboBox など) を使用して変更をトリガーすることもできます。データで。このシナリオでは、VLOOKUP 関数を使用して、ComboBox の選択に基づいて適切な値を取得します。選択が変更されると、VLOOKUP 関数はセルの値を更新します。セルの範囲が VLOOKUP 関数を使用している場合、ユーザーの操作で範囲全体を更新できるため、ダイナミック チャートのソースとして使用できます。

デモンストレーションを理解しやすくするために、ワークブックを最初から作成し、以下に概説するように段階的に進めます。

1. 空のワークブックを作成します。
1. ワークブックの最初のワークシートの Cells にアクセスします。
1. 名前付き範囲を作成して、セルにデータを挿入します。このデータは、ダイナミック チャートの系列として機能します。
1. 前の手順で作成した名前付き範囲に基づいて ComboBox を作成します。
1. VLOOKUP 関数のソースとなるセルにさらにデータを挿入します。
1. VLOOKUP 関数を (適切なパラメーターを使用して) セル範囲に挿入します。この範囲は、ダイナミック チャートのソースとして機能します。
1. 前の手順で作成した範囲に基づいてチャートを作成します。
1. 結果をディスクに保存します。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-UsingDynamicFormulas-UsingDynamicFormulas.java" >}}
