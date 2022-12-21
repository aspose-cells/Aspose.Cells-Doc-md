---
title: ODS ファイルの暗号化と復号化
type: docs
weight: 10
url: /ja/net/encrypt-and-decrypt-ods-files/
description: 純粋なネット ライブラリである .Net の Aspose.Cells を使用して ODS ファイルをパスワードで保護し、暗号化します。
---
{{% alert color="primary" %}}
 OpenOffice.org は、パスワード保護とファイルの暗号化をサポートするフル機能のオフィス スイートです。ただし、暗号化された ODS ファイルは、パスワードを入力した後でのみ OpenOffice で開くことができます。 Excel は暗号化された ODS ファイルを開くことができず、警告メッセージが表示される場合があります。暗号化オプションは、他のファイル タイプとは異なり、ODS ファイルには適用されません。
 Aspose.Cells では、ODS ファイルを暗号化および復号化できます。復号化された ODS ファイルは、Excel と OpenOffice の両方で開くことができます。
{{% /alert %}}

## **OpenOffice Calc で暗号化する**
1. 選択する**名前を付けて保存**をクリックし、**パスワード付きで保存**箱。
1. クリック**セーブ**ボタン。
1. 必要なパスワードを両方に入力します**パスワードを入力して開く**と**パスワードを認証する**表示される [パスワードの設定] ウィンドウのフィールド。
1. クリック**わかった**ボタンをクリックしてファイルを保存します。

## **.Net の Aspose.Cells で ODS ファイルを暗号化する**
ODS ファイルを暗号化するには、ファイルをロードして[**WorkbookSettings.Password**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/password)値を実際のパスワードに変更してから保存してください。出力された暗号化された ODS ファイルは、OpenOffice でのみ開くことができます。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-EncryptingODSFiles-1.cs" >}}

## **.Net の Aspose.Cells で ODS ファイルを復号化します。**

 ODS ファイルを復号化するには、[**LoadOptions.Password**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/properties/password) .ファイルがロードされたら、[**WorkbookSettings.Password**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/password)文字列を null にします。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-DecryptingODSFiles-1.cs" >}}
