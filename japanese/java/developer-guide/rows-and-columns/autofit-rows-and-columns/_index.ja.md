---
title: 行および列の自動調整
type: docs
weight: 20
url: /ja/java/autofit-rows-and-columns/
---

{{% alert color="primary" %}} 

Microsoft Excelは、セルの幅と高さをコンテンツに応じて自動的にサイズ変更する便利な機能を提供しています。ランタイムでセルの寸法を自動的にサイズ変更する機能をAspose.Cellsのユーザーも利用することができます。

{{% /alert %}} 
## **自動調整**
[Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)クラスを提供しています。このクラスはMicrosoft Excelファイルを表します。[Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) クラスには、Excelファイル内の各ワークシートにアクセスする[Worksheets](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#Worksheets) コレクションが含まれています。

ワークシートは[Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) クラスで表されます。[Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) クラスは、ワークシートを管理するための多くのプロパティとメソッドを提供しています。この記事では、[Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) クラスを使用して行や列の自動調整を行う方法について説明します。
### **行の自動調整 - シンプル**
行の幅と高さを自動調整する最も直感的な方法は、[Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) クラスの[autoFitRow](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitRow\(int\)) メソッドを呼び出すことです。[autoFitRow](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitRow\(int\)) メソッドには、リサイズされる行のインデックスがパラメータとして必要です。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-AutoFitRowsandColumns-AutoFitRowsandColumns.java" >}}
### **セルの範囲内のコンテンツに基づいて行を自動的に調整するためには、[autoFitRow](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitRow\(int,%20int,%20int\)) メソッドのオーバーロードバージョンを使用して行内のセル範囲で行を自動調整することができます。このメソッドには以下のパラメータが必要です:**
一行は多くの列で構成されます。Aspose.Cellsは、[autoFitRow](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitRow\(int,%20int,%20int\))メソッドのオーバーロードバージョンを呼び出すことで、行のコンテンツに基づいて自動的に行のサイズを調整することを開発者に許可します。次のパラメーターを取ります。

- **行インデックス**：自動調整される行のインデックス。
- **最初の列インデックス**：行の最初の列のインデックス。
- **最後の列インデックス**：行の最後の列のインデックス。

[autoFitRow](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitRow\(int,%20int,%20int\)) メソッドは、行内のすべての列の内容を確認してから行を自動的に調整します。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-AutoFitRowsinaRangeofCells-AutoFitRowsinaRangeofCells.java" >}}
### **列の自動調整 - 簡単な方法**
列の幅と高さを自動調整する最も簡単な方法は、[Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) クラスの[autoFitColumn](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitColumn\(int\)) メソッドを呼び出すことです。[autoFitColumn](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitColumn\(int\)) メソッドには、リサイズされる列のインデックスがパラメータとして必要です。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-AutoFitRowsandColumns-AutoFitRowsandColumns.java" >}}
### **セル範囲の列オートフィット**
1つの列は多くの行で構成されています。列内の範囲のセルの内容に基づいて、[autoFitColumn](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitColumn\(int,%20int,%20int\)) メソッドのオーバーロードされたバージョンを呼び出すことにより、列を自動的にフィットさせることが可能です。

- **列のインデックス**：自動的にフィットする必要のある列のインデックスを表します。
- **最初の行のインデックス**：列の最初の行のインデックスを表します。
- **最後の行のインデックス**：列の最後の行のインデックスを表します。

[autoFitColumn](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitColumn\(int,%20int,%20int\)) メソッドは、列内のすべての行の内容をチェックし、その後列を自動的にフィットさせます。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-AutoFitColumnsinaRangeofCells-AutoFitColumnsinaRangeofCells.java" >}}
### **結合されたセルの行のAutoFit**
Aspose.Cellsを使用して、[AutoFitterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitterOptions) APIを使用して結合セルでも行を自動的にフィットさせることが可能です。[AutoFitterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitterOptions) クラスには、結合セルの行を自動的にフィットさせるために使用できる[AutoFitMergedCellsType](https://reference.aspose.com/cells/java/com.aspose.cells/autofitteroptions#AutoFitMergedCellsType) プロパティがあります。[AutoFitMergedCellsType](https://reference.aspose.com/cells/java/com.aspose.cells/autofitteroptions#AutoFitMergedCellsType) は、次のメンバーを持つ[AutoFitMergedCellsType](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitMergedCellsType) 列挙型を受け入れます。

- [NONE](https://reference.aspose.com/cells/java/com.aspose.cells/autofitmergedcellstype#NONE)：結合セルを無視します。
- [FIRST_LINE](https://reference.aspose.com/cells/java/com.aspose.cells/autofitmergedcellstype#FIRST_LINE)：最初の行の高さのみを拡張します。
- [LAST_LINE](https://reference.aspose.com/cells/java/com.aspose.cells/autofitmergedcellstype#LAST_LINE)：最後の行の高さのみを拡張します。
- [EACH_LINE](https://reference.aspose.com/cells/java/com.aspose.cells/autofitmergedcellstype#EACH_LINE)：各行の高さのみを拡張します。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-RowsAndColumns-AutofitRowsforMergedCells-1.java" >}}

選択した行/列を所望の[AutoFitterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitterOptions) で自動的にフィットするために、範囲の行/列と[AutoFitterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitterOptions) インスタンスを受け入れる[autoFitRows](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitRows\(\)) & [autoFitColumns](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitColumns\(\)) メソッドのオーバーロードされたバージョンも使用できます。

上記のメソッドのシグネチャは次の通りです:

1. autoFitRows(int startRow, int endRow, [AutoFitterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitterOptions) options)
1. autoFitColumns(int firstColumn, int lastColumn, [AutoFitterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitterOptions) options)
## **重要なこと**
{{% alert color="primary" %}} 

セルが結合されている場合、*AutoFit* メソッドは適用されません。これは Microsoft Excel と同じ動作です。さらに、セル内のテキストが折り返されている場合、[autoFitColumn](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitColumn\(int\)) メソッドも適用されません。もう1つ注意すべき点は、*AutoFit* メソッドは時間がかかります。したがって、アプリケーションの効率を確保するためには、これらのメソッドを可能な限り少なく呼び出す必要があります。

{{% /alert %}}
