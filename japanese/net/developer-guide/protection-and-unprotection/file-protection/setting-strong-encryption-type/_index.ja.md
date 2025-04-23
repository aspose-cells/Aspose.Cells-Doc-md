---
title: 強力な暗号化方式の設定
type: docs
weight: 60
url: /ja/net/setting-strong-encryption-type/
---

{{% alert color="primary" %}} 

Microsoft Excel (97-2007/2010)では、スプレッドシートにパスワードを設定して保護し、暗号化することができます。これには暗号化アルゴリズムを提供するCrypto Service Providerが使用されます。Crypto Service Provider（CSP）は、異なる特性を持つ暗号化アルゴリズムのセットです。デフォルトのCSPは「Office 97/2000 Compatible」です。これは一部の公に知られているセキュリティの問題を持つCSPです。「弱い暗号化（XOR）」または「Office 97/2000 Compatible」暗号化タイプで保護されたスプレッドシートは容易にクラックできます。

この問題を解決するには、Microsoft Excelが提供する強力な暗号化タイプの1つを使用します。最強のCSPに暗号化タイプを変更することができます。強力な暗号化には、最低128ビットの鍵長が必要です；たとえば、「Microsoft Strong Cryptographic Provider」。

Aspose.Cells APIを使用して、強力な暗号化方式を使ったExcelファイルに暗号化し、パスワードを設定することもできます。

{{% /alert %}} 
## **Microsoft Excelでの暗号化の適用**
Microsoft Excel（たとえば2007）でファイルの暗号化を実装するには:

1. **ツール**メニューから**オプション**を選択します。
1. **セキュリティ**タブを選択します。
1. **開くためのパスワード**フィールドに値を入力します。
1. **高度** をクリックします。
1. 暗号化方式を選択し、パスワードを確認します。
## **Aspose.Cellsを使用した暗号化の適用**
以下のコード例は、ファイルに強力な暗号化を適用し、パスワードを設定します。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-SettingStrongEncryptionType-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
