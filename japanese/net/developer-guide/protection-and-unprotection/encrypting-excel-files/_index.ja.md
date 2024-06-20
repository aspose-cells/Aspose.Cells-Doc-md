---
title: Excelファイルの暗号化
type: docs
weight: 90
url: /ja/net/encrypting-excel-files/
---

{{% alert color="primary" %}}

Microsoft Excel (97 - 365)を使用して、スプレッドシートを暗号化およびパスワード保護することができます。暗号化には、暗号化サービスプロバイダー（CSP）によって提供されるアルゴリズムが使用されます。暗号化キーの長さを適切に選択することが重要です。一部のCSPは40ビットまたは56ビットを超える長さをサポートしていません。これは弱い暗号化と見なされます。強力な暗号化には、最小128ビットのキー長が必要です。Microsoft Windowsには、強力な暗号化タイプを提供するCSPも含まれています。例えば、「Microsoft Strong Cryptographic Provider」などです。128ビットの暗号化は、銀行がインターネットバンキングシステムとの接続を暗号化する際に使用するものです。

Aspose.Cellsを使用すると、任意の暗号化タイプでMicrosoft Excelファイルを暗号化およびパスワード保護することができます。

{{% /alert %}}

## **Microsoft Excel の使用**

Microsoft Excel（ここではMicrosoft Excel 2003）でファイルの暗号化設定を行うには：

1. **ツール**メニューから**オプション**を選択します。ダイアログが表示されます。
1. **セキュリティ**タブを選択します。
1. パスワードを入力し、**詳細**をクリックします。
1. 暗号化方式を選択し、パスワードを確認します。

## **Aspose.Cells を使用した暗号化**

次の例は、Aspose.Cells APIを使用してExcelファイルを暗号化およびパスワード保護する方法を示しています。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-EncryptingFiles-1.cs" >}}

### **修正パスワードを指定するオプション**

次の例は、Aspose.Cells APIを使用して既存のファイルの**修正パスワード**Microsoft Excelオプションを設定する方法を示しています。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-EncryptingFiles-SpecifyPasswordToModifyOption.cs" >}}

## **暗号化されたファイルのパスワードを確認します**

Aspose.Cells for .NETは、暗号化されたファイルのパスワードを検証するための[**VerifyPassword**](https://reference.aspose.com/cells/net/aspose.cells/fileformatutil/methods/verifypassword)メソッドを提供します。これらのメソッドは、ファイルストリームと検証する必要があるパスワードの2つのパラメータを受け入れます。
以下のコードスニペットは、提供されたパスワードが有効かどうかを確認する[**VerifyPassword**](https://reference.aspose.com/cells/net/aspose.cells/fileformatutil/methods/verifypassword)メソッドの使用を示しています。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-VerifyPassword-1.cs" >}}

## **Aspose.Cells を使用して ODS ファイルの暗号化/復号化**

Aspose.Cellsを使用すると、ODSファイルを暗号化および復号化することができます。復号されたODSファイルは、ExcelとOpenOfficeの両方で開くことができますが、暗号化されたODSファイルはOpenOfficeでのみパスワードを提供した後に開くことができます。Excelは暗号化されたODSファイルを開くことができず、警告メッセージが表示される場合があります。暗号化オプションは他のファイルタイプとは異なり、ODSファイルには適用されません。ODSファイルを暗号化するには、ファイルを読み込んでから保存する前に、実際のパスワードを[**WorkbookSettings.Password**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/password)の値に設定します。出力された暗号化されたODSファイルはOpenOfficeのみで開くことができます。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-EncryptingODSFiles-1.cs" >}}

ODSファイルを復号化するには、[**LoadOptions.Password**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/properties/password)によるパスワードの提供でファイルを読み込みます。ファイルが読み込まれたら、[**WorkbookSettings.Password**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/password)文字列をnullに設定します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-DecryptingODSFiles-1.cs" >}}
