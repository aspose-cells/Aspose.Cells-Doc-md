---
title: ワークシート ビュー
type: docs
weight: 10
url: /ja/java/worksheet-views/
---
## **改ページプレビュー**
すべてのワークシートは、次の 2 つのモードで表示できます。

- 通常のビュー。
- 改ページのプレビュー。

通常のビューは、ワークシートの既定のビューです。改ページ プレビューは、印刷時にワークシートを表示する編集ビューです。改ページのプレビューでは、各ページにどのようなデータが表示されるかが表示されるため、印刷範囲と改ページを調整できます。 Aspose.Cells を使用すると、開発者は通常のビューまたは改ページ プレビュー モードを有効にできます。
### **表示モードの制御**
Aspose.Cells は[ワークブック](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)Microsoft Excel ファイルを表すクラス。の[ワークブック](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)クラスには[ワークシート コレクション](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection)これにより、Excel ファイル内の各ワークシートにアクセスできます。

ワークシートは、[ワークシート](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)クラス。の[ワークシート](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)クラスには、ワークシートを管理するためのさまざまなプロパティとメソッドが用意されています。通常または改ページのプレビュー モードを有効にするには、[ワークシート](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)クラス'[setPageBreakPreview](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsPageBreakPreview)方法。
#### **通常表示を有効にする**
を使用して、任意のワークシートを通常のビューに設定します。[setPageBreakPreview](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsPageBreakPreview)の方法[ワークシート](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)クラスと合格**間違い**パラメータとして。
#### **改ページプレビューを有効にする**
を使用して、任意のワークシートを改ページ プレビューに設定します。[setPageBreakPreview](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsPageBreakPreview)の方法[ワークシート](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)クラスと合格**真実**パラメータとして。

の使用を示す完全な例を以下に示します。[ワークシート](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)クラス'[setPageBreakPreview](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsPageBreakPreview)メソッドを使用して、Excel ファイルの最初のワークシートで改ページ プレビュー モードを有効にします。

下のスクリーンショットでは、Book1.xls ファイルが標準表示になっていることがわかります。

**Book1.xls：修正前のワークシート** 

![todo:画像_代替_文章](worksheet-views_1.png)

Book1.xls は、[ワークブック](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)クラスとモードが最初のワークシートの改ページ プレビューに切り替えられます。変更されたファイルは、output.xls として保存されます。

**Output.xls: 修正後のワークシート** 

![todo:画像_代替_文章](worksheet-views_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-PageBreakPreview-PageBreakPreview.java" >}}
## **ズーム倍率**
Microsoft Excel には、ユーザーがワークシートのズームまたは倍率を設定できる機能があります。この機能は、ユーザーがワークシートの内容を小さいビューまたは大きいビューで表示するのに役立ちます。ユーザーはズーム倍率を任意の値に設定できます。

**Microsoft Excel を使用してズーム率を設定する** 

![todo:画像_代替_文章](worksheet-views_3.png)

Aspose.Cells では、開発者がワークシートのズーム率を設定することもできます。
### **ズーム倍率の制御**
Aspose.Cells は[ワークブック](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)Microsoft Excel ファイルを表すクラス。の[ワークブック](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)クラスには[ワークシート コレクション](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection)これにより、Excel ファイル内の各ワークシートにアクセスできます。

ワークシートは、[ワークシート](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)クラス。の[ワークシート](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)クラスには、ワークシートを管理するためのさまざまなプロパティとメソッドが用意されています。ワークシートのズーム倍率を設定するには、[ワークシート](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)クラス'[setZoom](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Zoom)方法。

の使用方法を示す完全な例を以下に示します。[setZoom](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Zoom)メソッドを使用して、Excel ファイルの最初のワークシートの倍率を設定します。

以下のスクリーンショットでは、Book1.xls ファイルがデフォルト ビューで表示されています。

**Book1.xls: 修正前のワークシート** 

![todo:画像_代替_文章](worksheet-views_4.png)

 Book1.xls ファイルは、[ワークブック](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)class で、最初のワークシートのズーム倍率は 75 に設定されています。変更されたファイルは output.xls として保存されます。

**Output.xls: 修正後のワークシート** 

![todo:画像_代替_文章](worksheet-views_5.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-ZoomFactor-ZoomFactor.java" >}}
## **フリーズペイン**
フリーズ ウィンドウは、Microsoft Excel によって提供される機能です。ペインをフリーズすると、ワークシートをスクロールするときにデータを選択して表示したままにすることができます。

**Microsoft Excel でフリーズ ペインを使用する** 

![todo:画像_代替_文章](worksheet-views_6.png)

Aspose.Cells を使用すると、開発者は実行時にフリーズ ペインをワークシートに適用することもできます。

Aspose.Cells は[ワークブック](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) Microsoft Excel ファイルを表すクラス。の[ワークブック](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)クラスには[ワークシート コレクション](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection)これにより、Excel ファイル内の各ワークシートにアクセスできます。

ワークシートは、[ワークシート](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)クラス。の[ワークシート](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)クラスには、ワークシートを管理するためのさまざまなプロパティとメソッドが用意されています。フリーズ ペインを構成するには、[ワークシート](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)クラス'[フリーズペイン](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#freezePanes\(int,%20int,%20int,%20int\)） 方法。の[フリーズペイン](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#freezePanes\(int,%20int,%20int,%20int\)メソッドは、次のパラメーターを取ります。

- **行**、フリーズが開始されるセルの行インデックス。
- **桁**、フリーズが開始されるセルの列インデックス。
- **凍結された行**、上部ペインに表示される行の数。
- **冷凍列**、左ペインに表示される列の数

の使用方法を示す完全な例を以下に示します。[ワークシート](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)クラス'[フリーズペイン](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#freezePanes\(int,%20int,%20int,%20int\)Excel ファイルの最初のワークシートの行と列 (C4 から始まり、4 行目と 3 列目で表され、行と列は 0 インデックスから始まります) を固定するメソッド。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-FreezePanes-FreezePanes.java" >}}


下のスクリーンショットでは、フリーズ ペインのない Book1.xls ファイルを確認できます。

**Book1.xls: 変更前のワークシート ビュー** 

![todo:画像_代替_文章](worksheet-views_7.png)

 Book1.xls ファイルは、[ワークブック](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)クラスを作成すると、最初のワークシートでいくつかの行と列が固定されます。変更されたファイルは、output.xls として保存されます。

**Outlook.xls: 変更後のワークシート ビュー** 

![todo:画像_代替_文章](worksheet-views_8.png)
## **ペインの分割**
同じワークシートに 2 つの異なるビューを表示するために画面を分割する必要がある場合は、ペインを分割します。 Microsoft Excel には、ワークシートの複数のコピーを表示したり、ワークシートの各ペインを個別にスクロールしたりできる非常に便利な機能、分割ペインがあります。

ペインは同時に機能します。一方を変更すると、同時に他方にも変更が反映されます。 Aspose.Cells は、ユーザーに分割ペイン機能を提供します。
### **分割ペインの適用と削除**
#### **ペインの分割**
Aspose.Cells は[ワークブック](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) Microsoft Excel ファイルを表すクラス。の[ワークブック](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)クラスには、Excel ファイルを管理するためのさまざまなプロパティとメソッドが用意されています。分割ビューを実装するには、[ワークシート](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)クラス'[スプリット](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#split\(\)） 方法。分割ペインを削除するには、[removeSplit](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#removeSplit\(\)） 方法。

この例では、読み込まれた単純なテンプレート ファイルを使用し、分割ペインの設定機能が最初のワークシートのセルに適用されます。更新されたファイルが保存されます。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-SplitPanes-SplitPanes.java" >}}



上記のコードを実行すると、生成されたファイルは分割ビューになります。

**出力ファイルでペインを分割する** 

![todo:画像_代替_文章](worksheet-views_9.png)
#### **ペインの削除**
開発者は、[ワークシート](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)クラス'[removeSplit](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#removeSplit\(\)） 方法。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-RemovePanes-RemovePanes.java" >}}


## **先行トピック**
- [ワークシートでゼロ値の表示を非表示にする](/cells/ja/java/hiding-the-display-of-zero-values-in-the-worksheet/)
- [ワークシートのタブの色を設定](/cells/ja/java/set-worksheet-tab-color/)
- [要素の表示と非表示](/cells/ja/java/show-and-hide-elements/)
- [ワークシートで値の代わりに数式を表示する](/cells/ja/java/show-formulas-instead-of-values-in-a-worksheet/)
- [エラー チェック オプションを使用する](/cells/ja/java/use-error-checking-options/)
