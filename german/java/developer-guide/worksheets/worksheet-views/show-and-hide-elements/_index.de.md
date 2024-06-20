---
title: Elemente anzeigen und ausblenden
type: docs
weight: 60
url: /de/java/show-and-hide-elements/
---

{{% alert color="primary" %}}

Aspose.Cells ermöglicht es dem Benutzer, Elemente einer Arbeitsmappe anzuzeigen und auszublenden, einschließlich Arbeitsblätter, Zeilen, Spalten, Registerkarten, Bildlaufleisten, Gitterlinien,

{{% /alert %}}

## **Arbeitsblatt anzeigen und ausblenden**

Eine Excel-Datei kann ein oder mehrere Arbeitsblätter enthalten. Immer wenn wir eine Excel-Datei erstellen, fügen wir Arbeitsblätter hinzu, in denen wir arbeiten. Jedes Arbeitsblatt in einer Excel-Datei ist unabhängig von anderen Arbeitsblättern und verfügt über eigene Daten- und Formatierungseinstellungen usw. Manchmal benötigen Entwickler möglicherweise, dass einige Arbeitsblätter in der Excel-Datei ausgeblendet und andere sichtbar sind, um ihre eigenen Interessen zu wahren. **Aspose.Cells** ermöglicht Entwicklern daher, die Sichtbarkeit der Arbeitsblätter in ihren Excel-Dateien zu steuern.

**Steuerung der Sichtbarkeit der Arbeitsblätter:**

Aspose.Cells bietet eine Klasse, [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook), die eine Excel-Datei repräsentiert. Die [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)-Klasse enthält eine [**WorksheetCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection), die den Zugriff auf jedes Arbeitsblatt in der Excel-Datei ermöglicht.

Ein Arbeitsblatt wird von der Klasse [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) repräsentiert. Die Klasse [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) bietet eine Vielzahl von Eigenschaften und Methoden zum Verwalten eines Arbeitsblatts. Um die Sichtbarkeit eines Arbeitsblatts zu steuern, können Entwickler die Methode [**setVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsVisible) der Klasse [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) verwenden.

### **Ein Arbeitsblatt sichtbar machen**

Entwickler können ein Arbeitsblatt sichtbar machen, indem sie **true** als Parameter an die [**setVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsVisible)-Methode der [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)-Klasse übergeben.

### **Arbeitsblatt ausblenden**

Entwickler können ein Arbeitsblatt ausblenden, indem sie **false** als Parameter an die [**setVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsVisible)-Methode der [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)-Klasse übergeben.

**Beispiel:**

Im Folgenden wird ein vollständiges Beispiel gezeigt, das die Verwendung der [**setVisible(false)**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsVisible)-Methode der [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)-Klasse zur Ausblendung des ersten Arbeitsblatts der Excel-Datei demonstriert.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-display-HideUnhideWorksheet-1.java" >}}

**Arbeitsblatt - Vor der Änderung:**

Im nachstehenden Screenshot ist zu sehen, dass die Datei **Book1.xls** drei Arbeitsblätter enthält: **Sheet1** , **Sheet2** und **Sheet3** .

![todo:image_alt_text](show-and-hide-elements_1.png)

**Abbildung:** Arbeitsblattansicht vor jeder Änderung

**Arbeitsblatt - Nach Ausführung des Beispielcodes:**

Die Datei **Book1.xls** wird mithilfe der [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)-Klasse geöffnet und dann wird das erste Arbeitsblatt der Datei **Book1.xls** verborgen. Die geänderte Datei wird als **output.xls** gespeichert, dessen bildliche Ansicht unten gezeigt wird:

![todo:image_alt_text](show-and-hide-elements_2.png)

**Abbildung:** Arbeitsblattansicht nach der Änderung

**Einstellen des Sichtbarkeitstyps**

Sie können auch die Arbeitsblätter auf besondere Weise ausblenden. Diese Funktion kann das Arbeitsblatt ausblenden, sodass Sie es nur wieder sichtbar machen können, indem Sie [**VisibilityType.VERY_HIDDEN**](https://reference.aspose.com/cells/java/com.aspose.cells/visibilitytype#VERY_HIDDEN) als Parameterwert für die [**setVisibilityType**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#VisibilityType)-Methode im Code angeben (es sei hier bemerkt, dass die Benutzer das Objekt nicht direkt über die Menüoptionen in MS Excel sichtbar machen können). Benutzer können auch die [**getVisibilityType**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#VisibilityType)-Methode verwenden, um zu überprüfen, ob ein Arbeitsblatt als Sehr versteckt markiert ist oder nicht.

## **Registerkarten anzeigen oder ausblenden**

Wenn Sie am unteren Rand einer Microsoft Excel-Datei genau hinsehen, sehen Sie eine Reihe von Steuerelementen. Dazu gehören:

- Registerkarten.
- Registerkarten-Scrolltasten.

Registerkarten stellen die Arbeitsblätter in der Excel-Datei dar. Klicken Sie auf eine beliebige Registerkarte, um zu diesem Arbeitsblatt zu wechseln. Je mehr Arbeitsblätter in der Arbeitsmappe sind, desto mehr Registerkarten gibt es. Wenn die Excel-Datei eine gute Anzahl von Arbeitsblättern hat, benötigen Sie Tasten, um zwischen ihnen zu navigieren. Daher bietet Microsoft Excel Registerkarten-Scrolltasten zum Scrollen durch die Registerkarten an.

**Registerkarten und Registerkarten-Bildlaufschaltflächen**

![todo:image_alt_text](show-and-hide-elements_3.png)

Mit Aspose.Cells können Entwickler die Sichtbarkeit von Registerkarten und Bildlaufschaltflächen für Registerkarten in Excel-Dateien steuern.

**Steuerung der Sichtbarkeit von Registerkarten:**
Aspose.Cells bietet eine Klasse, [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook), die eine Microsoft Excel-Datei repräsentiert. Die [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)-Klasse bietet eine Vielzahl von Eigenschaften und Methoden zum Verwalten einer Excel-Datei.

### **Registerkarten ausblenden**

Blenden Sie Registerkarten in einer Excel-Datei aus, indem Sie die [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)-Klasse und die [**getSettings().setShowTabs(false)**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#ShowTabs)-Methode verwenden.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-HideTabs-1.java" >}}

### **Sichtbarkeit von Registerkarten**

Machen Sie Registerkarten mit der [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)-Klasse und der [**getSettings().setShowTabs(true)**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#ShowTabs)-Methode sichtbar.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-DisplayTab-1.java" >}}

**Vollständiges Codebeispiel:**

Im Folgenden finden Sie ein vollständiges Beispiel, das eine Excel-Datei (book1.xls) öffnet, ihre Registerkarten ausblendet und die modifizierte Datei als output.xls speichert.

Sie können im folgenden Abbild sehen, dass die Datei Book1.xls Registerkarten enthält. Nach Ausführung des Beispiels werden die Registerkarten ausgeblendet, wie im Screenshot der Datei output.xls unten zu sehen ist.

**book1.xls: Excel-Datei vor jeglicher Änderung**

![todo:image_alt_text](show-and-hide-elements_4.png)

**output.xls: Excel-Datei nach der Änderung**

![todo:image_alt_text](show-and-hide-elements_5.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-HideTabs-1.java" >}}

## **Zeilen und Spalten anzeigen und ausblenden**

Alle Arbeitsblätter in einer Excel-Datei bestehen aus Zellen, die in Zeilen und Spalten angeordnet sind. Alle Zeilen und Spalten haben eindeutige Werte, die zur Identifizierung und zur Identifizierung einzelner Zellen verwendet werden. Beispielsweise sind Zeilen nummeriert - 1, 2, 3, 4 usw. - und Spalten sind alphabetisch geordnet - A, B, C, D usw. Die Zeilen- und Spaltenwerte werden in den Überschriften angezeigt. Mit Aspose.Cells können Entwickler die Sichtbarkeit dieser Zeilen- und Spaltenüberschriften steuern.

**Steuerung der Sichtbarkeit der Arbeitsblätter:**

Aspose.Cells bietet eine Klasse, [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook), die eine Microsoft Excel-Datei repräsentiert. Die Workbook-Klasse enthält eine WorksheetCollection, die den Zugriff auf jedes Arbeitsblatt in einer Excel-Datei ermöglicht.

Ein Arbeitsblatt wird durch die [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)-Klasse repräsentiert. Die Worksheet-Klasse bietet eine Vielzahl von Eigenschaften und Methoden zum Verwalten von Arbeitsblättern. Verwenden Sie die [**setRowColumnHeadersVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsRowColumnHeadersVisible)-Methode der Worksheet-Klasse, um die Sichtbarkeit von Zeilen- und Spaltenüberschriften zu steuern.

### **Zeilen-/Spaltenheader ausblenden**

Verbergen Sie Zeilen- und Spaltenüberschriften durch Verwendung der [**setRowColumnHeadersVisible(false)**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsRowColumnHeadersVisible) Methode der Klasse [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet).

### **Anzeigen von Zeilen-/Spaltenüberschriften**

Machen Sie Zeilen- und Spaltenüberschriften sichtbar, indem Sie die [**setRowColumnHeadersVisible(true)**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsRowColumnHeadersVisible) Methode der Klasse [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) verwenden.

Ein vollständiges Beispiel unten zeigt, wie die [**setRowColumnHeadersVisible(false)**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsRowColumnHeadersVisible) Methode der Klasse [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) verwendet wird, um die Zeilen- und Spaltenüberschriften des ersten Arbeitsblatts einer Excel-Datei zu verbergen.

Das unten stehende Bild zeigt, dass Buch1.xls drei Arbeitsblätter enthält: Blatt1, Blatt2 und Blatt3. Jedes Arbeitsblatt zeigt Zeilen- und Spaltenüberschriften.

**Book1.xls: Arbeitsblatt vor der Änderung**

![todo:image_alt_text](show-and-hide-elements_6.png)

Book1.xls wird mit der [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) Klasse geöffnet und die Zeilen- und Spaltenüberschriften des ersten Arbeitsblatts werden ausgeblendet. Die geänderte Datei wird als output.xls gespeichert.

**Arbeitsblattansicht nach der Änderung**

![todo:image_alt_text](show-and-hide-elements_7.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-HideUnhideWorksheet-1.java" >}}

## **Bildlaufleisten einblenden und ausblenden**

Scrollleisten werden verwendet, um durch die Inhalte einer Datei zu navigieren. Normalerweise gibt es zwei Arten von Scrollleisten:

- Vertikale Scrollleisten
- Horizontale Scrollleisten

Microsoft Excel bietet auch horizontale und vertikale Scrollleisten an, damit Benutzer durch die Inhalte des Arbeitsblatts scrollen können. Mit Aspose.Cells können Entwickler die Sichtbarkeit beider Arten von Scrollleisten in Excel-Dateien steuern.

**Steuerung der Sichtbarkeit der Scrollleisten:**

Aspose.Cells bietet eine Klasse, [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook), die eine Excel-Datei repräsentiert. Die Klasse [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) bietet eine Vielzahl von Eigenschaften und Methoden zur Verwaltung einer Excel-Datei. Um jedoch die Sichtbarkeit der Scrollleisten in der Excel-Datei zu steuern, können Entwickler die Methoden [**setVScrollBarVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#IsVScrollBarVisible) und [**setHScrollBarVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#IsHScrollBarVisible) der Klasse [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) verwenden.

### **Verbergen von Bildlaufleisten**

Ausblenden von Scrollleisten, indem die [**setVScrollBarVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#IsVScrollBarVisible) oder [**setHScrollBarVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#IsHScrollBarVisible) Methoden der Klasse [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) auf **false** gesetzt werden.

### **Sichtbarkeit von Bildlaufleisten herstellen**

Sichtbarkeit von Scrollleisten herstellen, indem die [**setVScrollBarVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#IsVScrollBarVisible) oder [**setHScrollBarVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#IsHScrollBarVisible) Methoden der Arbeitsmappe auf **true** gesetzt werden.

**Vollständiges Codebeispiel:**

Im Folgenden finden Sie einen vollständigen Code, der eine Excel-Datei, book1.xls, öffnet, beide Bildlaufleisten ausblendet und dann die modifizierte Datei als output.xls speichert.

Das folgende Screenshot zeigt die Datei Book1.xls mit beiden Scrollleisten. Die geänderte Datei wird als output.xls Datei gespeichert, wie unten gezeigt.

**Book1.xls: Excel-Datei vor jeder Änderung**

![todo:image_alt_text](show-and-hide-elements_8.png)

**output.xls: Excel-Datei nach der Änderung**

![todo:image_alt_text](show-and-hide-elements_9.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-display-DisplayHideScrollBars-1.java" >}}

## **Rasterlinien anzeigen und ausblenden**

Alle Arbeitsblätter von Microsoft Excel enthalten standardmäßig Rastlinien. Sie dienen dazu, Zellen abzugrenzen, sodass das Eingeben von Daten in bestimmte Zellen erleichtert wird. Rastlinien ermöglichen es uns, ein Arbeitsblatt als eine Sammlung von Zellen zu betrachten, wobei jede Zelle leicht identifizierbar ist.

Aspose.Cells ermöglicht es Ihnen auch, die Sichtbarkeit der Rastlinien zu steuern.

### **Steuerung der Sichtbarkeit von Rastlinien**

Aspose.Cells stellt eine Klasse, [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook), zur Verfügung, die eine Microsoft Excel-Datei darstellt. Die Klasse [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) enthält ein [**WorksheetCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection), das den Zugriff auf jedes Arbeitsblatt in der Datei ermöglicht.

Ein Arbeitsblatt wird durch die Klasse [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) dargestellt. Die Klasse [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) bietet eine Vielzahl von Eigenschaften und Methoden zum Verwalten von Arbeitsblättern. Um die Sichtbarkeit von Rastlinien zu steuern, verwenden Sie die [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)-Methode der Klasse [**setGridlinesVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsGridlinesVisible).

#### **Anzeigen von Rasterlinien**

Um Rastlinien sichtbar zu machen, verwenden Sie die [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)-Methode der Klasse [**setGridlinesVisible(true)**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsGridlinesVisible).

#### **Rasterspalten ausblenden**

Blendet Rastlinien mit der [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)-Methode der Klasse [**setGridlinesVisible(false)**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsGridlinesVisible) aus.

{{% alert color="primary" %}}

Rastlinien werden auf das gesamte Blatt angewendet. Um Rastlinien in einem Abschnitt eines Arbeitsblatts "auszublenden", verwenden Sie [Rahmenformatierung](/cells/de/java/create-table-by-using-border-lines-for-a-range/), um die Rahmen auf eine Farbe zu setzen, die sich in das Farbschema des Blatts einfügt.

{{% /alert %}}

**Beispiel: Rastlinien auf einem bestimmten Arbeitsblatt ausblenden**

Das folgende Beispiel demonstriert die Verwendung der [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)-Methode der Klasse [**setGridlinesVisible(false)**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsGridlinesVisible), um die Rastlinien des ersten Arbeitsblatts einer Excel-Datei auszublenden.

Der Screenshot zeigt, dass die Datei Book1.xls drei Arbeitsblätter enthält: Sheet1, Sheet2 und Sheet3. Alle diese Arbeitsblätter enthalten Rastlinien.

**Arbeitsblattansicht vor der Änderung**

![todo:image_alt_text](show-and-hide-elements_10.png)

Die Datei Book1.xls wird mit der Klasse [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) geöffnet und dann werden die Rastlinien des ersten Arbeitsblatts ausgeblendet. Die modifizierte Datei wird als Ausgabe.xls-Datei gespeichert.

**Arbeitsblattansicht nach der Änderung**

![todo:image_alt_text](show-and-hide-elements_11.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-DisplayHideGridlines-DisplayHideGridlines.java" >}}

### **Verwandte Artikel**

{{% alert color="primary" %}}

- [Seiteneinrichtungsfunktionen](/cells/de/java/page-setup-features/).
- [Zellen mit Rahmen umranden, um eine Tabelle zu erstellen](/cells/de/java/create-table-by-using-border-lines-for-a-range/).

{{% /alert %}}
