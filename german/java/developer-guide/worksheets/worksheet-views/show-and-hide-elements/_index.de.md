---
title: Elemente ein- und ausblenden
type: docs
weight: 60
url: /de/java/show-and-hide-elements/
---
{{% alert color="primary" %}}

Aspose.Cells ermöglicht dem Benutzer das Ein- und Ausblenden von Elementen einer Arbeitsmappe, einschließlich Arbeitsblättern, Zeilen, Spalten, Registerkarten, Bildlaufleisten, Gitternetzlinien,

{{% /alert %}}

## **Ein Arbeitsblatt ein- und ausblenden**

 Eine Excel-Datei kann ein oder mehrere Arbeitsblätter enthalten. Immer wenn wir eine Excel-Datei erstellen, fügen wir der Excel-Datei, in der wir arbeiten, Arbeitsblätter hinzu. Jedes Arbeitsblatt in einer Excel-Datei ist unabhängig von dem anderen Arbeitsblatt, da es seine eigenen Daten und Formatierungseinstellungen usw. hat. Manchmal müssen Entwickler möglicherweise einige Arbeitsblätter ausblenden und andere in der Excel-Datei aus eigenem Interesse sichtbar machen. So,**Aspose.Cells** ermöglicht Entwicklern, die Sichtbarkeit der Arbeitsblätter in ihren Excel-Dateien zu steuern.

**Steuern der Sichtbarkeit der Arbeitsblätter:**

 Aspose.Cells bietet eine Klasse,[**Arbeitsmappe**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) die eine Excel-Datei darstellt.[**Arbeitsmappe**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) Klasse enthält a[**Arbeitsblattsammlung**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)die den Zugriff auf jedes Arbeitsblatt in der Excel-Datei ermöglicht.

 Ein Arbeitsblatt wird durch dargestellt[**Arbeitsblatt**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) Klasse.[**Arbeitsblatt**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) Die Klasse bietet eine breite Palette von Eigenschaften und Methoden zum Verwalten eines Arbeitsblatts. Aber um die Sichtbarkeit eines Arbeitsblatts zu steuern, können Entwickler verwenden[**setVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsVisible) Methode der[**Arbeitsblatt**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) Klasse.

### **Ein Arbeitsblatt sichtbar machen**

 Entwickler können ein Arbeitsblatt durch Übergeben sichtbar machen**Stimmt** als Parameter für die[**setVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsVisible) Methode der[**Arbeitsblatt**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) Klasse.

### **Ausblenden eines Arbeitsblatts**

 Entwickler können ein Arbeitsblatt durch Übergeben ausblenden**FALSCH** als Parameter für die[**setVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsVisible) Methode der[**Arbeitsblatt**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) Klasse.

**Beispiel:**

 Nachfolgend finden Sie ein vollständiges Beispiel, das die Verwendung von demonstriert[**setVisible(false)**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsVisible) Methode von[**Arbeitsblatt**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) Klasse, um das erste Arbeitsblatt der Excel-Datei auszublenden.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-display-HideUnhideWorksheet-1.java" >}}

**Arbeitsblatt - Vor der Änderung:**

 Im Screenshot unten können Sie das sehen**Buch1.xls** Datei enthält drei Arbeitsblätter:**Blatt1** , **Blatt2** und**Blatt3** .

![todo: Bild_alt_Text](show-and-hide-elements_1.png)

**Figur:** Arbeitsblattansicht vor jeder Änderung

**Arbeitsblatt – nach dem Ausführen des Beispielcodes:**

**Buch1.xls** Datei wird mit dem geöffnet[**Arbeitsmappe**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) Klasse und dann das erste Arbeitsblatt der**Buch1.xls** Datei wird ausgeblendet. Die geänderte Datei wird gespeichert als**Ausgabe.xls**Datei, deren bildliche Ansicht unten gezeigt wird:

![todo: Bild_alt_Text](show-and-hide-elements_2.png)

**Figur:** Arbeitsblattansicht nach der Änderung

**Sichtbarkeitstyp festlegen**

 Sie können die Arbeitsblätter auch auf spezielle Weise ausblenden. Diese Funktion kann das Arbeitsblatt ausblenden, sodass Sie es nur durch Geben wieder sichtbar machen können[**Sichtbarkeitstyp.VERY_HIDDEN**](https://reference.aspose.com/cells/java/com.aspose.cells/visibilitytype#VERY_HIDDEN) als Parameterwert für die[**setVisibilityType**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#VisibilityType) -Methode im Code (hier ist zu beachten, dass der Benutzer das Objekt nicht direkt in MS Excel über dessen Menüoptionen sichtbar machen kann). Benutzer können auch verwenden[**getVisibilityType**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#VisibilityType) Methode, um zu prüfen, ob ein Arbeitsblatt als VeryHidden markiert ist oder nicht.

## **Registerkarten ein- oder ausblenden**

Wenn Sie sich das Ende einer Microsoft-Excel-Datei genau ansehen, sehen Sie eine Reihe von Steuerelementen. Diese beinhalten:

- Blattregisterkarten.
- Tab-Scroll-Schaltflächen.

Blattregisterkarten stellen die Arbeitsblätter in der Excel-Datei dar. Klicken Sie auf eine beliebige Registerkarte, um zu diesem Arbeitsblatt zu wechseln. Je mehr Arbeitsblätter in der Arbeitsmappe vorhanden sind, desto mehr Blattregisterkarten gibt es. Wenn die Excel-Datei eine große Anzahl von Arbeitsblättern enthält, benötigen Sie Schaltflächen, um durch sie zu navigieren. So stellt Microsoft Excel Schaltflächen zum Scrollen von Registerkarten bereit, um durch die Blattregisterkarten zu scrollen.

**Blattregisterkarten und Schaltflächen zum Scrollen von Registerkarten**

![todo: Bild_alt_Text](show-and-hide-elements_3.png)

Mit Aspose.Cells können Entwickler die Sichtbarkeit von Blattregisterkarten und Schaltflächen zum Scrollen von Registerkarten in Excel-Dateien steuern.

**Steuern der Sichtbarkeit von Registerkarten:**
 Aspose.Cells bietet eine Klasse,[**Arbeitsmappe**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) , die eine Microsoft Excel-Datei darstellt. Das[**Arbeitsmappe**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) -Klasse bietet eine Vielzahl von Eigenschaften und Methoden zum Verwalten einer Excel-Datei.

### **Registerkarten ausblenden**

 Blenden Sie Registerkarten in einer Excel-Datei aus, indem Sie die[**Arbeitsmappe**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) Klasse'[**getSettings().setShowTabs(false)**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#ShowTabs) Methode.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-HideTabs-1.java" >}}

### **Registerkarten sichtbar machen**

 Machen Sie Registerkarten mit sichtbar[**Arbeitsmappe**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) Klasse'[**getSettings().setShowTabs(true)**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#ShowTabs) Methode.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-DisplayTab-1.java" >}}

**Vollständiges Codebeispiel:**

Nachfolgend finden Sie ein vollständiges Beispiel, das eine Excel-Datei (book1.xls) öffnet, ihre Registerkarten ausblendet und die geänderte Datei als output.xls speichert.

In der Abbildung unten sehen Sie, dass die Datei Book1.xls Registerkarten enthält. Nachdem der Beispielcode ausgeführt wurde, werden die Registerkarten ausgeblendet, wie Sie auf dem Screenshot der Datei output.xls unten sehen können.

**book1.xls: Excel-Datei vor jeder Änderung**

![todo: Bild_alt_Text](show-and-hide-elements_4.png)

**output.xls: Excel-Datei nach der Änderung**

![todo: Bild_alt_Text](show-and-hide-elements_5.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-HideTabs-1.java" >}}

## **Zeilen und Spalten ein- und ausblenden**

Alle Arbeitsblätter in einer Excel-Datei bestehen aus Zellen, die in Zeilen und Spalten angeordnet sind. Alle Zeilen und Spalten haben eindeutige Werte, die zu ihrer Identifizierung und zur Identifizierung einzelner Zellen verwendet werden. Beispielsweise werden Zeilen nummeriert – 1, 2, 3, 4 usw. – und Spalten alphabetisch geordnet – A, B, C, D usw. Die Zeilen- und Spaltenwerte werden in den Kopfzeilen angezeigt. Mit Aspose.Cells können Entwickler die Sichtbarkeit dieser Zeilen- und Spaltenüberschriften steuern.

**Steuern der Sichtbarkeit der Arbeitsblätter:**

 Aspose.Cells bietet eine Klasse,[**Arbeitsmappe**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook), die eine Microsoft Excel-Datei darstellt. Die Workbook-Klasse enthält eine WorksheetCollection, die den Zugriff auf jedes Arbeitsblatt in einer Excel-Datei ermöglicht.

 Ein Arbeitsblatt wird durch dargestellt[**Arbeitsblatt**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)Klasse. Die Worksheet-Klasse bietet eine Vielzahl von Eigenschaften und Methoden zum Verwalten von Arbeitsblättern. Verwenden Sie die Worksheet-Klasse, um die Sichtbarkeit von Zeilen- und Spaltenüberschriften zu steuern.[**setRowColumnHeadersVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsRowColumnHeadersVisible) Methode.

### **Zeilen-/Spaltenüberschriften ausblenden**

 Blenden Sie Zeilen- und Spaltenüberschriften mit aus[**Arbeitsblatt**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) Klasse'[**setRowColumnHeadersVisible(false)**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsRowColumnHeadersVisible) Methode.

### **Zeilen-/Spaltenüberschriften sichtbar machen**

 Machen Sie Zeilen- und Spaltenüberschriften sichtbar, indem Sie die verwenden[**Arbeitsblatt**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) Klasse'[**setRowColumnHeadersVisible(true)**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsRowColumnHeadersVisible) Methode.

 Nachfolgend finden Sie ein vollständiges Beispiel, das die Verwendung von demonstriert[**Arbeitsblatt**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) Klasse'[**setRowColumnHeadersVisible(false)**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsRowColumnHeadersVisible) Methode zum Ausblenden von Zeilen- und Spaltenüberschriften des ersten Arbeitsblatts einer Excel-Datei.

Der folgende Screenshot zeigt, dass Book1.xls drei Arbeitsblätter enthält: Sheet1, Sheet2 und Sheet3. Jedes Arbeitsblatt zeigt Zeilen- und Spaltenüberschriften.

**Book1.xls: Arbeitsblatt vor der Änderung**

![todo: Bild_alt_Text](show-and-hide-elements_6.png)

 Book1.xls wird mit dem geöffnet[**Arbeitsmappe**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) Klasse' und die Zeilen- und Spaltenüberschriften auf dem ersten Arbeitsblatt sind ausgeblendet. Die geänderte Datei wird als output.xls gespeichert.

**Arbeitsblattansicht nach der Änderung**

![todo: Bild_alt_Text](show-and-hide-elements_7.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-HideUnhideWorksheet-1.java" >}}

## **Bildlaufleisten ein- und ausblenden**

Bildlaufleisten werden häufig verwendet, um durch den Inhalt einer Datei zu navigieren. Normalerweise gibt es zwei Arten von Bildlaufleisten:

- Vertikale Bildlaufleisten
- Horizontale Bildlaufleisten

Microsoft Excel bietet auch horizontale und vertikale Bildlaufleisten, damit Benutzer durch Arbeitsblattinhalte blättern können. Mit Aspose.Cells können Entwickler die Sichtbarkeit beider Arten von Bildlaufleisten in Excel-Dateien steuern.

**Steuern der Sichtbarkeit der Bildlaufleisten:**

 Aspose.Cells bietet eine Klasse,[**Arbeitsmappe**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) die eine Excel-Datei darstellt.[**Arbeitsmappe**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) -Klasse bietet eine Vielzahl von Eigenschaften und Methoden zum Verwalten einer Excel-Datei. Aber um die Sichtbarkeit der Bildlaufleisten in der Excel-Datei zu steuern, können Entwickler verwenden[**setVScrollBarVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#IsVScrollBarVisible) & [**setHScrollBarVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#IsHScrollBarVisible) Methoden der[**Arbeitsmappe**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) Klasse.

### **Bildlaufleisten ausblenden**

 Blenden Sie Bildlaufleisten aus, indem Sie die[**Arbeitsmappe**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) Klasse'[**setVScrollBarVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#IsVScrollBarVisible) oder[**setHScrollBarVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#IsHScrollBarVisible) Methoden zu**FALSCH**.

### **Bildlaufleisten sichtbar machen**

 Machen Sie Bildlaufleisten sichtbar, indem Sie die Workbook-Klasse festlegen.[**setVScrollBarVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#IsVScrollBarVisible) oder[**setHScrollBarVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#IsHScrollBarVisible) Methoden zu**Stimmt**.

**Vollständiges Codebeispiel:**

Unten ist ein vollständiger Code, der eine Excel-Datei, book1.xls, öffnet, beide Bildlaufleisten ausblendet und dann die geänderte Datei als output.xls speichert.

Der folgende Screenshot zeigt die Datei Book1.xls, die beide Bildlaufleisten enthält. Die geänderte Datei wird als output.xls-Datei gespeichert, die auch unten gezeigt wird.

**Book1.xls: Excel-Datei vor jeder Änderung**

![todo: Bild_alt_Text](show-and-hide-elements_8.png)

**output.xls: Excel-Datei nach der Änderung**

![todo: Bild_alt_Text](show-and-hide-elements_9.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-display-DisplayHideScrollBars-1.java" >}}

## **Rasterlinien ein- und ausblenden**

Alle Microsoft Excel-Arbeitsblätter haben standardmäßig Gitternetzlinien. Sie helfen dabei, Zellen abzugrenzen, sodass es einfach ist, Daten in bestimmte Zellen einzugeben. Gitternetzlinien ermöglichen es uns, ein Arbeitsblatt als eine Sammlung von Zellen anzuzeigen, wobei jede Zelle leicht identifizierbar ist.

Mit Aspose.Cells können Sie auch die Sichtbarkeit der Gitternetzlinien steuern.

### **Steuern der Sichtbarkeit von Gitternetzlinien**

 Aspose.Cells bietet eine Klasse,[**Arbeitsmappe**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) das stellt eine Microsoft Excel-Datei dar. Das[**Arbeitsmappe**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) Klasse enthält a[**Arbeitsblattsammlung**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) die den Zugriff auf jedes Arbeitsblatt in der Datei ermöglicht.

 Ein Arbeitsblatt wird durch dargestellt[**Arbeitsblatt**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) Klasse. Das[**Arbeitsblatt**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) -Klasse bietet eine Vielzahl von Eigenschaften und Methoden zum Verwalten von Arbeitsblättern. Um die Sichtbarkeit von Gitternetzlinien zu steuern, verwenden Sie das[**Arbeitsblatt**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) Klasse'[**setGridlinesVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsGridlinesVisible) Methode.

#### **Rasterlinien sichtbar machen**

 Um Rasterlinien sichtbar zu machen, verwenden Sie das[**Arbeitsblatt**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) Klasse'[**setGridlinesVisible(true)**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsGridlinesVisible) Methode.

#### **Ausblenden von Gitternetzlinien**

 Blenden Sie Gitternetzlinien mit dem aus[**Arbeitsblatt**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) Klasse'[**setGridlinesVisible(false)**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsGridlinesVisible) Methode.

{{% alert color="primary" %}}

Gitternetzlinien werden auf das gesamte Blatt angewendet. Verwenden Sie zum „Ausblenden“ von Gitternetzlinien in einem Abschnitt eines Arbeitsblatts[Randformatierung](/cells/de/java/create-table-by-using-border-lines-for-a-range/) , um die Ränder auf eine Farbe einzustellen, die sich in das Farbschema des Blatts einfügt.

{{% /alert %}}

**Beispiel: Ausblenden von Gitternetzlinien auf einem bestimmten Arbeitsblatt**

 Das folgende Beispiel demonstriert die Verwendung von[**Arbeitsblatt**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) Klasse'[**setGridlinesVisible(false)**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsGridlinesVisible) Methode zum Ausblenden von Gitternetzlinien des ersten Arbeitsblatts einer Excel-Datei.

Der folgende Screenshot zeigt, dass die Datei Book1.xls drei Arbeitsblätter enthält: Sheet1, Sheet2 und Sheet3. Alle diese Arbeitsblätter haben Gitterlinien.

**Arbeitsblattansicht vor der Änderung**

![todo: Bild_alt_Text](show-and-hide-elements_10.png)

 Die Datei Book1.xls wird mit dem geöffnet[**Arbeitsmappe**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) Klasse und dann werden die Gitternetzlinien des ersten Arbeitsblatts ausgeblendet. Die geänderte Datei wird als Datei output.xls gespeichert.

**Arbeitsblattansicht nach der Änderung**

![todo: Bild_alt_Text](show-and-hide-elements_11.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-DisplayHideGridlines-DisplayHideGridlines.java" >}}

### **In Verbindung stehende Artikel**

{{% alert color="primary" %}}

- [Seiteneinrichtungsfunktionen](/cells/de/java/page-setup-features/).
- [Rahmen zu Zellen hinzufügen, um eine Tabelle zu erstellen](/cells/de/java/create-table-by-using-border-lines-for-a-range/).

{{% /alert %}}
