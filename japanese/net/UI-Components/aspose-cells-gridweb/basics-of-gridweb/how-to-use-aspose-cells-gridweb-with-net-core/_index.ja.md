---
title: .NET Core でAspose.Cells.GridWebを使用する方法
type: docs
weight: 40
url: /ja/net/aspose-cells-gridweb/how-to-use-aspose-cells-gridweb-with-net-core/
keywords: GridWeb,dotnetcore
description: この記事では、.net core webアプリケーションでGridWebを使用する方法について紹介します。
---

{{% alert color="primary" %}} 

このトピックでは、Visual Studio.NET 2019を使用して.NET CoreアプリケーションでAspose.Cells.GridWebを使用する方法について説明します。このトピックは、Aspose.Cells.GridWebで作業する初心者レベルの開発者に役立ちます。

{{% /alert %}} 
## **.NET CoreでAspose.Cells.GridWebを使用する**
このトピックでは、Visual Studio 2019でサンプルのウェブサイトを作成することで、Aspose.Cells.GridWebの使用方法を示します。プロセスはステップに分かれています。
### **ステップ1：新しいプロジェクトの作成**
1. Visual Studio 2019を開きます。
1. **ファイル**メニューから**新規**、次に**プロジェクト**を選択します。
   新しいプロジェクトダイアログが開きます。
1. Visual Studioにインストールされたプロジェクトテンプレートから**ASP.NET Core Webアプリケーション**を選択し、**次へ**をクリックします。

![todo:image_alt_text](how-to-use-aspose-cells-gridweb-with-net-core_1.jpg)

1. プロジェクトの場所と名前を指定し、**作成**をクリックします。

![todo:image_alt_text](how-to-use-aspose-cells-gridweb-with-net-core_2.jpg)

1. **Webアプリケーション（モデル-ビュー-コントローラ）**テンプレートを選択し、**ASP .NET Core 2.1**が選択されていることを確認します。 

![todo:image_alt_text](how-to-use-aspose-cells-gridweb-with-net-core_3.jpg)

1. **作成**をクリックします。
### **ステップ2：初期ビューの確認**
新しく作成したプロジェクトを実行すると、ブラウザにデフォルトのテンプレートが表示されます。



![todo:image_alt_text](how-to-use-aspose-cells-gridweb-with-net-core_4.jpg)
### **ステップ3：Aspose.Cells.GridWebの追加**
1. 以下のNugetパッケージをプロジェクトに追加します

<PackageReference Include="Microsoft.AspNetCore.App" />
<PackageReference Include="Microsoft.AspNetCore.Razor.Design" Version="2.1.2" PrivateAssets="All" />
<PackageReference Include="Newtonsoft.Json" Version="12.0.3" />
<PackageReference Include="System.Drawing.Common" Version="4.7.0" />
<PackageReference Include="System.Text.Encoding.CodePages" Version="4.7.0" />

1. Aspose.Cells.GridWebパッケージを追加します

![todo:image_alt_text](how-to-use-aspose-cells-gridweb-with-net-core_5.jpg)

1. **Views**フォルダの**_ViewImports.cshtml**ファイルに以下を追加します。
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "GridWebCore-ViewImports.cs" >}}

変更後のファイルは以下のようになります

![todo:image_alt_text](how-to-use-aspose-cells-gridweb-with-net-core_6.jpg)

1. HomeControllerのIndexメソッドに以下のコードを入れます。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "GridWebCore-HomeController.cs" >}}

{{% alert color="primary" %}} 

SessionStorePathとImportExcelFileのパスを更新することを忘れないでください。

{{% /alert %}} 

![todo:image_alt_text](how-to-use-aspose-cells-gridweb-with-net-core_7.jpg)

1. **View > Home**ディレクトリの**Index.cshtml**ファイルに以下のコードを追加します。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "GridWebCore-IndexView.cs" >}}

変更後のファイルは以下のようになります

![todo:image_alt_text](how-to-use-aspose-cells-gridweb-with-net-core_8.jpg)

1. **Startup.cs**ファイルにSessionサポートとGridScheduedServiceを追加します
   1. **ConfigureServices**メソッドに以下のコードスニペットを追加します。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "GridWebCore-Startup1.cs" >}}

![todo:image_alt_text](how-to-use-aspose-cells-gridweb-with-net-core_9.jpg)

1. **Configure**メソッドに以下のコードスニペットを追加します。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "GridWebCore-Startup2.cs" >}}

![todo:image_alt_text](how-to-use-aspose-cells-gridweb-with-net-core_10.jpg)

最新のacw_clientを**wwwroot/js**ディレクトリに置きます{{% alert color="primary" %}}   {{% /alert %}}
一般的な編集操作のすべてのデフォルト操作を提供できるacwルートマップを処理する**AcwController**を追加します。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "GridWebCore-AcwController.cs" >}}

![todo:image_alt_text](how-to-use-aspose-cells-gridweb-with-net-core_11.jpg)
### **ステップ4：アプリのテスト**
アプリを実行すると、以下の画像に示すような出力が表示されます。

![todo:image_alt_text](how-to-use-aspose-cells-gridweb-with-net-core_12.jpg)
