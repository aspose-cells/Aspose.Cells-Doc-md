---
title: GridDesktop でのワークシートの拡大縮小
type: docs
weight: 160
url: /ja/net/aspose-cells-griddesktop/zoom-in-or-out-on-the-worksheet-in-griddesktop/
keywords: GridDesktop, 拡大縮小, 拡大, 縮小
description: この記事では、GridDesktop での拡大縮小方法を紹介します。
---

{{% alert color="primary" %}} 

データを扱う際、画面上のコンテンツを実際にフォントサイズを変更せずに拡大したいことがあります。たとえば、テキストを小さいフォントでフォーマットしているかもしれません。（これは印刷時にすべての情報を取得するためにしばしば必要です。）しかし、ワークシートで作業していると、フォントが小さすぎて読みにくい場合があります。

Microsoft Excel では、ドキュメントを素早く簡単に拡大縮小するためのズームスライダーが利用できます。ズームスライダーは通常、ソフトウェアウィンドウの右下隅にあります。

Aspose.Cells では、開発者がワークシートのズーム倍率を設定できるようになっており、その結果、コンテンツは所望のパーセンテージ値に従って表示されるはずです。

{{% /alert %}} 
## **Aspose.Cells.GridDesktop を使用した拡大縮小**
Aspose.Cells は、ワークシートを管理するための多くのプロパティとメソッドを持つ Aspose.Cells.GridDesktop.Worksheet クラスを提供しています。ワークシートのズーム倍率を設定するには、Worksheet クラスの Zoom プロパティを使用します。ズーム倍率は、Zoom プロパティに数値（整数）値を割り当てることで設定されます。

TrackBar (.NET) コントロールを使用して MS Excel のようなズームスライダーを構築します。WinForm プロジェクトで、Toolbox から Aspose.Cells.GridDesktop コントロールをフォームに配置し、その他の設定を行います。次に、GridDesktop コントロールの下に右下隅に TrackBar コントロールを配置し、TrackBar コントロールの値を示す Label コントロールを配置します。TrackBar コントロールのスクロールイベントに関連するコードを追加し、TrackBar コントロールをスクロールすると、GridDesktop がデータ/コンテンツを表示するためにズームインまたはズームアウトします。

以下に、GridDesktop のアクティブなワークシートのズーム倍率を設定する方法を示す例があります。まず、テンプレートの Excel ファイルを GridDesktop にインポートします。

フォームのロードイベントに以下のコードを書き込んで、GridDesktop にテンプレートの Excel ファイルを設定し、トラックバーの値を設定します。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ZoomingInOut-LoadEvent.cs" >}}


次に、トラックスクロールイベント内に以下のコードをコピーしてアプリケーションを実行します。トラックバーを移動すると、ワークシートのズーム倍率が変更されることに気づくでしょう。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ZoomingInOut-ZoomInOut.cs" >}}
