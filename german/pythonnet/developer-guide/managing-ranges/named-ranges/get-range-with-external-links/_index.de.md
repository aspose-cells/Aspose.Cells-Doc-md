---
title: Bereich mit externen Links abrufen
type: docs
weight: 120
url: /de/python-net/get-range-with-external-links/
description: Dieser Artikel zeigt, wie man einen Bereich mit externen Verknüpfungen mithilfe der Aspose.Cells for Python via .NET API erhält.
keywords: Python Excel Bibliothek, Python Bereich mit externen Verknüpfungen erhalten.
---

## **Bereich mit externen Links abrufen**

Oftmals greifen Excel-Dateien über externe Verknüpfungen auf Daten aus anderen Excel-Dateien zu. Aspose.Cells for Python via .NET bietet die Möglichkeit, diese externen Verknüpfungen mithilfe der Methode [**Name.get_referred_areas**](https://reference.aspose.com/cells/python-net/aspose.cells/name/get_referred_areas/#bool) abzurufen. Die Methode [**Name.get_referred_areas**](https://reference.aspose.com/cells/python-net/aspose.cells/name/get_referred_areas/#bool) gibt ein Array vom Typ [**ReferredArea**](https://reference.aspose.com/cells/python-net/aspose.cells/referredarea) zurück. Die Klasse [**ReferredArea**](https://reference.aspose.com/cells/python-net/aspose.cells/referredarea) bietet eine Eigenschaft [**external_file_name**](https://reference.aspose.com/cells/python-net/aspose.cells/referredarea/external_file_name/), die den Namen der externen Datei zurückgibt. Die Klasse [**ReferredArea**](https://reference.aspose.com/cells/python-net/aspose.cells/referredarea) stellt die folgenden Elemente bereit.

- [**end_column**](https://reference.aspose.com/cells/python-net/aspose.cells/referredarea/end_column/): Die Endspalte des Bereichs
- [**end_row**](https://reference.aspose.com/cells/python-net/aspose.cells/referredarea/end_row/): Die Endzeile des Bereichs
- [**external_file_name**](https://reference.aspose.com/cells/python-net/aspose.cells/referredarea/external_file_name/): Holen Sie den Namen der externen Datei, wenn dies ein externer Verweis ist.
- [**is_area**](https://reference.aspose.com/cells/python-net/aspose.cells/referredarea/is_area/): Gibt an, ob dies ein Bereich ist.
- [**is_external_link**](https://reference.aspose.com/cells/python-net/aspose.cells/referredarea/is_external_link/): Gibt an, ob dies ein externer Link ist.
- [**sheet_name**](https://reference.aspose.com/cells/python-net/aspose.cells/referredarea/sheet_name/): Gibt an, in welchem Blatt dieser Verweis steht.
- [**start_column**](https://reference.aspose.com/cells/python-net/aspose.cells/referredarea/start_column): Die Startspalte des Bereichs
- [**start_row**](https://reference.aspose.com/cells/python-net/aspose.cells/referredarea/start_row): Die Startzeile des Bereichs

Der unten angegebene Code demonstriert die Verwendung der Methode [**Name.get_referred_areas**](https://reference.aspose.com/cells/python-net/aspose.cells/name/get_referred_areas/#bool) zum Abrufen von Bereichen mit externen Links.

## **Beispielcode**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-Worksheets-GetRangeWithExternalLinks-1.py" >}}
