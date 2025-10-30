---
title: ODSファイルの暗号化と複合化
type: docs
weight: 10
url: /ja/python-net/encrypt-and-decrypt-ods-files/
description: Aspose.Cells for Python via .NETを使って、ODSファイルにパスワード保護と暗号化を掛けることができます。これは純粋な.NETライブラリです。
---

{{% alert color="primary" %}}
OpenOffice.orgはパスワード保護とファイルの暗号化をサポートする完全な機能を備えたオフィススイートです。ただし、暗号化されたODSファイルはパスワードを提供した後にのみOpenOfficeで開くことができ、Excelは暗号化されたODSファイルを開くことはできません。暗号化オプションは、その他のファイルタイプとは異なり、ODSファイルには適用されません。 
Aspose.Cells for Python via .NETは、ODSファイルの暗号化と復号化を可能にします。復号化されたODSファイルはExcelやOpenOfficeの両方で開くことができます。 
{{% /alert %}}

## **OpenOffice Calcで暗号化**
1. 「名前を付けて保存」を選択し、「パスワードで保存」ボックスをクリックします。
1. **保存**ボタンをクリックします。
1. 開いた「パスワードの設定」ウィンドウの「開くためのパスワードを入力」および「パスワードを確認」フィールドに希望するパスワードを入力します。 
1. ファイルを保存するために **OK** ボタンをクリックします。

## **ODSファイルの暗号化（暗号化とパスワード保護）にAspose.Cells for Python via .NETを使用します。**
ODSファイルを暗号化するには、ファイルを読み込んで保存する前に[**WorkbookSettings.password**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/password)の値を実際のパスワードに設定します。出力される暗号化されたODSファイルは、OpenOfficeでのみ開くことができます。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-EncryptingODSFiles-1.py" >}}

## **Aspose.Cells for Python via .NETを使って、強力な暗号化タイプのExcelファイルを暗号化し、パスワード保護することも可能です。**

ODSファイルを復号化するには、[**LoadOptions.password**](https://reference.aspose.com/cells/python-net/aspose.cells/loadoptions/password)によるパスワードの提供でファイルを読み込みます。ファイルが読み込まれたら、[**WorkbookSettings.password**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/password)文字列をnullに設定します。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-DecryptingODSFiles-1.py" >}}

{{< app/cells/assistant language="python-net" >}}
