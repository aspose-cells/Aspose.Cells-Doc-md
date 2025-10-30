---
title: VBAコードのデジタル署名が有効かどうかを確認する
type: docs
weight: 120
url: /ja/python-net/check-if-digital-signature-of-vba-code-is-valid/
---

{{% alert color="primary" %}}

Aspose.Cells for Python via .NETは、VBAコードのデジタル署名が有効かどうかを[**Workbook.vba_project.is_valid_signed**](https://reference.aspose.com/cells/python-net/aspose.cells.vba/vbaproject/is_valid_signed)プロパティを使用して確認できます。有効な署名の場合は**true**を返し、それ以外の場合は**false**を返します。VBAコードの署名は、コードを変更した場合に無効になります。

{{% /alert %}}

## **PythonでVBAコードのデジタル署名の有効性を確認する方法**

提供されたリンクから[サンプルのExcelファイル](5115030.xlsm)をダウンロードし、このプロパティの使用方法を示すコードを実演しています。同じExcelファイルには有効な署名がありますが、VBAコードを変更してワークブックを保存した後、再チェックすると署名が無効になることが分かります。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "VBAProject-CheckVbaSignatureIsValid.py" >}}

{{< app/cells/assistant language="python-net" >}}
