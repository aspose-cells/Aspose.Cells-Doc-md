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
行の高さと幅を自動調整する最も簡単な方法は、[Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)クラスの[autoFitRow](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitRow-int-)メソッドを呼び出すことです。 [autoFitRow](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitRow-int-)は、調整する行のインデックスをパラメータとして取ります。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-AutoFitRowsandColumns-AutoFitRowsandColumns.java" >}}
### **セルの範囲内のコンテンツに基づいて行を自動的に調整するためには、[autoFitRow](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitRow\(int,%20int,%20int\)) メソッドのオーバーロードバージョンを使用して行内のセル範囲で行を自動調整することができます。このメソッドには以下のパラメータが必要です:**
行は多くの列で構成されています。Aspose.Cellsでは、行内のセル範囲の内容に基づいて行を自動調整するために、[autoFitRow](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitRow-int-int-int-)メソッドのオーバーロードバージョンを呼び出すことができます。次のパラメータを取ります：

- **行インデックス**：自動調整される行のインデックス。
- **最初の列インデックス**：行の最初の列のインデックス。
- **最後の列インデックス**：行の最後の列のインデックス。

[autoFitRow](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitRow-int-int-int-)メソッドは、行内のすべての列の内容を確認してから、その行を自動調整します。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-AutoFitRowsinaRangeofCells-AutoFitRowsinaRangeofCells.java" >}}
### **列の自動調整 - 簡単な方法**
列の幅と高さを自動調整する最も簡単な方法は、[Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)クラスの[autoFitColumn](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitColumn-int-)メソッドを呼び出すことです。 [autoFitColumn](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitColumn-int-)は、調整したい列のインデックスをパラメータとして取ります。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-AutoFitRowsandColumns-AutoFitRowsandColumns.java" >}}
### **セル範囲の列オートフィット**
列は多くの行で構成されています。列の内容に基づいて列を自動調整するには、[autoFitColumn](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitColumn-int-int-int-)メソッドのオーバーロードバージョンを呼び出します。このメソッドは次のパラメータを取ります：

- **列のインデックス**：自動的にフィットする必要のある列のインデックスを表します。
- **最初の行のインデックス**：列の最初の行のインデックスを表します。
- **最後の行のインデックス**：列の最後の行のインデックスを表します。

[autoFitColumn](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitColumn-int-int-int-)メソッドは、列内のすべての行の内容を確認してから、その列を自動調整します。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-AutoFitColumnsinaRangeofCells-AutoFitColumnsinaRangeofCells.java" >}}
### **結合されたセルの行のAutoFit**
Aspose.Cellsを使用して、[AutoFitterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitterOptions) APIを使用して結合セルでも行を自動的にフィットさせることが可能です。[AutoFitterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitterOptions) クラスには、結合セルの行を自動的にフィットさせるために使用できる[AutoFitMergedCellsType](https://reference.aspose.com/cells/java/com.aspose.cells/autofitteroptions#AutoFitMergedCellsType) プロパティがあります。[AutoFitMergedCellsType](https://reference.aspose.com/cells/java/com.aspose.cells/autofitteroptions#AutoFitMergedCellsType) は、次のメンバーを持つ[AutoFitMergedCellsType](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitMergedCellsType) 列挙型を受け入れます。

- [NONE](https://reference.aspose.com/cells/java/com.aspose.cells/autofitmergedcellstype#NONE)：結合セルを無視します。
- [FIRST_LINE](https://reference.aspose.com/cells/java/com.aspose.cells/autofitmergedcellstype#FIRST-LINE):最初の行の高さのみを拡大します。
- [LAST_LINE](https://reference.aspose.com/cells/java/com.aspose.cells/autofitmergedcellstype#LAST-LINE): 最後の行の高さのみを拡大します。
- [EACH_LINE](https://reference.aspose.com/cells/java/com.aspose.cells/autofitmergedcellstype#EACH-LINE): 各行の高さのみを拡大します。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-RowsAndColumns-AutofitRowsforMergedCells-1.java" >}}

[autoFitRows](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitRows--)および[autoFitColumns](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitColumns--)のオーバーロードバージョンを使用し、行または列の範囲と[AutoFitterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitterOptions)のインスタンスを指定して、選択した行または列を自動調整することもできます。

上記のメソッドのシグネチャは次の通りです:

1. autoFitRows(int startRow, int endRow, [AutoFitterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitterOptions) options)
1. autoFitColumns(int firstColumn, int lastColumn, [AutoFitterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitterOptions) options)
## **重要なこと**
{{% alert color="primary" %}} 

セルが結合されている場合、*AutoFit*メソッドは適用されません。これはMicrosoft Excelと同じ動作です。さらに、セル内のテキストが折り返されている場合も、[autoFitColumn](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitColumn-int-)メソッドは適用されません。もう一つ注意すべき点は、*AutoFit*メソッドは時間がかかることです。そのため、アプリケーションの効率を保つために、これらのメソッドを必要最小限に呼び出すべきです。

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
