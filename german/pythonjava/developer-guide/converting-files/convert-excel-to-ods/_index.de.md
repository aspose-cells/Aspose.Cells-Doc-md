---
title: Excel in ODS konvertieren
type: docs
weight: 40
url: /de/python-java/convert-excel-to-ods/
---

## **Excel in ODS konvertieren**
ODS-Dateien werden vom Calc-Programm erstellt, das ein Teil der Apache OpenOffice Suite ist. ODS-Dateien speichern Daten, die in Zeilen und Spalten organisiert sind und mithilfe des OASIS OpenDocument-XML-basierten Standards formatiert sind.

Aspose.Cells for Python via Java unterstützt die Arbeit mit ODS-Dateien. Die folgenden Beispiele zeigen, wie Excel in eine ODS-Datei konvertiert wird.
### **Direkte Konvertierung**
Der einfachste Weg, eine Excel-Datei in ODS zu konvertieren, besteht darin, die Arbeitsmappe zu laden und sie zu speichern, indem [SaveFormat.ODS](https://reference.aspose.com/cells/python/asposecells.api/saveformat#ODS) als zweiter Parameter der [Workbook.save](https://reference.aspose.com/cells/python/asposecells.api/workbook#save\(java.lang.String,%20int\)) Methode übergeben wird.

Das folgende Code-Snippet zeigt, wie Excel direkt in ODS konvertiert wird

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "LoadingSavingConvertingAndManaging-ConvertingToODSFiles.py" >}}
### **Speichern Sie das ODS-Dokument gemäß den ODF 1.1- oder 1.2-Spezifikationen**
Aspose.Cells for Python via Java unterstützt das Speichern von ODS-Dateien in ODF 1.1- und ODF 1.2-Spezifikationen. Dafür bietet die API die Eigenschaft [OdsSaveOptions.setStrictSchema11()](https://reference.aspose.com/cells/python/asposecells.api/odssaveoptions#IsStrictSchema11). Wenn Sie diese Eigenschaft auf **true** setzen, wird die Datei mit der ODF 1.1-Spezifikation gespeichert. Der Standardwert von [OdsSaveOptions.setStrictSchema11()](https://reference.aspose.com/cells/python/asposecells.api/odssaveoptions#IsStrictSchema11) ist **false**, sodass die ohne besondere Einstellungen gespeicherte ODS-Datei mit der ODF 1.2-Spezifikation gespeichert wird.

Das folgende Code-Snippet zeigt, wie ODS-Dateien mit ODF 1.1- und 1.2-Spezifikationen gespeichert werden.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "LoadingSavingConvertingAndManaging-SaveODSFilesWithSpecifications.py" >}}
