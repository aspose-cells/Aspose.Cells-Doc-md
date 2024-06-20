---
title: ワークシートビュー
type: docs
weight: 10
url: /ja/java/worksheet-views/
---

## **ページブレークプレビュー**
すべてのワークシートは次の2つのモードで表示できます:

- 通常の表示。
- ページブレークプレビュー。

通常ビューはワークシートのデフォルトビューです。ページ区切りプレビューは、ワークシートを印刷時の表示として編集ビューします。ページ区切りプレビューでは、どのデータが各ページに表示されるかが示されるため、印刷エリアやページの区切りを調整できます。Aspose.Cellsを使用すると、通常ビューまたはページ区切りプレビューモードを有効にすることができます。
### **表示モードの制御**
Aspose.Cellsは、Microsoft Excelファイルを表す[Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)クラスを提供します。[Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)クラスには、Excelファイル内の各ワークシートにアクセスできる[WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection)が含まれています。

ワークシートは[Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)クラスによって表されます。[Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)クラスには、ワークシートを管理するための幅広い範囲のプロパティとメソッドが備わっています。通常ビューやページ区切りプレビューモードを有効にするには、[Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)クラスの[setPageBreakPreview](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsPageBreakPreview)メソッドを使用します。
#### **通常の表示の有効化**
ワークシートの[setPageBreakPreview](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsPageBreakPreview)メソッドを使用し、パラメータとして**false**を渡すことで、任意のワークシートを通常ビューに設定します。
#### **ページブレークプレビューの有効化**
ワークシートの[setPageBreakPreview](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsPageBreakPreview)メソッドを使用し、パラメータとして**true**を渡すことで、任意のワークシートをページ区切りプレビューに設定します。

以下は、[Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)クラスの[setPageBreakPreview](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsPageBreakPreview)メソッドの使用を実証する完全な例です。これにより、Excelファイルの最初のワークシートでページ区切りプレビューモードを有効にします。

以下のスクリーンショットでは、Book1.xlsファイルが通常ビューに表示されています。

**Book1.xls: 修正前のワークシート** 

![todo:image_alt_text](worksheet-views_1.png)

Book1.xlsは[Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) クラスで開かれ、最初のワークシートのモードがページ区切りプレビューに切り替えられます。修正されたファイルはoutput.xlsとして保存されます。

**Output.xls: 修正後のワークシート** 

![todo:image_alt_text](worksheet-views_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-PageBreakPreview-PageBreakPreview.java" >}}
## **ズームファクター**
Microsoft Excel には、ワークシートのズームやスケーリング要素を設定する機能があります。この機能は、ユーザーがワークシートの内容を小さなビューまたは大きなビューで表示するのに役立ちます。ユーザーは、ズーム要素を任意の値に設定できます。

**Microsoft Excelでのズームファクターの設定** 

![todo:image_alt_text](worksheet-views_3.png)

Aspose.Cellsは、開発者がワークシートのズームファクターを設定できるようにします。
### **ズームファクターの制御**
Aspose.Cellsは、Microsoft Excelファイルを表す[Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)クラスを提供します。[Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) クラスには、Excelファイル内の各ワークシートにアクセスできる[WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection)が含まれています。

ワークシートは[Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) クラスによって表されます。[Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) クラスには、ワークシートを管理するための幅広い範囲のプロパティとメソッドが備わっています。ワークシートのズームファクターを設定するには、[Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) クラスの[setZoom ](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Zoom)メソッドを使用します。

以下は、Excelファイルの最初のワークシートのズームファクターを設定するために[setZoom ](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Zoom)メソッドの使用方法を示す完全な例です。

以下のスクリーンショットでは、Book1.xlsファイルがデフォルトビューに表示されています。

**Book1.xls: 修正前のワークシート** 

![todo:image_alt_text](worksheet-views_4.png)

Book1.xlsファイルは[Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) クラスで開かれ、最初のワークシートのズームファクターが75に設定されます。修正されたファイルはoutput.xlsとして保存されます。

**Output.xls: モディファイ後のワークシート** 

![todo:image_alt_text](worksheet-views_5.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-ZoomFactor-ZoomFactor.java" >}}
## **ウィンドウ枠の固定**
ウィンドウ枠の固定は、Microsoft Excel が提供する機能です。枠を固定すると、ワークシートをスクロールしても表示され続けるデータを選択できます。

**Microsoft Excel での分割表示の利用方法** 

![todo:image_alt_text](worksheet-views_6.png)

Aspose.Cellsは開発者にワークシートへの分割表示の適用をランタイムで行う機能を提供しています。

Aspose.Cellsは、Microsoft Excelファイルを表す[Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)クラスを提供します。[Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)クラスには、Excelファイルの各ワークシートにアクセスできる[WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection)が含まれています。

ワークシートは[Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)クラスによって表されます。[Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)クラスには、ワークシートを管理するためのさまざまなプロパティやメソッドが提供されています。分割表示を構成するには、[Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)クラスの[freezePanes](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#freezePanes\(int,%20int,%20int,%20int\))メソッドを呼び出します。[freezePanes](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#freezePanes\(int,%20int,%20int,%20int\))メソッドは以下のパラメータを取ります:

- **行**、枠が開始するセルの行インデックス。
- **列**、枠が開始するセルの列インデックス。
- **固定行**、上部枠内に表示される行数。
- **固定列**、左部枠内に表示される列数。

以下に、Excelファイルの最初のワークシートの行と列（0インデックスから始まる）の4番目の行と3番目の列として表されるC4から行と列を固定する[Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)クラスの[freezePanes](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#freezePanes\(int,%20int,%20int,%20int\))メソッドの使用方法を示す完全な例が示されています。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-FreezePanes-FreezePanes.java" >}}


以下のスクリーンショットでは、分割表示がない Book1.xls ファイルが表示されます。

**Book1.xls: 修正前のワークシートビュー** 

![todo:image_alt_text](worksheet-views_7.png)

Book1.xls ファイルを[Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)クラスで開き、その後最初のワークシートにいくつかの行と列を固定します。修正されたファイルは output.xls として保存されます。

**Outlook.xls: 修正後のワークシートビュー** 

![todo:image_alt_text](worksheet-views_8.png)
## **画面の分割**
ワークシート内で二つの異なるビューを取得するには、画面を分割する必要があります。Microsoft Excel は、ワークシートのコピーを複数表示し、各パネで独立してスクロールできる非常に便利な機能を提供しています：画面の分割。

パネは同時に動作します。片方で変更を加えると、同時に他方にも変更が表示されます。Aspose.Cells は、ユーザーに対して画面の分割機能を提供しています。
### **画面の分割の適用と解除**
#### **画面の分割**
ここでは、簡単なテンプレートファイルを読み込んだ後、最初のワークシートのセルに分割表示機能を適用した例が示されています。更新されたファイルは保存されます。

例では、シンプルなテンプレート ファイルをロードして、最初のワークシートのセルに分割パネル機能を適用し、更新されたファイルを保存します。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-SplitPanes-SplitPanes.java" >}}



**出力ファイルの分割表示**

ペインを削除 

![todo:image_alt_text](worksheet-views_9.png)
#### **パネルの削除**
[Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) クラスの [removeSplit](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#removeSplit\(\)) メソッドを使用して分割ウィンドウを削除できます。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-RemovePanes-RemovePanes.java" >}}


## **高度なトピック**
- [ワークシートでゼロの値の表示を非表示にする](/cells/ja/java/hiding-the-display-of-zero-values-in-the-worksheet/)
- [ワークシートタブの色を設定する](/cells/ja/java/set-worksheet-tab-color/)
- [要素を表示および非表示にする](/cells/ja/java/show-and-hide-elements/)
- [ワークシートで値の代わりに数式を表示する](/cells/ja/java/show-formulas-instead-of-values-in-a-worksheet/)
- [エラーチェックオプションを使用する](/cells/ja/java/use-error-checking-options/)
