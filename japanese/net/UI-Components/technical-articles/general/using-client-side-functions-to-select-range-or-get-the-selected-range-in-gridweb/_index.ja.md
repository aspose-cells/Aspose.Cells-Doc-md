---
title: クライアント側の関数を使用して範囲を選択するか、GridWeb で選択した範囲を取得する
type: docs
weight: 60
url: /ja/net/using-client-side-functions-to-select-range-or-get-the-selected-range-in-gridweb/
---
{{% alert color="primary" %}} 

次のクライアント側関数を使用して、範囲を選択したり、JavaScript を使用して GridWeb で選択された範囲を取得したりできます。

- getSelectRange()
- setSelectRange()
- clearSelections()

getSelectRange() は、最後に選択された範囲を返します。 setSelectRange() は、指定された範囲を選択します。 clearSelections() は、現在のアクティブ セルを除くすべての選択をクリアします。

{{% /alert %}} 
## **クライアント側関数を使用して範囲を選択するか、JavaScript を使用して GridWeb で選択された範囲を取得する**
次のコードは、これらの関数の使用法を説明しています。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Articles-UsingClientSideRangeFunctions-UsingRangeFunctions.aspx" >}}
