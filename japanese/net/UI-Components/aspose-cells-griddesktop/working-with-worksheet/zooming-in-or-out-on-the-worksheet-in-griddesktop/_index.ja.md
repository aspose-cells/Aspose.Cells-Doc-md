---
title: GridDesktop でのワークシートのズームインまたはズームアウト
type: docs
weight: 160
url: /ja/net/zooming-in-or-out-on-the-worksheet-in-griddesktop/
---
{{% alert color="primary" %}} 

データを操作しているときに、実際にはフォント サイズを変更せずに画面上のコンテンツを拡大したい場合があります。たとえば、小さいフォントを使用するようにテキストを書式設定している場合があります。 (これは多くの場合、印刷物にすべての情報を取得するために必要です。) ただし、ワークシートで作業する場合、フォントが非常に小さいため読みにくいです。

Microsoft Excel では、ズーム スライダーを使用して、ドキュメントをすばやく簡単に拡大および縮小できます。ズーム スライダーは通常、ソフトウェア ウィンドウの右下隅にあります。

Aspose.Cells では、開発者がワークシートのズーム率を設定することもできるため、目的のパーセンテージ値に従って内容が表示されます。

{{% /alert %}} 
## **Aspose.Cells.GridDesktop を使用したズームインまたはズームアウト**
Aspose.Cells は、ワークシートを管理するための幅広いプロパティとメソッドを持つ Aspose.Cells.GridDesktop.Worksheet クラスを提供します。ワークシートのズーム倍率を設定するには、Worksheet クラスの Zoom プロパティを使用します。ズーム倍率は、数値 (整数) 値を Zoom プロパティに割り当てることによって設定されます。

TrackBar (.NET) コントロールを使用して、MS Excel のようなズーム スライダーを作成します。 WinForm プロジェクトでは、Toolbox から Aspose.Cells.GridDesktop コントロールをフォームに配置し、いくつかのプロパティを指定して、それに応じて名前、サイズ、またはその他の側面を設定します。ここで、TrackBar コントロールを GridDesktop コントロールの下の右下隅に配置し、TrackBar コントロールのハンドルを介して指定したパーセンテージ値を表示する Label コントロールも配置します。 TrackBar の Scroll イベントに相対的なコード行を追加するため、Trackbar コントロールをスクロールすると、GridDesktop はズームインまたはズームアウトして、データ/コンテンツを表示する必要があります。

Zoom プロパティを使用して GridDesktop のアクティブなワークシートのズーム倍率を設定する方法を示す完全な例を以下に示します。まず、テンプレートの Excel ファイルを GridDesktop にインポートします。

フォームの Load イベントに以下のコードを記述して、テンプレートの Excel ファイルを GridDesktop に設定し、トラックバーの値を設定します。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ZoomingInOut-LoadEvent.cs" >}}


以下のコードをトラック スクロール イベント内にコピーして、アプリケーションを実行します。トラック バーを移動すると、ワークシートのズーム プロパティが変更されることがわかります。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ZoomingInOut-ZoomInOut.cs" >}}
