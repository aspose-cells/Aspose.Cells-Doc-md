---
title: Assign and Validate Digital Signatures
linktitle: Signature
type: docs
weight: 100
url: /java/assign-and-validate-digital-signatures/
description: Excel file digital signature and verification. To protect the authenticity of a workbook's content in an Excel file, you can add a digital signature using Java code with Aspose.Cells for Java.
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

A digital signature provides assurance that a workbook file is valid and no one has altered it. You can create a personal digital signature by using the **SELFCERT** tool shipped with the Microsoft Office suite or any other tool. You can even purchase a digital signature. After you create or acquire a digital signature, you must attach it to your workbook. Attaching a digital signature is similar to sealing an envelope. If an envelope arrives sealed, you have some level of assurance that no one has tampered with its contents.

Aspose.Cells for Java API **provides** the [**com.aspose.cells.DigitalSignatureCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/DigitalSignatureCollection) & [**com.aspose.cells.DigitalSignature**](https://reference.aspose.com/cells/java/com.aspose.cells/DigitalSignature) classes to sign the spreadsheets as well as validate them.

{{% /alert %}}

## **Signing the Spreadsheets**

The signing process requires a certificate, as discussed above. In addition to the certificate, you must also have its password to successfully sign the spreadsheets using the Aspose.Cells API.

The following code snippet demonstrates the usage of Aspose.Cells for Java API to sign a spreadsheet.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SigningSpreadsheets-SigningSpreadsheets.java" >}}

{{% alert color="primary" %}}

In case the specified password does not match the certificate's password, an exception of type *javax.crypto.BadPaddingException* will be thrown.

{{% /alert %}}

## **Validating the Spreadsheets**

The following code snippet demonstrates the usage of Aspose.Cells for Java API to validate the spreadsheet.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ValidatingSpreadsheets-ValidatingSpreadsheets.java" >}}
{{< app/cells/assistant language="java" >}}
