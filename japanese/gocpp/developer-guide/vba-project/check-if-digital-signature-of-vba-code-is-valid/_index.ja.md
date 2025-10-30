---
title: GolangとC++を用いてVBAコードのデジタル署名が有効かどうかを確認
linktitle: VBAコードのデジタル署名が有効かどうかを確認する
type: docs
weight: 120
url: /ja/go-cpp/check-if-digital-signature-of-vba-code-is-valid/
description: GolangとC++でAspose.Cellsを使用してVBAコードのデジタル署名の有効性を確認する方法を学習
---

{{% alert color="primary" %}}

Aspose.Cellsは、[**Workbook.VbaProject.IsValidSigned**](https://reference.aspose.com/cells/go-cpp/vbaproject/isvalidsigned/) プロパティを使用してVBAコードのデジタル署名が有効かどうかを確認できます。有効な署名の場合は**true**を返し、そうでなければ**false**を返します。VBAコードを変更すると、そのデジタル署名は無効になります。

{{% /alert %}}

## **C++でVBAコードのデジタル署名が有効かどうかを確認する**

以下のコードは、提供されたリンクからダウンロードできる[サンプルExcelファイル](5115030.xlsm)を使用して、このプロパティの使用例を示しています。同じExcelファイルには有効な署名がありますが、そのVBAコードを変更して保存し、再度確認すると署名が無効になっていることがわかります。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CheckIfDigitalSignatureOfVbaCodeIsValid.go" >}}
