---
title: デジタル署名の割り当てと検証
linktitle: 署名
type: docs
weight: 140
url: /ja/python-net/assign-and-validate-digital-signatures/
description: Excelファイルのデジタル署名および検証。Excelファイルの内容の正当性を保護するために、Aspose.Cells for Python via .NETを使ってC#コードでデジタル署名を追加できます。
keywords: Excelファイルのデジタル署名、Excelにデジタル署名を追加、デジタル署名の検証方法。
---

{{% alert color="primary" %}}

デジタル署名は、ブックファイルが有効であり、誰もがそれを変更していないことを保証します。 **Microsoft Selfcert.exe**または他のツールを使用して個人用のデジタル署名を作成したり、デジタル署名を購入したりすることができます。デジタル署名を作成した後は、それをブックに添付する必要があります。デジタル署名を添付することは、封筒を封印することと似ています。封がされた封筒が届いた場合、その内容が誰もが触れていないレベルの保証が得られます。

{{% /alert %}}

## **紹介**

デジタル署名を添付するには、デジタル署名ダイアログを使用します。デジタル署名ダイアログには有効な証明書が一覧表示されます。デジタル署名ダイアログでは、証明書を表示し、使用する証明書を選択することができます。ブックにデジタル署名がある場合、署名の名前が**証明書名**フィールドに表示されます。デジタル署名ダイアログの**削除**ボタンをクリックすると、Microsoft Excelはデジタル署名も削除します。

## **Excelにデジタル署名を追加する方法**

Aspose.Cells for Python via .NETは、デジタル署名を割り当て・検証するための[**Aspose.Cells.DigitalSignatures**](https://reference.aspose.com/cells/python-net/aspose.cells.digitalsignatures/digitalsignature)名前空間を提供します。この名前空間には、デジタル署名の追加と検証に役立つ便利な機能が含まれています。

Aspose.Cells for Python via .NET API を使用してタスクを実行する方法を説明したサンプルコードをご覧ください。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-AssignAndValidateDigitalSignatures.py" >}}



## **高度なトピック**
- [すでに署名されたExcelファイルにデジタル署名を追加する](/cells/ja/python-net/add-digital-signature-to-an-already-signed-excel-file/)
- [ワークシートに署名行を追加](/cells/ja/python-net/add-signature-line/)
- [XAdES署名のサポート](/cells/ja/python-net/support-for-xades-signature/)

{{< app/cells/assistant language="python-net" >}}
