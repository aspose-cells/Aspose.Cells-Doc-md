---
title: Konvertieren Sie Excel in ODS
type: docs
weight: 40
url: /de/python-java/convert-excel-to-ods/
---
## **Konvertieren Sie Excel in ODS**
ODS-Dateien werden vom Calc-Programm erstellt, das Teil der Apache OpenOffice Suite ist. ODS-Dateien speichern Daten, die in Zeilen und Spalten organisiert und mit dem XML-basierten Standard OASIS OpenDocument formatiert sind.

Aspose.Cells for Python via Java unterstützt funktionierende ODS-Dateien. Die folgenden Beispiele demonstrieren die Konvertierung von Excel in eine ODS-Datei.
### **Direkte Konvertierung**
Der einfachste Weg, eine Excel-Datei in ODS zu konvertieren, besteht darin, die Arbeitsmappe zu laden und im Vorbeigehen zu speichern[SaveFormat.ODS](https://reference.aspose.com/cells/python/asposecells.api/saveformat#ODS) als zweiter Parameter der[Arbeitsmappe.speichern](https://reference.aspose.com/cells/python/asposecells.api/workbook#save\(java.lang.String,%20int\)) Methode.

Der folgende Codeausschnitt demonstriert die direkte Konvertierung von Excel in ODS

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "LoadingSavingConvertingAndManaging-ConvertingToODSFiles.py" >}}
### **Speichern Sie das ODS-Dokument in den ODF 1.1- oder 1.2-Spezifikationen**
Aspose.Cells for Python via Java unterstützt das Speichern von ODS-Dateien in den Spezifikationen ODF 1.1 und ODF 1.2. Dafür sorgt die API[OdsSaveOptions.setStrictSchema11()](https://reference.aspose.com/cells/python/asposecells.api/odssaveoptions#IsStrictSchema11) Eigentum. Setzen Sie diese Eigenschaft auf**Stimmt** speichert die Datei mit der ODF 1.1-Spezifikation. Der Standardwert von[OdsSaveOptions.setStrictSchema11()](https://reference.aspose.com/cells/python/asposecells.api/odssaveoptions#IsStrictSchema11) ist**FALSCH**, sodass die ohne spezielle Einstellungen gespeicherte ODS-Datei mit der ODF 1.2-Spezifikation gespeichert wird.

Der folgende Codeausschnitt demonstriert das Speichern von ODS-Dateien mit ODF 1.1- und 1.2-Spezifikationen.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "LoadingSavingConvertingAndManaging-SaveODSFilesWithSpecifications.py" >}}
