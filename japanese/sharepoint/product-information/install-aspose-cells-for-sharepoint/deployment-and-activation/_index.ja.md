---
title: デプロイメントおよびアクティベーション
type: docs
weight: 20
url: /ja/sharepoint/deployment-and-activation/
---

{{% alert color="primary" %}} 

[Aspose.Cells for SharePointのインストール](/cells/ja/sharepoint/installing-aspose-cells-for-sharepoint/)は、インストールプロセスを案内します。この記事は、インストールプロセスが展開およびアクティブ化される内容を説明しています。

{{% /alert %}} 
### **デプロイメント**
Aspose.Cells for SharePointは次のアクションをデプロイ中に実行します：

1. **Aspose.Cells.SharePoint.dll**をグローバルアセンブリキャッシュにインストールし、**web.config**ファイルにSafeControlエントリを追加します。
1. フィーチャーマニフェストとその他必要なファイルを適切なディレクトリにインストールします。
1. フィーチャーをSharePointデータベースに登録し、フィーチャースコープでのアクティベーションが可能にします。
### **Activation**
Aspose.Cells for SharePointはサイト（サイトコレクション）レベルの機能としてパッケージ化されており、サイトコレクションで有効化および無効化ができます。 

有効化中、機能はサイトコレクションの親Webアプリケーションの仮想ディレクトリにいくつかの変更を加えます:

1. サイトマップファイルに変換設定ページを追加します。
1. 必要なリソースファイルを仮想ディレクトリのApp_GlobalResourcesフォルダにコピーします。
