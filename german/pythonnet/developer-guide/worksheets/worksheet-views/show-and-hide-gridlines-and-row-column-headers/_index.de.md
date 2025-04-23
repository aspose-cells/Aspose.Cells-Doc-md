---
title: Rastlinien und Zeilen / Spaltenüberschriften ein und ausblenden
type: docs
weight: 30
url: /de/python-net/show-and-hide-gridlines-and-row-column-headers/
description: Dieser Artikel bietet Beispielcode für die Verwendung der Aspose.Cells für Python via .NET API, um Gitterlinien, Zeilen und Spaltenüberschriften eines Excel Arbeitsblatts programmatisch auszublenden oder anzuzeigen.
keywords: Python Excel Bibliothek, Gitterlinien anzeigen und ausblenden, Zeilen und Spaltenüberschriften in Python anzeigen und ausblenden, Gitterlinien und Zeilen /Spaltenüberschriften in Python anzeigen und ausblenden.
---

{{% alert color="primary" %}}

Aspose.Cells für Python via .NET unterstützt das Ausblenden und Anzeigen der Gitterlinien des Arbeitsblatts, die standardmäßig sichtbar sind. Es bietet auch die Steuerung der Sichtbarkeit der Zeilen- und Spaltenüberschriften des Arbeitsblatts.

{{% /alert %}}

## **Rasterlinien anzeigen und ausblenden**

Alle Excel-Arbeitsblätter haben standardmäßig Rasterlinien. Sie helfen dabei, Zellen abzugrenzen, sodass es einfach ist, Daten in bestimmte Zellen einzugeben. Rasterlinien ermöglichen es uns, ein Arbeitsblatt als eine Sammlung von Zellen zu betrachten, bei der jede Zelle leicht identifizierbar ist.

### **Steuerung der Sichtbarkeit der Rastlinien**

Aspose.Cells für Python via .NET stellt eine Klasse [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/) bereit, die eine Microsoft Excel-Datei repräsentiert. Die Klasse [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/) enthält eine [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets/)-Sammlung, die Entwicklern den Zugriff auf jedes Arbeitsblatt in der Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch die Klasse [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/) dargestellt. Die Klasse [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/) bietet eine Vielzahl von Eigenschaften und Methoden zur Verwaltung eines Arbeitsblatts. Um die Sichtbarkeit der Gitterlinien zu steuern, verwenden Sie die Eigenschaft [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/) der Klasse [**is_gridlines_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_gridlines_visible/). [**is_gridlines_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_gridlines_visible/) ist eine Boolesche Eigenschaft, was bedeutet, dass sie nur einen Wert **true** oder **false** speichern kann.

#### **Anzeigen von Rasterlinien**

Machen Sie die Rasterlinien sichtbar, indem Sie die Eigenschaft [**is_gridlines_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_gridlines_visible/) der Klasse [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) auf **true** setzen.

#### **Rasterspalten ausblenden**

Blenden Sie die Rasterlinien aus, indem Sie die Eigenschaft [**is_gridlines_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_gridlines_visible/) der Klasse [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) auf **false** setzen.

Ein vollständiges Beispiel unten zeigt, wie die Eigenschaft [**is_gridlines_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_gridlines_visible/) verwendet wird, indem eine Excel-Datei (book1.xls) geöffnet, die Rasterlinien auf dem ersten Arbeitsblatt ausgeblendet und die modifizierte Datei als output.xls gespeichert wird.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Views-Display-DisplayHideGridlines-1.py" >}}

## **Zeigen und Ausblenden der Zeilen- und Spaltenüberschriften**

Alle Arbeitsblätter in einer Excel-Datei bestehen aus Zellen, die in Reihen und Spalten angeordnet sind. Alle Reihen und Spalten haben eindeutige Werte, die zu ihrer Identifikation verwendet werden, sowie zur Identifikation einzelner Zellen. Zum Beispiel sind Reihen nummeriert – 1, 2, 3, 4 usw. – und Spalten sind alphabetisch geordnet – A, B, C, D usw. Die Werte der Reihen und Spalten werden in den Kopfzeilen angezeigt. Mit Aspose.Cells für Python via .NET können Entwickler die Sichtbarkeit dieser Reihen- und Spaltenüberschriften steuern.

### **Steuerung der Sichtbarkeit der Arbeitsblätter**

Aspose.Cells für Python via .NET stellt eine Klasse [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/) bereit, die eine Microsoft Excel-Datei repräsentiert. Die Klasse [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/) enthält eine [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets/)-Sammlung, die den Zugriff auf jedes Arbeitsblatt in der Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch die Klasse [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/) dargestellt. Die Klasse [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/) bietet eine Vielzahl von Eigenschaften und Methoden zur Verwaltung eines Arbeitsblatts. Um die Sichtbarkeit der Reihen- und Spaltenüberschriften zu steuern, verwenden Sie die Eigenschaft [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/) der Klasse [**is_row_column_headers_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_row_column_headers_visible/). [**is_row_column_headers_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_row_column_headers_visible/) ist eine Boolesche Eigenschaft, was bedeutet, dass sie nur einen Wert **true** oder **false** speichern kann.

#### **Anzeigen von Zeilen-/Spaltenüberschriften**

Machen Sie die Zeilen- und Spaltenüberschriften sichtbar, indem Sie die Eigenschaft [**is_row_column_headers_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_row_column_headers_visible/) der Klasse [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) auf **true** setzen.

#### **Zeilen-/Spaltenheader ausblenden**

Blenden Sie die Zeilen- und Spaltenüberschriften aus, indem Sie die Eigenschaft [**is_row_column_headers_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_row_column_headers_visible/) der Klasse [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) auf **false** setzen.

Ein vollständiges Beispiel unten zeigt, wie die Eigenschaft [**is_row_column_headers_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_row_column_headers_visible/) verwendet wird, indem eine Excel-Datei (book1.xls) geöffnet, die Zeilen- und Spaltenüberschriften auf dem ersten Arbeitsblatt ausgeblendet und die modifizierte Datei als output.xls gespeichert wird.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Views-Display-DisplayHideRowColumnHeaders-1.py" >}}

{{% alert color="primary" %}}

Es ist auch möglich, die [**unhide_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/unhide_rows) und [**unhide_columns**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/unhide_columns) Methoden der [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) Klasse zu verwenden, um mehrere Zeilen und Spalten sichtbar zu machen.

{{% /alert %}}
