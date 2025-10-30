---
title: Benutzerdefinierte Dezimal und Gruppentrennzeichen für Arbeitsmappe festlegen
type: docs
weight: 110
url: /de/python-net/specify-custom-number-decimal-and-group-separators-for-workbook/
description: Ändern Sie die Dezimal und Gruppentrennzeichen in MS Excel und mit C# Code durch Verwendung der Aspose.Cells für Python via .NET API.
keywords: benutzerdefinierten Dezimaltrennzeichen in Excel festlegen, benutzerdefiniertes Dezimaltrennzeichen in Excel c#, benutzerdefiniertes Gruppentrennzeichen in Excel festlegen, benutzerdefiniertes Gruppentrennzeichen in Excel c#, benutzerdefinierte Dezimal und Gruppentrennzeichen in Excel festlegen, benutzerdefinierte Dezimal und Gruppentrennzeichen in Excel c#, Dezimal und Gruppentrennzeichen in Excel c# ändern, Dezimal und Gruppentrennzeichen in Excel ändern, Dezimaltrennzeichen in Excel ändern, Dezimaltrennzeichen in Excel c# ändern, Gruppentrennzeichen in Excel ändern, Gruppentrennzeichen in Excel c# ändern
---

{{% alert color="primary" %}}

In Microsoft Excel können Sie die benutzerdefinierten Dezimal- und Tausendertrennzeichen festlegen, anstatt die Systemtrennzeichen aus den **Erweiterten Excel-Optionen** zu verwenden, wie im untenstehenden Screenshot gezeigt.

Aspose.Cells für Python via .NET stellt die Eigenschaften [**WorkbookSettings.number_decimal_separator**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/number_decimal_separator/) und [**WorkbookSettings.number_group_separator**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/number_group_separator/) bereit, um benutzerdefinierte Trennzeichen für die Formatierung/Parsing von Zahlen festzulegen.

{{% /alert %}}

## **Benutzerdefinierte Trennzeichen mit Microsoft Excel festlegen**

Der folgende Screenshot zeigt die **Erweiterten Excel-Optionen** und hebt den Abschnitt hervor, um die **Benutzerdefinierten Trennzeichen** festzulegen.

![todo:image_alt_text](specify-custom-number-decimal-and-group-separators-for-workbook_1.png)

## **Benutzerdefinierte Trennzeichen mit Aspose.Cells für Python via .NET angeben**

Der folgende Beispielcode zeigt, wie man die benutzerdefinierten Trennzeichen mithilfe der Aspose.Cells für Python via .NET API festlegt. Es legt die Dezimal- und Gruppentrennzeichen als Punkt und Leerzeichen fest.

### C#-Code zum Festlegen benutzerdefinierter Dezimal- und Gruppentrennzeichen

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-CustomDecimalAndGroupSeparator.py" >}}

{{< app/cells/assistant language="python-net" >}}
