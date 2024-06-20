---
title: 元の値を使用してデータを検索
type: docs
weight: 380
url: /ja/net/search-data-using-original-values/
description: Aspose.Cells for .NET APIを介して元の値を使用してデータを検索する方法を学びます。
keywords: 元の値を使用してデータを検索する、元の値を使用してデータを見つける、元の値を使用してデータを検索する、元の値を使用してデータを見つける
---

{{% alert color="primary" %}}

データの値がある形式でフォーマットされているため、値が隠されていることがあります。たとえば、セルD4に式=Sum(A1:A2)があり、その値が20であるが、---としてフォーマットされている場合、値20は非表示であり、Microsoft Excelの検索オプションでは見つけることはできません。ただし、Aspose.Cellsを使用して[**LookInType.OriginalValues**](https://reference.aspose.com/cells/net/aspose.cells/lookintype)を使用してそれを見つけることができます。

{{% /alert %}}

以下のサンプルコードは上記の点を説明しています。Microsoft Excelの検索オプションでは見つけることができないセルD4を見つけますが、Aspose.Cellsを使用して[**LookInType.OriginalValues**](https://reference.aspose.com/cells/net/aspose.cells/lookintype)を使用してそれを見つけることができます。詳細については、コード内のコメントをお読みください。

## C#コードを使用して元の値を検索する

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-SearchDataUsingOriginalValues-SearchDataUsingOriginalValues.cs" >}}

## サンプルコードによって生成されたコンソール出力

上記のサンプルコードのコンソール出力は次の通りです。

{{< highlight java >}}

Aspose.Cells.Cell [ D4; ValueType : IsNumeric; Value : ---; Formula:=SUM(A1:A2)]

{{< /highlight >}}
