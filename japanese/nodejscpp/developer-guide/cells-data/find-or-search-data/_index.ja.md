---  
title: データの検索または検索
type: docs  
weight: 50  
url: /ja/nodejs-cpp/find-or-search-data/  
description: 指定されたデータを含むセルを見つけたり検索したりする方法について、Aspose.Cells for Node.js via C++ APIを通じて学びます。  
keywords: Node.jsを通じてC++でデータを検索、またはC++でNode.jsを通じてデータを検索、Node.jsを通じてC++で数式を含むセルを検索、またはC++でNode.jsを通じて数式を含むセルを検索、FindOptionsを使用したデータまたは数式検索（Node.js経由）、FindOptionsを使用したデータまたは数式の検索（Node.js経由）、特定の文字列値または数字を含むセルの検索（Node.js経由）、「特定の文字列値または数字を含むセルの検索」、または検索  
---  

{{% alert color="primary" %}}  
Microsoft Excelユーザーは、指定したデータを含むセルを見つけることができます。  
{{% /alert %}}  

## **指定されたデータを含むセルの検索**  

### **Microsoft Excel の使用**  

Microsoft Excelユーザーは、指定したデータを含むセルを見つけることができます。Microsoft Excelの[検索]メニューから[編集]を選択すると、検索値を指定できるダイアログが表示されます。  

ここでは、「オレンジ」の値を検索しています。Aspose.Cellsでは、指定された値を含むワークシート内のセルを検索できます。  

### **Aspose.Cells for Node.js via C++を使用して**  

Aspose.Cellsは、Microsoft Excelファイルを表すクラス[**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)を提供します。[**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)クラスには、Excelファイルの各ワークシートにアクセスできる[**Workbook.getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--)コレクションが含まれます。ワークシートは[**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)クラスで表されます。[**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)クラスは、ワークシート内のすべてのセルを表す[**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--)コレクションを提供します。[**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells)コレクションは、ユーザー指定のデータを含むセルを検索するためのさまざまなメソッドを提供します。これらのメソッドのいくつかについては、以下で詳述します。  

{{% alert color="primary" %}}  
すべての検索メソッドは、指定されたデータを検索するセルの参照を返します。  
{{% /alert %}}  

## **指定された数式を含むセルの検索**  

開発者は、[**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells)コレクションの[**find**](https://reference.aspose.com/cells/nodejs-cpp/cells/#find-object-cell-findoptions-)メソッドを呼び出すことによって、指定された数式をワークシート内で見つけることができます。通常、[**find**](https://reference.aspose.com/cells/nodejs-cpp/cells/#find-object-cell-findoptions-)メソッドは3つのパラメータを受け取ります。  

- **Object:** 検索する対象。型はint、double、DateTime、string、boolのいずれか。  
- **前のセル:** 同じオブジェクトを持つ前のセル。このパラメータは、最初から検索する場合はnullに設定できます。  
- **FindOptions:** 必要なオブジェクトを見つけるためのオプション。  

以下の例では、検索メソッドの練習にワークシートデータを使用します:  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-SearchData-FindCellsContainFormula.js" >}}


## **FindOptionsを使用したデータまたは式の検索**  

さまざまな[**FindOptions**](https://reference.aspose.com/cells/nodejs-cpp/findoptions)を用いて、[**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells)コレクションの[**Cells.find(object, Cell)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#find-object-cell-)メソッドを呼び出すことで、指定された値を検索可能です。通常、[**find**](https://reference.aspose.com/cells/nodejs-cpp/cells/#find-object-cell-findoptions-)メソッドは次のパラメータを受け取ります。  

- **検索値**、検索するデータまたは値。  
- **前のセル**、同じ値を含んでいた最後のセル。最初から検索する場合は、このパラメーターをnullに設定できます。  
- **検索オプション**、検索オプション。  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-SearchData-FindDataUsingFindOptions.js" >}}


## **指定された文字列値を見つけることが可能です。異なる{2}を持つ{1}コレクション内に見つかった{0}メソッドを呼び出すことで。**  

同じ[**find**](https://reference.aspose.com/cells/nodejs-cpp/cells/#find-object-cell-findoptions-)メソッドを[**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells)コレクションで呼び出し、さまざまな[**FindOptions**](https://reference.aspose.com/cells/nodejs-cpp/findoptions)を用いて文字列値を検索できる。  

[**FindOptions.setLookInType**](https://reference.aspose.com/cells/nodejs-cpp/findoptions/#setLookInType-lookintype-)と[**FindOptions.setLookAtType**](https://reference.aspose.com/cells/nodejs-cpp/findoptions/#setLookAtType-lookattype-)のプロパティを指定します。以下の例では、これらのプロパティを使用してセルの文字列の最初、中央、最後にあるさまざまな数の文字列を持つセルを見つける方法を示しています。  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-SearchData-FindCellsContainSpecifyString.js" >}}



## **高度なトピック**  
- [指定したスタイルのセルを見つける](/cells/ja/nodejs-cpp/find-cells-with-specific-style/)  
- [セルの値がシングルクォートマークで始まるかどうかを検索](/cells/ja/nodejs-cpp/find-if-the-cell-value-starts-with-single-quote-mark/)  
- [元の値を使用したデータの検索](/cells/ja/nodejs-cpp/search-data-using-original-values/)  

