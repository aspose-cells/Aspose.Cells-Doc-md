---
title: Rastlinien und Zeilen / Spaltenüberschriften ein und ausblenden
type: docs
weight: 30
url: /de/net/show-and-hide-gridlines-and-row-column-headers/
description: Dieser Artikel enthält Beispielcode für die Verwendung der C# API oder der .NET Bibliothek zum programmgesteuerten Ausblenden oder Anzeigen von Rasterlinien, Zeilen und Spaltenüberschriften eines Excel Arbeitsblatts.
---

{{% alert color="primary" %}}

Aspose.Cells unterstützt das Ausblenden und Anzeigen von Rasterlinien des Arbeitsblatts, die standardmäßig sichtbar sind. Es ermöglicht auch die Kontrolle der Sichtbarkeit von Zeilen- und Spaltenüberschriften des Arbeitsblatts.

{{% /alert %}}

## **Rasterlinien anzeigen und ausblenden**

Alle Excel-Arbeitsblätter haben standardmäßig Rasterlinien. Sie helfen dabei, Zellen abzugrenzen, sodass es einfach ist, Daten in bestimmte Zellen einzugeben. Rasterlinien ermöglichen es uns, ein Arbeitsblatt als eine Sammlung von Zellen zu betrachten, bei der jede Zelle leicht identifizierbar ist.

### **Steuerung der Sichtbarkeit der Rastlinien**

Aspose.Cells stellt eine Klasse [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) bereit, die eine Microsoft Excel-Datei repräsentiert. Die Klasse [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) enthält eine [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)-Sammlung, die es Entwicklern ermöglicht, auf jedes Arbeitsblatt in der Excel-Datei zuzugreifen. Ein Arbeitsblatt wird durch die Klasse [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) dargestellt. Die Klasse [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) bietet eine Vielzahl von Eigenschaften und Methoden zur Verwaltung eines Arbeitsblatts. Um die Sichtbarkeit von Rasterlinien zu steuern, verwenden Sie die Eigenschaft [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) der Klasse [**IsGridlinesVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isgridlinesvisible). [**IsGridlinesVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isgridlinesvisible) ist eine boolesche Eigenschaft, die nur einen **true**- oder **false**-Wert speichern kann.

#### **Anzeigen von Rasterlinien**

Machen Sie die Rasterlinien sichtbar, indem Sie die Eigenschaft [**IsGridlinesVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isgridlinesvisible) der Klasse [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) auf **true** setzen.

#### **Rasterspalten ausblenden**

Blenden Sie die Rasterlinien aus, indem Sie die Eigenschaft [**IsGridlinesVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isgridlinesvisible) der Klasse [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) auf **false** setzen.

Ein vollständiges Beispiel unten zeigt, wie die Eigenschaft [**IsGridlinesVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isgridlinesvisible) verwendet wird, indem eine Excel-Datei (book1.xls) geöffnet, die Rasterlinien auf dem ersten Arbeitsblatt ausgeblendet und die modifizierte Datei als output.xls gespeichert wird.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-DisplayHideGridlines-1.cs" >}}

## **Zeigen und Ausblenden der Zeilen- und Spaltenüberschriften**

Alle Arbeitsblätter in einer Excel-Datei bestehen aus Zellen, die in Zeilen und Spalten angeordnet sind. Alle Zeilen und Spalten haben eindeutige Werte, die zur Identifizierung und zum Identifizieren einzelner Zellen verwendet werden. Beispielsweise sind Zeilen nummeriert – 1, 2, 3, 4 usw. – und Spalten sind alphabetisch geordnet – A, B, C, D usw. Die Zeilen- und Spaltenwerte werden in den Überschriften angezeigt. Mit Aspose.Cells können Entwickler die Sichtbarkeit dieser Zeilen- und Spaltenüberschriften steuern.

### **Steuerung der Sichtbarkeit der Arbeitsblätter**

Aspose.Cells stellt eine Klasse [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) bereit, die eine Microsoft Excel-Datei repräsentiert. Die Klasse [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) enthält eine [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)-Sammlung, die es Entwicklern ermöglicht, auf jedes Arbeitsblatt in der Excel-Datei zuzugreifen. Ein Arbeitsblatt wird durch die Klasse [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) dargestellt. Die Klasse [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) bietet eine Vielzahl von Eigenschaften und Methoden zur Verwaltung eines Arbeitsblatts. Um die Sichtbarkeit der Zeilen- und Spaltenüberschriften zu steuern, verwenden Sie die Eigenschaft [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) der Klasse [**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isrowcolumnheadersvisible). [**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isrowcolumnheadersvisible) ist eine boolesche Eigenschaft, die nur einen **true** oder **false**-Wert speichern kann.

#### **Anzeigen von Zeilen-/Spaltenüberschriften**

Machen Sie die Zeilen- und Spaltenüberschriften sichtbar, indem Sie die Eigenschaft [**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isrowcolumnheadersvisible) der Klasse [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) auf **true** setzen.

#### **Zeilen-/Spaltenheader ausblenden**

Blenden Sie die Zeilen- und Spaltenüberschriften aus, indem Sie die Eigenschaft [**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isrowcolumnheadersvisible) der Klasse [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) auf **false** setzen.

Ein vollständiges Beispiel unten zeigt, wie die Eigenschaft [**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isrowcolumnheadersvisible) verwendet wird, indem eine Excel-Datei (book1.xls) geöffnet, die Zeilen- und Spaltenüberschriften auf dem ersten Arbeitsblatt ausgeblendet und die modifizierte Datei als output.xls gespeichert wird.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-DisplayHideRowColumnHeaders-1.cs" >}}

{{% alert color="primary" %}}

Es ist auch möglich, die [**UnhideRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/unhiderows) und [**UnhideColumns**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/unhidecolumns) Methoden der [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) Klasse zu verwenden, um mehrere Zeilen und Spalten sichtbar zu machen.

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
