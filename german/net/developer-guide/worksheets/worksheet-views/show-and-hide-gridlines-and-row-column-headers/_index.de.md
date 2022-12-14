---
title: Rasterlinien und Spaltenüberschriften ein- und ausblenden
type: docs
weight: 30
url: /de/net/show-and-hide-gridlines-and-row-column-headers/
---
{{% alert color="primary" %}}

Aspose.Cells unterstützt das Ein- und Ausblenden von Gitternetzlinien des Arbeitsblatts, die standardmäßig sichtbar sind. Es bietet auch die Kontrolle der Sichtbarkeit der Zeilen-Spalten-Kopfzeilen des Arbeitsblatts.

{{% /alert %}}

## **Rasterlinien ein- und ausblenden**

Alle Excel-Arbeitsblätter haben standardmäßig Gitternetzlinien. Sie helfen dabei, Zellen abzugrenzen, sodass es einfach ist, Daten in bestimmte Zellen einzugeben. Gitternetzlinien ermöglichen es uns, ein Arbeitsblatt als eine Sammlung von Zellen anzuzeigen, wobei jede Zelle leicht identifizierbar ist.

### **Steuern der Sichtbarkeit der Gitternetzlinien**

Aspose.Cells bietet eine Klasse,[**Arbeitsmappe**](https://reference.aspose.com/cells/net/aspose.cells/workbook), die eine Microsoft Excel-Datei darstellt. Das[**Arbeitsmappe**](https://reference.aspose.com/cells/net/aspose.cells/workbook)Klasse enthält a[**Arbeitsblätter**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)Sammlung, die es Entwicklern ermöglicht, auf jedes Arbeitsblatt in der Excel-Datei zuzugreifen. Ein Arbeitsblatt wird durch dargestellt[**Arbeitsblatt**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) Klasse. Das[**Arbeitsblatt**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) -Klasse bietet eine Vielzahl von Eigenschaften und Methoden zum Verwalten eines Arbeitsblatts. Um die Sichtbarkeit von Gitternetzlinien zu steuern, verwenden Sie die[**Arbeitsblatt**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) Klasse[**IsGridlinesVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isgridlinesvisible) Eigentum.[**IsGridlinesVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isgridlinesvisible) ist eine boolesche Eigenschaft, was bedeutet, dass sie nur a speichern kann**Stimmt** oder**FALSCH** Wert.

#### **Rasterlinien sichtbar machen**

 Machen Sie die Gitternetzlinien sichtbar, indem Sie das einstellen[**Arbeitsblatt**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) Klasse[**IsGridlinesVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isgridlinesvisible) Eigentum zu**Stimmt**.

#### **Ausblenden von Gitternetzlinien**

 Gitternetzlinien ausblenden, indem Sie die[**Arbeitsblatt**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) Klasse[**IsGridlinesVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isgridlinesvisible) Eigentum zu**FALSCH**.

 Nachfolgend finden Sie ein vollständiges Beispiel, das die Verwendung von demonstriert[**IsGridlinesVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isgridlinesvisible)-Eigenschaft, indem Sie eine Excel-Datei (book1.xls) öffnen, die Gitternetzlinien auf dem ersten Arbeitsblatt ausblenden und die geänderte Datei als output.xls speichern.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-DisplayHideGridlines-1.cs" >}}

## **Zeilen-Spalten-Überschriften ein- und ausblenden**

Alle Arbeitsblätter in einer Excel-Datei bestehen aus Zellen, die in Zeilen und Spalten angeordnet sind. Alle Zeilen und Spalten haben eindeutige Werte, die verwendet werden, um sie und einzelne Zellen zu identifizieren. Beispielsweise werden Zeilen nummeriert – 1, 2, 3, 4 usw. – und Spalten alphabetisch geordnet – A, B, C, D usw. Die Zeilen- und Spaltenwerte werden in den Kopfzeilen angezeigt. Mit Aspose.Cells können Entwickler die Sichtbarkeit dieser Zeilen- und Spaltenüberschriften steuern.

### **Steuern der Sichtbarkeit der Arbeitsblätter**

Aspose.Cells bietet eine Klasse,[**Arbeitsmappe**](https://reference.aspose.com/cells/net/aspose.cells/workbook), die eine Microsoft Excel-Datei darstellt. Das[**Arbeitsmappe**](https://reference.aspose.com/cells/net/aspose.cells/workbook)Klasse enthält a[**Arbeitsblätter**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)Sammlung, die es Entwicklern ermöglicht, auf jedes Arbeitsblatt in der Excel-Datei zuzugreifen. Ein Arbeitsblatt wird durch dargestellt[**Arbeitsblatt**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)Klasse. Das[**Arbeitsblatt**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) -Klasse bietet eine Vielzahl von Eigenschaften und Methoden zum Verwalten eines Arbeitsblatts. Um die Sichtbarkeit von Zeilen- und Spaltenüberschriften zu steuern, verwenden Sie die[**Arbeitsblatt**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) Klasse[**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isrowcolumnheadersvisible) Eigentum.[**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isrowcolumnheadersvisible) ist eine boolesche Eigenschaft, was bedeutet, dass sie nur a speichern kann**Stimmt** oder**FALSCH**Wert.

#### **Zeilen-/Spaltenüberschriften sichtbar machen**

 Machen Sie Zeilen- und Spaltenüberschriften sichtbar, indem Sie die[**Arbeitsblatt**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) Klasse[**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isrowcolumnheadersvisible) Eigentum zu**Stimmt**.

#### **Zeilen-/Spaltenüberschriften ausblenden**

 Blenden Sie Zeilen- und Spaltenüberschriften aus, indem Sie die[**Arbeitsblatt**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) Klasse[**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isrowcolumnheadersvisible) Eigentum zu**FALSCH**.

Nachfolgend finden Sie ein vollständiges Beispiel, das die Verwendung von zeigt[**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isrowcolumnheadersvisible)-Eigenschaft, indem Sie eine Excel-Datei (book1.xls) öffnen, die Zeilen- und Spaltenüberschriften auf dem ersten Arbeitsblatt ausblenden und die geänderte Datei als output.xls speichern.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-DisplayHideRowColumnHeaders-1.cs" >}}

{{% alert color="primary" %}}

 Es ist auch möglich, die zu verwenden[**Zeilen einblenden**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/unhiderows) und[**Spalten einblenden**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/unhidecolumns) Methoden der[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) -Klasse, um mehrere Zeilen und Spalten sichtbar zu machen.

{{% /alert %}}
