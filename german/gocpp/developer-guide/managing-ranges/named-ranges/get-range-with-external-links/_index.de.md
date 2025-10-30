---
title: Geltungsbereich mit externen Links mit Golang über C++ abrufen
linktitle: Bereich mit externen Links abrufen
type: docs
weight: 120
url: /de/go-cpp/get-range-with-external-links/
description: Erfahren Sie, wie Sie mit Aspose.Cells in Golang über C++ Bereiche mit externen Links in Excel Dateien abrufen.
---

## **Bereich mit externen Links abrufen**

Häufig greifen Excel-Dateien auf Daten aus anderen Excel-Dateien über externe Links zu. Aspose.Cells ermöglicht die Abfrage dieser externen Links mit der [**Name.GetReferredAreas**](https://reference.aspose.com/cells/go-cpp/name/getreferredareas/)-Methode. Die [**Name.GetReferredAreas**](https://reference.aspose.com/cells/go-cpp/name/getreferredareas/)-Methode gibt ein Array vom Typ [**ReferredArea**](https://reference.aspose.com/cells/cpp/aspose.cells/referredarea/) zurück. Die [**ReferredArea**](https://reference.aspose.com/cells/cpp/aspose.cells/referredarea/)-Klasse bietet eine [**GetExternalFileName()**](https://reference.aspose.com/cells/cpp/aspose.cells/referredarea/getexternalfilename/)-Eigenschaft, die den Namen der externen Datei liefert. Die [**ReferredArea**](https://reference.aspose.com/cells/cpp/aspose.cells/referredarea/)-Klasse stellt die folgenden Mitglieder bereit.

- [**GetEndColumn()**](https://reference.aspose.com/cells/go-cpp/referredarea/getendcolumn/): Die Endspalte des Bereichs
- [**GetEndRow()**](https://reference.aspose.com/cells/go-cpp/referredarea/getendrow/): Die Endzeile des Bereichs
- [**GetExternalFileName()**](https://reference.aspose.com/cells/go-cpp/referredarea/getexternalfilename/): Holt den Namen der externen Datei, falls dies eine externe Referenz ist
- [**IsArea**](https://reference.aspose.com/cells/go-cpp/referredarea/isarea/): Gibt an, ob dies ein Bereich ist
- [**IsExternalLink**](https://reference.aspose.com/cells/go-cpp/referredarea/isexternallink/): Gibt an, ob dies eine externe Verknüpfung ist
- [**GetSheetName()**](https://reference.aspose.com/cells/go-cpp/referredarea/getsheetname/): Gibt an, in welchem Blatt sich diese Referenz befindet
- [**GetStartColumn()**](https://reference.aspose.com/cells/go-cpp/referredarea/getstartcolumn/): Der Anfangsspalte des Bereichs
- [**GetStartRow()**](https://reference.aspose.com/cells/go-cpp/referredarea/getstartrow/): Die Startzeile des Bereichs

Der nachstehende Beispielcode zeigt die Verwendung der [**Name.GetReferredAreas**](https://reference.aspose.com/cells/go-cpp/name/getreferredareas/)-Methode, um Bereiche mit externen Verknüpfungen zu erhalten.

## **Beispielcode**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-GetRangeWithExternalLinks.go" >}}
