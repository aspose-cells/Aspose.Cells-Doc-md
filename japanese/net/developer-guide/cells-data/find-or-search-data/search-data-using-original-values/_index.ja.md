---
title: 元の値を使用したデータの検索
type: docs
weight: 380
url: /ja/net/search-data-using-original-values/
description: Aspose.Cells for .NET API を通じて元の値を使用してデータを検索する方法を学習します。
keywords: Search Data using Original Values, Find Data using Original Values, Search Data by Original Values, Find Data by Original Values
---
{{% alert color="primary" %}}

データが何らかの方法でフォーマットされているために、データの値が非表示になることがあります。たとえば、セル D4 に数式 =Sum(A1:A2) があり、その値が 20 であるが、--- と書式設定されているとします。この場合、値 20 は非表示になり、Microsoft Excel 検索オプションを使用して見つけることができません。ただし、Aspose.Cells を使用すると見つけることができます。[**LookInType.OriginalValues**](https://reference.aspose.com/cells/net/aspose.cells/lookintype)

{{% /alert %}}

次のサンプル コードは、上記の点を示しています。 Excel の検索オプション Microsoft を使用して検索できないセル D4 を検索しますが、Aspose.Cells を使用すると検索できます。[**LookInType.OriginalValues**](https://reference.aspose.com/cells/net/aspose.cells/lookintype)。詳細については、コード内のコメントを読んでください。

##  C# 元の値を使用してデータを検索するコード

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-SearchDataUsingOriginalValues-SearchDataUsingOriginalValues.cs" >}}

## サンプルコードによって生成されたコンソール出力

上記のサンプルコードのコンソール出力を次に示します。

{{< highlight "java" >}}

Aspose.Cells.Cell [ D4; ValueType : IsNumeric; Value : ---; Formula:=SUM(A1:A2)]

{{< /highlight >}}
