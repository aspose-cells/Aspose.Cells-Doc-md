---
title: WPF アプリケーションで Aspose.Cells.GridDesktop を使用する
type: docs
weight: 50
url: /ja/net/using-aspose-cells-griddesktop-in-wpf-application/
---
{{% alert color="primary" %}} 

この記事では、Windows Presentation Foundation (WPF) Designer for Visual Studio を使用して、WPF アプリケーションで Aspose.Cells.GridDesktop などの Windows フォーム コントロールをホストする方法を示します。
プロセスのデモンストレーションに Visual Studio 2015 を使用しますが、Visual Studio 2008 以降を含む任意のバージョンを使用できます。

{{% /alert %}} 

このチュートリアルでは、Aspose.Cells.GridDesktop コントロールを WPF アプリケーションに追加するプロセスについて説明します。これを試すには、WPF 開発をサポートする Visual Studio IDE の任意のバージョンが必要です。
## **Visual Studio を使用して WPF アプリケーションを作成する**
まず、Visual Studio IDE を使用して WPF アプリケーションを作成します。クリック**ファイル** >> **新しい** >> **計画**メニューと選択**WPF アプリケーション**テンプレートから、プロジェクトに名前を付けてクリックします**わかった**.プロジェクトを 2.0 以上の .NET フレームワークにターゲット設定できますが、クライアント プロファイル .NET フレームワークは使用できません。
## **必要な名前空間への参照を追加する**
[ソリューション エクスプローラー] ウィンドウから [参照] を右クリックし、[参照の追加] メニューを選択して、次のアセンブリへの参照を追加します。

- WindowsFormsIntegration アセンブリ (WindowsFormsIntegration.dll)。
- Windows フォーム アセンブリ (System.Windows.Forms.dll)。
- Aspose.Cells.GridDesktop アセンブリ (Aspose.Cells.GridDesktop.dll)。

このアクションにより、必要なアセンブリがアプリケーションに追加されます。アセンブリをアプリケーションの Bin フォルダーにコピーします。
## **XAML への参照を追加する**
次に、XAML ファイルに移動し、次の名前空間とアセンブリ参照を Windows タグ内に追加します。

{{< highlight "java" >}}

 xmlns:wf="clr-namespace:System.Windows.Forms;assembly=System.Windows.Forms"

xmlns:gridDesktop="clr-namespace:Aspose.Cells.GridDesktop;assembly=Aspose.Cells.GridDesktop">

{{< /highlight >}}

**最後の Windows タグは、次のようになります。**

![todo:画像_代替_文章](using-aspose-cells-griddesktop-in-wpf-application_1.png)
## **Aspose.Cells.GridDesktop コントロールを XAML に追加**
XAML の Grid タグ内に以下のコードを追加するだけです。の**Windowsフォームホスト**タグは、Windows フォーム コントロールと**gridDesktop:GridDesktop**タグは、Aspose.Cells.GridDesktop コントロールを表します。コード内で簡単に参照できるように、コントロールに名前を付けることもできます。

{{< highlight "java" >}}

 <WindowsFormsHost Loaded="FrameworkElement_OnLoaded">

    <WindowsFormsHost.Child>

        <gridDesktop:GridDesktop x:Name="grid" />

    </WindowsFormsHost.Child>

</WindowsFormsHost>

{{< /highlight >}}

**最終的な XAML は次のようになります。** 

![todo:画像_代替_文章](using-aspose-cells-griddesktop-in-wpf-application_2.png)
## **Aspose.Cells.GridDesktop を使用**
これで、他の Windows Forms アプリケーションと同様に、.cs ファイルの Aspose.Cells.GridDesktop コントロールにアクセスして使用できるようになりました。デモンストレーションを簡単にするために、サンプル スプレッドシートを Aspose.Cells.GridDesktop コントロールにロードして保存し直しています。さらに、FrameworkElement_OnLoaded イベントを使用して、次のステートメントをトリガーしました。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-UsingGridDesktopInWpf-MainWindow.xaml-UsingGridDesktopInWpf.cs" >}}
## **ビルドして実行**
次に、次を使用してアプリケーションをビルドして実行します**F5**また**始める** Visual Studio UI のボタン。
