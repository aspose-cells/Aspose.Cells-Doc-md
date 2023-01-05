---
title: Aspose.Cells グリッド コントロールを Visual Studio.NET と統合する
type: docs
weight: 10
url: /ja/net/integrate-aspose-cells-grid-controls-with-visual-studio-net/
---
{{% alert color="primary" %}} 

 Visual Studio.NET 開発者は、コントロールを**ツールボックス**Windows または Web フォームに送信します。 Aspose.Cells グリッド スイートは、MSI インストーラーと一緒に、または一連の DLL パッケージとしてダウンロードできます。この記事では、Aspose.Cells.Grid コントロールが、インストーラーではなく DLL を使用してインストールされた Visual Studio.NET で使用できるようにする方法について説明します。

{{% /alert %}} 
## **Aspose.Cells グリッド コントロールを Visual Studio.NET と統合する**
Aspose.Cells Grid コントロールを Visual Studio.NET と統合するには:

1. ツールボックスを開きます。
1. [全般] タブ (またはコントロールを追加するその他のタブ) を選択します。
1. [全般] タブを右クリックします。
1.  Visual Studio.NET 2003 の場合: 選択**アイテムの追加/削除**メニューから。
1. Visual Studio.NET 2005 で、**アイテムを選択**メニューから。 [ツールボックスのカスタマイズ] ダイアログが表示されます (このプロセスは、新しい VS.NET IDE (例: VS.NET 2013/2015 以降) とほぼ同じです)。
1. クリック**ブラウズ** Aspose.Cells.GridDesktop.dll および Aspose.Cells.GridWeb.dll ファイルを見つけます。
1.  DLL を選択してクリックします。**開ける**. [ツールボックスのカスタマイズ] ダイアログに、Aspose.Cells Grid Suite のコントロールが含まれるようになりました。新しく追加されたコントロールは、ダイアログによって強調表示されます。
1. クリック**わかった** Visual Studio.NET ツールボックスにコントロールを追加します。

 Aspose.Cells グリッド コントロールがツールボックスに追加されます**全般的**タブ。 GridWeb コントロールのみがアクティブではありません。これは、Windows Forms アプリケーションで作業しているためです。 GridWeb は Web フォームで作業している場合にのみ使用できますが、GridDesktop は Windows フォームでのみ使用できます。
