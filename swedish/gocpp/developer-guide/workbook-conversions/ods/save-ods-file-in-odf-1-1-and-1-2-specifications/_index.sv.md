---
title: Spara ODS fil i ODF 1.1, 1.2 och 1.3 specifikationer med Golang via C++
linktitle: Spara som ODF 1.1, 1.2 och 1.3
description: Konvertera Excel till ODF 1.1, 1.2 och 1.3 specifikationer med Aspose.Cells och C++.
type: docs
weight: 230
url: /sv/go-cpp/save-ods-file-in-odf-1-1-and-1-2-specifications/
---

{{% alert color="primary" %}}

Aspose.Cells stöder att spara en ODS-fil (**OpenDocument Spreadsheet**) i ODF (**OpenDocument Format**) 1.1, 1.2 och 1.3 specifikationer. Aspose.Cells har egenskapen [**OdsSaveOptions.GetOdfStrictVersion()**](https://reference.aspose.com/cells/go-cpp/odssaveoptions/getodfstrictversion/) som specificerar ODF-versionen för att spara ODS-filer. Standardvärdet för denna egenskap är [**OpenDocumentFormatVersionType.Odf12**](https://reference.aspose.com/cells/cpp/aspose.cells.ods/opendocumentformatversiontype/), så ODS-filen som sparas utan denna inställning använder 1.2-specifikationerna.

{{% /alert %}}

Nedan skapar exempel på kod ett arbetsboksobjekt, lägger till ett värde i cell A1 på första arbetsbladet och sparar sedan ODS-filen i ODF 1.1, 1.2 och 1.3-specifikationer. Som standard sparas ODS-filen i ODF 1.2-specifikation.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SaveOdsFileInOdf11And12Specifications.go" >}}
