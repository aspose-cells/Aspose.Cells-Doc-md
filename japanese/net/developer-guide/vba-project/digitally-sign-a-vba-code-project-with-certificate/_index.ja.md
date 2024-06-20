---
title: 証明書でVBAコードプロジェクトにデジタル署名する
type: docs
weight: 110
url: /ja/net/digitally-sign-a-vba-code-project-with-certificate/
---

{{% alert color="primary" %}}

Aspose.Cellsを使用してVBAコードプロジェクトにデジタル署名することができます。 [**Workbook.VbaProject.Sign()**](https://reference.aspose.com/cells/net/aspose.cells.vba/vbaproject/methods/sign) 方法を使用してください。 Excelファイルが証明書でデジタル署名されているかどうかを確認するには、次の手順に従ってください。

- **開発**タブから**Visual Basic**をクリックして**Visual Basic for Applications IDE**を開きます
- **Visual Basic for Applications IDE**の**ツール** > **デジタル署名...** をクリックします。

そうすると**デジタル署名フォーム**が表示され、ドキュメントが証明書でデジタル署名されているかどうかが表示されます。

{{% /alert %}} 

## **C#でVBAコードプロジェクトに証明書でデジタル署名する**

次のサンプルコードでは、[**Workbook.VbaProject.Sign()**](https://reference.aspose.com/cells/net/aspose.cells.vba/vbaproject/methods/sign) メソッドの使用方法を示しています。サンプルコードの入力および出力ファイルは任意のExcelファイルと任意の証明書を使用してテストできます。

- サンプルのExcelファイル（5115028.xlsm）
- [サンプルpfxファイル（5115039.pfx）](5115039.pfx)でデジタル署名を作成します。このコードを実行するためにこのファイルをコンピューターにインストールしてください。パスワードは1234です。
- サンプルコードによって生成された出力Excelファイル（5115029.xlsm）

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingVBAModules-DigitallySignVbaProjectWithCertificate-1.cs" >}}
