---
title: Arbeitsblätter schützen
type: docs
weight: 10
url: /de/net/protecting-worksheets/
---
{{% alert color="primary" %}}

Wenn ein Arbeitsblatt geschützt ist, sind die Aktionen, die ein Benutzer ausführen kann, eingeschränkt. Sie können beispielsweise keine Daten eingeben, Zeilen oder Spalten einfügen oder löschen usw.

{{% /alert %}}

## **Arbeitsblätter schützen**

### **Einführung**

Die allgemeinen Schutzoptionen in Microsoft Excel sind:

- Inhalt
- Objekte
- Szenarien

Geschützte Arbeitsblätter verstecken oder schützen sensible Daten nicht und unterscheiden sich daher von der Dateiverschlüsselung. Im Allgemeinen ist der Arbeitsblattschutz für Präsentationszwecke geeignet. Es verhindert, dass der Endbenutzer Daten, Inhalt und Formatierung im Arbeitsblatt ändert.

### **Schützen Sie ein Arbeitsblatt**

 Aspose.Cells bietet eine Klasse,[**Arbeitsmappe**](https://reference.aspose.com/cells/net/aspose.cells/workbook) das stellt eine Microsoft Excel-Datei dar. Das[**Arbeitsmappe**](https://reference.aspose.com/cells/net/aspose.cells/workbook) Klasse enthält a[**Arbeitsblätter**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) Sammlung, die den Zugriff auf jedes Arbeitsblatt in einer Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch dargestellt[**Arbeitsblatt**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)Klasse.

 Das[**Arbeitsblatt**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) Klasse bietet die[**Beschützen**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/protect/index) Methode, die zum Anwenden des Schutzes auf das Arbeitsblatt verwendet wird.[**Beschützen**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/protect/methods/1) Die Methode akzeptiert die folgenden Parameter:

-  Schutztyp, der auf das Arbeitsblatt anzuwendende Schutztyp. Die Schutzart wird mit Hilfe der angewendet[**Schutztyp**](https://reference.aspose.com/cells/net/aspose.cells/protectiontype)Aufzählung.
- Neues Passwort, das neue Passwort, das zum Schutz des Arbeitsblatts verwendet wird.
- Altes Passwort, das alte Passwort, wenn das Arbeitsblatt bereits passwortgeschützt ist. Wenn das Arbeitsblatt noch nicht geschützt ist, übergeben Sie einfach null.

 Das[**Schutztyp**](https://reference.aspose.com/cells/net/aspose.cells/protectiontype)Enumeration enthält die folgenden vordefinierten Schutztypen:

|**Schutztypen**|**Beschreibung**|
|:- |:- |
|Alles|Der Benutzer kann auf diesem Arbeitsblatt nichts ändern|
|Inhalt|Der Benutzer kann keine Daten in dieses Arbeitsblatt eingeben|
|Objekte|Der Benutzer kann Zeichnungsobjekte nicht ändern|
|Szenarien|Der Benutzer kann gespeicherte Szenarien nicht ändern|
|Struktur|Der Benutzer kann die Struktur nicht ändern|
|Windows|Der Schutz wird auf Fenster angewendet|
|Keiner|Es wird kein Schutz angewendet|

Das folgende Beispiel zeigt, wie Sie ein Arbeitsblatt mit einem Kennwort schützen.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Security-Protecting-ProtectingWorksheet-1.cs" >}}

Nachdem der obige Code zum Schützen des Arbeitsblatts verwendet wurde, können Sie den Schutz auf dem Arbeitsblatt überprüfen, indem Sie es öffnen. Sobald Sie die Datei öffnen und versuchen, einige Daten zum Arbeitsblatt hinzuzufügen, wird das folgende Dialogfeld angezeigt:

|**Eine Dialogwarnung, dass ein Benutzer das Arbeitsblatt nicht ändern kann**|
|:- |
|![todo: Bild_alt_Text](protecting-worksheets_1.png)|

Um das Arbeitsblatt zu bearbeiten, heben Sie den Schutz des Arbeitsblatts auf, indem Sie das auswählen**Schutz** , dann**Blattschutz aufheben** von dem**Werkzeug** Menüpunkt.

Nachdem Sie den Menüpunkt „Blattschutz aufheben“ ausgewählt haben, wird ein Dialogfeld geöffnet, in dem Sie aufgefordert werden, das Kennwort einzugeben, damit Sie wie unten gezeigt an dem Arbeitsblatt arbeiten können:

|![todo: Bild_alt_Text](protecting-worksheets_2.png)|

### **Schützen Sie einige Cells im Arbeitsblatt mit Microsoft Excel**

 Es kann bestimmte Szenarien geben, in denen Sie nur einige Zellen im Arbeitsblatt sperren müssen. Wenn Sie bestimmte Zellen im Arbeitsblatt sperren möchten, müssen Sie alle anderen Zellen im Arbeitsblatt entsperren. Alle Zellen in einem Arbeitsblatt sind bereits zum Sperren initialisiert, Sie können dies überprüfen, indem Sie eine beliebige Excel-Datei in MS Excel öffnen und auf klicken**Format | Cells...** zeigen**Cells formatieren**Dialogfeld und klicken Sie dann auf**Schutz** und sehen Sie, dass ein Kontrollkästchen mit der Bezeichnung "Gesperrt" standardmäßig aktiviert ist.

Die folgenden Punkte beschreiben, wie Sie mit MS Excel einige Zellen sperren. Diese Methode gilt für Microsoft Office Excel 97, 2000, 2002, 2003 und höhere Versionen.

1.  Wählen Sie das gesamte Arbeitsblatt aus, indem Sie auf klicken**Wählen Sie Alle** Schaltfläche (das graue Rechteck direkt über der Zeilennummer für Zeile 1 und links von Spaltenbuchstabe A).
1.  Klicken**Cells** auf der**Format** Menü, klicken Sie auf die**Schutz** Registerkarte, und löschen Sie dann die**Gesperrt** Kontrollkästchen.
 Dadurch werden alle Zellen auf dem Arbeitsblatt entsperrt
 Wenn die**Cells** Befehl nicht verfügbar ist, können Teile des Arbeitsblatts bereits gesperrt sein. Auf der**Werkzeug** Menü, zeigen Sie auf**Schutz** , und klicken Sie dann auf**Blattschutz aufheben**.
1.  Wählen Sie nur die Zellen aus, die Sie sperren möchten, und wiederholen Sie Schritt 2, aber wählen Sie diesmal die aus**Gesperrt** Kontrollkästchen.
1.  Auf der**Werkzeug** Menü, zeigen Sie auf**Schutz** , klicken**Schutzblatt** und dann klicken**OK**.
1.  Im**Schutzblatt** Im Dialogfeld haben Sie die Möglichkeit, ein Kennwort anzugeben und die Elemente auszuwählen, die Benutzer ändern können sollen.

### **Schützen Sie einige Cells im Arbeitsblatt mit Aspose Cells**

Bei dieser Methode verwenden wir Aspose.Cells API nur, um die Aufgabe zu erledigen.

 Beispiel: Das folgende Beispiel zeigt, wie einige Zellen im Arbeitsblatt geschützt werden. Es entsperrt zuerst alle Zellen im Arbeitsblatt und sperrt dann 3 Zellen (A1, B1, C1) darin. Schließlich schützt es das Arbeitsblatt. Das[**Stil**](https://reference.aspose.com/cells/net/aspose.cells/style)Objekt enthält eine boolesche Eigenschaft,[**Ist gesperrt**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/islocked) . Sie können einstellen[**Ist gesperrt**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/islocked) Eigenschaft auf wahr oder falsch und anwenden*Spalte/Zeile.ApplyStyle()* Methode zum Sperren oder Entsperren der Zeile/Spalte mit Ihren gewünschten Attributen.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Security-Protecting-ProtectingSpecificCellsinaWorksheet-1.cs" >}}

### **Schützen Sie eine Zeile im Arbeitsblatt**

 Aspose.Cells ermöglicht es Ihnen, jede Zeile im Arbeitsblatt einfach zu sperren. Hier können wir Gebrauch machen[**ApplyStyle()**](https://reference.aspose.com/cells/net/aspose.cells/row/methods/applystyle) Methode von[**Aspose.Cells.Row**](https://reference.aspose.com/cells/net/aspose.cells/row) Klasse zu bewerben[**Stil**](https://reference.aspose.com/cells/net/aspose.cells/style) zu einer bestimmten Zeile im Arbeitsblatt. Diese Methode akzeptiert zwei Argumente: a[**Stil**](https://reference.aspose.com/cells/net/aspose.cells/style) Objekt und[**StyleFlag**](https://reference.aspose.com/cells/net/aspose.cells/styleflag) -Objekt, das alle Elemente enthält, die sich auf die angewendete Formatierung beziehen.

 Das folgende Beispiel zeigt, wie eine Zeile im Arbeitsblatt geschützt wird. Es entsperrt zuerst alle Zellen im Arbeitsblatt und sperrt dann die erste Zeile darin. Schließlich schützt es das Arbeitsblatt. Das[**Stil**](https://reference.aspose.com/cells/net/aspose.cells/style) Objekt enthält eine boolesche Eigenschaft,[**Ist gesperrt**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/islocked) . Sie können einstellen[**Ist gesperrt**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/islocked) -Eigenschaft auf „true“ oder „false“ setzen, um die Zeile/Spalte mithilfe von zu sperren oder zu entsperren[**StyleFlag**](https://reference.aspose.com/cells/net/aspose.cells/styleflag)Objekt.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Security-Protecting-ProtectingSpecificRowInWorksheet-1.cs" >}}

### **Schützen Sie eine Spalte im Arbeitsblatt**

 Aspose.Cells ermöglicht es Ihnen, jede Spalte im Arbeitsblatt einfach zu sperren. Hier können wir Gebrauch machen[**ApplyStyle()**](https://reference.aspose.com/cells/net/aspose.cells/column/methods/applystyle) Methode von[**Aspose.Cells.Column**](https://reference.aspose.com/cells/net/aspose.cells/column) Klasse zu bewerben[**Stil**](https://reference.aspose.com/cells/net/aspose.cells/style) zu einer bestimmten Spalte im Arbeitsblatt. Diese Methode akzeptiert zwei Argumente: a[**Stil**](https://reference.aspose.com/cells/net/aspose.cells/style) Objekt und[**StyleFlag**](https://reference.aspose.com/cells/net/aspose.cells/styleflag)-Objekt, das alle Elemente enthält, die sich auf die angewendete Formatierung beziehen.

Das folgende Beispiel zeigt, wie eine Spalte im Arbeitsblatt geschützt wird. Es entsperrt zuerst alle Zellen im Arbeitsblatt und sperrt dann die erste Spalte darin. Schließlich schützt es das Arbeitsblatt. Das[**Stil**](https://reference.aspose.com/cells/net/aspose.cells/style) Objekt enthält eine boolesche Eigenschaft,[**Ist gesperrt**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/islocked) . Sie können einstellen[**Ist gesperrt**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/islocked) -Eigenschaft auf „true“ oder „false“ setzen, um die Zeile/Spalte mithilfe von zu sperren oder zu entsperren[**StyleFlag**](https://reference.aspose.com/cells/net/aspose.cells/styleflag)Objekt.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Security-Protecting-ProtectColumnWorksheet-1.cs" >}}

### **Benutzern erlauben, Bereiche zu bearbeiten**

Das folgende Beispiel zeigt, wie Sie Benutzern erlauben, einen Bereich in einem geschützten Arbeitsblatt zu bearbeiten.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Security-Protecting-EditRangesWorksheet-1.cs" >}}
