---
title: 強力な暗号化方式の設定
type: docs
weight: 10
url: /ja/java/setting-strong-encryption-type/
---

{{% alert color="primary" %}}

Microsoft Excel (97-2007/2010) は、スプレッドシートを暗号化し、パスワードで保護することができます。これには暗号サービスプロバイダが提供するアルゴリズムが使用されます。暗号サービスプロバイダ（CSP）とは、異なる性質の暗号アルゴリズムのセットです。デフォルトのCSPは「Office 97/2000互換」です。これは一部の公に知られているセキュリティ上の問題を抱えたCSPです。『弱い暗号化（XOR）』や「Office 97/2000互換」暗号方式で保護されたスプレッドシートは簡単に解読できます。

この問題を克服するために、Microsoft Excelが提供する強力な暗号化方式を使用してください。暗号化方式を最も強力なCSPに変更することができます。強力な暗号化には、最低128ビットの鍵長が必要です。例えば『Microsoft Strong Cryptographic Provider』です。

Aspose.Cells APIを使用して、強力な暗号化方式を使ったExcelファイルに暗号化し、パスワードを設定することもできます。

{{% /alert %}}

## **Microsoft Excelでの暗号化の適用**

Microsoft Excel（たとえば2007）でファイルの暗号化を実装するには:

1. **ツール**メニューから**オプション**を選択します。
1. **セキュリティ**タブを選択します。
1. **開くためのパスワード**フィールドに値を入力します。
1. **高度** をクリックします。
1. 暗号化方式を選択し、パスワードを確認します。

   **Microsoft Excelでの暗号化設定**

![todo:image_alt_text](setting-strong-encryption-type_1.png)

## **Aspose.Cellsを使用した暗号化の適用**

以下のコード例では、ファイルに強力な暗号化を適用し、パスワードを設定しています。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ApplyingEncryption-ApplyingEncryption.java" >}}
