---  
title: オートフィルタを更新した後のすべての非表示行のインデックスを取得する 
type: docs  
weight: 320  
url: /ja/nodejs-cpp/get-all-hidden-rows-indices-after-refreshing-autofilter/  
description: AutoFilterを更新した後にすべての非表示行のインデックスを取得する方法について、Aspose.Cells for Node.js via C++ APIを使用して学習します。  
keywords: AutoFilterをリフレッシュした後のすべての非表示行のインデックスをNode.js(C++)経由で取得  
---  

## **可能な使用シナリオ**  

ワークシートで自動フィルターを適用すると、一部の行が自動的に非表示になります。しかし、エクセルのエンドユーザーによって手動で既に非表示にされている行もあり、それらは自動フィルターによるものではありません。そのため、自動フィルターにより非表示となった行と手動で非表示にされた行を区別することは難しいです。Aspose.Cells for Node.js via C++はこの問題を[**AutoFilter.refresh(hideRows)**](https://reference.aspose.com/cells/nodejs-cpp/autofilter/#refresh-boolean-)配列を用いて解決します。この方法は、自動フィルターによって非表示になったが手動ではない行の行インデックスを返します。  

## **オートフィルタの更新後の非表示行インデックスの取得**  

Excelのエンドユーザーによって手動で非表示になった行を含む[サンプルExcelファイル](64716909.xlsx)をロードし、自動フィルターを適用・更新し、非表示の行のインデックスを返す[**AutoFilter.refresh(hideRows)**](https://reference.aspose.com/cells/nodejs-cpp/autofilter/#refresh-boolean-)メソッドを使用した例。これらのインデックスとセルの名前・値もコンソールに出力されます。  

## **サンプルコード**  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-Autofilter-GetAllHiddenRowsIndicesAfterRefreshingAutoFilter.js" >}}


## **コンソール出力**  

{{< highlight java >}}  

Printing Rows Indices, Cell Names and Values Hidden By AutoFilter.  

\--------------------------  

1       A2      Apple  

2       A3      Apple  

3       A4      Apple  

6       A7      Apple  

7       A8      Apple  

11      A12     Pear  

12      A13     Pear  

{{< /highlight >}}  
