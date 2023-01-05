---
title: ODS ファイルの暗号化と復号化
type: docs
weight: 10
url: /ja/java/encrypt-and-decrypt-ods-files/
description: パスワードで保護し、純粋な Java ライブラリである Aspose.Cells for Java を使用して ODS ファイルを暗号化します。
---
{{% alert color="primary" %}}
OpenOffice.org は、パスワード保護とファイルの暗号化をサポートするフル機能のオフィス スイートです。ただし、暗号化された ODS ファイルは、パスワードを入力した後にのみ OpenOffice で開くことができます。 Excel は暗号化された ODS ファイルを開くことができず、警告メッセージが表示される場合があります。暗号化オプションは、他のファイル タイプとは異なり、ODS ファイルには適用されません。
 Aspose.Cells は、ODS ファイルの暗号化と復号化を許可します。復号化された ODS ファイルは、Excel と OpenOffice の両方で開くことができます。
{{% /alert %}}

## **OpenOffice Calc で暗号化する**
1. 選択する**名前を付けて保存**をクリックし、**パスワード付きで保存**箱。
1. クリック**セーブ**ボタン。
1. 必要なパスワードを両方に入力します**パスワードを入力して開く**と**パスワードを認証する**表示される [パスワードの設定] ウィンドウのフィールド。
1. クリック**わかった**ボタンをクリックしてファイルを保存します。

## **暗号化/復号化 ODS ファイル:**

 ODS ファイルを暗号化するには、ファイルをロードし、実際のパスワードを[**WorkbookSettings.setPassword()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#Password)保存する前に。出力の暗号化された ODS ファイルは、OpenOffice でのみ開くことができます。 ODS ファイルを復号化するには、[**LoadOptions.setPassword()**](https://reference.aspose.com/cells/java/com.aspose.cells/loadoptions#Password) .ファイルがロードされたら、関数を呼び出します[**Workbook.unprotect()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#unprotect(java.lang.String) ) 引数として実際のパスワードを使用し、最後に null をに渡します[**Workbook.getWorkbookSettings().setPassword()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#Password).

### **サンプルコード:**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-EncryptingODSFiles-EncryptingODSFiles.java" >}}
