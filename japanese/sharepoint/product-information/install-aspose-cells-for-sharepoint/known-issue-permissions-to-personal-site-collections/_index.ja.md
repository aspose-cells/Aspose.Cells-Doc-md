---
title: 既知の問題 - 個人用サイト コレクションへのアクセス許可
type: docs
weight: 40
url: /ja/sharepoint/known-issue-permissions-to-personal-site-collections/
---
{{% alert color="primary" %}} 

既定では、SharePoint は個人用サイトを管理するための完全なアクセス許可をポータル管理者に付与しません。そのため、個人用サイト コレクションのアクティブ化と非アクティブ化は、ポータル管理者によって実行されると失敗する場合があります。これには、セットアップ中のアクティブ化と非アクティブ化が含まれます。

{{% /alert %}} 
### **個人用サイトへの許可の付与**
インストール中にこの問題が発生すると、Microsoft.SharePoint.SPFeature.Activate() で UnauthorizedAccessException が SharePoint トレース ログに記録されます。アンインストールの一部として非アクティブ化が失敗すると、失敗した非アクティブ化の最後のセットアップ画面に UnauthorizedAccessException が表示されます。

この問題を回避するには、ポータル管理者に MySite Web アプリケーションを管理する権限を付与します。

1. に行く**SharePoint サーバーの全体管理**を選択します。**アプリケーション管理**タブ。
1. 選ぶ**Web アプリケーションのポリシー**下**アプリケーションのセキュリティ**グループ。
1. [個人用サイト] で正しい Web アプリケーションを選択していることを確認してください。**ウェブアプリケーション**右のリスト。
1. 選択する**ユーザーを追加**左上にあります。
1. 選ぶ**すべてのゾーン**デフォルトでは**ユーザーを追加**画面をクリックして**次**.
1. 「個人用サイト」Web アプリケーションを制御する適切なユーザーまたは Active Directory グループを追加します。
1. コントロールのレベルを選択します。

   **ユーザーの追加と制御レベルの設定** 

![todo:画像_代替_文章](known-issue-permissions-to-personal-site-collections_1.png)




1. クリック**終了**.
