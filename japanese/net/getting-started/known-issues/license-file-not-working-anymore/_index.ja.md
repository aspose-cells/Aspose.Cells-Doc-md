﻿---
title: ライセンス ファイルが機能しなくなった
type: docs
weight: 60
url: /ja/net/license-file-not-working-anymore/
---
## **症状**

Web プロジェクトを新しいサーバーに移動/公開すると、ライセンス ファイルが機能しなくなることにユーザーが不満を感じることがあります。ライセンス ファイルが以前の (古い) サーバーで適切に機能していたため、不満を感じていましたが、今では追加のライセンスを取得しています。**評価著作権に関する警告**新しいサーバー環境でワークシートに透かしを入れます (コンポーネントを使用してレポートを生成するときはいつでも)。

### **シナリオ**

「私たちは、ASP.NET Web プロジェクトで Aspose.Cells を使用して Excel レポートを生成/操作してきました。使用している有効なライセンスを取得しました。数日前に、Web サイトを新しいサーバーに移動しました。アップグレードや変更はまったくありませんでした。 Aspose.Cells.dll および関連する .lic ファイルを含む、すべてのファイルを新しいサーバーに移動したことを確認し、単純にしました。新しいサーバー環境で Excel レポートを生成しようとすると、**評価著作権に関する警告**レポートの透かしシート。サイトの [My Orders] セクションから新しいライセンス ファイルをダウンロードしてインストールしようとしましたが、問題はまったく解決しませんでした。参考までに、Aspose.Cells.lic ファイルを Aspose.Cells.dll コンポーネント ファイルと一緒にサイトの bin フォルダーに配置することでライセンスを実装しますが、前述のように、古いサーバーでは問題なく動作しました。"

### **解決**

Aspose には、クリーンで信頼性の高いライセンス メカニズムがあります。通常、問題は展開の問題に関連している必要があります。ライセンス ファイルが (サーバー上で) 正常に機能する場合、他のサーバー/環境でも同様に正常に機能するはずです。通常、ユーザーはアプリケーションを使用します_開始またはセッション_global.asax ファイルでイベントなどを開始して、そこにライセンス コードを配置します。そのため、アプリケーションが_開始 / セッション_新しい場所でライセンス コードを処理するために開始イベントが発生しません。ここで、Aspose.Cells は、コンポーネントがパスでライセンス ファイルを見つけられない場合、常に例外をスローすることに注意してください。ユーザーは、ライセンス コード (どこに配置しても) が処理され、ライセンス コードを配置するイベントがトリガーされることを確認する必要があります。ユーザーは、関連サービス、つまり「World Wide Web Publishing」を再起動して、アプリケーションが_開始 / セッション_新しいサーバー環境でプロジェクトにアクセスすると、開始イベントがトリガーされます。

### **確認**

また、確認してください…

- プロジェクトで有効なライセンス ファイルを使用しています。
- 少なくともライセンス ファイルが機能しなくなる可能性があるため、ライセンス ファイルを編集または変更しないでください。
- ライセンス サブスクリプションの有効期限に注意する必要があります (lic ファイルをメモ帳で開き、有効期限を確認するだけです)。
- ライセンス サブスクリプションの有効期限が切れた後にリリースされたバージョン (Aspose.Cells.dll) を使用していません。ここで注意していただきたいのは、ライセンス ファイルには有効期限がありませんが、サブスクリプションの有効期限後にリリースされるコンポーネント バージョンを使用している場合は、追加の**評価著作権に関する警告**Excelファイルを作成するたびに透かしシート。

### **参考文献**

<https://forum.aspose.com/t/license-file-not-working-on-new-server/83110>

<https://forum.aspose.com/t/license-not-being-detected/83516/4>
