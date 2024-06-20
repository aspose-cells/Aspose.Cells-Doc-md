---
title: シートの有効化とワークシート内のセルの有効化
type: docs
weight: 5
url: /ja/java/activating-sheets-and-activating-a-cell-in-worksheet/
---

{{% alert color="primary" %}}

時には、Microsoft ExcelファイルをExcelで開くときに特定のワークシートが有効になり表示されることが求められます。同様に、特定のセルを有効にしてスクロールバーをアクティブなセルを表示するように設定したいことがあります。Aspose.Cellsでは、以下に示すタスクをすべて実行できます。

アクティブな**シート**は、作業中のシートです: タブの上のアクティブなシートの名前は通常太字で表示されます。
アクティブな**セル**は選択されたセルであり、入力を開始するときにデータが入力されるセルです。同時にアクティブなセルは1つだけです。アクティブなセルは太い枠でハイライト表示されます。

{{% /alert %}}

## **シートの有効化とセルのアクティブ化**

Aspose.Cellsでは、ワークブック内のアクティブなシートを設定するために**[**WorksheetCollection.ActiveSheetIndex**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#ActiveSheetIndex) プロパティ**が役立ちます。同様に、ワークシート内のアクティブなセルを設定および取得するために**[**Worksheet.ActiveCell**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#ActiveCell) プロパティ**を使用できます。

特定のデータを表示するために水平または垂直のスクロールバーが行や列のインデックス位置にあることを確認するには、**[**Worksheet.FirstVisibleRow**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#FirstVisibleRow) プロパティ**と**[**Worksheet.FirstVisibleColumn**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#FirstVisibleColumn) プロパティ**を使用します。

以下の例は、ワークシートを有効にし、その中でアクティブなセルを作成する方法を示しています。コードの実行時に生成される出力は次のとおりです。スクロールバーは1番目の可視行および列として2行目と2列目にスクロールされています。

**B2セルをアクティブセルとして設定**

![todo:image_alt_text](activating-sheets-and-activating-a-cell-in-worksheet_1.png)

## Excelでアクティブなワークシートを設定するJavaコード

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ActivatingSheetsandActivatingCell-ActivatingSheetsandActivatingCell.java" >}}

{{% alert color="primary" %}}

**評価**モード（有効なライセンスを設定しない状態）では、アクティブなワークシートは常に評価用途の透かしを含むワークシートになります。この動作はアプリケーションの開始時にライセンスを設定することでのみ上書きできます。

{{% /alert %}}
