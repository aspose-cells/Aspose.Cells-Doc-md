---
title: 導入とアクティベーション
type: docs
weight: 20
url: /ja/sharepoint/deployment-and-activation/
---
{{% alert color="primary" %}} 

[インストール Aspose.Cells for SharePoint](/cells/ja/sharepoint/installing-aspose-cells-for-sharepoint/)インストール プロセスを順を追って説明します。この記事では、インストール プロセスの展開とアクティブ化について説明します。

{{% /alert %}} 
### **展開**
Aspose.Cells for SharePoint は、展開中に次のアクションを実行します。

1. インストール**Aspose.Cells.SharePoint.dll**グローバル アセンブリ キャッシュに追加し、SafeControl エントリを**web.config**ファイル。
1. 機能マニフェストとその他の必要なファイルを適切なディレクトリにインストールします。
1. フィーチャーを SharePoint データベースに登録し、フィーチャー スコープでアクティブ化できるようにします。
### **アクティベーション**
Aspose.Cells for SharePoint は、サイト (サイト コレクション) レベルの機能としてパッケージ化されており、サイト コレクションでアクティブ化および非アクティブ化できます。

アクティブ化中、この機能は、サイト コレクションの親 Web アプリケーションの仮想ディレクトリにいくつかの変更を加えます。

1. 変換設定ページをサイトマップ ファイルに追加します。
1. 必要なリソース ファイルを仮想ディレクトリの App_GlobalResources フォルダーにコピーします。
