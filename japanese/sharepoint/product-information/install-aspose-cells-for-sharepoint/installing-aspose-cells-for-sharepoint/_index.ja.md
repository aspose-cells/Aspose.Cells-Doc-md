---
title: Aspose.Cells for SharePoint のインストール
type: docs
weight: 10
url: /ja/sharepoint/installing-aspose-cells-for-sharepoint/
---

{{% alert color="primary" %}} 

Aspose.Cells for SharePointはAspose.Cells.SharePoint.zipアーカイブとしてダウンロードできます。 

{{% /alert %}} 
### **アーカイブ内容**
Aspose.Cells.SharePoint.zipアーカイブには次のものが含まれています:

- Aspose.Cells.SharePoint.wsp – SharePointソリューションファイル。Aspose.Cells for SharePointはSharePointソリューションとしてパッケージ化されており、サーバーファーム全体でのデプロイ/取り消しや機能の有効化/無効化を容易にします。
- Aspose_LicenseAgreement.rtf – エンドユーザーライセンス契約
- Aspose.Cells for SharePoint.pdf – ユーザー向けドキュメント
- Aspose.Cells for SharePoint Documentation.chm – パブリックAPIリファレンス付きユーザー向けドキュメント
- setup.exe – セットアッププログラム
- setup.exe.config – セットアップ構成ファイル

インストールの前にセットアッププログラムは次の条件をチェックします:

- WSS 3.0、MOSS 2007、またはSharePoint 2010がインストールされている。
- ユーザーがSharePointソリューションをインストールする権限を持っている。
- SharePointデータベースがオンラインである。
- WSS管理サービスが開始されている。
- WSSタイマーサービスが開始されている。

WSS管理サービスとタイマーサービスは、いくつかのセットアップアクションがすべてのサーバーに展開されるためにタイマージョブに依存するため必要です。 
#### **Aspose.Cells for SharePointをインストールするには**
1. Aspose.Cells.SharePoint zipをMOSS 7.0またはWSS 3.0サーバーのローカルドライブに展開します。
1. setup.exeを実行し、画面の指示に従います。

セットアッププログラムは以下のアクションを実行します:

1. インストールの前提条件をチェックします。チェックに合格しない場合、セットアップは続行しません。 

   **システムチェック** 

![todo:image_alt_text](installing-aspose-cells-for-sharepoint_1.png)




1. エンドユーザーライセンス契約を表示します。ユーザーは合意しなければアクションを実行できません。 

   **エンドユーザーライセンス契約** 

![todo:image_alt_text](installing-aspose-cells-for-sharepoint_2.png)




1. デプロイ先選択ダイアログを表示します。ユーザーが機能をアクティブ化するWebアプリケーションとサイトコレクションを選択します。下の図を参照してください。 

   **デプロイ先** 

![todo:image_alt_text](installing-aspose-cells-for-sharepoint_3.png)




1. サーバーファームに機能を展開します。 

   **インストール実行中** 

![todo:image_alt_text](installing-aspose-cells-for-sharepoint_4.png)




1. 選択したサイトコレクションの機能をアクティブ化し、親Webアプリケーションを構成します。
1. 機能が展開およびアクティブ化されたWebアプリケーションとサイトコレクションの一覧を表示します。 

   **インストール完了** 

![todo:image_alt_text](installing-aspose-cells-for-sharepoint_5.png)
