---
title: スプレッドシート エディタ はじめに
type: docs
weight: 10
url: /ja/java/spreadsheet-editor-getting-started/
---
**目次**

- [序章](#SpreadsheetEditorGettingStarted-Introduction)
- [システム要求](#SpreadsheetEditorGettingStarted-SystemRequirements)
- [ダウンロードとインストール](#SpreadsheetEditorGettingStarted-DownloadandInstallation)
- [サポート](#SpreadsheetEditorGettingStarted-Support)
- [助ける](#SpreadsheetEditorGettingStarted-Contribute)
- [ライセンス](#SpreadsheetEditorGettingStarted-License)
### **序章**
Html5 スプレッドシート エディターは、Web ブラウザーでスプレッドシート ドキュメントを表示および編集できる Web アプリケーションです。 Excel、SpreadsheetML、CVS、OpenDocument、および Microsoft Excel でサポートされている他の多くの形式をサポートしています。セルの編集、書式設定、数式の編集、行と列の管理など、すべての基本機能がサポートされています。

![todo:画像_代替_文章](aowcrc1.png)

 HTML5 スプレッドシート エディターは、[Aspose.Cells for Java](https://products.aspose.com/cells/java/)また、それらを使用して、Java アプリケーションでスプレッドシートを作成、操作、およびレンダリングする方法を示します。

**特徴**

- ファイルの操作
 対応フォーマット
 ローカルファイルを開く
 Dropbox から開く
 URLから開く
 新しいスプレッドシートを作成する
 さまざまな形式にエクスポート
- シートの操作
 シートの追加と削除
 シートの名前を変更
 シートを切り替える
- 行と列の操作
 行を追加
 列を追加
 行を削除
 列を削除
 列の幅と行の高さ
- Cellsでの作業
 セルの選択
 セルの編集
 式の編集
 Cell アライメント
 クリア Cell
 - セルを追加
 セルを削除
- テキスト書式設定の操作
 太字、斜体、下線
 フォントのスタイルとサイズ
 クリアフォーマット
### **システム要求**
**ソフトウェア要件**

- CDI 対応 Java アプリケーションサーバー
- [Aspose.Cells for Java](https://products.aspose.com/cells/java/)
- [JavaServer Faces 2.0](https://javaee.github.io/javaserverfaces-spec/)
- [プライムフェイス5.1](https://www.primefaces.org/)

**ハードウェア要件**

ハードウェア要件は、HTML5 スプレッドシート エディターをデプロイするために選択した Java アプリケーション サーバーと、同時に開くスプレッドシートの数によって異なります。以下は概算で、環境の初期設定に役立ちます。

- 2GHzのCPU
- 2GBのRAM
- 500MBのディスク
### **ダウンロードとインストール**
HTML5 Spreadsheet Editor は Java EE アプリケーションであり、CDI をサポートする任意の Java アプリケーション サーバー Web プロファイルにデプロイできます。でテストされています[グラスフィッシュ](https://javaee.github.io/glassfish/).

**ソースコード**

プロジェクトのソースは次の場所にあります。[ギットハブ](https://github.com/aspose-cells/Aspose.Cells-for-Java/).また、次のサイトで Git ミラーを維持しています。

- [ビットバケット](https://bitbucket.org/asposeshowcase/html5_spreadsheet_editor_by_aspose.cells_for_java)
- [Google コード](https://code.google.com/archive/p/html5-spreadsheet-editor/)
- [ソースフォージ](https://sourceforge.net/p/html5-spreadsheet-editor/)

次のいずれかのコマンドを使用して、コマンド ラインからソース コードをダウンロードします。

**ギットハブ**

{{< highlight "bash" >}}

 git clone https://github.com/aspose-cells/Aspose.Cells-for-Java.git

{{< /highlight >}}

**ビットバケット**

{{< highlight "bash" >}}

 git clone https://bitbucket.org/asposeshowcase/html5_spreadsheet_editor_by_aspose.cells_for_java.git

{{< /highlight >}}

**Google コード**

{{< highlight "bash" >}}

 git clone https://code.google.com/p/html5-spreadsheet-editor/

{{< /highlight >}}

**ソースフォージ**

{{< highlight "bash" >}}

 git clone git://git.code.sf.net/p/html5-spreadsheet-editor/code html5-spreadsheet-editor-code

{{< /highlight >}}

**Maven を使用してビルド**

プロジェクトのビルド プロセスは Maven を使用して管理されます。したがって、IDE を使用せずにコマンド ラインから WAR ファイルを準備できます。次のコマンドを使用して、デプロイ用の WAR を生成します。対応するアプリケーション サーバーのドキュメントは、生成された WAR とその依存関係を展開する方法に役立ちます。

{{< highlight "java" >}}

 mvn clean install

{{< /highlight >}}

**NetBeans の使用**

を使用してプロジェクトを管理するのは非常に簡単です[NetBeans IDE](https://netbeans.apache.org/)NetBeans は Java 開発者の間で人気のある IDE の 1 つで、Oracle が後援しています。

- プロジェクトのソース コードをダウンロードします。
- プロジェクトを NetBeans IDE で開きます。
- クリック***走る***ツールバーのボタン。
- 選択する***グラスフィッシュ***サーバーをアプリケーション サーバーとして使用します。

**Eclipse の使用**

[エクリプスIDE](http://www.eclipse.org/ide/)と呼ばれるMavenプロジェクトをインポートするための公式統合を提供します[M2エクリプス](http://www.eclipse.org/m2e/):

1. M2Eclipse を Eclipse IDE にインストールします。インストール手順は、同社の Web サイトに記載されています。
1. プロジェクトのソース コードをダウンロードします。
1. 開く***輸入***ファイルメニューのダイアログ。
1. 選択する***Maven プロジェクト***インポートダイアログから。
1. クリック***次***.
1. クリック***ブラウズ***ソースコードの場所を選択します。
1. 選択する***pom.xml***以下のリストから。
1. クリック***終了***.

Eclipse IDE は、プロジェクトをインポートしてロードする必要があります。
### **サポート**
**バグレポート**

バグ レポートを送信するには、新しい問題を作成します。[Github プロジェクトページ](https://github.com/AsposeShowcase/Html5_Spreadsheet_Editor_by_Aspose.Cells_for_Java/issues)そしてラベルを貼る***バグ***.

**機能リクエスト**

フィードバックとご要望の機能をお待ちしております。新しい機能または既存の機能強化をリクエストするには、新しい問題を作成してください。[Github プロジェクトページ](https://github.com/AsposeShowcase/Html5_Spreadsheet_Editor_by_Aspose.Cells_for_Java/issues)そしてラベルを貼る***エンハンスメント***.

**質問とヘルプ**

を使用して、HTML5 スプレッドシート エディターに関連するあらゆる種類の質問をすることができます。[Githubの問題](https://github.com/AsposeShowcase/Html5_Spreadsheet_Editor_by_Aspose.Cells_for_Java/issues).新しい問題を作成して適用するだけです***質問***ラベル。

**Aspose.Cells for Java フォーラム**

Aspose 製品フォーラムは、試用版と有料版の両方のお客様に完全なサポートを提供します。専門家が年中無休 24 時間体制でヘルプを提供し、質問に答えます。訪問[製品フォーラムはこちら](https://forum.aspose.com/c/cells/9).

**Aspose ブログ**

当社に連絡して、当社の製品とオファーに関する最新ニュースを入手してください。申し込む[当ブログはこちら](http://blog.aspose.com).
### **助ける**
[](https://github.com/AsposeShowcase/Html5_Spreadsheet_Editor_by_Aspose.Cells_for_Java)

[!\[todo:image_alt_text\]](https://s3.amazonaws.com/github/ribbons/forkme_right_red_aa0000.png)](https://github.com/AsposeShowcase/Html5_スプレッドシート_編集者_沿って_Aspose.Cells_為に_Java)


HTML5 スプレッドシート エディターはオープン ソース プロジェクトであり、誰もがプロジェクトに貢献できる最大限のオプションを提供します。

**ソースコード**

プロジェクトのソースは次の場所にあります。[ギットハブ](https://github.com/AsposeShowcase/Html5_Spreadsheet_Editor_by_Aspose.Cells_for_Java).また、次のサイトで Git ミラーを維持しています。

- [ビットバケット](https://bitbucket.org/asposeshowcase/html5_spreadsheet_editor_by_aspose.cells_for_java)
- [ソースフォージ](https://sourceforge.net/p/html5-spreadsheet-editor/)

**プルリクエスト**

プロジェクトにソース コードを提供するには、Github 経由でプル リクエストを送信するだけです。詳細については、Github の記事を参照してください。[プル リクエストを作成する](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request).
### **ライセンス**
**MITライセンス**

寄稿者の負担を最小限に抑えるために、最もリベラルなオープン ソース ライセンスの 1 つを使用しています。 HTML5 スプレッドシート エディタは以下でリリースされています[MITライセンス](https://opensource.org/licenses/mit-license.php).

**Aspose 免許**

この製品は Aspose ライセンスなしで動作します。[制限付き](/cells/ja/java/licensing/).制限を取り除くには、[無料の一時ライセンス](https://purchase.aspose.com/temporary-license)また[フルライセンスを購入](https://purchase.aspose.com/buy).

デフォルトでは、エディタはロードを試みます**Aspose.Total.Java.lic**からのファイル**src/main/resources/com/aspose/spreadsheeteditor**ディレクトリ。ライセンス ファイルをこのディレクトリにコピーするだけです。デフォルトの動作は、**Asposeライセンス**クラス。
