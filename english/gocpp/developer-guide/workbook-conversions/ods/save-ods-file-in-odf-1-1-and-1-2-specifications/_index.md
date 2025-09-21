---
title: Save ODS File in ODF 1.1, 1.2 and 1.3 Specifications with Golang via C++
linktitle: Save as ODF 1.1, 1.2 and 1.3
description: Convert Excel to ODF 1.1, 1.2 and 1.3 Specifications with Aspose.Cells using C++.
type: docs
weight: 230
url: /go-cpp/save-ods-file-in-odf-1-1-and-1-2-specifications/
---

{{% alert color="primary" %}}

Aspose.Cells supports saving an ODS file (**OpenDocument Spreadsheet**) in the ODF (**OpenDocument Format**) 1.1, 1.2 and 1.3 specifications. Aspose.Cells has [**OdsSaveOptions.GetOdfStrictVersion()**](https://reference.aspose.com/cells/go-cpp/odssaveoptions/getodfstrictversion/) property that specifies the ODF version for saving ODS files. The default value of this property is [**OpenDocumentFormatVersionType.Odf12**](https://reference.aspose.com/cells/cpp/aspose.cells.ods/opendocumentformatversiontype/), so the ODS file saved without this setting uses the 1.2 specifications.

{{% /alert %}}

The sample code below creates a workbook object, adds some value to cell A1 on the first worksheet and then saves the ODS file in ODF 1.1, 1.2 and 1.3 specifications. By default, the ODS file is saved in ODF 1.2 specification.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SaveOdsFileInOdf11And12Specifications.go" >}}