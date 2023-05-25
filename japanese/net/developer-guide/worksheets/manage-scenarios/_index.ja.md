---
title: ワークシートからのシナリオの作成、操作、または削除
linktitle: シナリオの管理
type: docs
weight: 190
url: /ja/net/create-manipulate-or-remove-scenarios-from-worksheets/
description: この記事では、.NET API を含む C# ライブラリを使用して、プログラムで Excel ワークシートからシナリオを作成、操作、または削除する方法を学習します。
keywords: create scenario worksheet c#, remove scenario excel worksheet c#, manipulate scenario worksheet c#
---
{{% alert color="primary" %}}

場合によっては、スプレッドシートでシナリオを作成、操作、または削除する必要があります。シナリオとは、「もしも？」という名前が付けられたものです。 1 つ以上の数式によってリンクされた変数入力セルを含むモデル。シナリオを作成する前に、異なる値を挿入できるセルに依存する数式が少なくとも 1 つ含まれるようにワークシートを設計します。次の例は、Aspose.Cells API を使用して、ワークブック内のワークシートからシナリオを作成および削除する方法を示しています。

{{% /alert %}}

Aspose.Cells は、いくつかの便利なクラスを提供します。たとえば、[**シナリオコレクション**](https://reference.aspose.com/cells/net/aspose.cells/scenariocollection), [**シナリオ**](https://reference.aspose.com/cells/net/aspose.cells/scenario), [**シナリオ入力セルコレクション**](https://reference.aspose.com/cells/net/aspose.cells/scenarioinputcellcollection)、 と[**シナリオ入力セル**](https://reference.aspose.com/cells/net/aspose.cells/scenarioinputcell)クラス。また、[**ワークシート.シナリオ**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/scenarios)財産。以下のサンプル コードは、いくつかのシナリオを含む XLSX Excel ファイルを開き、既存のシナリオを削除します。また、Excel ファイルを保存する前に、新しいシナリオをワークシートに追加します。この例では、シナリオを含む非常に単純なテンプレート ファイルを使用します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CreateManipulateRemoveScenarios-1.cs" >}}
