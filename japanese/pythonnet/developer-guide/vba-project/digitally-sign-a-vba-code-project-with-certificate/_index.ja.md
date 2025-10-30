---
title: 証明書でVBAコードプロジェクトにデジタル署名する
type: docs
weight: 110
url: /ja/python-net/digitally-sign-a-vba-code-project-with-certificate/
---

{{% alert color="primary" %}}

Aspose.Cells for Python via .NETの[**Workbook.vba_project.sign()**](https://reference.aspose.com/cells/python-net/aspose.cells.vba/vbaproject/sign/#aspose.cells.digitalsignatures.DigitalSignature)メソッドを使用して、VBAコードプロジェクトにデジタル署名を付与できます。証明書を用いたデジタル署名の確認手順を以下に示します。

- **開発**タブから**Visual Basic**をクリックして**Visual Basic for Applications IDE**を開きます
- **Visual Basic for Applications IDE**の**ツール** > **デジタル署名...** をクリックします。

そうすると**デジタル署名フォーム**が表示され、ドキュメントが証明書でデジタル署名されているかどうかが表示されます。

{{% /alert %}} 

## **証明書を使用してVBAコードプロジェクトにデジタル署名を行う方法（Python）**

次のサンプルコードでは、[**Workbook.vba_project.sign()**](https://reference.aspose.com/cells/python-net/aspose.cells.vba/vbaproject/sign/#aspose.cells.digitalsignatures.DigitalSignature) メソッドの使用方法を示しています。サンプルコードの入力および出力ファイルは任意のExcelファイルと任意の証明書を使用してテストできます。

- サンプルのExcelファイル（5115028.xlsm）
- [サンプルpfxファイル（5115039.pfx）](5115039.pfx)でデジタル署名を作成します。このコードを実行するためにこのファイルをコンピューターにインストールしてください。パスワードは1234です。
- サンプルコードによって生成された出力Excelファイル（5115029.xlsm）

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "VBAProject-DigitallySignVbaProjectWithCertificate-1.py" >}}

{{< app/cells/assistant language="python-net" >}}
