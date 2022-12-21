---
title: Excel ファイルの暗号化と復号化
type: docs
weight: 10
url: /ja/python-java/encrypt-and-decrypt-excel-files/
description: Python を使用して Excel ファイルを暗号化および復号化する方法。Excel ファイルのロックとロック解除。
---
{{% alert color="primary" %}}

Microsoft Excel (97 - 365) では、スプレッドシートを暗号化し、パスワードで保護できます。暗号化サービス プロバイダー (CSP) によって提供されるアルゴリズムを使用します。これは、さまざまなプロパティを持つ一連の暗号化アルゴリズムです。デフォルトの CSP は「Office 97/2000 互換」または「弱い暗号化 (XOR)」です。適切な暗号化キーの長さを選択することが重要です。一部の CSP は、40 ビットまたは 56 ビットを超えるビットをサポートしていません。これは弱い暗号化と見なされます。強力な暗号化を行うには、128 ビット以上のキー長が必要です。 Microsoft Windows には、「Microsoft 強力な暗号化プロバイダー」などの強力な暗号化タイプも提供する CSP が含まれています。 128 ビット暗号化は、銀行がインターネット バンキング システムとの接続を暗号化するために使用するものです。

Aspose.Cells for Python を使用すると、目的の暗号化タイプで Microsoft Excel ファイルを暗号化し、パスワードで保護できます。

{{% /alert %}}

## **Microsoft エクセルを使う**

Microsoft Excel (ここでは Microsoft Excel 2003) でファイル暗号化設定を設定するには:

1. から**ツール**メニュー、選択**オプション**.ダイアログが表示されます。
1. を選択**安全**タブ。
1. パスワードを入力してクリック**高度**
1. 暗号化タイプを選択し、パスワードを確認します。

## **Aspose.Cells で Excel ファイルを暗号化する**

次の例は、Aspose.Cells API を使用して Excel ファイルを暗号化し、パスワードで保護する方法を示しています。

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Examples-CSharp-Files-Utility-EncryptingFiles-1.py" >}}

## **Aspose.Cells で Excel ファイルを復号化する**
パスワードで保護された Excel ファイルを開き、次のコードとして Aspose.Cells API を使用して復号化するのは非常に困難です。

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Decrypt-Excel-File.py" >}}


