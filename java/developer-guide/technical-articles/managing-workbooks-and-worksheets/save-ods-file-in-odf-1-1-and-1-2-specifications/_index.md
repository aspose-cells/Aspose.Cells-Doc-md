---
title: Save ODS file in ODF 1.1 and 1.2 Specifications
type: docs
weight: 170
url: /java/save-ods-file-in-odf-1-1-and-1-2-specifications/
---

{{% alert color="primary" %}}

Aspose.Cells supports saving (**OpenDocument Spreadsheet**) ODS file in (**OpenDocument Format**) ODF 1.1 and ODF 1.2 specifications. Aspose.Cells has added [**OdsSaveOptions.setStrictSchema11()**](https://apireference.aspose.com/cells/java/com.aspose.cells/odssaveoptions#IsStrictSchema11) property to use ODF 1.1 specification for saving ODS files. The default value of this property is **false**, so ODS file saved without this special settings will use the 1.2 specification.

{{% /alert %}}

The sample code below creates the workbook object, adds some value in cell A1 of the first worksheet and then saves the ODS file in ODF 1.1 and 1.2 specifications. By default, ODS file is saved in ODF 1.2 specification.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SaveODSfile-SaveODSfile.java" >}}
