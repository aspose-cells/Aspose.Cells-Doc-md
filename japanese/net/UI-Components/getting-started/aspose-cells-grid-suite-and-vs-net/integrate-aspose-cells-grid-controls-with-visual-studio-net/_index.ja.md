---
title: Aspose.Cells GridコントロールをVisual Studio.NETに統合する
type: docs
weight: 10
url: /ja/net/integrate-aspose-cells-grid-controls-with-visual-studio-net/
description: この記事では、Visual Studio.NETでGridWebおよびGridDesktopコントロールを使用する方法について説明します。
keywords:  GridWeb,GridDesktop,visual studio,control,integrate
---

{{% alert color="primary" %}} 

Visual Studio.NET開発者は、Aspose.Cells GridスイートをMSIインストーラーとしてダウンロードしたり、一連のDLLパッケージとして入手したりすることができます。この記事では、DLLの代わりにインストーラーを使用してVisual Studio.NETにAspose.Cells.Gridコントロールを統合する際の手順について説明します。

{{% /alert %}} 
## **Visual Studio.NETにAspose.Cells Gridコントロールを統合するには:**
1. ツールボックスを開きます。

1. ツールボックスを開きます。
1. 一般タブ（またはコントロールを追加したい他のタブ）を選択します。
1. 一般タブを右クリックします。
1. Visual Studio.NETで、メニューから**Choose Items**を選択します。カスタマイズ ツールボックス ダイアログが表示されます（このプロセスは、新しいVS.NET IDE（例：VS.NET 2013/2015以降）でもほぼ同じです）。
1. **参照**をクリックして、Aspose.Cells.GridDesktop.dllおよびAspose.Cells.GridWeb.dllファイルを見つけます。
1. DLLを選択して、**開く**をクリックします。カスタマイズ ツールボックス ダイアログには、Aspose.Cells Grid Suiteのコントロールが含まれます。新しく追加されたコントロールは、ダイアログでハイライト表示されます。
1. **OK**をクリックして、コントロールをVisual Studio.NETツールボックスに追加します。

Aspose.Cellsグリッドコントロールがツールボックスの**一般**タブに追加されています。ただし、GridWebコントロールはアクティブではありません。これは、Windowsフォームアプリケーションで作業しているためです。Webフォームで作業している場合にのみGridWebが利用可能であり、GridDesktopはWindowsフォームのみで使用できます。
