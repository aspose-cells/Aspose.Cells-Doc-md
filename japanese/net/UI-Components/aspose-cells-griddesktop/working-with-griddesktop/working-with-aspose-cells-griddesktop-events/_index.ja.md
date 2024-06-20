---
title: Aspose.Cells.GridDesktop イベントの操作
type: docs
weight: 30
url: /ja/net/aspose-cells-griddesktop/work-with-aspose-cells-griddesktop-events/
keywords: GridDesktop, イベント, イベント
description: この記事では、GridDesktop でイベントを使用する方法について紹介します。
---

{{% alert color="primary" %}} 

イベントは、コントロールやクラスで変更が発生したときに通知を送信するために使用されます。Aspose.Cells.GridDesktop には、コントロールで特定の変更が発生したときに特定のタスクを実行するために使用される複数のイベントがあります。このトピックでは、Aspose.Cells.GridDesktop コントロールでサポートされているすべてのイベントについて紹介し、これらのイベントをどのように処理するかを説明します。

{{% /alert %}} 
## **紹介**
Aspose.Cells.GridDesktop コントロールでは、特定のイベントがトリガーされたときに操作をより細かく制御できる複数のイベントがサポートされています。以下に、Aspose.Cells.GridDesktop コントロールでサポートされているイベントの完全なリストが表示されています。

{{% alert color="primary" %}} 

このリストには、Aspose.Cells.GridDesktop が Control クラスから継承したイベントは含まれていません。

{{% /alert %}} 

|**イベント**|**説明**|
| :- | :- |
|BeforeCalculate|ワークブック内の数式を計算する前に発生します。|
|BeforeLoadFile|ファイルからワークブックが読み込まれる前に発生します。|
|ColumnHeaderClick|列ヘッダーがクリックされたときに発生します。|
|ColumnHeaderDoubleClick|列ヘッダーがダブルクリックされたときに発生します。|
|CellDataChanged|グリッドセル内のデータまたは値が変更されたときに発生します。このイベントは、Value プロパティや GridCell の SetCellValue メソッドを使用してプログラムでセルの値が変更された場合にもトリガーされる可能性があります。|
|CellButtonClick|セルボタンがクリックされたときに発生します。|
|CellCheckedChanged|セルのチェックボックスの Checked プロパティが変更されたときに発生します。|
|CellSelectedIndexChanged|セルコンボボックスの SelectedIndex プロパティが変更されたときに発生します。|
|CellClick|Gridのセルがクリックされたときに発生します。|
|CellDoubleClick|Gridのセルがダブルクリックされたときに発生します。|
|CellKeyPressed|セルにフォーカスがある状態でキーが押されたときに発生します。 CellKeyPressedイベントのイベントハンドラを作成する場合は、Aspose.Cells.GridDesktop.WorksheetEventArgs引数のHandledプロパティをtrueに設定して、GridDesktopコントロールがキーイベントを処理しないようにします。|
|AfterInsertColumns|列が挿入されたときに発生します。Aspose.Cells.GridDesktop.WorksheetEventArgs引数のIndexプロパティを使用して列のインデックスを取得できます。|
|AfterInsertRows|行が挿入されたときに発生します。Aspose.Cells.GridDesktop.WorksheetEventArgs引数のIndexプロパティを使用して行のインデックスを取得できます。|
|FailLoadFile|ブックの読み込みに失敗したときに発生します。|
|FinishCalculate|ブック内の数式の計算処理が終了した後に発生します。|
|FinishLoadFile|ブックが読み込まれたときに発生します。|
|FocusedCellChanged|セルのフォーカスが変更されたときに発生します。|
|RowHeaderClick|行ヘッダがクリックされたときに発生します。|
|RowHeaderDoubleClick|行ヘッダがダブルクリックされたときに発生します。|
|RowColumnHiddenChanged|行または列の非表示状態が変更されたときに発生します。|
|SelectedSheetIndexChanged|ユーザーが新しいワークシートを選択したときに発生します。つまり、選択されたシートが1つのワークシートから別のワークシートに変更されたときに発生します。このイベントは、プログラムによってもトリガーされ、その場合はGridDesktopコントロールのActiveSheetIndexプロパティが変更されたときです。|
## **グリッドイベントの処理**
特定のイベントがトリガーされたときに特定の操作を実行するために、イベントハンドラを作成します。イベントハンドラは、特定のイベントがトリガーされたときに特定のタスクを実行します。以下に、Visual Studio.NETを使用して簡単なGridイベントを処理するためにイベントハンドラを設定する方法が示されています。

**ステップ1：Aspose.Cells.GridDesktopコントロールのイベントの選択**

1. Visual StudioでAspose.Cells.GridDesktopコントロールを選択し、**プロパティ**ダイアログを開きます。
1. **イベント**タブをクリックします。
1. イベントを選択します。（この例では、**CellClick**イベントが選択されます）。

**ステップ2：イベントハンドラの作成**

1. **プロパティ**ダイアログで選択したイベントをダブルクリックします。
1. イベントがダブルクリックされると、Visual Studio.NETによってイベントハンドラが作成されます。以下は、イベントがGridControlコントロールのために作成されるデザイナー生成コードです。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-GridDesktopEvents.Designer-DesignerGeneratedCode.cs" >}}


次に、イベントハンドラの内部に所望の操作を実行するためのコードを追加します。この例では、通知用のメッセージボックスを表示するためのコードを追加しました。 
Visual StudioがGridDesktopコントロールのCellClickイベントに追加したイベントハンドラを確認してください。以下にそのようなコードが表示されます。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-GridDesktopEvents-ClickEvent.cs" >}}


**ステップ3：アプリケーションの実行**

1. アプリケーションをビルドして実行します。
1. グリッドのセルがクリックされるたびに、「セルがクリックされました」というメッセージボックスが表示されます。
