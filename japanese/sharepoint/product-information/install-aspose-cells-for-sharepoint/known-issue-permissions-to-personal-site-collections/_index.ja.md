---
title: 既知の問題  パーソナルサイトコレクションへのアクセス権
type: docs
weight: 40
url: /ja/sharepoint/known-issue-permissions-to-personal-site-collections/
---

{{% alert color="primary" %}} 

SharePointでは、デフォルトでポータル管理者にパーソナルサイトを管理する権限が与えられません。そのため、ポータル管理者がパーソナルサイトコレクションのアクティブ化や非アクティブ化を行うと、失敗する場合があります。これはセットアップ中にも含まれます。

{{% /alert %}} 
### **パーソナルサイトへの権限付与**
この問題がインストール中に発生した場合、Microsoft.SharePoint.SPFeature.Activate()でUnauthorizedAccessExceptionがSharePointトレースログに記録されます。アンインストールの一環として非アクティブ化に失敗した場合、失敗した非アクティブ化の最後のセットアップ画面にUnauthorizedAccessExceptionが表示されます。

この問題を回避するには、ポータル管理者にMySite Webアプリケーションを管理する権限を与えます:

1. **SharePoint Central Administration**に移動し、**アプリケーション管理**タブを選択します。
1. **アプリケーションセキュリティ**グループの下にある**Webアプリケーションのポリシー**を選択します。
1. 右側の**Webアプリケーション**リストで、自分の“My Site”に正しいWebアプリケーションを選択してください。
1. 左上の**ユーザーの追加**を選択します。
1. **ユーザーの追加**画面ではデフォルトで**すべてのゾーン**を選択し、**次へ**をクリックします。
1. “My Site” Webアプリケーションを管理するための適切なユーザーまたはアクティブディレクトリーグループを追加します。
1. コントロールレベルを選択します。 

   **ユーザーの追加とコントロールレベルの設定** 

![todo:image_alt_text](known-issue-permissions-to-personal-site-collections_1.png)




1. **完了**をクリックします。
