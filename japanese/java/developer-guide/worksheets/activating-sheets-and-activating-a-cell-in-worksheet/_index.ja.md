---
title: シートのアクティブ化とワークシートでの Cell のアクティブ化
type: docs
weight: 5
url: /ja/java/activating-sheets-and-activating-a-cell-in-worksheet/
---
{{% alert color="primary" %}}

ユーザーが Excel で Microsoft Excel ファイルを開いたときに、特定のワークシートをアクティブにして表示する必要がある場合があります。同様に、特定のセルをアクティブにして、アクティブ セルを表示するようにスクロール バーを設定することもできます。 Aspose.Cells は、以下に示すように、これらすべてのタスクを実行できます。

- アン**アクティブシート**は作業中のシートです。タブ上のアクティブなシートの名前は、デフォルトで太字になっています。
- アン**アクティブセル**選択されたセル (入力を開始したときにデータが入力されるセル) です。一度にアクティブになるセルは 1 つだけです。アクティブ セルは、太い境界線で強調表示されます。

{{% /alert %}}

## **シートの有効化と Cell の有効化**

Aspose.Cells は、シートとセルをアクティブ化するための特定の API 呼び出しを提供します。たとえば、[**WorksheetCollection.ActiveSheetIndex**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#ActiveSheetIndex)プロパティは、ワークブックのアクティブ シートを設定するのに役立ちます。同様に、[**Worksheet.ActiveCell**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#ActiveCell)プロパティを使用して、ワークシート内のアクティブ セルを設定および取得できます。

水平または垂直スクロールバーが、特定のデータを表示したい行と列のインデックス位置にあることを確認するには、[**Worksheet.FirstVisibleRow**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#FirstVisibleRow)と[**Worksheet.FirstVisibleColumn**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#FirstVisibleColumn)プロパティ。

次の例は、ワークシートをアクティブにして、その中にアクティブ セルを作成する方法を示しています。コードを実行すると、次の出力が生成されます。スクロールバーがスクロールされ、2 番目の行と 2 番目の列が最初に表示される行と列になります。

**B2セルをアクティブセルに設定**

![todo:画像_代替_文章](activating-sheets-and-activating-a-cell-in-worksheet_1.png)

## Java Excel でアクティブなワークシートを設定するコード

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ActivatingSheetsandActivatingCell-ActivatingSheetsandActivatingCell.java" >}}

{{% alert color="primary" %}}

の**評価**モード、つまり;有効なライセンスを設定しないと、アクティブなワークシートは常に評価版の透かしを含むものになります。この動作は、アプリケーションの開始時にライセンスを設定することによってのみオーバーライドできます。

{{% /alert %}}
