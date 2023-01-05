---
title: 強力な暗号化タイプの設定
type: docs
weight: 10
url: /ja/java/setting-strong-encryption-type/
---
{{% alert color="primary" %}}

Microsoft Excel (97-2007/2010) では、スプレッドシートを暗号化し、パスワードで保護できます。これは、Crypto Service Provider によって提供されるアルゴリズムを使用します。暗号化サービス プロバイダー (または CSP) は、さまざまなプロパティを持つ一連の暗号化アルゴリズムです。デフォルトの CSP は「Office 97/2000 互換」です。これは、公開されている既知のセキュリティ上の問題がある CSP です。 「弱い暗号化 (XOR)」または「Office 97/2000 互換」暗号化タイプで保護されたスプレッドシートは、簡単にクラックできます。

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

   **Microsoft Excel での暗号化の設定**

![todo:画像_代替_文章](setting-strong-encryption-type_1.png)

## **Aspose.Cells による暗号化の適用**

以下のコード例では、ファイルに強力な暗号化を適用し、パスワードを設定しています。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ApplyingEncryption-ApplyingEncryption.java" >}}
