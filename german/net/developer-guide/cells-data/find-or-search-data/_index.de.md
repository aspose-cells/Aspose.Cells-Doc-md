---
title: Daten suchen oder suchen
type: docs
weight: 50
url: /de/net/find-or-search-data/
description: Erfahren Sie, wie Sie Zellen in einem Arbeitsblatt finden oder durchsuchen, die bestimmte Daten über Aspose.Cells for .NET API enthalten.
keywords: Find data, Search data, Find Cells Containing a Formula, Search Cells Containing a Formula, Find Data or Formulas using FindOptions, Search Data or Formulas using FindOptions, Find or Search Cells Containing Specified String Value or Number, Find or Search cells contains specified data
---
{{% alert color="primary" %}}

Microsoft Excel ermöglicht Benutzern das Suchen von Zellen in einem Arbeitsblatt, die bestimmte Daten enthalten.

{{% /alert %}}

##  **Es wurde festgestellt, dass Cells die angegebenen Daten enthält**

###  **Mit Microsoft Excel**

 Microsoft Excel ermöglicht Benutzern das Suchen von Zellen in einem Arbeitsblatt, die bestimmte Daten enthalten. Wenn Sie auswählen**Bearbeiten** von dem**Finden** Im Menü Microsoft Excel wird ein Dialog angezeigt, in dem Sie den Suchwert angeben können.

Hier suchen wir nach dem Wert „Oranges“. Aspose.Cells ermöglicht es Entwicklern außerdem, Zellen im Arbeitsblatt zu finden, die bestimmte Werte enthalten.

###  **Verwenden Sie Aspose.Cells**

 Aspose.Cells bietet eine Klasse,[**Arbeitsmappe**](https://reference.aspose.com/cells/net/aspose.cells/workbook) , das eine Microsoft Excel-Datei darstellt. Der[**Arbeitsmappe**](https://reference.aspose.com/cells/net/aspose.cells/workbook) Klasse enthält a[**Arbeitsblätter**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) Sammlung, die den Zugriff auf jedes Arbeitsblatt in der Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch dargestellt[**Arbeitsblatt**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) Klasse. Der[**Arbeitsblatt**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) Klasse bietet a[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) Sammlung, die alle Zellen im Arbeitsblatt darstellt. Der[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)Die Sammlung bietet mehrere Methoden zum Suchen von Zellen in einem Arbeitsblatt, die benutzerdefinierte Daten enthalten. Einige dieser Methoden werden im Folgenden ausführlicher besprochen.

{{% alert color="primary" %}}

Alle Find-Methoden geben die Referenzen der Zellen zurück, die die angegebenen zu durchsuchenden Daten enthalten.

{{% /alert %}}

##  **Cells finden, das eine Formel enthält**

 Entwickler können eine bestimmte Formel im Arbeitsblatt finden, indem sie die aufrufen[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) Sammlung[**Finden**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/find/index) Methode. Typischerweise ist die[**Finden**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/find/index)Die Methode akzeptiert drei Parameter:

- **Objekt:**Das zu suchende Objekt. Der Typ sollte int,double,DateTime,string,bool sein.
- **Vorherige Zelle:**Vorherige Zelle mit demselben Objekt. Dieser Parameter kann auf null gesetzt werden, wenn von Anfang an gesucht wird.
- FindOptions: Optionen zum Finden des gewünschten Objekts.

Die folgenden Beispiele verwenden Arbeitsblattdaten zum Üben von Suchmethoden:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Find-FindingCellsContainingFormula-1.cs" >}}

##  **Suchen von Daten oder Formeln mit FindOptions**

 Mit dem ist es möglich, bestimmte Werte zu finden[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) Sammlung[**Finden**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/find/index) Methode mit verschiedenen[**FindOptions**](https://reference.aspose.com/cells/net/aspose.cells/findoptions) . Typischerweise ist die[**Finden**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/find/index)Die Methode akzeptiert die folgenden Parameter:

- *Suchwert**, die Daten oder der Wert, nach denen gesucht werden soll.
- *Vorherige Zelle**, die letzte Zelle, die denselben Wert enthielt. Dieser Parameter kann bei der Suche von Anfang an auf Null gesetzt werden.
- *Suchoptionen**, die Suchoptionen.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Find-FindingDataOrFormulasUsingFindOptions-1.cs" >}}

##  **Es wird gefunden, dass Cells den angegebenen Zeichenfolgenwert oder die angegebene Zeichenfolge enthält**

 Es ist möglich, bestimmte Zeichenfolgenwerte zu finden, indem Sie diese aufrufen[**Finden**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/find/index) Methode gefunden in der[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) Sammlung mit diversen[**FindOptions**](https://reference.aspose.com/cells/net/aspose.cells/findoptions).

 Präzisiere das[**FindOptions.LookInType**](https://reference.aspose.com/cells/net/aspose.cells/findoptions/properties/lookintype) Und[**FindOptions.LookAtType**](https://reference.aspose.com/cells/net/aspose.cells/findoptions/properties/lookattype) Eigenschaften. Der folgende Beispielcode veranschaulicht, wie diese Eigenschaften verwendet werden, um Zellen mit einer unterschiedlichen Anzahl von Zeichenfolgen zu finden**Anfang** oder am**Center** oder am**Ende** des Zellstrangs.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Find-FindingCellsContainingStringValueOrNumber-1.cs" >}}

##  **Vorabthemen**
- [Finden Sie Cells mit spezifischem Stil](/cells/de/net/find-cells-with-specific-style/)
- [Finden Sie heraus, ob der Zellenwert mit einem einfachen Anführungszeichen beginnt](/cells/de/net/find-if-the-cell-value-starts-with-single-quote-mark/)
- [Suchen Sie nach Daten anhand der Originalwerte](/cells/de/net/search-data-using-original-values/)
