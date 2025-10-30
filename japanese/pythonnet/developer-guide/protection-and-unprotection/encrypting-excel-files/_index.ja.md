---
title: Excelファイルの暗号化
type: docs
weight: 90
url: /ja/python-net/encrypting-excel-files/
---

{{% alert color="primary" %}}

Microsoft Excel (97 - 365)を使用して、スプレッドシートを暗号化およびパスワード保護することができます。暗号化には、暗号化サービスプロバイダー（CSP）によって提供されるアルゴリズムが使用されます。暗号化キーの長さを適切に選択することが重要です。一部のCSPは40ビットまたは56ビットを超える長さをサポートしていません。これは弱い暗号化と見なされます。強力な暗号化には、最小128ビットのキー長が必要です。Microsoft Windowsには、強力な暗号化タイプを提供するCSPも含まれています。例えば、「Microsoft Strong Cryptographic Provider」などです。128ビットの暗号化は、銀行がインターネットバンキングシステムとの接続を暗号化する際に使用するものです。

Aspose.Cells for Python via .NETを使ってMicrosoft Excelファイルを暗号化し、パスワード保護を行うことができます。

{{% /alert %}}

## **Microsoft Excel の使用**

Microsoft Excel（ここではMicrosoft Excel 2003）でファイルの暗号化設定を行うには：

1. **ツール**メニューから**オプション**を選択します。ダイアログが表示されます。
1. **セキュリティ**タブを選択します。
1. パスワードを入力し、**詳細**をクリックします。
1. 暗号化方式を選択し、パスワードを確認します。

## **Aspose.Cells を使用した暗号化**

この例は、Aspose.Cells for Python via .NET APIを使用してExcelファイルを暗号化し、パスワード保護する方法を示しています。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-EncryptingFiles-1.py" >}}

### **修正パスワードを指定するオプション**

この例は、既存のファイルに対してAspose.Cells for Python via .NETを使って**変更パスワード**を設定する方法を示しています。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-SpecifyPasswordToModifyOption.py" >}}

## **暗号化されたファイルのパスワードを確認します**

暗号化されたファイルのパスワードを確認するには、Aspose.Cells for Python via .NETが[**verify_password**](https://reference.aspose.com/cells/python-net/aspose.cells/fileformatutil/verify_password)メソッドを提供します。これらのメソッドは、ファイルストリームと検証したいパスワードの2つのパラメータを受け取ります。
以下のコードスニペットは、提供されたパスワードが有効かどうかを確認する[**verify_password**](https://reference.aspose.com/cells/python-net/aspose.cells/fileformatutil/verify_password)メソッドの使用を示しています。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-VerifyPassword-1.py" >}}

## **ODSファイルの暗号化/復号化**

Aspose.Cells for Python via .NETは、ODSファイルの暗号化と復号化をサポートします。復号化されたODSファイルはExcelとOpenOfficeの両方で開けますが、暗号化されたODSファイルはパスワード入力後にOpenOfficeでのみ開くことが可能です。Excelでは暗号化されたODSファイルを開けず、警告が出ることがあります。ODSファイルの暗号化には、ファイルをロードして実際のパスワードを設定し（[**WorkbookSettings.password**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/password)に設定）、保存します。出力された暗号化ODSファイルはOpenOfficeだけで開けます。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-EncryptingODSFiles-1.py" >}}

ODSファイルを復号化するには、[**LoadOptions.password**](https://reference.aspose.com/cells/python-net/aspose.cells/loadoptions/password)によるパスワードの提供でファイルを読み込みます。ファイルが読み込まれたら、[**WorkbookSettings.password**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/password)文字列をnullに設定します。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-DecryptingODSFiles-1.py" >}}

{{< app/cells/assistant language="python-net" >}}
