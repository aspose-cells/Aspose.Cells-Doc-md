---
title: デジタル署名の割り当てと検証
linktitle: サイン
type: docs
weight: 140
url: /ja/net/assign-and-validate-digital-signatures/
description: Excel ファイルのデジタル署名、検証。ワークブックの Excel ファイルのコンテンツの信頼性を保護するために、C# コードと .Net の Aspose.Cells を使用してデジタル署名を追加できます。
---
{{% alert color="primary" %}}

デジタル署名は、ブック ファイルが有効であり、誰も変更していないことを保証します。を使用して、個人のデジタル署名を作成できます。**Microsoft Selfcert.exe**またはその他のツールを使用するか、デジタル署名を購入できます。デジタル署名を作成したら、それをブックに添付する必要があります。デジタル署名を添付することは、封筒を封印することに似ています。封筒が封印された状態で届いた場合、だれもその内容を改ざんしていないことをある程度保証できます。

{{% /alert %}}

## **序章**

デジタル署名ダイアログを使用して、デジタル署名を添付します。 [デジタル署名] ダイアログに有効な証明書が一覧表示されます。 [デジタル署名] ダイアログを使用して、証明書を表示し、使用する証明書を選択できます。ワークブックにデジタル署名がある場合、署名の名前が**証明書名**分野。をクリックすると**削除する**ボタンをクリックすると、Microsoft Excel はデジタル署名も削除します。

Aspose.Cells は[**Aspose.Cells.DigitalSignatures**](https://reference.aspose.com/cells/net/aspose.cells.digitalsignatures/digitalsignature)名前空間を使用してジョブを実行します (デジタル署名の割り当てと検証)。名前空間には、デジタル署名を追加および検証するための便利な機能がいくつかあります。

Aspose.Cells for .NET API を使用してタスクを実行する方法を説明する次のサンプル コードを参照してください。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-AssignAndValidateDigitalSignatures-AssignAndValidateDigitalSignatures.cs" >}}



## **先行トピック**
- [署名済みの Excel ファイルにデジタル署名を追加する](/cells/ja/net/add-digital-signature-to-an-already-signed-excel-file/)
- [ワークシートに署名欄を追加する](/cells/ja/net/add-signature-line/)
- [XAdES署名のサポート](/cells/ja/net/support-for-xades-signature/)
