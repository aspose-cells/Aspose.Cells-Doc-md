---
title: .NET コアで Aspose.Cells.GridWeb を使用する方法
type: docs
weight: 40
url: /ja/net/how-to-use-aspose-cells-gridweb-with-net-core/
---
{{% alert color="primary" %}} 

このトピックでは、Visual Studio.NET 2019 を使用して .NET コア アプリケーションで Aspose.Cells.GridWeb を使用する方法について説明します。

{{% /alert %}} 
## **.NETコアでAspose.Cells.GridWebを使用**
このトピックでは、Visual Studio 2019 でサンプル Web サイトを作成して、Aspose.Cells.GridWeb を使用する方法を示します。プロセスはステップに分割されています。
### **ステップ 1: 新しいプロジェクトの作成**
1. Visual Studio 2019 を開きます。
1. から**ファイル**メニュー、選択**新しい**、 それから**計画**.
新規プロジェクトの作成ダイアログが開きます。
1. 選択する**ASP.NET コア Web アプリケーション**Visual Studio にインストールされたプロジェクト テンプレートから、**次**.

![todo:画像_代替_文章](how-to-use-aspose-cells-gridweb-with-net-core_1.jpg)

1. プロジェクトの場所と名前を指定してクリックします**作成**.

![todo:画像_代替_文章](how-to-use-aspose-cells-gridweb-with-net-core_2.jpg)

1. を選択**Web アプリケーション (Model-View-Controller)**テンプレートを作成し、**ASP .NET コア 2.1**が選択されます。

![todo:画像_代替_文章](how-to-use-aspose-cells-gridweb-with-net-core_3.jpg)

1. クリック**作成**.
### **ステップ 2: 初期ビューの確認**
新しく作成されたプロジェクトを実行すると、下の画像に示すように、ブラウザーに既定のテンプレートが表示されます。



![todo:画像_代替_文章](how-to-use-aspose-cells-gridweb-with-net-core_4.jpg)
### **ステップ 3: Aspose.Cells.GridWeb を追加する**
1. 次の Nuget パッケージをプロジェクトに追加します

<PackageReference Include="Microsoft.AspNetCore.App" />
<PackageReference Include="Microsoft.AspNetCore.Razor.Design" Version="2.1.2" PrivateAssets="All" />
<PackageReference Include="Newtonsoft.Json" Version="12.0.3" />
<PackageReference Include="System.Drawing.Common" Version="4.7.0" />
<PackageReference Include="System.Text.Encoding.CodePages" Version="4.7.0" />

1. Aspose.Cells.GridWeb パッケージを追加

![todo:画像_代替_文章](how-to-use-aspose-cells-gridweb-with-net-core_5.jpg)

1. Views フォルダーの **_ViewImports.cshtml** ファイルに以下を追加します。
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "GridWebCore-ViewImports.cs" >}}

変更後のファイルは次のようになります

![todo:画像_代替_文章](how-to-use-aspose-cells-gridweb-with-net-core_6.jpg)

1. 次のコードを HomeController の Index メソッドに追加します。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "GridWebCore-HomeController.cs" >}}

{{% alert color="primary" %}} 

SessionStorePath と ImportExcelFile パスを忘れずに更新してください。

{{% /alert %}} 

![todo:画像_代替_文章](how-to-use-aspose-cells-gridweb-with-net-core_7.jpg)

1. に次のコードを追加します。**インデックス.cshtml** View > Home ディレクトリにあるファイル。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "GridWebCore-IndexView.cs" >}}

変更後のファイルは次のようになります。

![todo:画像_代替_文章](how-to-use-aspose-cells-gridweb-with-net-core_8.jpg)

1. Startup.cs ファイルにセッション サポートと GridScheduedService を追加します。
 1. 次のコード スニペットを ConfigureServices メソッドに追加します。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "GridWebCore-Startup1.cs" >}}

![todo:画像_代替_文章](how-to-use-aspose-cells-gridweb-with-net-core_9.jpg)

1. 次のコード スニペットを Configure メソッドに追加します。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "GridWebCore-Startup2.cs" >}}

![todo:画像_代替_文章](how-to-use-aspose-cells-gridweb-with-net-core_10.jpg)

1. 最新の acw_client を次のディレクトリに置きます: **wwwroot/js** {{% alert color="primary" %}} {{% /alert %}}
1. 追加**AcwController**コントローラーで、一般的な編集アクションのすべてのデフォルト操作を提供できる acw ルート マップを処理します。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "GridWebCore-AcwController.cs" >}}

![todo:画像_代替_文章](how-to-use-aspose-cells-gridweb-with-net-core_11.jpg)
### **ステップ 4: アプリをテストする**
アプリを実行すると、下の画像に示すような出力が得られます。

![todo:画像_代替_文章](how-to-use-aspose-cells-gridweb-with-net-core_12.jpg)
