---
title: Aspose.Grid.Web を Aspose.Cells.GridWeb にアップグレード
type: docs
weight: 30
url: /ja/net/upgrade-aspose-grid-web-to-aspose-cells-gridweb/
---
{{% alert color="primary" %}}

アップグレードを容易にするために、既存のユーザー、特に古い Aspose.Grid.Web を使用していて、統合された Aspose.Cells.GridWeb にアップグレードする必要があるユーザーにとって重要な情報を説明するドキュメントを維持しています。

これらは簡単なメモを目的としています。詳細については、[開発者ガイド](/cells/ja/net/developer-guide/).

{{% /alert %}}

## **Aspose.Cells.GridWeb へのアップグレード**

Aspose.Grid.Web ユーザーが新しい Aspose.Cells.GridWeb にアップグレードすると、問題が発生する可能性があります。 Aspose.Grid.Web は名前が変更され、Aspose.Cells の一部になっていることに注意してください。そのため、古いバージョンのコントロールを継続または修正することはありません。

最新の Aspose.Cells.GridWeb コンポーネントにアップグレードするのは難しくありません。

{{% alert color="primary" %}}

API にはいくつかの変更があります。メンバー、構造体、列挙型などを持つクラスは同じままです。ほとんどの変更は、コントロールの名前空間とその他のタグまたは属性に対して行われています。

{{% /alert %}}

以下は、現在変更されている名前空間のリストとその他の属性/タグです。

1. Aspose.Grid.Web 名前空間は Aspose.Cells.GridWeb に名前が変更されました。
1. Aspose.Grid.Web.Data 名前空間は Aspose.Cells.GridWeb.Data に名前が変更されました。
1. Aspose.Grid.Web.Design 名前空間は Aspose.Cells.GridWeb.Design に名前が変更されました。
1. Aspose.Grid.Formula 名前空間は Aspose.Cells.GridFormula に名前が変更され、コンポーネントの最近のリリースでは、この名前空間はパブリック API から完全に削除されました。
1. タグ agw:GridWeb は aspx 形式で acw:GridWeb に変更されました。
1. 古い Aspose.Grid.Web クライアント パス agw_クライアント、acw に変更されました_Aspose.Cells.GridWeb のクライアント。
1.  web.config ファイルのクライアント パス設定。例:

{{< highlight "java" >}}

 <appSettings> 

    <add key="aspose.grid.web.agw_client_path" value="/agw_client/" />

    <add key="aspose.grid.web.force_script_path" value="true" />

</appSettings>



{{< /highlight >}}

に変わりました

{{< highlight "java" >}}

 <appSettings>

    <add key="aspose.cells.gridweb.acw_client_path" value="/acw_client/" />

    <add key="aspose.cells.gridweb.force_script_path" value="true" />

</appSettings>



{{< /highlight >}}
