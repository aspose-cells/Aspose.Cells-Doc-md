---
title: デジタル署名の割り当てと検証
linktitle: 署名
type: docs
weight: 100
url: /ja/java/assign-and-validate-digital-signatures/
description: Excelファイルのデジタル署名と検証。Excelファイルのワークブックの内容の真正性を保護するために、Javaコードを使用してデジタル署名を追加できます。Aspose.Cells for Java。
---

{{% alert color="primary" %}}

デジタル署名により、ワークブックファイルが有効であることと、誰もがそれを改ざんしていないことが保証されます。Microsoft Officeスイートに含まれる**SELFCERT**ツールやその他のツールを使用して、個人用のデジタル署名を作成できます。デジタル署名を取得または作成した後は、ワークブックに添付する必要があります。デジタル署名を添付することは封筒を封印することに似ています。封筒が封印された状態で届くと、その内容が誰も改ざんしていないという程度の保証が得られます。

Aspose.Cells for Java APIは、スプレッドシートに署名を追加し、検証するための[**com.aspose.cells.DigitalSignatureCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/DigitalSignatureCollection)および[**com.aspose.cells.DigitalSignature**](https://reference.aspose.com/cells/java/com.aspose.cells/DigitalSignature)クラスを提供します。

{{% /alert %}}

## **スプレッドシートに署名するには、前述の証明書が必要です。証明書とともに、Aspose.Cells APIを使用してスプレッドシートに署名するためには、パスワードも必要です。**

指定されたパスワードが証明書のパスワードと一致しない場合、*javax.crypto.BadPaddingException*型の例外がスローされます。

次のコードスニペットは、Aspose.Cells for Java APIを使用してスプレッドシートに署名する方法を示しています。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SigningSpreadsheets-SigningSpreadsheets.java" >}}

{{% alert color="primary" %}}

指定されたパスワードが証明書のパスワードと一致しない場合、*javax.crypto.BadPaddingException*型の例外がスローされます。

{{% /alert %}}

## **スプレッドシートの検証**

次のコードスニペットは、Aspose.Cells for Java APIを使用してスプレッドシートを検証する方法を示しています。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ValidatingSpreadsheets-ValidatingSpreadsheets.java" >}}
{{< app/cells/assistant language="java" >}}
