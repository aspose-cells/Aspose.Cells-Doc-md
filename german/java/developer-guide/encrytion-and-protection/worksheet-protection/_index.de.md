---
title: Arbeitsblatt schützen und entschützen
type: docs
weight: 50
url: /de/java/protect-and-unprotect-worksheet/
---

## **Arbeitsblätter schützen**

Wenn ein Arbeitsblatt geschützt ist, sind die Aktionen, die ein Benutzer durchführen kann, eingeschränkt. Beispielsweise kann er keine Daten eingeben, Zeilen oder Spalten einfügen oder löschen usw. Die allgemeinen Schutzmöglichkeiten in Microsoft Excel sind:

- Inhalt
- Objekte
- Szenarien

Geschützte Arbeitsblätter verbergen oder schützen keine sensiblen Daten, daher unterscheidet es sich von der Dateiverschlüsselung. Im Allgemeinen eignet sich der Arbeitsblattschutz für Präsentationszwecke. Es verhindert, dass der Endbenutzer Daten, Inhalte und Formatierungen im Arbeitsblatt ändert.

### **Hinzufügen oder Entfernen des Schutzes**

Aspose.Cells bietet eine Klasse, [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook), die eine Microsoft Excel Datei repräsentiert. Die Klasse Workbook enthält eine WorksheetCollection, die den Zugriff auf jedes Arbeitsblatt in einer Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch die Klasse [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) repräsentiert.

Die Klasse Worksheet bietet die Methode [**Protect**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#protect(int)), die zum Anwenden von Schutz auf ein Arbeitsblatt verwendet wird. Die Protect-Methode akzeptiert die folgenden Parameter:

- Schutzttyp, der Typ des Schutzes, der auf das Arbeitsblatt angewendet werden soll. Der Schutzttyp wird mithilfe der Enumeration [**ProtectionType**](https://reference.aspose.com/cells/java/com.aspose.cells/ProtectionType) angewendet.
- Neues Passwort, das neue Passwort, das zum Schutz des Arbeitsblatts verwendet wird.
- Altes Kennwort, das alte Kennwort, wenn das Arbeitsblatt bereits kennwortgeschützt ist. Wenn das Arbeitsblatt noch nicht geschützt ist, einfach null übergeben.

Die Enumeration ProtectionType enthält die folgenden vordefinierten Schutzttypen:

|**Schutztypen**|**Beschreibung**|
| :- | :- |
|[**ALL**](https://reference.aspose.com/cells/java/com.aspose.cells/protectiontype#ALL)|Benutzer kann auf diesem Arbeitsblatt nichts ändern|
|[**CONTENTS**](https://reference.aspose.com/cells/java/com.aspose.cells/protectiontype#CONTENTS)|Benutzer kann in diesem Arbeitsblatt keine Daten eingeben|
|[**OBJECTS**](https://reference.aspose.com/cells/java/com.aspose.cells/protectiontype#OBJECTS)|Benutzer kann Zeichenobjekte nicht ändern|
|[**SCENARIOS**](https://reference.aspose.com/cells/java/com.aspose.cells/protectiontype#SCENARIOS)|Benutzer kann gespeicherte Szenarien nicht ändern|
|[**STRUCTURE**](https://reference.aspose.com/cells/java/com.aspose.cells/protectiontype#STRUCTURE)|Benutzer kann gespeicherte Struktur nicht ändern|
|[**WINDOWS**](https://reference.aspose.com/cells/java/com.aspose.cells/protectiontype#WINDOWS)|Benutzer kann gespeicherte Fenster nicht ändern|
|[**NONE**](https://reference.aspose.com/cells/java/com.aspose.cells/protectiontype#NONE)|Kein Schutz|

Das folgende Beispiel zeigt, wie ein Arbeitsblatt mit einem Passwort geschützt wird.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-ProtectingWorksheet-ProtectingWorksheet.java" >}}

Nachdem der obige Code zum Schützen des Arbeitsblatts verwendet wurde, überprüfen Sie den Schutz des Arbeitsblatts, indem Sie es öffnen. Sobald Sie die Datei öffnen und einige Daten in das Arbeitsblatt eingeben, wird der folgende Dialog angezeigt:

**Ein Dialog, der vorwarnt, dass ein Benutzer das Arbeitsblatt nicht ändern kann** 

![todo:image_alt_text](protect-and-unprotect-worksheet_1.png)

Um am Arbeitsblatt zu arbeiten, heben Sie den Schutz des Arbeitsblatts auf, indem Sie im Menüpunkt **Extras** die Option **Blattschutz aufheben** auswählen, wie unten gezeigt.

**Auswählen der Option Blattschutz aufheben** 

![todo:image_alt_text](protect-and-unprotect-worksheet_2.png)

Ein Dialog fordert zur Eingabe eines Kennworts auf.

**Eingabe des Passworts zum Entsperren des Arbeitsblatts** 

![todo:image_alt_text](protect-and-unprotect-worksheet_3.png)

### **Schutz einiger Zellen**

Es könnte bestimmte Szenarien geben, in denen Sie nur einige Zellen im Arbeitsblatt sperren müssen. Wenn Sie bestimmte Zellen im Arbeitsblatt sperren möchten, müssen Sie alle anderen Zellen im Arbeitsblatt entsperren. Alle Zellen in einem Arbeitsblatt sind bereits für das Sperren initialisiert, Sie können dies überprüfen, indem Sie eine Excel-Datei in MS Excel öffnen und auf **Format | Zellen...** klicken, um den Dialog **Zellen formatieren** anzuzeigen. Klicken Sie dann auf die Registerkarte Schutz und sehen Sie, dass ein Kontrollkästchen mit der Aufschrift "Gesperrt" standardmäßig aktiviert ist.

Im Folgenden werden die beiden Herangehensweisen zur Umsetzung der Aufgabe beschrieben.

**Methode 1:**

Die folgenden Punkte beschreiben, wie Sie mit MS Excel einige Zellen sperren können. Diese Methode gilt für Microsoft Office Excel 97, 2000, 2002, 2003 und neuere Versionen.

1. Wählen Sie das gesamte Arbeitsblatt aus, indem Sie auf die Schaltfläche Alle auswählen (das graue Rechteck direkt über der Zeilennummer für Zeile 1 und links von der Spaltenüberschrift A) klicken.
1. Klicken Sie im Menü Format auf Zellen, klicken Sie auf die Registerkarte Schutz und deaktivieren Sie das Kontrollkästchen Gesperrt.

   Dies entsperrt alle Zellen im Arbeitsblatt

{{% alert color="primary" %}}

Wenn der Befehl Zellen nicht verfügbar ist, sind möglicherweise Teile des Arbeitsblatts bereits gesperrt. Klicken Sie im Menü Extras auf Schutz und dann auf Arbeitsblatt schützen.

{{% /alert %}}

1. Wählen Sie nur die Zellen aus, die Sie sperren möchten, und wiederholen Sie Schritt 2, aber aktivieren Sie dieses Mal das Kontrollkästchen Gesperrt.
1. Wählen Sie im Menü **Extras** Schutz aus, klicken Sie auf **Arbeitsblatt schützen** und klicken Sie dann auf **OK**.

{{% alert color="primary" %}}

Im Dialogfeld Arbeitsblatt schützen haben Sie die Möglichkeit, ein Passwort zu spezifizieren und die Elemente auszuwählen, die Benutzer ändern können.

{{% /alert %}}

**Methode 2:**

In dieser Methode verwenden wir nur die Aspose.Cells-API, um die Aufgabe zu erledigen.

Das folgende Beispiel zeigt, wie Sie einige Zellen im Arbeitsblatt schützen können. Es entsperrt zuerst alle Zellen im Arbeitsblatt und sperrt dann 3 Zellen (A1, B1, C1). Schließlich schützt es das Arbeitsblatt. Eine Zeile / Spalte verfügt über eine Style-API, die eine Methode set Locked enthält. Sie können diese Methode verwenden, um die Zeile / Spalte zu sperren oder zu entsperren.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-ProtectingSpecificCellsinaWorksheet-ProtectingSpecificCellsinaWorksheet.java" >}}

### **Schützen Sie eine Zeile im Arbeitsblatt**

Aspose.Cells ermöglicht es Ihnen, jede Zeile im Arbeitsblatt ganz einfach zu sperren. Hier können wir die [**applyStyle()**](https://reference.aspose.com/cells/java/com.aspose.cells/row#applyStyle(com.aspose.cells.Style,%20com.aspose.cells.StyleFlag))-Methode der Klasse [**Row**](https://reference.aspose.com/cells/java/com.aspose.cells/Row) verwenden, um einem bestimmten Zeile im Arbeitsblatt ein Style anzuwenden. Diese Methode nimmt zwei Argumente an: ein [**Style**](https://reference.aspose.com/cells/java/com.aspose.cells/Style)-Objekt und einen [**StyleFlag**](https://reference.aspose.com/cells/java/com.aspose.cells/StyleFlag)-Struktur, die alle Mitglieder im Zusammenhang mit der angewandten Formatierung enthält.

Das folgende Beispiel zeigt, wie Sie eine Zeile im Arbeitsblatt schützen können. Es entsperrt zuerst alle Zellen im Arbeitsblatt und sperrt dann die erste Zeile. Schließlich schützt es das Arbeitsblatt. Eine Zeile / Spalte verfügt über eine Style-API, die eine Methode setCellLocked enthält. Sie können die Zeile / Spalte mit der StyleFlag-Struktur sperren oder entsperren.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-ProtectRowWorksheet-ProtectRowWorksheet.java" >}}

### **Schützen Sie eine Spalte im Arbeitsblatt**

Aspose.Cells ermöglicht es Ihnen, jede Spalte im Arbeitsblatt einfach zu sperren. Hier können wir die Methode [**applyStyle()**](https://reference.aspose.com/cells/java/com.aspose.cells/column#applyStyle(com.aspose.cells.Style,%20com.aspose.cells.StyleFlag)) der Klasse [**Column**](https://reference.aspose.com/cells/java/com.aspose.cells/Column) verwenden, um den Stil auf eine bestimmte Spalte im Arbeitsblatt anzuwenden. Diese Methode nimmt zwei Argumente entgegen: ein [**Style**](https://reference.aspose.com/cells/java/com.aspose.cells/Style)-Objekt und ein [**StyleFlag**](https://reference.aspose.com/cells/java/com.aspose.cells/StyleFlag)-Struktur, die alle Mitglieder im Zusammenhang mit der angewendeten Formatierung enthält.

Das folgende Beispiel zeigt, wie man eine Spalte im Arbeitsblatt schützt. Es werden zunächst alle Zellen im Arbeitsblatt entsperrt und dann die erste Spalte gesperrt. Schließlich wird das Arbeitsblatt geschützt. Eine Zeile/eine Spalte hat eine Style-API, die die Methode setLocked enthält. Sie können die Zeile/die Spalte mithilfe der Struktur StyleFlag sperren oder entsperren.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-ProtectColumnWorksheet-ProtectColumnWorksheet.java" >}}

## **Arbeitsblatt entsperren**

[Schutz von Arbeitsblättern](/cells/de/java/protect-and-unprotect-worksheet/#protect-worksheets) und [Erweiterte Schutzeinstellungen seit Excel XP](/cells/de/java/protect-and-unprotect-worksheet/#advanced-protection-settings-since-excel-xp) behandelt verschiedene Ansätze zur Sicherung von Arbeitsblättern. Was ist, wenn ein Entwickler den Schutz von einem geschützten Arbeitsblatt zur Laufzeit entfernen muss, damit Änderungen an der Datei vorgenommen werden können? Dies kann leicht mit Aspose.Cells erreicht werden.

### **Verwendung von Microsoft Excel**

Um den Schutz von einem Arbeitsblatt zu entfernen:

Wählen Sie im **Extras**-Menü **Schutz**, gefolgt von **Arbeitsblatt entsperren**.

**Auswahl des Befehls Arbeitsblatt entsperren** 

![todo:image_alt_text](protect-and-unprotect-worksheet_4.png)

Der Schutz wird entfernt, es sei denn, das Arbeitsblatt ist passwortgeschützt. In diesem Fall fordert ein Dialogfeld das Passwort an.

**Eingabe des Passworts zum Entsperren des Arbeitsblatts** 

![todo:image_alt_text](protect-and-unprotect-worksheet_5.png)

### **Verwendung von Aspose.Cells**

Ein Arbeitsblatt kann entsperrt werden, indem die [**Unprotect**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#unprotect--)-Methode der Klasse [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) aufgerufen wird. Die [**Unprotect**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#unprotect--)-Methode kann auf folgende Weise verwendet werden, wie unten beschrieben.

### **Entsperren eines einfach geschützten Arbeitsblatts**

Ein einfach geschütztes Arbeitsblatt ist eines, das nicht mit einem Passwort geschützt ist. Solche Arbeitsblätter können entsperrt werden, indem die Methode unprotect ohne Parameter aufgerufen wird.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-UnprotectingSimplyProtectedWorksheet-UnprotectingSimplyProtectedWorksheet.java" >}}

### **Entsperren eines passwortgeschützten Arbeitsblatts**

Ein passwortgeschütztes Arbeitsblatt ist eines, das mit einem Passwort geschützt ist. Solche Arbeitsblätter können entsperrt werden, indem eine überladene Version der Unprotect-Methode aufgerufen wird, die das Passwort als Parameter entgegennimmt.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-UnprotectProtectSheet-UnprotectProtectSheet.java" >}}

## **Erweiterte Schutzeinstellungen seit Excel XP**

[Schutz von Arbeitsblättern](/cells/de/java/protect-and-unprotect-worksheet/#protect-worksheets) behandelt das Schützen eines Arbeitsblatts in Microsoft Excel 97 und 2000. Seit der Veröffentlichung von Excel 2002 oder XP hat Microsoft viele erweiterte Schutzeinstellungen hinzugefügt. Diese Schutzeinstellungen beschränken oder erlauben Benutzern:

- Zeilen oder Spalten löschen.
- Inhalte, Objekte oder Szenarien bearbeiten.
- Zellen, Zeilen oder Spalten formatieren.
- Zeilen, Spalten oder Hyperlinks einfügen.
- Gesperrte oder ungesperrte Zellen auswählen.
- Pivot-Tabellen verwenden und vieles mehr.

Aspose.Cells unterstützt alle erweiterten Schutzeinstellungen, die von Excel XP und späteren Versionen angeboten werden.

### **Erweiterte Schutzeinstellungen mit Excel XP und späteren Versionen verwenden**

Um die Schutzeinstellungen in Excel XP anzuzeigen:

1. Wählen Sie im Menü **Extras** die Option **Schutz** und dann **Arbeitsblatt schützen**.
   Es wird ein Dialogfeld angezeigt.

   **Dialogfeld zur Anzeige von Schutzoptionen in Excel XP**

![todo:image_alt_text](protect-and-unprotect-worksheet_6.png)

1. Arbeitsblattfunktionen erlauben oder einschränken oder ein Passwort anwenden.

### **Erweiterte Schutzeinstellungen mit Aspose.Cells verwenden**

Aspose.Cells unterstützt alle erweiterten Schutzeinstellungen.

Aspose.Cells stellt eine Klasse, [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook), bereit, die eine Microsoft Excel-Datei darstellt. Die Workbook-Klasse enthält eine WorksheetCollection-Sammlung, die den Zugriff auf jedes Arbeitsblatt in der Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch die Klasse [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) dargestellt.

Die Worksheet-Klasse bietet die Protection-Eigenschaft, die verwendet wird, um diese erweiterten Schutzeinstellungen anzuwenden. Die Protection-Eigenschaft ist tatsächlich ein Objekt der Klasse [**Protection**](https://reference.aspose.com/cells/java/com.aspose.cells/protection), das mehrere boolesche Eigenschaften zum Deaktivieren oder Aktivieren von Einschränkungen enthält.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-AdvancedProtectionSettingsUsingAsposeCells-AdvancedProtectionSettingsUsingAsposeCells.java" >}}

Unten finden Sie eine kleine Beispielanwendung. Es öffnet eine Excel-Datei und verwendet die meisten von Excel XP und späteren Versionen unterstützten erweiterten Schutzeinstellungen.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-AdvancedProtection-AdvancedProtection.java" >}}

{{% alert color="primary" %}}

Speichern Sie die Datei im Format EXCEL97TO2003 oder XLSX, da diese erweiterten Schutzeinstellungen nur von MS Excel XP und späteren Versionen unterstützt werden.

{{% /alert %}}

### **Problem mit Zellsperre**

Wenn Sie möchten, dass Benutzer das Bearbeiten von Zellen einschränken, müssen die Zellen vor der Anwendung von Schutzeinstellungen gesperrt sein. Andernfalls können die Zellen bearbeitet werden, auch wenn das Arbeitsblatt geschützt ist. In Microsoft Excel XP können Zellen durch den folgenden Dialog gesperrt werden:

**Dialog zum Sperren von Zellen in Excel XP** 

![todo:image_alt_text](protect-and-unprotect-worksheet_7.png)

Es ist auch möglich, Zellen mithilfe der Aspose.Cells API zu sperren. Jede Zelle verfügt über eine Style-API, die wiederum eine Methode setLocked enthält. Verwenden Sie diese, um Zellen zu sperren oder zu entsperren.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-LockCell-LockCell.java" >}}
