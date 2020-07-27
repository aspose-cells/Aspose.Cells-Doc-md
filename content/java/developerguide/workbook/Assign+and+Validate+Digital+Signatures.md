+++
title = "Assign and Validate Digital Signatures" 
description = "" 
weight = 12102 
+++

Aspose.Cells for Java : Assign and Validate Digital Signatures  

# Aspose.Cells for Java : Assign and Validate Digital Signatures


A digital signature provides assurance that a workbook file is valid and no one has altered it. You can create a personal digital signature by using the **SELFCERT** tool shipped with Microsoft Office suite or any other tool. You can even purchase a digital signature. After you create or acquire a digital signature, you must attach it to your workbook. Attaching a digital signature is similar to sealing an envelope. If an envelope arrives sealed, you have some level of assurance that no one has tampered with its contents.

Aspose.Cells for Java API provide the [com.aspose.cells.DigitalSignatureCollection](https://apireference.aspose.com/java/cells/com.aspose.cells/DigitalSignatureCollection) & [com.aspose.cells.DigitalSignature](https://apireference.aspose.com/java/cells/com.aspose.cells/DigitalSignature) classes to sign the spreadsheets as well as validate them.

#### Signing the Spreadsheets

Signing process requires a certificate as discussed above. Along with the certificate, one should also have its password to successfully sign the spreadsheets using the Aspose.Cells API.

The following code snippet demonstrates the usage of Aspose.Cells for Java API to sign a spreadsheet.


In case the specified password does not match with the password of certificate then an exception of type *javax.crypto.BadPaddingException* will be thrown.

#### Validating the Spreadsheets

The following code snippet demonstrates the usage of Aspose.Cells for Java API to validate the spreadsheet.

