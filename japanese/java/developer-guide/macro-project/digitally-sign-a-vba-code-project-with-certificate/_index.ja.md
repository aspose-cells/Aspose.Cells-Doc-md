---
title: 証明書でVBAコードプロジェクトにデジタル署名する
type: docs
weight: 110
url: /ja/java/digitally-sign-a-vba-code-project-with-certificate/
---

{{% alert color="primary" %}}

Aspose.Cellsを使用してVBAコードプロジェクトにデジタル署名することができます。 [**Workbook.VbaProject.Sign()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbaproject#sign-com.aspose.cells.DigitalSignature-) 方法を使用してください。 Excelファイルが証明書でデジタル署名されているかどうかを確認するには、次の手順に従ってください。

- **開発**タブから**Visual Basic**をクリックして**Visual Basic for Applications IDE**を開きます
- **Visual Basic for Applications IDE**の**ツール** > **デジタル署名...**をクリック

そうすると**デジタル署名フォーム**が表示され、ドキュメントが証明書でデジタル署名されているかどうかが表示されます。

{{% /alert %}} 

## **C#でVBAコードプロジェクトに証明書でデジタル署名する**

次のサンプルコードは、[**Workbook.VbaProject.Sign()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbaproject#sign-com.aspose.cells.DigitalSignature-) 方法を使用する方法を示しています。サンプルコードの入出力ファイルは次のとおりです。任意のExcelファイルと任意の証明書を使用してこのコードをテストできます。

- サンプルのExcelファイル（5115028.xlsm）
- [サンプルpfxファイル（5115039.pfx）](5115039.pfx)でデジタル署名を作成します。このコードを実行するためにこのファイルをコンピューターにインストールしてください。パスワードは1234です。
- サンプルコードによって生成された出力Excelファイル（5115029.xlsm）

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "ManagingVBAModules-DigitallySignVbaProjectWithCertificate.java" >}}
{{< app/cells/assistant language="java" >}}
