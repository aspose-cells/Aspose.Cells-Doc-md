---
title: Spezifizieren Sie benutzerdefinierte Dezimal und Gruppentrennzeichen für das Arbeitsbuch mit Golang über C++
linktitle: Benutzerdefinierte Dezimal und Gruppentrennzeichen spezifizieren
type: docs
weight: 110
url: /de/go-cpp/specify-custom-number-decimal-and-group-separators-for-workbook/
description: Ändern Sie Dezimal und Gruppentrennzeichen für Zahlen in MS Excel und mit Golang über C++ durch die Verwendung der Aspose.Cells for C++ API.
keywords: spezifiziere benutzerdefinierten Dezimaltrennzeichen in Excel, spezifiziere benutzerdefiniertes Dezimaltrennzeichen in Excel c++, spezifiere benutzerdefinierten Gruppentrennzeichen in Excel, spezifiere benutzerdefiniertes Gruppentrennzeichen in Excel c++, spezifiziere benutzerdefiniertes Dezimal und Gruppentrennzeichen in Excel, spezifiziere benutzerdefiniertes Dezimal und Gruppentrennzeichen in Excel c++, ändere Dezimal und Gruppentrennzeichen in Excel, ändere Dezimal und Gruppentrennzeichen in Excel, ändere Dezimaltrennzeichen in Excel, ändere Dezimaltrennzeichen in Excel c++, ändere Gruppentrennzeichen in Excel, ändere Gruppentrennzeichen in Excel c++
---

{{% alert color="primary" %}}

In Microsoft Excel können Sie die benutzerdefinierten Dezimal- und Tausendertrennzeichen festlegen, anstatt die Systemtrennzeichen aus den **Erweiterten Excel-Optionen** zu verwenden, wie im untenstehenden Screenshot gezeigt.

Aspose.Cells stellt die Eigenschaften [**WorkbookSettings.GetNumberDecimalSeparator()**](https://reference.aspose.com/cells/go-cpp/workbooksettings/getnumberdecimalseparator/) und [**WorkbookSettings.GetNumberGroupSeparator()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getnumbergroupseparator/) zur Verfügung, um benutzerdefinierte Trennzeichen für die Formatierung/Analyse von Zahlen festzulegen.

{{% /alert %}}

## **Benutzerdefinierte Trennzeichen mit Microsoft Excel festlegen**

Der folgende Screenshot zeigt die **Erweiterten Excel-Optionen** und hebt den Abschnitt hervor, um die **Benutzerdefinierten Trennzeichen** festzulegen.

![todo:image_alt_text](specify-custom-number-decimal-and-group-separators-for-workbook_1.png)

## **Benutzerdefinierte Trennzeichen mit Aspose.Cells festlegen**

Der folgende Beispielcode verdeutlicht, wie die benutzerdefinierten Trennzeichen mithilfe der Aspose.Cells-API festgelegt werden. Es legt die benutzerdefinierten Dezimal- und Gruppentrennzeichen als Punkt und Leerzeichen fest.

### C++ Code zur Spezifikation benutzerdefinierter Dezimal- und Gruppentrennzeichen

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SpecifyCustomNumberDecimalAndGroupSeparatorsForWorkbook.go" >}}
