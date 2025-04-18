---
title: Add Digital Signature to an already signed Excel file
type: docs
weight: 20
url: /python-net/add-digital-signature-to-an-already-signed-excel-file/
description: This article describes how to Add Digital Signature to an already signed Excel file using C# codes with Aspose.Cells for Python via .NET.
keywords: Add Digital Signature to an already signed Excel file, How to add a digital signature to an already signed Excel document.
---

## **Possible Usage Scenarios**

Aspose.Cells for Python via .NET provides the [**Workbook.add_digital_signature**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/add_digital_signature) method that you can use to add digital signature to an already signed Excel file.

{{% alert color="primary" %}}

Please note while adding a digital signature to an already signed Excel document, if the original document is Aspose.Cells for Python via .NET generated document, it works well. But if the original document is generated by other engines (e.g. Microsoft Excel etc.), Aspose.Cells for Python via .NET cannot keep the file same after loading and re-saving it, this will make the original signature to be invalid.

{{% /alert %}}

## **How to Add Digital Signature to an Already Signed Excel File**

The following sample code demonstrated how to make use of [**Workbook.add_digital_signature**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/add_digital_signature) method to add digital signature to already signed Excel file. Please check the [sample Excel file](50528280.xlsx) used in this code. This file is already digitally signed. Please check the [output Excel file](50528281.xlsx) generated by the code. We have used the demo certificate named [AsposeDemo.pfx](50528279.pfx) in this code which has a password **aspose**. The screenshot shows the effect of the sample code on the sample Excel file after execution.

![todo:image_alt_text](add-digital-signature-to-an-already-signed-excel-file_1.png)

## **Sample Code**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-AddDigitalSignatureToAnAlreadySignedExcelFile.py" >}}

