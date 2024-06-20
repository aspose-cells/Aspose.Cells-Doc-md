---
title: VBAコードのデジタル署名が有効かどうかを確認する
type: docs
weight: 120
url: /ja/net/check-if-digital-signature-of-vba-code-is-valid/
---

{{% alert color="primary" %}}

Aspose.Cellsを使用して、VBAコードのデジタル署名が有効かどうかを確認することができます。[**Workbook.VbaProject.IsValidSigned**](https://reference.aspose.com/cells/net/aspose.cells.vba/vbaproject/properties/isvalidsigned)プロパティを使用すると、署名が有効であれば**true**を返し、それ以外の場合は**false**を返します。VBAコードを変更すると、そのデジタル署名は無効になります。

{{% /alert %}}

## **C#でVBAコードのデジタル署名が有効かどうかを確認する**

提供されたリンクから[サンプルのExcelファイル](5115030.xlsm)をダウンロードし、このプロパティの使用方法を示すコードを実演しています。同じExcelファイルには有効な署名がありますが、VBAコードを変更してワークブックを保存した後、再チェックすると署名が無効になることが分かります。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingVBAModules-CheckVbaSignatureIsValid-CheckVbaSignatureIsValid.cs" >}}
