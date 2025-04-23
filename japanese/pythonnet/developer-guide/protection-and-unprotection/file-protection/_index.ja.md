---
title: Excelファイルの暗号化および復号化
type: docs
weight: 10
url: /ja/python-net/encrypt-and-decrypt-excel-files/
description: Pythonを使用してExcelファイルを暗号化および復号化する方法。Excelファイルをロックし、ロックを解除します。
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

## **Aspose.CellsでExcelファイルを暗号化**

この例は、Aspose.Cells for Python via .NET APIを使用してExcelファイルを暗号化し、パスワード保護する方法を示しています。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-EncryptingFiles-1.py" >}}

### **修正パスワードを指定するオプション**

この例は、既存のファイルに対してAspose.Cells for Python via .NETを使って**変更パスワード**を設定する方法を示しています。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-SpecifyPasswordToModifyOption.py" >}}


## **Aspose.CellsでExcelファイルを復号化**
パスワード保護されたエクセルファイルを開き、次のコードのようにAspose.Cells for Python via .NET APIを使用して復号化するのは非常に簡単です：

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-Decrypt-Excel-File.py" >}}


## **高度なトピック**
- [ODSファイルの暗号化および復号化](/cells/ja/python-net/encrypt-and-decrypt-ods-files/)
- [強力な暗号化タイプの設定](/cells/ja/python-net/setting-strong-encryption-type/)
- [ブックを書き込み保護する際に著者を指定する](/cells/ja/python-net/specify-author-while-write-protecting-workbook/)
- [暗号化されたファイルのパスワードの検証](/cells/ja/python-net/verify-password-of-encrypted-excel-and-ods-files/)

