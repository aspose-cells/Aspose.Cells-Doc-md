---
title: すでに署名されたExcelファイルにデジタル署名を追加する
type: docs
weight: 20
url: /ja/python-net/add-digital-signature-to-an-already-signed-excel-file/
description: この資料は、Aspose.Cells for Python via .NETを使用して既に署名されたExcelファイルにC#コードでデジタル署名を追加する方法について説明しています。
keywords: すでに署名されたExcelファイルにデジタル署名を追加する方法
---

## **可能な使用シナリオ**

Aspose.Cells for Python via .NETは、既に署名されたExcelファイルにデジタル署名を追加できる [**Workbook.add_digital_signature**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/add_digital_signature) メソッドを提供します。

{{% alert color="primary" %}}

既に署名されたExcelドキュメントにデジタル署名を追加する際、元のドキュメントがAspose.Cells for Python via .NETで作成されたものであれば正常に動作します。ただし、他のエンジン（例：Microsoft Excel等）で生成された場合、Aspose.Cells for Python via .NETは読み込みと再保存後にファイルの状態を維持できず、これにより元の署名が無効になる可能性があります。

{{% /alert %}}

## **すでに署名されたExcelファイルにデジタル署名を追加する方法**

次のサンプルコードは、[**Workbook.add_digital_signature**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/add_digital_signature)メソッドを使用してすでに署名されたExcelファイルにデジタル署名を追加する方法を示しています。このコードで使用されているサンプルExcelファイルについては、[サンプルExcelファイル](50528280.xlsx)をご確認ください。このファイルはすでにデジタルで署名されています。コードでデモ証明書である[AsposeDemo.pfx](50528279.pfx)を使用し、そのパスワードは **aspose** です。スクリーンショットは、コードの実行後にサンプルExcelファイルに与える効果を示しています。

![todo:image_alt_text](add-digital-signature-to-an-already-signed-excel-file_1.png)

## **サンプルコード**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-AddDigitalSignatureToAnAlreadySignedExcelFile.py" >}}

