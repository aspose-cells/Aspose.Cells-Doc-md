---
title: クライアント側からのフォント設定の更新
type: docs
weight: 170
url: /ja/net/update-font-from-client-side/
---
{{% alert color="primary" %}}

このトピックでは、Aspose.Cells.GridWeb コントロールのクライアント側からのフォント設定の変更について説明します。

{{% /alert %}}

Aspose.Cells GridWeb は、クライアント側からのフォント設定の変更をサポートするようになりました。このために、API は次の機能を提供します。

- **updateCellFontStyle**: Params - 通常/斜体/太字/斜体&&太字の r/i/b/ib
- **updateCellFontSize**: Params - フォント名など 'System'
- **updateCellFontName**: パラメータ - フォントサイズなど「12pt」
- **updateCellFontColor**: パラメータ - none/u/l/ul/ for none/underline/strikout/underline&&strikout
- **updateCellFontLine**: Params - #aa22ee のような html の色、または緑、赤などのよく知られた色の名前...
- **updateCellBackGroundColor**: Params - #aa22ee のような html の色、または緑、赤などのよく知られた色の名前...

次のコード スニペットは、GridWeb でクライアント側からフォント設定を変更する方法を示しています。

## サンプルコード

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples.GridWeb-CSharp-Worksheets-UpdateFontFromClientSide.aspx" >}}
