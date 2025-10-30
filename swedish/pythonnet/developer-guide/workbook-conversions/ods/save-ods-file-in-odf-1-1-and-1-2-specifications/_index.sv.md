---
title: Spara ODS fil enligt ODF 1.1 och 1.2 specifikationerna
linktitle: Spara som ODF 1.1 och 1.2 
description: Konvertera Excel till ODF 1.1 och 1.2 specifikationer med Aspose.Cells.
type: docs
weight: 230
url: /sv/python-net/save-ods-file-in-odf-1-1-and-1-2-specifications/
description: Hur man sparar en ODS fil i ODF 1.1 och 1.2 specifikationer med Aspose.Cells för Python via .NET API.
keywords: Python Spara ODS fil i ODF 1.1 och 1.2 specifikationer, Spara ODS fil i ODF 1.1 och 1.2 specifikationer Pyton via NET.
---

{{% alert color="primary" %}}

Aspose.Cells for Python via .NET stöder att spara en ODS-fil (**OpenDocument Spreadsheet**) i specifikationerna för ODF (**OpenDocument Format**) 1.1 och 1.2. Aspose.Cells för Python via .NET har egenskapen [**OdsSaveOptions.is_strict_schema11**](https://reference.aspose.com/cells/python-net/aspose.cells/odssaveoptions/is_strict_schema11/) som specifierar användningen av ODF 1.1-specifikationen för att spara ODS-filer. Standardvärdet för denna egenskap är **false**, så ODS-filen som sparas utan denna inställning använder 1.2-specifikationerna.

{{% /alert %}}

Nedan finns ett källkodsexempel som skapar en arbetsbok och lägger till något värde i cell A1 på den första arbetsbladet och sedan sparar ODS-filen i ODF 1.1 och 1.2 specifikationer. Som standard sparas ODS-filen i ODF 1.2-specifikationen.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-OdsFileSaveOptions-SaveODSFileinODF11and12Specifications.py" >}}
{{< app/cells/assistant language="python-net" >}}
