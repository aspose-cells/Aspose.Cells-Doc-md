---
title: C++で証明書を使用してVBAコードプロジェクトに電子署名を付与します
linktitle: 証明書でVBAコードプロジェクトにデジタル署名する
type: docs
weight: 110
url: /ja/go-cpp/digitally-sign-a-vba-code-project-with-certificate/
description: Aspose.Cells for C++を使用してVBAコードプロジェクトにデジタル署名を付与する方法について学びます。
---

{{% alert color="primary" %}} 

Aspose.Cellsの[**Workbook.VbaProject.Sign()**](https://reference.aspose.com/cells/go-cpp/vbaproject/sign/)メソッドを使用して、VBAコードプロジェクトにデジタル署名を付与できます。Excelファイルが証明書でデジタル署名されているかどうかを確認する手順に従ってください。

- **開発者**タブから**Visual Basic**をクリックして、**Visual Basic for Applications IDE**を開きます。
- **Visual Basic for Applications IDE**の**ツール** > **デジタル署名...**をクリックします。

これにより、ドキュメントが証明書でデジタル署名されているかどうかを示す**デジタル署名フォーム**が表示されます。

{{% /alert %}} 

## **C++で証明書を使用してVBAコードプロジェクトに電子署名を付与します**

次のサンプルコードは、[**Workbook.VbaProject.Sign()**](https://reference.aspose.com/cells/go-cpp/vbaproject/sign/)メソッドの使用方法を示しています。サンプルコードの入力および出力ファイルはこちらです。このコードは、任意のExcelファイルと証明書を使ってテストできます。

- サンプルのExcelファイル（5115028.xlsm）
- [サンプルpfxファイル（5115039.pfx）](5115039.pfx)でデジタル署名を作成します。このコードを実行するためにこのファイルをコンピューターにインストールしてください。パスワードは1234です。
- サンプルコードによって生成された出力Excelファイル（5115029.xlsm）

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DigitallySignAVbaCodeProjectWithCertificate.go" >}}
