---
title: Aspose.Grid.WebをAspose.Cells.GridWebにアップグレードする
type: docs
weight: 30
url: /ja/net/aspose-cells-gridweb/upgrade-aspose-grid-web-to-aspose-cells-gridweb/
keywords: GridWeb 
description: この記事では、GridWebのアップグレード方法について紹介します。
---

{{% alert color="primary" %}}

アップグレードを容易にするために、既存ユーザー向けに特に古いAspose.Grid.Webを使用し、Aspose.Cells.GridWebにアップグレードする必要があるユーザー向けに重要な情報を記述したドキュメントを維持しています。

これらは簡単なメモのつもりであり、[開発者ガイド](/cells/ja/net/aspose-cells-gridweb/developer-guide/)のセクションを見ることでさらに情報を見つけることができるはずです。

{{% /alert %}}

## **Aspose.Cells.GridWebにアップグレードする**

Aspose.Grid.Webのユーザーは、新しいAspose.Cells.GridWebを使用する際に問題に遭遇する可能性があります。 Aspose.Grid.WebはAspose.Cellsの一部として名前が変更され、旧バージョンのコントロールの継続や修正は行わないことに留意する必要があります。 

最新のAspose.Cells.GridWebコンポーネントへのアップグレードは難しくありません。

{{% alert color="primary" %}}

クラス、構造体、列挙型などのメンバーを持つAPIにはわずかな変更があります。変更の大部分はコントロールの名前空間やその他のタグまたは属性に加えられています。

{{% /alert %}}

以下は、変更された名前空間リストとその他の属性/タグです：

1. Aspose.Grid.Web名前空間はAspose.Cells.GridWebに変更されました。
1. Aspose.Grid.Web.Data名前空間はAspose.Cells.GridWeb.Dataに変更されました。
1. Aspose.Grid.Web.Design名前空間はAspose.Cells.GridWeb.Designに変更されました。
1. Aspose.Grid.Formula名前空間はAspose.Cells.GridFormulaに改名され、コンポーネントの最新リリースでは、該当する名前空間が公開APIから完全に削除されました。
1. aspxフォーム内でagw:GridWebタグがacw:GridWebに変更されました。
1. 以前のAspose.Grid.Webクライアントパスであるagw_clientはAspose.Cells.GridWebのためにacw_clientに変更されました。
1. Web.configファイル内のクライアントパスの設定例： 

{{< highlight java >}}

 <appSettings> 

    <add key="aspose.grid.web.agw_client_path" value="/agw_client/" />

    <add key="aspose.grid.web.force_script_path" value="true" />

</appSettings>



{{< /highlight >}}

から 

{{< highlight java >}}

 <appSettings>

    <add key="aspose.cells.gridweb.acw_client_path" value="/acw_client/" />

    <add key="aspose.cells.gridweb.force_script_path" value="true" />

</appSettings>



{{< /highlight >}}
