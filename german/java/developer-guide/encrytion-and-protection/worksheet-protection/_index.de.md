---
title: Arbeitsblatt zum Schützen und Aufheben des Schutzes
type: docs
weight: 50
url: /de/java/protect-and-unprotect-worksheet/
---
## **Arbeitsblätter schützen**

Wenn ein Arbeitsblatt geschützt ist, sind die Aktionen, die ein Benutzer ausführen kann, eingeschränkt. Sie können beispielsweise keine Daten eingeben, Zeilen oder Spalten einfügen oder löschen usw. Die allgemeinen Schutzoptionen in Microsoft Excel sind:

- Inhalt
- Objekte
- Szenarien

Geschützte Arbeitsblätter verstecken oder schützen sensible Daten nicht und unterscheiden sich daher von der Dateiverschlüsselung. Im Allgemeinen ist der Arbeitsblattschutz für Präsentationszwecke geeignet. Es verhindert, dass der Endbenutzer Daten, Inhalt und Formatierung im Arbeitsblatt ändert.

### **Schutz hinzufügen oder entfernen**

 Aspose.Cells bietet eine Klasse,[**Arbeitsmappe**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) , die eine Microsoft Excel-Datei darstellt. Die Workbook-Klasse enthält eine WorksheetCollection, die den Zugriff auf jedes Arbeitsblatt in einer Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch dargestellt[**Arbeitsblatt**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) Klasse.

 Die Worksheet-Klasse stellt die[**Beschützen**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#protect(int))-Methode, mit der ein Arbeitsblatt geschützt wird. Die Protect-Methode akzeptiert die folgenden Parameter:

-  Schutztyp, der auf das Arbeitsblatt anzuwendende Schutztyp. Die Schutzart wird mit Hilfe der angewendet[**Schutztyp**](https://reference.aspose.com/cells/java/com.aspose.cells/ProtectionType) Aufzählung.
- Neues Passwort, das neue Passwort, das zum Schutz des Arbeitsblatts verwendet wird.
- Altes Passwort, das alte Passwort, wenn das Arbeitsblatt bereits passwortgeschützt ist. Wenn das Arbeitsblatt noch nicht geschützt ist, übergeben Sie einfach eine Null.

Die ProtectionType-Enumeration enthält die folgenden vordefinierten Schutztypen:

|**Schutztypen**|**Beschreibung**|
|:- |:- |
|[**ALLE**](https://reference.aspose.com/cells/java/com.aspose.cells/protectiontype#ALL)|Der Benutzer kann nichts auf diesem Arbeitsblatt ändern|
|[**INHALT**](https://reference.aspose.com/cells/java/com.aspose.cells/protectiontype#CONTENTS)|Der Benutzer kann keine Daten in dieses Arbeitsblatt eingeben|
|[**OBJEKTE**](https://reference.aspose.com/cells/java/com.aspose.cells/protectiontype#OBJECTS)|Der Benutzer kann Zeichnungsobjekte nicht ändern|
|[**SZENARIEN**](https://reference.aspose.com/cells/java/com.aspose.cells/protectiontype#SCENARIOS)|Der Benutzer kann gespeicherte Szenarien nicht ändern|
|[**STRUKTUR**](https://reference.aspose.com/cells/java/com.aspose.cells/protectiontype#STRUCTURE)|Der Benutzer kann die gespeicherte Struktur nicht ändern|
|[**FENSTER**](https://reference.aspose.com/cells/java/com.aspose.cells/protectiontype#WINDOWS)|Der Benutzer kann gespeicherte Fenster nicht ändern|
|[**KEINER**](https://reference.aspose.com/cells/java/com.aspose.cells/protectiontype#NONE)|Kein Schutz|

Das folgende Beispiel zeigt, wie Sie ein Arbeitsblatt mit einem Kennwort schützen.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-ProtectingWorksheet-ProtectingWorksheet.java" >}}

Nachdem der obige Code zum Schützen des Arbeitsblatts verwendet wurde, überprüfen Sie den Schutz auf dem Arbeitsblatt, indem Sie es öffnen. Sobald Sie die Datei öffnen und versuchen, einige Daten zum Arbeitsblatt hinzuzufügen, wird das folgende Dialogfeld angezeigt:

**Eine Dialogwarnung, dass ein Benutzer das Arbeitsblatt nicht ändern kann** 

![todo: Bild_alt_Text](protect-and-unprotect-worksheet_1.png)

Um das Arbeitsblatt zu bearbeiten, heben Sie den Schutz des Arbeitsblatts auf, indem Sie das auswählen**Schutz** , dann**Blattschutz aufheben** von dem**Werkzeug** Menüpunkt wie unten gezeigt.

**Wählen Sie den Menüpunkt „Blattschutz aufheben“.** 

![todo: Bild_alt_Text](protect-and-unprotect-worksheet_2.png)

Ein Dialogfeld wird geöffnet, in dem Sie zur Eingabe eines Kennworts aufgefordert werden.

**Geben Sie ein Passwort ein, um den Schutz des Arbeitsblatts aufzuheben** 

![todo: Bild_alt_Text](protect-and-unprotect-worksheet_3.png)

### **Schutz einiger weniger Cells**

 Es kann bestimmte Szenarien geben, in denen Sie nur einige Zellen im Arbeitsblatt sperren müssen. Wenn Sie bestimmte Zellen im Arbeitsblatt sperren möchten, müssen Sie alle anderen Zellen im Arbeitsblatt entsperren. Alle Zellen in einem Arbeitsblatt sind bereits zum Sperren initialisiert, Sie können dies überprüfen, indem Sie eine beliebige Excel-Datei in MS Excel öffnen und auf klicken**Format | Cells...** zeigen**Cells formatieren** Dialogfeld und klicken Sie dann auf die Registerkarte Schutz und sehen Sie, dass ein Kontrollkästchen mit der Bezeichnung "Gesperrt" standardmäßig aktiviert ist.

Im Folgenden sind die beiden Ansätze zur Implementierung der Aufgabe aufgeführt.

**Methode 1:**

Die folgenden Punkte beschreiben, wie Sie mit MS Excel einige Zellen sperren. Diese Methode gilt für Microsoft Office Excel 97, 2000, 2002, 2003 und höhere Versionen.

1. Wählen Sie das gesamte Arbeitsblatt aus, indem Sie auf die Schaltfläche Alle auswählen klicken (das graue Rechteck direkt über der Zeilennummer für Zeile 1 und links neben dem Spaltenbuchstaben A).
1. Klicken Sie im Menü Format auf Cells, klicken Sie auf die Registerkarte Schutz, und deaktivieren Sie dann das Kontrollkästchen Gesperrt.

 Dadurch werden alle Zellen auf dem Arbeitsblatt entsperrt

{{% alert color="primary" %}}

Wenn der Befehl Zellen nicht verfügbar ist, sind Teile des Arbeitsblatts möglicherweise bereits gesperrt. Zeigen Sie im Menü Extras auf Schutz und klicken Sie dann auf Blattschutz aufheben .

{{% /alert %}}

1. Wählen Sie nur die Zellen aus, die Sie sperren möchten, und wiederholen Sie Schritt 2, aktivieren Sie diesmal jedoch das Kontrollkästchen Gesperrt.
1.  Auf der**Werkzeug** Menü, auswählen**Schutz** , klicken**Schutzblatt** , und klicken Sie dann auf**OK**.

{{% alert color="primary" %}}

Im Dialogfeld „Blatt schützen“ haben Sie die Möglichkeit, ein Kennwort anzugeben und die Elemente auszuwählen, die Benutzer ändern können sollen.

{{% /alert %}}

**Methode2:**

Bei dieser Methode verwenden wir Aspose.Cells API nur, um die Aufgabe zu erledigen.

Das folgende Beispiel zeigt, wie einige Zellen im Arbeitsblatt geschützt werden. Es entsperrt zuerst alle Zellen im Arbeitsblatt und sperrt dann 3 Zellen (A1, B1, C1) darin. Schließlich schützt es das Arbeitsblatt. Eine Zeile/Spalte hat einen Stil API, der außerdem eine festgelegte Locked-Methode enthält. Mit dieser Methode können Sie die Zeile / Spalte sperren oder entsperren.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-ProtectingSpecificCellsinaWorksheet-ProtectingSpecificCellsinaWorksheet.java" >}}

### **Schützen Sie eine Zeile im Arbeitsblatt**

 Aspose.Cells ermöglicht es Ihnen, jede Zeile im Arbeitsblatt einfach zu sperren. Hier können wir Gebrauch machen[**applyStyle()**](https://reference.aspose.com/cells/java/com.aspose.cells/row#applyStyle(com.aspose.cells.Style,%20com.aspose.cells.StyleFlag) ) Methode von[**Die Zeile**](https://reference.aspose.com/cells/java/com.aspose.cells/Row) Klasse, um Style auf eine bestimmte Zeile im Arbeitsblatt anzuwenden. Diese Methode akzeptiert zwei Argumente: a[**Stil**](https://reference.aspose.com/cells/java/com.aspose.cells/Style) Objekt und[**StyleFlag**](https://reference.aspose.com/cells/java/com.aspose.cells/StyleFlag) struct, die alle Member enthält, die sich auf die angewendete Formatierung beziehen.

Das folgende Beispiel zeigt, wie eine Zeile im Arbeitsblatt geschützt wird. Es entsperrt zuerst alle Zellen im Arbeitsblatt und sperrt dann die erste Zeile darin. Schließlich schützt es das Arbeitsblatt. Eine Zeile/Spalte hat einen Stil API, der außerdem eine setCellLocked-Methode enthält. Sie können die Zeile / Spalte mit der StyleFlag-Struktur sperren oder entsperren.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-ProtectRowWorksheet-ProtectRowWorksheet.java" >}}

### **Schützen Sie eine Spalte im Arbeitsblatt**

 Aspose.Cells ermöglicht es Ihnen, jede Spalte im Arbeitsblatt einfach zu sperren. Hier können wir Gebrauch machen[**applyStyle()**](https://reference.aspose.com/cells/java/com.aspose.cells/column#applyStyle(com.aspose.cells.Style,%20com.aspose.cells.StyleFlag) ) Methode von[**Spalte**](https://reference.aspose.com/cells/java/com.aspose.cells/Column) -Klasse, um Style auf eine bestimmte Spalte im Arbeitsblatt anzuwenden. Diese Methode akzeptiert zwei Argumente: a[**Stil**](https://reference.aspose.com/cells/java/com.aspose.cells/Style) Objekt und[**StyleFlag**](https://reference.aspose.com/cells/java/com.aspose.cells/StyleFlag) struct, die alle Member enthält, die sich auf die angewendete Formatierung beziehen.

Das folgende Beispiel zeigt, wie eine Spalte im Arbeitsblatt geschützt wird. Es entsperrt zuerst alle Zellen im Arbeitsblatt und sperrt dann die erste Spalte darin. Schließlich schützt es das Arbeitsblatt. Eine Zeile/Spalte hat einen Stil API, der außerdem eine festgelegte Locked-Methode enthält. Sie können die Zeile / Spalte mit der StyleFlag-Struktur sperren oder entsperren.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-ProtectColumnWorksheet-ProtectColumnWorksheet.java" >}}

## **Heben Sie den Schutz eines Arbeitsblatts auf**

[Arbeitsblätter schützen](/cells/de/java/protect-and-unprotect-worksheet/#protect-worksheets) und[Erweiterte Schutzeinstellungen seit Excel XP](/cells/de/java/protect-and-unprotect-worksheet/#advanced-protection-settings-since-excel-xp) diskutierten verschiedene Ansätze zum Schutz von Arbeitsblättern. Was ist, wenn ein Entwickler zur Laufzeit den Schutz von einem geschützten Arbeitsblatt entfernen muss, damit einige Änderungen an der Datei vorgenommen werden können? Das geht ganz einfach mit Aspose.Cells.

### **Mit Microsoft Excel**

So entfernen Sie den Schutz von einem Arbeitsblatt:

 Von dem**Werkzeug** Menü, auswählen**Schutz** gefolgt von**Blattschutz aufheben**.

**Blattschutz aufheben auswählen** 

![todo: Bild_alt_Text](protect-and-unprotect-worksheet_4.png)

Der Schutz wird entfernt, es sei denn, das Arbeitsblatt ist passwortgeschützt. In diesem Fall fragt ein Dialog nach dem Passwort.

**Geben Sie ein Passwort ein, um den Schutz des Arbeitsblatts aufzuheben** 

![todo: Bild_alt_Text](protect-and-unprotect-worksheet_5.png)

### **Mit Aspose.Cells**

 Der Schutz eines Arbeitsblatts kann durch Aufrufen von aufgehoben werden[**Arbeitsblatt**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) Klasse'[**Schutz aufheben**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#unprotect() ) Methode. Das[**Schutz aufheben**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#unprotect())-Methode kann auf zwei Arten verwendet werden, die unten beschrieben werden.

### **Aufheben des Schutzes eines einfach geschützten Arbeitsblatts**

Ein einfach geschütztes Arbeitsblatt ist eines, das nicht mit einem Passwort geschützt ist. Der Schutz solcher Arbeitsblätter kann aufgehoben werden, indem die unprotect-Methode aufgerufen wird, ohne einen Parameter zu übergeben.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-UnprotectingSimplyProtectedWorksheet-UnprotectingSimplyProtectedWorksheet.java" >}}

### **Schutz eines passwortgeschützten Arbeitsblatts aufheben**

Ein passwortgeschütztes Arbeitsblatt ist ein Arbeitsblatt, das mit einem Passwort geschützt ist. Der Schutz solcher Arbeitsblätter kann aufgehoben werden, indem eine überladene Version der Unprotect-Methode aufgerufen wird, die das Kennwort als Parameter akzeptiert.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-UnprotectProtectSheet-UnprotectProtectSheet.java" >}}

## **Erweiterte Schutzeinstellungen seit Excel XP**

[Arbeitsblätter schützen](/cells/de/java/protect-and-unprotect-worksheet/#protect-worksheets) besprochen, ein Arbeitsblatt in Microsoft Excel 97 und 2000 zu schützen. Aber seit der Veröffentlichung von Excel 2002 oder XP hat Microsoft viele erweiterte Schutzeinstellungen hinzugefügt. Diese Schutzeinstellungen beschränken oder erlauben Benutzern Folgendes:

- Zeilen oder Spalten löschen.
- Bearbeiten Sie Inhalte, Objekte oder Szenarien.
- Zellen, Zeilen oder Spalten formatieren.
- Zeilen, Spalten oder Hyperlinks einfügen.
- Wählen Sie gesperrte oder entsperrte Zellen aus.
- Verwenden Sie Pivot-Tabellen und vieles mehr.

Aspose.Cells unterstützt alle erweiterten Schutzeinstellungen, die von Excel XP und späteren Versionen angeboten werden.

### **Erweiterte Schutzeinstellungen mit Excel XP und späteren Versionen**

So zeigen Sie die in Excel XP verfügbaren Schutzeinstellungen an:

1.  Von dem**Werkzeug** Menü, auswählen**Schutz** gefolgt von**Schutzblatt**.
 Ein Dialogfeld wird angezeigt.

   **Dialog zum Anzeigen von Schutzoptionen in Excel XP**

![todo: Bild_alt_Text](protect-and-unprotect-worksheet_6.png)

1. Erlauben oder beschränken Sie Arbeitsblattfunktionen oder wenden Sie ein Passwort an.

### **Erweiterte Schutzeinstellungen mit Aspose.Cells**

Aspose.Cells unterstützt alle erweiterten Schutzeinstellungen.

 Aspose.Cells bietet eine Klasse,[**Arbeitsmappe**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) , die eine Microsoft Excel-Datei darstellt. Die Workbook-Klasse enthält eine WorksheetCollection-Auflistung, die den Zugriff auf jedes Arbeitsblatt in der Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch dargestellt[**Arbeitsblatt**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) Klasse.

 Die Worksheet-Klasse stellt die Protection-Eigenschaft bereit, die zum Anwenden dieser erweiterten Schutzeinstellungen verwendet wird. Das Schutzgut ist in der Tat ein Objekt des[**Schutz**](https://reference.aspose.com/cells/java/com.aspose.cells/protection) Klasse, die mehrere boolesche Eigenschaften zum Deaktivieren oder Aktivieren von Einschränkungen kapselt.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-AdvancedProtectionSettingsUsingAsposeCells-AdvancedProtectionSettingsUsingAsposeCells.java" >}}

Unten ist eine kleine Beispielanwendung. Es öffnet eine Excel-Datei und verwendet die meisten erweiterten Schutzeinstellungen, die von Excel XP und späteren Versionen unterstützt werden.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-AdvancedProtection-AdvancedProtection.java" >}}

{{% alert color="primary" %}}

Speichern Sie die Datei im EXCEL97TO2003- oder XLSX-Format, da diese erweiterten Schutzeinstellungen nur von MS Excel XP und späteren Versionen unterstützt werden.

{{% /alert %}}

### **Cell Sperrproblem**

Wenn Sie verhindern möchten, dass Benutzer Zellen bearbeiten, müssen die Zellen gesperrt werden, bevor Schutzeinstellungen angewendet werden. Andernfalls können die Zellen bearbeitet werden, auch wenn das Arbeitsblatt geschützt ist. In Microsoft Excel XP können Zellen über den folgenden Dialog gesperrt werden:

**Dialog zum Sperren von Zellen in Excel XP** 

![todo: Bild_alt_Text](protect-and-unprotect-worksheet_7.png)

Es ist auch möglich, Zellen unter der Nummer Aspose.Cells API zu sperren. Jede Zelle hat einen Stil API, der außerdem eine setLocked-Methode enthält. Verwenden Sie es, um Zellen zu sperren oder zu entsperren.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-LockCell-LockCell.java" >}}
