---
title: デジタル署名の割り当てと検証
linktitle: 署名
type: docs
weight: 140
url: /ja/net/assign-and-validate-digital-signatures/
description: Excelファイルのデジタル署名、検証。Excelファイルのワークブックの内容の信頼性を保護するために、Aspose.Cells for .Netを使用してC#コードでデジタル署名を追加することができます。
keywords: Excelファイルのデジタル署名、Excelにデジタル署名を追加、デジタル署名の検証方法。
---

{{% alert color="primary" %}}

デジタル署名は、ブックファイルが有効であり、誰もがそれを変更していないことを保証します。 **Microsoft Selfcert.exe**または他のツールを使用して個人用のデジタル署名を作成したり、デジタル署名を購入したりすることができます。デジタル署名を作成した後は、それをブックに添付する必要があります。デジタル署名を添付することは、封筒を封印することと似ています。封がされた封筒が届いた場合、その内容が誰もが触れていないレベルの保証が得られます。

{{% /alert %}}

## **紹介**

デジタル署名を添付するには、デジタル署名ダイアログを使用します。デジタル署名ダイアログには有効な証明書が一覧表示されます。デジタル署名ダイアログでは、証明書を表示し、使用する証明書を選択することができます。ブックにデジタル署名がある場合、署名の名前が**証明書名**フィールドに表示されます。デジタル署名ダイアログの**削除**ボタンをクリックすると、Microsoft Excelはデジタル署名も削除します。

## **Excelにデジタル署名を追加する方法**

Aspose.Cellsは、デジタル署名を割り当ておよび検証するための[**Aspose.Cells.DigitalSignatures**](https://reference.aspose.com/cells/net/aspose.cells.digitalsignatures/digitalsignature)名前空間を提供しています。この名前空間には、デジタル署名を追加および検証するための便利な機能がいくつか含まれています。

Aspose.Cells for .NET APIを使用してタスクを実行する方法を説明するサンプルコードを参照してください。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-AssignAndValidateDigitalSignatures-AssignAndValidateDigitalSignatures.cs" >}}



## **高度なトピック**
- [すでに署名されたExcelファイルにデジタル署名を追加する](/cells/ja/net/add-digital-signature-to-an-already-signed-excel-file/)
- [ワークシートに署名行を追加](/cells/ja/net/add-signature-line/)
- [XAdES署名のサポート](/cells/ja/net/support-for-xades-signature/)
