---
title: Sitefinity Export Users to Excel
type: docs
weight: 20
url: /ja/net/sitefinity-export-users-to-excel/
---

**内容の要約**

- [紹介](#SitefinityExportUserstoExcel-Introduction)
- [システム要件およびサポートされるプラットフォーム](#SitefinityExportUserstoExcel-SystemRequirementsandSupportedPlatforms) 
  - [システム要件](#SitefinityExportUserstoExcel-SystemRequirements)
  - [サポートされているプラットフォーム](#SitefinityExportUserstoExcel-SupportedPlatforms)
- [ソースコード](#SitefinityExportUserstoExcel-SourceCode) 
  - [ソースコードの構成方法](#SitefinityExportUserstoExcel-Howtoconfigurethesourcecode)
- [インストールと使用法](#SitefinityExportUserstoExcel-InstallationandUsage) 
  - [ダウンロード](#SitefinityExportUserstoExcel-Downloading)
  - [インストール](#SitefinityExportUserstoExcel-Installing)
- [使用とビデオデモ](#SitefinityExportUserstoExcel-UsingandVideoDemo) 
  - [を使用する](#SitefinityExportUserstoExcel-Using)
  - [ビデオデモ](#SitefinityExportUserstoExcel-VideoDemo)
- [サポート](#SitefinityExportUserstoExcel-Support)
- [拡張と貢献](#SitefinityExportUserstoExcel-ExtendandContribute)
## **紹介**
Aspose .NET Export Users to Excel for SiteFinity Module は開発者が SiteFinity ユーザーを Microsoft Excel や OpenOffice Spreadsheet にエクスポートできるようにするもので、Aspose.Cells が提供する強力なスプレッドシート作成機能をデモンストレーションしています。

## **システム要件およびサポートされるプラットフォーム**
### **システム要件**
Aspose.Cells .NET for Sitefinity アドオンをセットアップするには、以下の要件を満たす必要があります:

- ASP.NET 4.0 上で動作する Sitefinity CMS

この Sitefinity アドオンをセットアップする際に問題が発生した場合は、お気軽にお問い合わせください。
### **サポートされているプラットフォーム**
このアドオンはすべてのバージョンでサポートされています

- ASP.NET 4.0 上で動作する Sitefinity CMS
## **ソースコード**
最新のソースコードを以下の場所から取得できます

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/SiteFinity)
### **ソースコードの構成方法**
以下のアイテムがインストールされている必要があります

- Visual Studio 2010 またはそれ以降

開始するための簡単なステップに従ってください

1. ソースコードをダウンロード/クローンします。
1. Visual Studio 2010を開き、**ファイル** > **プロジェクトを開く** を選択してください
1. ダウンロードした最新のソースコードに移動し、 **.sln** ファイルを開きます。
## **インストールと使用法**
### **ダウンロード**
Aspose .NET Content Exporter for Sitefinity モジュールを以下の場所からダウンロードできます

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases)
### **インストール**
ダウンロードしたら、以下の手順に従って Add-on を Sitefinity ウェブサイトにインストールしてください:

**ステップ 1: ファイルを Sitefinity インストールにコピー**

ダウンロードした ZIP ファイルを解凍してください。次の作業を実行するには、サーバー上の Sitefinity インストールフォルダに FTP または直接アクセスする必要があります:

1. Aspose.Cells.dll と Aspose.SiteFinity.ExportUsersToExcel.dll を Sitefinity インストールの **bin** フォルダにコピーします。
1. **bin** フォルダがある場所に、**Addons** フォルダをコピーします。

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
   1. **~/Addons/Aspose.SiteFinity.ExportUsersToExcel/AsposeExportUsersToExcel.ascx** を追加します。

   1. **コントロールCLRタイプまたは仮想パス** フィールドに ` ` を入力します。
   1. 次のように **名前**、**タイトル**、**説明** を追加します:
      Aspose.SiteFinity.ExportUsersToExcel
      Aspose Export SiteFinity Users to Excel
      SiteFinityユーザーをExcelにエクスポート
   1. 他のすべてのフィールドはそのままにしておくことができます。
1. 終了したら、**変更を保存** をクリックします。
   ウィジェットがツールボックスに登録され、Sitefinityで使用できます。
## **使用とビデオデモ**
### **を使用する**
Aspose Sitefinity Export Users to Excelアドオンをインストールして構成した後、ウェブサイトで使用を開始するのは本当に簡単です。次の簡単な手順に従ってください:

1. サイトフィニティに管理者レベルのアカウントでログインしていることを確認します。
1. エクスポートアドオンを追加したいページに移動します。ページが編集モードで開かれていることを確認します。
1. 右側の**ウィジェットをドラッグ**メニューからAspose Export Users to Excelを選択し、位置にドラッグします。


Aspose Sitefinity Export Users to Excelを正常に追加しました。
### **ビデオデモ**
このモジュールを実際に動作する[ビデオ](https://www.youtube.com/watch?v=O1524u-Pom4)をご覧ください。
## **サポート**
Asposeが立ち上がって最初の日から、良い製品だけを提供するだけでは不十分だと分かっていました。良いサービスも提供する必要がありました。私たち自身も開発者であり、技術的な問題やソフトウェアの不具合が必要なことを妨げるときにどれだけイライラするか理解しています。私たちは問題を解決するためにここにいて、それを作り出すためではありません。

そのため、無料サポートを提供しています。製品を購入したか、評価を使用しているかに関わらず、私たちの製品を使用するすべての人にフルの注意と尊敬を提供する価値があります。

Aspose.Cells .NET for Sitefinityモジュールに関連する問題や提案を次のプラットフォームのいずれかを使用してログに記録できます

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/issues)
## **拡張と貢献**
Aspose Sitefinityウィジェット/モジュールはオープンソースであり、そのソースコードは以下の主要なソーシャルコーディングウェブサイトで利用可能です。開発者はソースコードをダウンロードして、機能を自分の要件に応じて拡張することが推奨されています。
