---
title: VBA コードのデジタル署名が有効かどうかを確認する
type: docs
weight: 120
url: /ja/net/check-if-digital-signature-of-vba-code-is-valid/
---
{{% alert color="primary" %}}

Aspose.Cells を使用すると、VBA コードのデジタル署名が有効かどうかを確認できます。[**Workbook.VbaProject.IsValidSigned**](https://reference.aspose.com/cells/net/aspose.cells.vba/vbaproject/properties/isvalidsigned)財産。戻ってきます**真実**署名が有効な場合、それ以外の場合は返されます**間違い**VBA コードを変更すると、VBA コードのデジタル署名が無効になります。

{{% /alert %}}

## **VBA コードのデジタル署名が C# で有効かどうかを確認する**

次のコードは、[サンプルエクセルファイル](5115030.xlsm)提供されたリンクからダウンロードできます。同じ Excel ファイルには有効な署名がありますが、VBA コードを変更してワークブックを保存し、再確認すると、署名が無効になっていることがわかります。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingVBAModules-CheckVbaSignatureIsValid-CheckVbaSignatureIsValid.cs" >}}
