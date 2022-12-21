---
title: 強力な暗号化タイプの設定
type: docs
weight: 60
url: /ja/net/setting-strong-encryption-type/
---
{{% alert color="primary" %}} 

Microsoft Excel (97-2007/2010) では、スプレッドシートを暗号化し、パスワードで保護できます。これは、Crypto Service Provider によって提供されるアルゴリズムを使用します。暗号化サービス プロバイダー (または CSP) は、さまざまなプロパティを持つ一連の暗号化アルゴリズムです。デフォルトの CSP は「Office 97/2000 互換」です。これは、公に知られているいくつかのセキュリティ上の問題がある CSP です。 「弱い暗号化 (XOR)」または「Office 97/2000 互換」暗号化タイプで保護されたスプレッドシートは、簡単にクラックできます。

この問題を解決するには、Microsoft Excel が提供する強力な暗号化タイプのいずれかを使用してください。暗号化の種類を利用可能な最強の CSP に変更できます。強力な暗号化には、「Microsoft 強力な暗号化プロバイダー」のように、128 ビット以上のキー長が必要です。

Aspose.Cells API を使用して、強力な暗号化タイプで Excel ファイルを暗号化し、パスワードで保護することもできます。

{{% /alert %}} 
## **Microsoft Excel で暗号化を適用する**
Microsoft Excel (2007 など) でファイル暗号化を実装するには:

1. から**ツール**メニュー、選択**オプション**.
1. を選択**安全**タブ。
1. の値を入力します**開くためのパスワード**分野。
1. クリック**高度**.
1. 暗号化タイプを選択し、パスワードを確認します。
## **Aspose.Cells による暗号化の適用**
以下のコード例では、ファイルに強力な暗号化を適用し、パスワードを設定しています。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-SettingStrongEncryptionType-1.cs" >}}
