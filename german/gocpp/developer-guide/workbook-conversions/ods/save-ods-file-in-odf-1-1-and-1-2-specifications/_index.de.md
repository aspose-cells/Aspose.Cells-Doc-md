---
title: ODS Datei in ODF 1.1, 1.2 und 1.3 Spezifikationen mit Golang über C++ speichern
linktitle: Als ODF 1.1, 1.2 und 1.3 speichern
description: Excel in ODF 1.1, 1.2 und 1.3 mit Aspose.Cells unter Verwendung von C++ konvertieren.
type: docs
weight: 230
url: /de/go-cpp/save-ods-file-in-odf-1-1-and-1-2-specifications/
---

{{% alert color="primary" %}}

Aspose.Cells unterstützt das Speichern einer ODS-Datei (**OpenDocument Tabelle**) im ODF (**OpenDocument Format**) 1.1, 1.2 und 1.3 Spezifikationen. Aspose.Cells hat [**OdsSaveOptions.GetOdfStrictVersion()**](https://reference.aspose.com/cells/go-cpp/odssaveoptions/getodfstrictversion/) Eigenschaft, die die ODF-Version für das Speichern von ODS-Dateien angibt. Der Standardwert dieser Eigenschaft ist [**OpenDocumentFormatVersionType.Odf12**](https://reference.aspose.com/cells/cpp/aspose.cells.ods/opendocumentformatversiontype/), daher verwendet die gespeicherte ODS-Datei ohne diese Einstellung die Spezifikation 1.2.

{{% /alert %}}

Der folgende Beispielcode erstellt ein Arbeitsmappe-Objekt, fügt einigen Wert in Zelle A1 auf dem ersten Arbeitsblatt hinzu und speichert dann die ODS-Datei in den ODF 1.1, 1.2 und 1.3 Spezifikationen. Standardmäßig wird die ODS-Datei im ODF 1.2 Spezifikation gespeichert.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SaveOdsFileInOdf11And12Specifications.go" >}}
