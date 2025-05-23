---
title: NuGetを使用してAspose Cellsをインストールします
type: docs
weight: 30
url: /ja/net/installation/
---


## **NuGetを介してAspose.Cells for .NETをインストールします**
.NET用のAspose APIをダウンロードおよびインストールする最も簡単な方法は、Microsoft Visual StudioとNuGetパッケージマネージャを開きます。 "aspose" と検索して、希望のAspose APIを見つけます。「インストール」をクリックすると、選択したAPIがプロジェクトにダウンロードおよび参照されます。

注意: より詳しい情報については、Aspose.CellsのNuGetウェブページをご覧ください: 
[Aspose.Cells for .NET NuGetパッケージ](https://www.nuget.org/packages/Aspose.Cells/)

### **Package Manager GUIを使用してAspose.Cellsをインストールします**
パッケージマネージャーGUIを使用してAspose.Cellsコンポーネントを参照するには、次の手順に従います:

- Visual Studioでソリューション/プロジェクトを開きます。
- ソリューション エクスプローラーを介して同じオプションに簡単にアクセスすることもできます。ソリューションまたはプロジェクトを右クリックし、コンテキストメニューから「NuGetパッケージの管理」を選択します。
- 左側のメニューから「オンライン」を選択し、「Aspose.Cells」と入力してAspose.Cells .NETパッケージを検索します。
- Aspose.Cells for .NETエントリの隣にある「インストール」ボタンをクリックして、最新バージョンをプロジェクトにインストールします。
### **Package Manager Consoleを使用してAspose.Cellsをインストールします**
パッケージマネージャーコンソールを使用してAspose.Cellsコンポーネントを参照するには、次の手順に従います:

- Visual Studioでソリューション/プロジェクトを開きます。
- メニューから「ツール」->「ライブラリ パッケージ マネージャー」->「パッケージ マネージャー コンソール」を選択して、パッケージ マネージャー コンソールを開きます。
  - コマンド「Install-Package Aspose.Cells」を入力し、Enter キーを押して最新の完全リリースをアプリケーションにインストールします。または、「-prerelease」接尾辞をコマンドに追加して、ホットフィックスを含む最新リリースがインストールされるようにすることもできます。
- 「Aspose.Cellsをダウンロードしています...」というメッセージがウィンドウの左下に表示されることを確認できます。
- ダウンロードが完了すると、以下の確認メッセージが表示されます。Aspose EULAに慣れていない場合は、URLで参照されているライセンスを読むのが良いアイデアです。
- これで、Aspose.Cellsが正常にアプリケーションに追加および参照されているはずです。
## **.NETプロジェクトからAspose.Cellsを参照する**
アプリケーションでAspose.Cellsを使用するには、それに参照を追加します。Visual Studio を使用して参照を追加するには:

1. **ソリューション エクスプローラ**で、参照を追加するプロジェクト ノードを展開します。
1. プロジェクトの **参照** ノードを右クリックし、メニューから **参照の追加** を選択します。
1. **参照の追加** ダイアログ ボックスで、.NET タブ (デフォルトで選択されています) を選択します。MSI インストーラを使用してインストールした場合、Aspose.Cells が上のペインに表示されます。
1. それを選択し、**選択** をクリックします。

DLLをダウンロードするか解凍している場合:

1. **[参照]** ボタンを使用して Aspose.Cells.dll ファイルを見つけます。Aspose.Cells は、ダイアログ ボックスの **選択されたコンポーネント** ペインに表示されるはずです。
1. **OK** をクリックします。Aspose.Cells の参照がプロジェクトの **参照** ノードの下に表示されます。
### **VS.NET 2010 クライアント プロファイル プロジェクトからコンポーネントを参照する**
プロジェクトの対象フレームワークが .NET Framework 3.5/4 クライアント プロファイルの場合、インストールディレクトリの net_ClientProfile フォルダにある Aspose.Cells.dll コンポーネント ファイルを使用します。例:

- VS.NET 2010 の **ソリューション エクスプローラ** で、プロジェクトの **参照** を右クリックし、**参照の追加** を選択します。
- ダイアログで **[参照]** タブを選択し、ドロップダウンメニューから **を見る** をクリックします。
- インストールディレクトリ内の Aspose.Cells.dll コンポーネント ファイルを見つけて選択します。例: .../Program Files/Aspose/Aspose.Cells for .NET/Bin/net_ClientProfile/ **(製品をMSIインストーラでインストールしたことを確認してください.)**
- ダイアログを閉じるために **OK** をクリックします。

{{% alert color="primary" %}} 

VS.NET 2010 プロジェクトの対象フレームワークが".NET Framework 4" やその他の場合は、単純に net4.0/net2.0 フォルダにある Aspose.Cells.dll コンポーネント ファイルを使用します。

{{% /alert %}} 
## **Aspose.Cells Grid Controls を .NET プロジェクトから参照する**
アプリケーションでグリッド コントロールを使用するにはそれに参照を追加してください。Visual Studio でグリッド コントロールに参照を追加するには、次の手順を実行します:

- **ソリューション エクスプローラ** で、参照を追加したいプロジェクト ノードを展開します。
- プロジェクトの **参照** ノードを右クリックし、メニューから **参照の追加** を選択します。
- **参照の追加** ダイアログ ボックスで、デフォルトで **.NET タブ** が選択されます。MSI インストーラを使用して Aspose.Cells for .NET をインストールした場合、Aspose.Cells.GridDesktop と Aspose.Cells.GridWeb が上部ペインに表示されます。
- それらを選択して **選択** をクリックします。
- Aspose.Cells.GridDesktop と Aspose.Cells.GridWeb の参照がプロジェクトの参照ノードの下に表示されます。

DLL のみをダウンロードして展開した場合:

- **[参照]** ボタンを使用して Aspose.Cells.GridDesktop.dll および Aspose.Cells.GridWeb.dll ファイルを見つけます。Aspose.Cells Grid Suite が参照され、ダイアログ ボックスの **選択されたコンポーネント** ペインに表示されるはずです。
- **OK.** をクリックします。
## **Aspose.Cells for .NET のアンインストール**
Aspose.Cells for .NET を展開するために MSI インストーラを使用した場合、次の手順に従って完全にコンポーネントとコントロール、関連するデモおよびドキュメントを削除します:

- **スタート** メニューから **設定**、次に **コントロール パネル** を選択します。
- **プログラムの追加と削除** をクリックします。
- Aspose.Cells for .NET (バージョン) を選択します。
- Aspose.Cells を削除するには **変更/削除** をクリックします。
{{< app/cells/assistant language="csharp" >}}
