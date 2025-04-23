---  
title: 元の値を使用してデータを検索
type: docs  
weight: 380  
url: /ja/nodejs-cpp/search-data-using-original-values/  
description: Aspose.Cells for Node.js via C++ APIを使用して、元の値を使ったデータの検索方法を学びましょう。  
keywords: 元の値を使ったデータ検索（Node.js via C++）、元の値を使ったデータ取得（Node.js via C++）、元の値でデータを検索（Node.js via C++）、元の値でデータを見つける（Node.js via C++）  
---  

{{% alert color="primary" %}}  

データの値がある形式でフォーマットされているため、値が隠されていることがあります。たとえば、セルD4に式=Sum(A1:A2)があり、その値が20であるが、---としてフォーマットされている場合、値20は非表示であり、Microsoft Excelの検索オプションでは見つけることはできません。ただし、Aspose.Cellsを使用して[**LookInType.OriginalValues**](https://reference.aspose.com/cells/nodejs-cpp/lookintype)を使用してそれを見つけることができます。  

{{% /alert %}}  

以下のサンプルコードは上記の点を説明しています。Microsoft Excelの検索オプションでは見つけることができないセルD4を見つけますが、Aspose.Cellsを使用して[**LookInType.OriginalValues**](https://reference.aspose.com/cells/nodejs-cpp/lookintype)を使用してそれを見つけることができます。詳細については、コード内のコメントをお読みください。  

## Node.jsで元の値を使ったデータ検索コード例  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-SearchData-SearchDataUsingOriginalValues.js" >}}


## サンプルコードによって生成されたコンソール出力  

上記のサンプルコードのコンソール出力は次の通りです。  

{{< highlight java >}}  

Aspose.Cells.Cell [ D4; ValueType : IsNumeric; Value : ---; Formula:=SUM(A1:A2)]  

{{< /highlight >}}  

