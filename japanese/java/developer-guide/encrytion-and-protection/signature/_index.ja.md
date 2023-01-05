---
title: デジタル署名の割り当てと検証
linktitle: サイン
type: docs
weight: 100
url: /ja/java/assign-and-validate-digital-signatures/
description: Excel ファイルのデジタル署名、検証。ワークブックの Excel ファイルのコンテンツの信頼性を保護するために、C# コードと .Net の Aspose.Cells を使用してデジタル署名を追加できます。
---
{{% alert color="primary" %}}

デジタル署名は、ブック ファイルが有効であり、誰も変更していないことを保証します。を使用して、個人のデジタル署名を作成できます。**セルフサート**ツールは、Microsoft Office スイートまたはその他のツールに同梱されています。デジタル署名を購入することもできます。デジタル署名を作成または取得したら、それをワークブックに添付する必要があります。デジタル署名を添付することは、封筒を封印することに似ています。封筒が封印された状態で届いた場合、だれもその内容を改ざんしていないことをある程度保証できます。

 Aspose.Cells for Java API 提供[**com.aspose.cells.DigitalSignatureCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/DigitalSignatureCollection) & [**com.aspose.cells.DigitalSignature**](https://reference.aspose.com/cells/java/com.aspose.cells/DigitalSignature)クラスを使用してスプレッドシートに署名し、検証します。

{{% /alert %}}

## **スプレッドシートへの署名**

上記のように、署名プロセスには証明書が必要です。証明書とともに、Aspose.Cells API を使用してスプレッドシートに正常に署名するためのパスワードも必要です。

次のコード スニペットは、Aspose.Cells for Java API を使用してスプレッドシートに署名する方法を示しています。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SigningSpreadsheets-SigningSpreadsheets.java" >}}

{{% alert color="primary" %}}

指定されたパスワードが証明書のパスワードと一致しない場合、タイプの例外*javax.crypto.BadPaddingException*投げられます。

{{% /alert %}}

## **スプレッドシートの検証**

次のコード スニペットは、Aspose.Cells for Java API を使用してスプレッドシートを検証する方法を示しています。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ValidatingSpreadsheets-ValidatingSpreadsheets.java" >}}
