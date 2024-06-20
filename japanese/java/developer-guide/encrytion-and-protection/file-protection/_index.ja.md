---
title: Excelファイルの暗号化および復号化
type: docs
weight: 40
url: /ja/java/encrypt-and-decrypt-excel-files/
description: Javaを使用してExcelファイルを暗号化および復号化する方法。Excelファイルをロックおよびアンロックします。
---

{{% alert color="primary" %}}
Microsoft Excel（97 - 365）を使用すると、スプレッドシートを暗号化/パスワード保護することができます。それはCryptoサービスプロバイダによって提供される暗号化アルゴリズムを利用します。デフォルトのCSPは「Office 97/2000 Compatible」または「Week Encryption (XOR)」です。また、適切な暗号化キー長を選択することが重要です。一部の暗号サービスプロバイダは40ビットまたは56ビットを超える長さをサポートしないことがあります。これは弱い暗号化タイプと見なされます。ただし、強力な暗号化タイプには、最小128ビットの鍵長が必要です。Microsoft Windowsには、銀行がインターネットバンキングシステムとの接続を暗号化するために使用する128ビットの暗号化が含まれています。Aspose.Cellsを使用して、希望の暗号化タイプでExcelファイルを暗号化/パスワード保護することができます。

{{% /alert %}}

## **MS Excelの使用**

MS Excel（たとえばMS Excel 2003）では、ファイルの暗号化設定を実装するために次のようにできます:

- **ツール**メニューから**オプション**を選択し、**セキュリティ**タブを選択します。
- **開くためのパスワード**を入力し、**詳細**ボタンをクリックします。
- 暗号化タイプを選択し、パスワードを確認します。

![todo:image_alt_text](encrypting-excel-files_1.png)

**図: オプションダイアログ**

![todo:image_alt_text](encrypting-excel-files_2.png)

**図: 暗号化タイプダイアログ**

## **Excelファイルの暗号化**
以下の例は、Aspose.Cells API を使用して Excel ファイルを暗号化 / パスワードで保護する方法を示しています。

### **サンプルコード:**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-EncryptingFiles-EncryptingFiles.java" >}}


## **Aspose.CellsでExcelファイルを復号化**
パスワードで保護されたExcelファイルを開くことや、Aspose.Cells APIを使用して復号化することは次のコードに示す通り非常に簡単です。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Decrypt-Excel-File.java" >}}



