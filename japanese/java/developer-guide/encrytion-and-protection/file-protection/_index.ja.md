---
title: Excel ファイルの暗号化と復号化
type: docs
weight: 40
url: /ja/java/encrypt-and-decrypt-excel-files/
description: Javaを使用してExcelファイルを暗号化および復号化する方法. Excel ファイルをロックおよびロック解除します。
---
{{% alert color="primary" %}}
Microsoft Excel (97 - 365 ) では、スプレッドシートを暗号化/パスワード保護できます。 Crypto Service Provider が提供するアルゴリズムを利用します。暗号化サービス プロバイダー (CSP) は、さまざまなプロパティを持つ一連の暗号化アルゴリズムです。デフォルトの CSP は、「Office 97/2000 互換」または「週暗号化 (XOR)」です。適切な暗号化キーの長さを選択することも重要です。暗号化サービス プロバイダーの中には、40 ビットまたは 56 ビットを超えるビットをサポートしていないものがあります。これは、弱い暗号化タイプと見なされます。ただし、強力な暗号化タイプの場合、最小キー長は 128 ビットである必要があります。 Microsoft Windows には、「Microsoft 強力な暗号化プロバイダー」など、強力な暗号化タイプも提供する暗号化サービス プロバイダーが含まれています。 128 ビット暗号化は、銀行がインターネット バンキング システムとの接続を暗号化するために使用するものです。 Aspose.Cells を使用すると、目的の暗号化タイプで Excel ファイルを暗号化/パスワード保護できます。

{{% /alert %}}

## **MS Excel の使用**

MS Excel (MS Excel 2003 など) でファイル暗号化設定を実装するには、次のことを試してください。

- から**ツール**メニュー、選択**オプション**を選択し、**安全**タブ。
- 入力**開くためのパスワード**をクリックし、**高度**ボタン。
- 暗号化タイプを選択し、パスワードを確認します。

![todo:画像_代替_文章](encrypting-excel-files_1.png)

**図: [オプション] ダイアログ**

![todo:画像_代替_文章](encrypting-excel-files_2.png)

**図: [暗号化の種類] ダイアログ**

## **Excelファイルの暗号化**
次の例は、Aspose.Cells API を使用して Excel ファイルを暗号化/パスワード保護する方法を示しています。

### **サンプルコード:**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-EncryptingFiles-EncryptingFiles.java" >}}


## **Aspose.Cells で Excel ファイルを復号化する**
パスワードで保護された Excel ファイルを開き、次のコードとして Aspose.Cells API を使用して復号化するのは非常に困難です。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Decrypt-Excel-File.java" >}}



