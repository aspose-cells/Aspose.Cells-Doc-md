---
title: Aspose.Cells Forms for Sitefinity
type: docs
weight: 10
url: /ja/net/aspose-cells-forms-for-sitefinity/
---

## **紹介**

Aspose.Cells Dynamic Forms for Sitefinityモジュールを使用すると、ユーザーは動的なアンケートと調査を生成し、ユーザーの入力をExcelスプレッドシートに保存し、結果をAspose.Cellsを使用してExcel、テキスト、CSV、およびOpenDocumentスプレッドシートにエクスポートできます。このモジュールは、Aspose.Cells for .NETによって提供される強力なスプレッドシート作成機能を示しています。

|<p>![todo:image_alt_text](aspose-cells-forms-for-sitefinity_1)</p><p></p>|
| :- |

### **モジュールの機能**

この初期バージョンのモジュールには、以下の機能が豊富に備わっており、フォームの構築とエクスポートプロセスを簡単かつ使いやすくしています

- Excelでフォームフィールドの設定を保存
- フォームのユーザー入力データをExcelに保存
- 新しいフォームフィールドの追加と既存のフォームフィールドの更新を許可
- テキストボックス、複数行テキストボックス、ラジオボタン、チェックボックス、ドロップダウンリスト、ドロップダウンリストアイテムタイプフィールドを追加できる
- 各フィールドにラベルを追加/更新できる
- フォームフィールドを表示/非表示にできる
- コンテンツの長さに合わせて自動的に列幅を調整し、ヘッダーカラムの書式を太字のテキストに適用
- マイクロソフトエクセルドキュメント（.xls、.xlsx、.xlsb）へのデータのエクスポートを許可
- タブ区切りテキストドキュメント（*.txt）へのデータのエクスポートを許可
- CSV（カンマ区切り）（*.csv）へのデータのエクスポートを許可
- OpenDocumentスプレッドシート（*.ods）へのデータのエクスポートを許可
- エクスポート前に出力形式を選択するオプションを提供
- エクスポートされたドキュメントは自動的にブラウザに送信されてダウンロードされます

## **システム要件およびサポートされるプラットフォーム**

Aspose.Cells .NET for Sitefinity アドオンをセットアップするには、以下の要件を満たす必要があります:

- ASP.NET 4.0 上で動作する Sitefinity CMS

この Sitefinity アドオンをセットアップする際に問題が発生した場合は、お気軽にお問い合わせください。

このアドオンはすべてのバージョンでサポートされています

- ASP.NET 4.0 上で動作する Sitefinity CMS

## **ダウンロードとインストール**

### **ダウンロード**

Aspose .NET Content Exporter for Sitefinity モジュールを以下の場所からダウンロードできます

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/SiteFinity/Aspose.SiteFinity.FormBuilder.ToExcel)

### **インストール**

ダウンロードしたら、以下の手順に従って Add-on を Sitefinity ウェブサイトにインストールしてください:

**ステップ 1: ファイルを Sitefinity インストールにコピー**

ダウンロードした ZIP ファイルを解凍してください。次の作業を実行するには、サーバー上の Sitefinity インストールフォルダに FTP または直接アクセスする必要があります:

1. **Aspose.Cells.dll**および**Aspose.Sitefinity.FormBuilder.dll**をSitefinityインストールのbinフォルダにコピーしてください
1. **bin** フォルダがある Sitefinity インストールのルートに **Addons** フォルダをコピーします。

**ステップ 2: Sitefinity で Aspose Sitefinity Content Export アドオンを登録**

1. Log into your Sitefinity CMS with an ‘**Administrator**’ account. The login page can be reached by <http://www.mywebsite.com/sitefinity>
1. **管理** をクリックして、**設定** を選択します。
   基本設定ページが表示されます。
1. **高度な** リンクをクリックします。
   設定ページが表示されます。
1. 左側のペインで、**ツールボックス**の後に**ツールボックス**、 **ページコントロール**、**セクション** 、**コンテンツツールボックスセクション**、**ツール** の順にクリックします。
1. **新規作成** をクリックします。
   ウィジェット登録フォームが表示されます。
1. 次のようにフォームフィールドを入力します: 
   1. **有効** が選択されていることを確認します。 
      1. **コントロール CLR タイプまたは仮想パス** フィールドに入力します。 
         1. **~/Addons/Aspose.SiteFinity.FormBuilder.ToExcel/Edit.ascx** を追加します
      1. 次のように **名前**、**タイトル**、**説明** を追加します: 
         SiteFinity ユーザーに Aspose **PageName** （例：Edit、View、Export）フォームを追加します。
         Aspose **PageName** フォーム（例：Aspose 編集フォーム、Aspose 表示フォーム、Aspose エクスポートフォーム）
         Sitefinity 用の **PageName** フォームビルダー＆エクスポーター
      1. 他のすべてのフィールドはそのままにしておくことができます。
      1. 終了したら、**変更を保存** をクリックします。
      ウィジェットがツールボックスに登録され、Sitefinity で使用できるようになります。（以下の画像を参照）

|<p>![todo:image_alt_text](picture1.png)</p><p></p>|
| :- |

## **使用とビデオデモ**

### **を使用する**

Aspose.Cells Dynamic Forms Builder for Sitefinity Users アドオンをインストールして構成した後、ウェブサイトで使用を開始するのは本当に簡単です。以下の簡単な手順に従ってください：

1. サイトフィニティに管理者レベルのアカウントでログインしていることを確認します。
1. プラグインを追加したいページに移動します。ページが編集モードで開かれていることを確認してください。
右側の**ウィジェットをドラッグ** メニューから Aspose 編集/表示/エクスポートフォームを選択して、位置にドラッグします。（以下の画像を参照）

|<p>![todo:image_alt_text](aspose-cells-forms-for-sitefinity_2)</p><p></p>|
| :- |

Aspose.Cells Dynamic Form Builder for Sitefinity モジュールをページに正常に追加しました。

#### **Asposeライセンスの適用方法**

このプラグインは Aspose.Cells の評価版を使用しています。評価を完了したら、[Aspose 購入ウェブサイト](https://purchase.aspose.com/buy) でライセンスを購入できます。
評価メッセージと機能の制限を解除するには、製品ライセンスを適用する必要があります。製品を購入した後、ライセンスファイルを受け取ります。以下の手順に従ってライセンスを適用してください。

- ライセンスファイルが **Aspose.Total.lic** という名前であることを確認してください。
- **Aspose.Total.lic** ファイルを Sitefinity ウェブサイトの **App_Data** フォルダに配置してください。たとえば、「Sitefinityルートフォルダ/App_Data/Aspose.Total.lic」

#### **動的フォームの設定**

1. ログインしていることを確認し、ページメニューをクリックして、**アクション列の近くにある最初の行の **表示** オプションボタンをクリックしてください。  
1. オプションラベルの近くに利用可能な**編集**ボタンをクリックしてください。
1. いくつかの事前定義フィールドがありますが、**グリッド内の **編集** をクリックするだけで編集/非表示にできます。
1. 任意のタイプの新しいフィールド **（テキストボックス、マルチラインテキストボックス、ラジオボタン、チェックボックス、ドロップダウンリスト、タイトル、成功メッセージ）** を作成/削除/更新できます。

#### **動的フォームの送信**

1. フィールドに入力してください。
1. **送信** ボタンをクリックしてデータを保存してください。
1. 各 **送信** ボタンクリックで新しいレコードがExcelに保存されます。

#### **保存されたデータのエクスポート**

1. ログインしていることを確認し、ページメニューに移動し、**アクション列の近くにある最初の行の** 表示** オプションボタンをクリックしてください。
1. **エクスポートアイコン** にマウスを合わせ、**それをクリック** するとエクスポートページが開きます。
1. **エクスポートタイプ** を選択してください。
1. **データをエクスポート** ボタンをクリックしてください。
1. エクスポートタイプに応じたエクスポートデータファイルがダウンロード/開くポップアップが表示されます。

Aspose Sitefinity Export Users to Excelを正常に追加しました。

### **ビデオデモ**

このモジュールを実際に見るために、[ビデオ](https://www.youtube.com/watch?v=La5WMCvafR0)をご覧ください。

## **サポート、拡張、貢献**

### **サポート**

Asposeが立ち上がって最初の日から、良い製品だけを提供するだけでは不十分だと分かっていました。良いサービスも提供する必要がありました。私たち自身も開発者であり、技術的な問題やソフトウェアの不具合が必要なことを妨げるときにどれだけイライラするか理解しています。私たちは問題を解決するためにここにいて、それを作り出すためではありません。

そのため、無料サポートを提供しています。製品を購入したか、評価を使用しているかに関わらず、私たちの製品を使用するすべての人にフルの注意と尊敬を提供する価値があります。
Aspose.Cells .NET for Sitefinityモジュールに関連する問題や提案を次のプラットフォームのいずれかを使用してログに記録できます

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/issues)

### **拡張と貢献**

#### **ソースコード**

最新のソースコードを以下からダウンロードできます:

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET)

#### **ソースコードの設定方法**

以下のアイテムがインストールされている必要があります

- Visual Studio 2013 またはそれ以上

開始するための簡単なステップに従ってください

1. ソースコードをダウンロード/クローンします。
1. Visual Studio 2013 を開き、**ファイル** > **プロジェクトを開く** を選択してください。
1. ダウンロードした最新のソースコードに移動し、**.sln** ファイルを開いてください。
