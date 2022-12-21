---
title: 元の値を使用してデータを検索する
type: docs
weight: 380
url: /ja/net/search-data-using-original-values/
---
{{% alert color="primary" %}}

何らかの方法でフォーマットされているために、データの値が隠されている場合があります。たとえば、セル D4 に数式 =Sum(A1:A2) があり、その値が 20 であるが --- として書式設定されている場合、値 20 は非表示になり、Microsoft Excel 検索オプションを使用して見つけることができません。ただし、Aspose.Cells を使用して見つけることができます。[**LookInType.OriginalValues**](https://reference.aspose.com/cells/net/aspose.cells/lookintype)

{{% /alert %}}

次のサンプル コードは、上記の点を示しています。 Microsoft Excel検索オプションを使用しても見つからないセルD4が見つかりますが、Aspose.Cellsを使用して見つけることができます[**LookInType.OriginalValues**](https://reference.aspose.com/cells/net/aspose.cells/lookintype).詳細については、コード内のコメントをお読みください。

## C# 元の値を使用してデータを検索するコード

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-SearchDataUsingOriginalValues-SearchDataUsingOriginalValues.cs" >}}

## サンプル コードによって生成されたコンソール出力

上記のサンプル コードのコンソール出力を次に示します。

{{< highlight "java" >}}

Aspose.Cells.Cell [ D4; ValueType : IsNumeric; Value : ---; Formula:=SUM(A1:A2)]{{< /highlight >}}
