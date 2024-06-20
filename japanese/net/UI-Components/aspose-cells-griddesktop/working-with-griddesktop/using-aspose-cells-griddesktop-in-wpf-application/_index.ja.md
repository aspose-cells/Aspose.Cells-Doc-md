---
title: WPFアプリケーションでAspose.Cells.GridDesktopを使用する
type: docs
weight: 50
url: /ja/net/aspose-cells-griddesktop/use-aspose-cells-griddesktop-in-wpf-application/
keywords: GridDesktop,wpf
description: この記事では、WPFアプリケーションでGridDesktopを使用する方法について紹介します。
---

{{% alert color="primary" %}} 

この記事では、Windows Presentation Foundation（WPF）デザイナーを使用して、Aspose.Cells.GridDesktopなどのWindows FormsコントロールをWPFアプリケーションでホストする方法について説明します。 
このプロセスをデモンストレーションするためにVisual Studio 2015を使用しますが、Visual Studio 2008以降を含む任意のバージョンを使用できます。

{{% /alert %}} 

このチュートリアルでは、Aspose.Cells.GridDesktopコントロールをWPFアプリケーションに追加する手順を説明します。WPF開発をサポートするVisual Studio IDEの任意のバージョンを使用して、自分の環境で試すことができます。
## **Visual Studioを使用してWPFアプリケーションを作成します**
まず、Visual Studio IDEを使用してWPFアプリケーションを作成します。**File** >> **New** >> **Project** メニューをクリックし、テンプレートから **WPF Application** を選択し、プロジェクト名を入力して **OK** をクリックします。プロジェクトを2.0以降の任意の.NET Frameworkにターゲット設定できますが、クライアントプロファイル.NET Frameworkでは使用できません。
## **必要な名前空間への参照を追加します**
ソリューションエクスプローラーウィンドウから References を右クリックし、Add Reference メニューを選択して、次のアセンブリに参照を追加します。

- WindowsFormsIntegration アセンブリ (WindowsFormsIntegration.dll)。
- Windows Forms アセンブリ (System.Windows.Forms.dll)。
- Aspose.Cells.GridDesktop アセンブリ (Aspose.Cells.GridDesktop.dll)。

この操作により、必要なアセンブリがアプリケーションに追加され、つまり、アセンブリがアプリケーションの Bin フォルダにコピーされます。
## **XAML への参照を追加**
次に、XAML ファイルに移動し、Windows タグ内に次の名前空間およびアセンブリ参照を追加します。

{{< highlight java >}}

 xmlns:wf="clr-namespace:System.Windows.Forms;assembly=System.Windows.Forms"

xmlns:gridDesktop="clr-namespace:Aspose.Cells.GridDesktop;assembly=Aspose.Cells.GridDesktop">

{{< /highlight >}}

**最終的な Windows タグは以下のようになります。**

![todo:image_alt_text](using-aspose-cells-griddesktop-in-wpf-application_1.png)
## **XAML に Aspose.Cells.GridDesktop コントロールを追加**
単純に、XAML の Grid タグ内に以下のコードを追加します。**WindowsFormsHost** タグは Windows Forms コントロールをホストするために使用され、**gridDesktop:GridDesktop** タグは Aspose.Cells.GridDesktop コントロールを表します。このコントロールに名前を付けて、コードで簡単に参照できるようにすることもできます。

{{< highlight java >}}

 <WindowsFormsHost Loaded="FrameworkElement_OnLoaded">

    <WindowsFormsHost.Child>

        <gridDesktop:GridDesktop x:Name="grid" />

    </WindowsFormsHost.Child>

</WindowsFormsHost>

{{< /highlight >}}

**最終的な XAML は以下のようになります。** 

![todo:image_alt_text](using-aspose-cells-griddesktop-in-wpf-application_2.png)
## **Aspose.Cells.GridDesktop を使用する**
これで、.cs ファイルで他の Windows Forms アプリケーションと同様に Aspose.Cells.GridDesktop コントロールにアクセスして使用できます。デモンストレーションを簡単に保つために、Aspose.Cells.GridDesktop コントロールでサンプルのスプレッドシートをロードして保存するだけです。また、FrameworkElement_OnLoaded イベントを使用して、次のステートメントをトリガーします。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-UsingGridDesktopInWpf-MainWindow.xaml-UsingGridDesktopInWpf.cs" >}}
## **ビルドして実行**
Visual Studio UI の **F5** または **Start** ボタンを使用して、アプリケーションをビルドして実行します。
