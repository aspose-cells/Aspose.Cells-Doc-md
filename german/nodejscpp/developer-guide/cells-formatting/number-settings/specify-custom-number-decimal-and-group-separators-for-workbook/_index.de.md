---
title: Benutzerdefinierte Dezimal und Gruppentrennzeichen für Arbeitsmappe festlegen
linktitle: Benutzerdefinierte Dezimal und Gruppentrennzeichen für Arbeitsmappe festlegen
type: docs
weight: 110
url: /de/nodejs-cpp/specify-custom-number-decimal-and-group-separators-for-workbook/
description: Ändern Sie Dezimal und Gruppentrennzeichen in Excel mit Aspose.Cells for Node.js via C++. 
keywords: Geben Sie benutzerdefinierte Dezimal und Gruppentrennzeichen in Excel Node.js via C++ an, ändern Sie Dezimal und Gruppentrennzeichen in Excel Node.js via C++, ändern Sie Dezimal und Gruppentrennzeichen in Excel node.js via C++
---

{{% alert color="primary" %}}

In Microsoft Excel können Sie die benutzerdefinierten Dezimal- und Tausendertrennzeichen festlegen, anstatt die Systemtrennzeichen aus den **Erweiterten Excel-Optionen** zu verwenden, wie im untenstehenden Screenshot gezeigt.

Aspose.Cells stellt die Methoden [**WorkbookSettings.setNumberDecimalSeparator(string)**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#setNumberDecimalSeparator-string-) und [**WorkbookSettings.setNumberGroupSeparator(string)**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#setNumberGroupSeparator-string-) zum Festlegen der benutzerdefinierten Trennzeichen für die Formatierung/Analyse von Zahlen bereit.

{{% /alert %}}

## **Benutzerdefinierte Trennzeichen mit Microsoft Excel festlegen**

Der folgende Screenshot zeigt die **Erweiterten Excel-Optionen** und hebt den Abschnitt hervor, um die **Benutzerdefinierten Trennzeichen** festzulegen.

![todo:image_alt_text](specify-custom-number-decimal-and-group-separators-for-workbook_1.png)

## **Angabe benutzerdefinierter Trennzeichen mit Aspose.Cells for Node.js via C++**

Der folgende Beispielcode verdeutlicht, wie die benutzerdefinierten Trennzeichen mithilfe der Aspose.Cells-API festgelegt werden. Es legt die benutzerdefinierten Dezimal- und Gruppentrennzeichen als Punkt und Leerzeichen fest.

### Node.js-Code zur Spezifizierung benutzerdefinierter Dezimal- und Gruppentrennzeichen für Zahlen

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-NumberSetting-SpecifyCustomNumberDecimalAndGroupSeparators.js" >}}


