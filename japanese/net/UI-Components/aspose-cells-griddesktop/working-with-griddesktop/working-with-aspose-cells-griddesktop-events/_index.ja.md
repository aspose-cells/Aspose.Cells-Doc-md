---
title: Aspose.Cells.GridDesktop イベントの操作
type: docs
weight: 30
url: /ja/net/working-with-aspose-cells-griddesktop-events/
---
{{% alert color="primary" %}} 

イベントは、コントロールまたはクラスで変更が発生したときに通知を送信するために使用されます。 Aspose.Cells.GridDesktop には、コントロールで特定の変更が発生したときに特定のタスクを実行するために使用されるいくつかのイベントがあります。このトピックでは、Aspose.Cells.GridDesktop コントロールでサポートされているすべてのイベントを紹介し、それらのイベントを処理する方法について説明します。

{{% /alert %}} 
## **序章**
Aspose.Cells.GridDesktop コントロールは、特定のイベントがトリガーされたときに操作を実行するためのより詳細な制御を提供する複数のイベントをサポートします。以下は、Aspose.Cells.GridDesktop コントロールでサポートされているイベントの完全なリストです。

{{% alert color="primary" %}} 

このリストには、Control クラスから Aspose.Cells.GridDesktop によって継承されるイベントは含まれていません。

{{% /alert %}} 

|**イベント**|**説明**|
|:- |:- |
|計算前|ワークブックで数式を計算する前に発生します。|
|BeforeLoadFile|ワークブックがファイルから読み込まれる前に発生します。|
|列ヘッダーのクリック|列ヘッダーがクリックされたときに発生します。|
|列ヘッダーDoubleClick|列ヘッダーがダブルクリックされたときに発生します。|
|CellDataChanged|Grid セル内のデータまたは値が変更されたときに発生します。このイベントは、GridCell の Value プロパティまたは SetCellValue メソッドを使用してプログラムでセルの値が変更された場合にもトリガーされます。|
|セルボタンクリック|セル ボタンがクリックされたときに発生します。|
|CellCheckedChanged|セル チェックボックスの Checked プロパティが変更されたときに発生します。|
|CellSelectedIndexChanged|セル コンボ ボックスの SelectedIndex プロパティが変更されたときに発生します。|
|セルクリック|Grid セルがクリックされたときに発生します。|
|セルダブルクリック|Grid セルがダブルクリックされたときに発生します。|
|CellKeyPressed|セルにフォーカスがあるときにキーが押されると発生します。 CellKeyPressed イベントのイベント ハンドラーを作成する場合は、CellKeyEventArgs 引数の Handled プロパティを true に設定して、GridDesktop コントロールがキー イベントを処理しないようにします。|
|AfterInsertColumns|列が挿入されたときに発生します。 Aspose.Cells.GridDesktop.WorksheetEventArgs 引数の Index プロパティを使用して、列インデックスを取得できます。|
|AfterInsertRows|行が挿入されたときに発生します。 Aspose.Cells.GridDesktop.WorksheetEventArgs 引数の Index プロパティを使用して行インデックスを取得できます。|
|FailLoadFile|ワークブックの読み込みに失敗した場合に発生します。|
|仕上げ計算|ワークブックで数式を計算した後に発生します。|
|FinishLoadFile|ブックが読み込まれたときに発生します。|
|FocusedCellChanged|セルのフォーカスが変更されるたびに発生します。|
|行ヘッダーのクリック|行ヘッダーがクリックされたときに発生します。|
|RowHeaderDoubleClick|行ヘッダーがダブルクリックされたときに発生します。|
|RowColumnHiddenChanged|行または列の非表示ステータスが変更されたときに発生します。|
|選択したシートのインデックスが変更されました|ユーザーが新しいワークシートを選択したとき、つまり、選択したシートが別のワークシートに変更されたときに発生します。このイベントは、GridDesktop コントロールの ActiveSheetIndex プロパティが変更された場合に、プログラムによってトリガーすることもできます。|
## **グリッド イベントの処理**
特定のイベントがトリガーされたときに特定の操作を実行するには、イベント ハンドラーを作成します。イベント ハンドラーは、特定のイベントがトリガーされたときに特定のタスクを実行します。以下では、Visual Studio.NET を使用して単純な Grid イベントを処理するようにイベント ハンドラーが設定されています。

**ステップ 1: Aspose.Cells.GridDesktop コントロールのイベントを選択する**

1. Visual Studio で、Aspose.Cells.GridDesktop コントロールを選択し、その**プロパティ**ダイアログ。
1. クリック**イベント**タブ。
1. イベントを選択します。 (この例では、**セルクリック**イベントが選択されます)。

**ステップ 2: イベント ハンドラーの作成**

1. で選択したイベントをダブルクリックします。**プロパティ**ダイアログ。
1. イベントがダブルクリックされると、Visual Studio.NET によってイベント ハンドラーが作成されます。以下は、GridControl コントロールのイベントが作成されることを示す、デザイナーが生成したコードです。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-GridDesktopEvents.Designer-DesignerGeneratedCode.cs" >}}


ここで、イベント ハンドラー内で目的の操作を実行するコードを追加します。この例では、通知用のメッセージ ボックスを表示するコード行を追加しました。
Visual Studio が GridDesktop コントロールの CellClick イベントに追加したイベント ハンドラーを見てください。以下のコードのようになります。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-GridDesktopEvents-ClickEvent.cs" >}}


**ステップ 3: アプリケーションの実行**

1. アプリケーションをビルドして実行します。
1. グリッド セルをクリックすると、「Cell がクリックされました」というメッセージが表示されたメッセージ ボックスが表示されます。
