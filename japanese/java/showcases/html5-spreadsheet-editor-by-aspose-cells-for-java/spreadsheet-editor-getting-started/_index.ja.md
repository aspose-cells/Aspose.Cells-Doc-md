---
title: スプレッドシートエディター入門
type: docs
weight: 10
url: /ja/java/spreadsheet-editor-getting-started/
---

**目次**

- [紹介](#SpreadsheetEditorGettingStarted-Introduction)
- [システム要件](#SpreadsheetEditorGettingStarted-SystemRequirements)
- [ダウンロードとインストール](#SpreadsheetEditorGettingStarted-DownloadandInstallation)
- [サポート](#SpreadsheetEditorGettingStarted-Support)
- [貢献](#SpreadsheetEditorGettingStarted-Contribute)
- [ライセンス](#SpreadsheetEditorGettingStarted-License)
### **紹介**
Html5スプレッドシートエディターは、Webブラウザでスプレッドシートドキュメントを表示および編集できるWebアプリケーションです。Excel、SpreadsheetML、CVS、OpenDocumentなど、Microsoft Excelがサポートする多くのフォーマットをサポートしています。セルの編集、書式設定、数式の編集、行と列の管理など、すべての基本的な機能がサポートされています。

![todo:image_alt_text](aowcrc1.png)

HTML5スプレッドシートエディターは、[Aspose.Cells for Java](https://products.aspose.com/cells/java/)の多くの機能を使用し、それらを使用してJavaアプリケーションでスプレッドシートを作成、操作、描画する方法を示しています。

**機能**

- ファイル操作 
  - サポートされる形式
  - ローカルファイルを開く
  - Dropboxから開く
  - URLから開く
  - 新しいスプレッドシートを作成する
  - さまざまな形式にエクスポート
- シートでの作業 
  - シートの追加と削除
  - シートの名前変更
  - シート間の切り替え
- 行と列での作業 
  - 行の追加
  - 列の追加
  - 行の削除
  - 列の削除
  - 列幅と行の高さ
- セルでの作業 
  - セルの選択
  - セルの編集
  - 式の編集
  - セルの配置
  - セルのクリア
  - セルの追加
  - セルの削除
- テキスト書式の作業 
  - 太字、斜体、下線
  - フォントスタイルとサイズ
  - 書式のクリア
### **システム要件**
**ソフトウェア要件**

- CDI対応のJavaアプリケーションサーバ
- [Aspose.Cells for Java](https://products.aspose.com/cells/java/)
- [JavaServer Faces 2.0](https://javaee.github.io/javaserverfaces-spec/)
- [Primefaces 5.1](https://www.primefaces.org/)

**ハードウェア要件**

ハードウェア要件は、HTML5スプレッドシートエディタをデプロイするJavaアプリケーションサーバと同時に開くスプレッドシートの数に基づくため、異なります。以下は、環境を初期設定するのに役立つ見積りです。

- 2 GHz CPU
- 2 GB RAM
- 500 MBディスク
### **ダウンロードとインストール**
HTML5スプレッドシートエディタはJava EEアプリケーションであり、CDIサポートを備えた任意のJavaアプリケーションサーバのWebプロファイルにデプロイできます。 [Glassfish](https://javaee.github.io/glassfish/) でテスト済みです。

**ソース コード**

プロジェクトのソースコードは[Github](https://github.com/aspose-cells/Aspose.Cells-for-Java/)で利用できます。以下のサイトでもGitミラーを維持しています:

- [Bitbucket](https://bitbucket.org/asposeshowcase/html5_spreadsheet_editor_by_aspose.cells_for_java)
- [Google Code](https://code.google.com/archive/p/html5-spreadsheet-editor/)
- [SourceForge](https://sourceforge.net/p/html5-spreadsheet-editor/)

以下のコマンドのいずれかを使用して、コマンドラインからソースコードをダウンロードできます:

**Github**

{{< highlight bash >}}

 git clone https://github.com/aspose-cells/Aspose.Cells-for-Java.git

{{< /highlight >}}

**Bitbucket**

{{< highlight bash >}}

 git clone https://bitbucket.org/asposeshowcase/html5_spreadsheet_editor_by_aspose.cells_for_java.git

{{< /highlight >}}

**Google Code**

{{< highlight bash >}}

 git clone https://code.google.com/p/html5-spreadsheet-editor/

{{< /highlight >}}

**SourceForge**

{{< highlight bash >}}

 git clone git://git.code.sf.net/p/html5-spreadsheet-editor/code html5-spreadsheet-editor-code

{{< /highlight >}}

**Mavenを使用してビルド**

プロジェクトのビルドプロセスはMavenを使用して管理されています。IDEなしでコマンドラインからWARファイルを準備できます。デプロイ用にWARを生成するには、以下のコマンドを使用してください。対応するアプリケーションサーバーのドキュメントが、生成されたWARおよびその依存関係のデプロイ方法を指示します。

{{< highlight java >}}

 mvn clean install

{{< /highlight >}}

**NetBeansを使用する**

[NetBeans IDE](https://netbeans.apache.org/)を使用してプロジェクトを管理することは非常に簡単です。NetBeansはJava開発者の間で人気のあるIDEの1つであり、Oracleが提供しています。

- プロジェクトのソースコードをダウンロードします。
- NetBeans IDEでプロジェクトを開きます。
- ツールバーの***実行***ボタンをクリックします。
- アプリケーションサーバーとして***Glassfish***を選択します。

**Eclipseを使用する**

[Eclipse IDE](http://www.eclipse.org/ide/)は、Mavenプロジェクトをインポートするための公式統合である[M2Eclipse](http://www.eclipse.org/m2e/)を提供しています:

1. Eclipse IDEにM2Eclipseをインストールします。インストール手順は彼らのウェブサイトで説明されています。
1. プロジェクトのソースコードをダウンロードします。
1. ファイルメニューから***インポート***ダイアログを開きます。
1. インポートダイアログから***Mavenプロジェクト***を選択します。
1. ***次へ***をクリックします。
1. ソースコードの場所を選択するために***参照***をクリックします。
1. リストから***pom.xml***を選択します。
1. ***完了***をクリックします。

Eclipse IDEはプロジェクトをインポートおよびロードするはずです。
### **サポート**
**バグレポート**

バグレポートを送信するには、[Githubプロジェクトページ](https://github.com/AsposeShowcase/Html5_Spreadsheet_Editor_by_Aspose.Cells_for_Java/issues)で新しい問題を作成し、***bug***ラベルを適用します。

**機能リクエスト**

お客様のフィードバックとリクエストされる機能には、大変感謝しています。新しい機能または既存の機能の改善をリクエストするには、[Githubプロジェクトページ](https://github.com/AsposeShowcase/Html5_Spreadsheet_Editor_by_Aspose.Cells_for_Java/issues)で新しい問題を作成し、***enhancement***ラベルを適用してください。

**質問とヘルプ**

HTML5スプレッドシートエディタに関連するあらゆる種類の質問を[Githubのissue](https://github.com/AsposeShowcase/Html5_Spreadsheet_Editor_by_Aspose.Cells_for_Java/issues)で質問できます。新しい問題を作成し、***question***ラベルを適用してください。

**Aspose.Cells for Javaフォーラム**

Asposeの商品フォーラムでは、トライアル利用者と有料利用者の両方に対して完全なサポートを提供しています。専門家が24時間365日体制でサポートや質問に答えています。[商品フォーラムはこちら](https://forum.aspose.com/c/cells/9)をご覧ください。

**Aspose ブログ**

連絡を取り合い、当社製品や特典に関する最新情報をご覧ください。[こちらからブログを購読してください](http://blog.aspose.com)。
### **貢献**
[](https://github.com/AsposeShowcase/Html5_Spreadsheet_Editor_by_Aspose.Cells_for_Java)

[!\[todo:image_alt_text\](https://s3.amazonaws.com/github/ribbons/forkme_right_red_aa0000.png)](https://github.com/AsposeShowcase/Html5_Spreadsheet_Editor_by_Aspose.Cells_for_Java)


HTML5 スプレッドシート エディターは、誰もがプロジェクトに貢献できる最大限のオプションを提供するオープンソース プロジェクトです。

**ソース コード**

プロジェクトのソースは[GitHub](https://github.com/AsposeShowcase/Html5_Spreadsheet_Editor_by_Aspose.Cells_for_Java)で利用可能です。以下のサイトでも Git ミラーを維持しています:

- [Bitbucket](https://bitbucket.org/asposeshowcase/html5_spreadsheet_editor_by_aspose.cells_for_java)
- [SourceForge](https://sourceforge.net/p/html5-spreadsheet-editor/)

**プル リクエスト**

プロジェクトにソース コードを貢献するには、GitHub を介してプル リクエストを送信してください。GitHub の記事[プルリクエストの作成](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request)で詳細をご覧いただけます。
### **ライセンス**
**MIT ライセンス**

最小限の責任を負うための最も寛容なオープンソース ライセンスの1つを使用しています。HTML5 スプレッドシート エディターは[MIT ライセンス](https://opensource.org/licenses/mit-license.php)の下でリリースされています。

**Aspose ライセンス**

製品はAspose ライセンスなしで動作しますが、[制限付き](/cells/ja/java/licensing/)で動作します。制限を解除するには、[無料の一時ライセンス](https://purchase.aspose.com/temporary-license)を取得するか、[フルライセンスを購入](https://purchase.aspose.com/buy)してください。

デフォルトでは、エディターは**src/main/resources/com/aspose/spreadsheeteditor**ディレクトリから**Aspose.Total.Java.lic**ファイルを読み込みます。ライセンス ファイルをこのディレクトリにコピーしてください。デフォルトの動作は、**AsposeLicense** クラスを編集することで変更できます。
