---
title: Sitefinity ユーザーを Excel にエクスポート
type: docs
weight: 20
url: /ja/net/sitefinity-export-users-to-excel/
---
**目次のまとめ**

- [序章](#SitefinityExportUserstoExcel-Introduction)
- [システム要件とサポートされるプラットフォーム](#SitefinityExportUserstoExcel-SystemRequirementsandSupportedPlatforms) 
  - [システム要求](#SitefinityExportUserstoExcel-SystemRequirements)
  - [サポートされているプラットフォーム](#SitefinityExportUserstoExcel-SupportedPlatforms)
- [ソースコード](#SitefinityExportUserstoExcel-SourceCode) 
  - [ソースコードの構成方法](#SitefinityExportUserstoExcel-Howtoconfigurethesourcecode)
- [インストールと使用法](#SitefinityExportUserstoExcel-InstallationandUsage) 
  - [ダウンロード中](#SitefinityExportUserstoExcel-Downloading)
  - [インストール](#SitefinityExportUserstoExcel-Installing)
- [使用およびビデオデモ](#SitefinityExportUserstoExcel-UsingandVideoDemo) 
  - [使用する](#SitefinityExportUserstoExcel-Using)
  - [ビデオデモ](#SitefinityExportUserstoExcel-VideoDemo)
- [サポート](#SitefinityExportUserstoExcel-Support)
- [拡張して貢献する](#SitefinityExportUserstoExcel-ExtendandContribute)
## **序章**
Aspose .NET ユーザーを Excel にエクスポートして SiteFinity モジュールを作成すると、開発者は SiteFinity ユーザーを Microsoft Excel または OpenOffice スプレッドシートにエクスポートできます。このモジュールは、Aspose.Cells によって提供される強力なスプレッドシート作成機能を示しています。

## **システム要件とサポートされるプラットフォーム**
### **システム要求**
Sitefinity アドオン用に Aspose.Cells .NET をセットアップするには、次の要件を満たす必要があります。

- ASP.NET 4.0 で実行されている Sitefinity CMS

この Sitefinity アドオンの設定に問題がある場合は、お気軽にお問い合わせください。
### **サポートされているプラットフォーム**
アドオンは、のすべてのバージョンでサポートされています

- ASP.NET 4.0 で実行されている Sitefinity CMS
## **ソースコード**
最新のソース コードは、次のいずれかの場所から入手できます。

- [ギットハブ](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/SiteFinity)
### **ソースコードの構成方法**
ソースコードを開いて拡張するには、以下をインストールする必要があります

- Visual Studio 2010 以降

開始するには、次の簡単な手順に従ってください

1. ソースコードをダウンロード/クローンします。
1. Visual Studio 2010 を開き、選択します**ファイル** > **プロジェクトを開く**
1. ダウンロードした最新のソース コードを参照し、**.sln**ファイル。
## **インストールと使用法**
### **ダウンロード中**
Aspose .NET Content Exporter for Sitefinity モジュールは、次のいずれかの場所からダウンロードできます。

- [ギットハブ](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases)
### **インストール**
ダウンロードしたら、次の手順に従ってアドオンを Sitefinity Web サイトにインストールしてください。

**ステップ 1: ファイルを Sitefinity インストールにコピーする**

ダウンロードしたZIPファイルを解凍してください。以下を実行するには、FTP またはサーバー上の Sitefinity インストール フォルダーへの直接アクセスが必要です。

1.  Aspose.Cells.dll と Aspose.SiteFinity.ExportUsersToExcel.dll を**置き場**Sitefinity インストールのフォルダー。
1. コピー**アドオン** Sitefinity インストールのルートにあるフォルダ**置き場**フォルダがあります。

**ステップ 2: Aspose Sitefinity コンテンツ エクスポート アドオンを Sitefinity に登録する**

1. ' を使用して Sitefinity CMS にログインします。**管理者** ' アカウント。ログインページには次の方法でアクセスできます<http://www.mywebsite.com/sitefinity>
1. クリック**管理**その後**設定**.
[基本設定] ページが表示されます。
1. クリック**高度**リンク。
 [設定] ページが表示されます。
1. 左ペインで、**ツールボックス**に続く**ツールボックス**、 それから**ページコントロール**, **セクション**と**コンテンツ ツールボックス セクション**、 それから**ツール。**
1. クリック**新しく作る**.
ウィジェット登録フォームが表示されます。
1. フォーム フィールドに次のように入力します。
 1. 確認する**有効**が選択されます。
 1. ~/Addons/Aspose.SiteFinity.ExportUsersToExcel/AsposeExportUsersToExcel.ascx を追加します。

 1. ` `**CLR タイプまたは仮想パスを制御する**分野。
 1.追加**名前**, **題名**と**説明**次のように：
 Aspose.SiteFinity.ExportUsersToExcel
 Aspose SiteFinity ユーザーを Excel にエクスポート
SiteFinity ユーザーを Excel にエクスポートする
1. 他のすべてのフィールドはそのままにしておくことができます。
1. 終了したら、**変更内容を保存**.
ウィジェットはツールボックスに登録され、Sitefinity で使用できます。
## **使用およびビデオデモ**
### **使用する**
Aspose Sitefinity Export Users to Excel アドオンをインストールして構成したら、Web サイトで簡単に使用を開始できます。開始するには、次の簡単な手順に従ってください。

1. 管理者レベルのアカウントで Sitefinity にログインしていることを確認してください。
1. Export アドオンを追加するページに移動します。ページが編集モードで開かれていることを確認します。
1. から**ウィジェットをドラッグ**右側のメニューで、[Aspose ユーザーを Excel にエクスポート] を選択し、所定の位置にドラッグします。


Aspose Sitefinity エクスポート ユーザーを Excel に正常に追加しました。
### **ビデオデモ**
チェックしてください[ビデオ](https://www.youtube.com/watch?v=O1524u-Pom4)モジュールの動作を確認するには、以下を参照してください。
## **サポート**
Aspose の最初の日から、私たちはお客様に良い製品を提供するだけでは十分ではないことを知っていました。また、優れたサービスを提供する必要もありました。私たち自身も開発者であり、技術的な問題やソフトウェアの異常によって必要な作業ができなくなると、どれほどイライラするかを理解しています。問題を作成するのではなく、問題を解決するためにここにいます。

そのため、無料サポートを提供しています。私たちの製品を購入したか、評価を使用しているかにかかわらず、私たちの製品を使用するすべての人は、私たちの十分な注意と尊敬に値します.

次のプラットフォームのいずれかを使用して、Sitefinity モジュールの Aspose.Cells .NET に関連する問題または提案を記録できます。

- [ギットハブ](https://github.com/aspose-cells/Aspose.Cells-for-.NET/issues)
## **拡張して貢献する**
Aspose Sitefinity ウィジェット/モジュールはオープン ソースであり、そのソース コードは、以下に示す主要なソーシャル コーディング Web サイトで入手できます。開発者は、ソース コードをダウンロードし、独自の要件に従って機能を拡張することをお勧めします。
