---
title: 証明書を使用して VBA コード プロジェクトにデジタル署名する
type: docs
weight: 110
url: /ja/net/digitally-sign-a-vba-code-project-with-certificate/
---
{{% alert color="primary" %}}

Aspose.Cells を使用して VBA コード プロジェクトにデジタル署名できます。[**Workbook.VbaProject.Sign()**](https://reference.aspose.com/cells/net/aspose.cells.vba/vbaproject/methods/sign)方法。次の手順に従って、Excel ファイルが証明書でデジタル署名されているかどうかを確認してください。

- クリック**ビジュアルベーシック**から**デベロッパー**開くタブ**Visual Basic for Applications IDE**
- クリック**ツール** > **デジタル署名...**の**Visual Basic for Applications IDE**

そして、それは**デジタル署名フォーム**ドキュメントが証明書でデジタル署名されているかどうかを示します。

{{% /alert %}} 

## **C# の証明書を使用して VBA コード プロジェクトにデジタル署名する**

次のサンプル コードは、[**Workbook.VbaProject.Sign()**](https://reference.aspose.com/cells/net/aspose.cells.vba/vbaproject/methods/sign)方法。サンプル コードの入力ファイルと出力ファイルを次に示します。任意の Excel ファイルと任意の証明書を使用して、このコードをテストできます。

- [ソースの Excel ファイル](5115028.xlsm)サンプルコードで使用します。
- [サンプル pfx ファイル](5115039.pfx)デジタル署名を作成します。このコードを実行するには、コンピュータにインストールしてください。パスワードは 1234 です。
- [Excelファイルを出力](5115029.xlsm)サンプルコードによって生成されます。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingVBAModules-DigitallySignVbaProjectWithCertificate-1.cs" >}}
