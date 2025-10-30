---
title: Hämta intervall med externa länkar
type: docs
weight: 120
url: /sv/python-net/get-range-with-external-links/
description: Denna artikel visar hur man hämtar intervall med externa länkar genom Aspose.Cells för Python via .NET API.
keywords: Python Excel bibliotek, Python Hämta intervall med externa länkar.
---

## **Hämta intervall med externa länkar**

Många gånger hämtar Excel-filer data från andra Excel-filer med hjälp av externa länkar. Aspose.Cells för Python via .NET ger möjlighet att hämta dessa externa länkar genom att använda [**Name.get_referred_areas**](https://reference.aspose.com/cells/python-net/aspose.cells/name/get_referred_areas/#bool) metoden. [**Name.get_referred_areas**](https://reference.aspose.com/cells/python-net/aspose.cells/name/get_referred_areas/#bool) metoden returnerar en array av typen [**ReferredArea**](https://reference.aspose.com/cells/python-net/aspose.cells/referredarea). Klassen [**ReferredArea**](https://reference.aspose.com/cells/python-net/aspose.cells/referredarea) tillhandahåller en [**external_file_name**](https://reference.aspose.com/cells/python-net/aspose.cells/referredarea/external_file_name/) egenskap som returnerar namnet på den externa filen. Klassen [**ReferredArea**](https://reference.aspose.com/cells/python-net/aspose.cells/referredarea) exponerar följande medlemmar.

- [**end_column**](https://reference.aspose.com/cells/python-net/aspose.cells/referredarea/end_column/): Slutkolumnen för området
- [**end_row**](https://reference.aspose.com/cells/python-net/aspose.cells/referredarea/end_row/): Slutraden för området
- [**external_file_name**](https://reference.aspose.com/cells/python-net/aspose.cells/referredarea/external_file_name/): Hämta det externa filnamnet om det är en extern referens
- [**is_area**](https://reference.aspose.com/cells/python-net/aspose.cells/referredarea/is_area/): Anger om det här är ett område
- [**is_external_link**](https://reference.aspose.com/cells/python-net/aspose.cells/referredarea/is_external_link/): Anger om det här är en extern länk
- [**sheet_name**](https://reference.aspose.com/cells/python-net/aspose.cells/referredarea/sheet_name/): Anger vilket blad denna referens är i
- [**start_column**](https://reference.aspose.com/cells/python-net/aspose.cells/referredarea/start_column): Startkolumnen för området
- [**start_row**](https://reference.aspose.com/cells/python-net/aspose.cells/referredarea/start_row): Startraden för området

Det givna kodexemplet nedan demonstrerar användningen av [**Name.get_referred_areas**](https://reference.aspose.com/cells/python-net/aspose.cells/name/get_referred_areas/#bool) metod för att hämta intervall med externa länkar.

## **Exempelkod**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-Worksheets-GetRangeWithExternalLinks-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
