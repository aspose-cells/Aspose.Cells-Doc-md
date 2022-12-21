---
title: Excel ファイルの暗号化
type: docs
weight: 90
url: /ja/net/encrypting-excel-files/
---
{{% alert color="primary" %}}

Microsoft Excel (97 - 365) では、スプレッドシートを暗号化し、パスワードで保護できます。暗号化サービス プロバイダー (CSP) によって提供されるアルゴリズムを使用します。これは、さまざまなプロパティを持つ一連の暗号化アルゴリズムです。デフォルトの CSP は「Office 97/2000 互換」または「弱い暗号化 (XOR)」です。適切な暗号化キーの長さを選択することが重要です。一部の CSP は、40 ビットまたは 56 ビットを超えるビットをサポートしていません。これは弱い暗号化と見なされます。強力な暗号化を行うには、128 ビット以上のキー長が必要です。 Microsoft Windows には、「Microsoft 強力な暗号化プロバイダー」などの強力な暗号化タイプも提供する CSP が含まれています。 128 ビット暗号化は、銀行がインターネット バンキング システムとの接続を暗号化するために使用するものです。

Aspose.Cells を使用すると、目的の暗号化タイプで Microsoft Excel ファイルを暗号化し、パスワードで保護できます。

{{% /alert %}}

## **Microsoft エクセルを使う**

Microsoft Excel (ここでは Microsoft Excel 2003) でファイル暗号化設定を設定するには:

1. から**ツール**メニュー、選択**オプション**.ダイアログが表示されます。
1. を選択**安全**タブ。
1. パスワードを入力してクリック**高度**
1. 暗号化タイプを選択し、パスワードを確認します。

## **Aspose.Cellsで暗号化**

次の例は、Aspose.Cells API を使用して Excel ファイルを暗号化し、パスワードで保護する方法を示しています。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-EncryptingFiles-1.cs" >}}

### **オプションを変更するためのパスワードの指定**

次の例は、**変更するパスワード** Microsoft Aspose.Cells API を使用した既存ファイルの Excel オプション。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-EncryptingFiles-SpecifyPasswordToModifyOption.cs" >}}

## **暗号化されたファイルのパスワードを確認する**

暗号化されたファイルのパスワードを確認するには、Aspose.Cells for .NET を指定します。[**パスワードを照合します**](https://reference.aspose.com/cells/net/aspose.cells/fileformatutil/methods/verifypassword)方法。これらのメソッドは、検証が必要なファイル ストリームとパスワードの 2 つのパラメータを受け入れます。
次のコード スニペットは、[**パスワードを照合します**](https://reference.aspose.com/cells/net/aspose.cells/fileformatutil/methods/verifypassword)提供されたパスワードが有効かどうかを検証するメソッド。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-VerifyPassword-1.cs" >}}

## **Aspose.Cells を使用した ODS ファイルの暗号化/復号化**

Aspose.Cells では、ODS ファイルを暗号化および復号化できます。復号化された ODS ファイルは、Excel と OpenOffice の両方で開くことができますが、暗号化された ODS ファイルは、パスワードを入力した後でのみ OpenOffice で開くことができます。 Excel は暗号化された ODS ファイルを開くことができず、警告メッセージが表示される場合があります。暗号化オプションは、他のファイル タイプとは異なり、ODS ファイルには適用されません。 ODS ファイルを暗号化するには、ファイルをロードして[**WorkbookSettings.Password**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/password)値を実際のパスワードに変更してから保存してください。出力された暗号化された ODS ファイルは、OpenOffice でのみ開くことができます。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-EncryptingODSFiles-1.cs" >}}

 ODS ファイルを復号化するには、[**LoadOptions.Password**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/properties/password) .ファイルがロードされたら、[**WorkbookSettings.Password**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/password)文字列を null にします。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-DecryptingODSFiles-1.cs" >}}
