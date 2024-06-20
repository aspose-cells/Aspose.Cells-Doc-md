---
title: Arbeitsblätter schützen
type: docs
weight: 10
url: /de/net/protecting-worksheets/
---

{{% alert color="primary" %}}

Wenn ein Arbeitsblatt geschützt ist, sind die Aktionen, die ein Benutzer durchführen kann, eingeschränkt. Zum Beispiel kann er keine Daten eingeben, Zeilen oder Spalten einfügen oder löschen usw.

{{% /alert %}}

## **Arbeitsblätter schützen**

### **Einführung**

Die allgemeinen Schutzeinstellungen in Microsoft Excel sind:

- Inhalt
- Objekte
- Szenarien

Geschützte Arbeitsblätter verbergen oder schützen keine sensiblen Daten, daher unterscheidet es sich von der Datei-Verschlüsselung. Allgemein ist der Arbeitsblattschutz für Präsentationszwecke geeignet. Er verhindert, dass der Endbenutzer Daten, Inhalt und Formatierung im Arbeitsblatt ändert.

### **Ein Arbeitsblatt schützen**

Aspose.Cells bietet eine Klasse, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook), die eine Microsoft Excel-Datei repräsentiert. Die Klasse [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) enthält eine [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)-Sammlung, die den Zugriff auf jedes Arbeitsblatt in einer Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch die Klasse [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) repräsentiert.

Die Klasse [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) bietet die Methode [**Protect**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/protect/index), die zum Anwenden des Schutzes auf das Arbeitsblatt verwendet wird. [**Protect**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/protect/methods/1) Methode akzeptiert die folgenden Parameter:

- Schutztyp, der Typ des Schutzes, der auf das Arbeitsblatt angewendet werden soll. Der Schutztyp wird mithilfe der [**ProtectionType**](https://reference.aspose.com/cells/net/aspose.cells/protectiontype)-Enumeration angewendet.
- Neues Passwort, das neue Passwort, das zum Schutz des Arbeitsblatts verwendet wird.
- Altes Kennwort, das alte Kennwort, wenn das Arbeitsblatt bereits passwortgeschützt ist. Wenn das Arbeitsblatt noch nicht geschützt ist, dann einfach null übergeben.

Die [**ProtectionType**](https://reference.aspose.com/cells/net/aspose.cells/protectiontype)-Aufzählung enthält die folgenden vordefinierten Schutztypen:

|**Schutztypen**|**Beschreibung**|
| :- | :- |
|All|Der Benutzer kann nichts auf diesem Arbeitsblatt ändern|
|Contents|Der Benutzer kann keine Daten in dieses Arbeitsblatt eingeben|
|Objects|Der Benutzer kann Zeichenobjekte nicht ändern|
|Scenarios|Der Benutzer kann gespeicherte Szenarien nicht ändern|
|Structure|Der Benutzer kann die Struktur nicht ändern|
|Windows|Der Schutz wird auf Fenster angewendet|
|None|Es ist kein Schutz angewendet|

Das folgende Beispiel zeigt, wie ein Arbeitsblatt mit einem Passwort geschützt wird.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Security-Protecting-ProtectingWorksheet-1.cs" >}}

Nachdem der obige Code zum Schutz des Arbeitsblatts verwendet wurde, können Sie den Schutz auf dem Arbeitsblatt überprüfen, indem Sie es öffnen. Sobald Sie die Datei öffnen und versuchen, einige Daten in das Arbeitsblatt einzufügen, sehen Sie den folgenden Dialog:

|**Ein Dialog, der darauf hinweist, dass ein Benutzer das Arbeitsblatt nicht ändern kann**|
| :- |
|![todo:image_alt_text](protecting-worksheets_1.png)|

Um am Arbeitsblatt zu arbeiten, heben Sie den Schutz des Arbeitsblatts auf, indem Sie im **Werkzeuge**-Menüpunkt **Schutz** und dann **Arbeitsblatt entsperren** auswählen.

Nachdem Sie den Menüpunkt Arbeitsblatt entsperren ausgewählt haben, öffnet sich ein Dialog, der Sie auffordert, das Passwort einzugeben, damit Sie am Arbeitsblatt arbeiten können, wie unten gezeigt:

|![todo:image_alt_text](protecting-worksheets_2.png)|

### **Einige Zellen im Arbeitsblatt mit Microsoft Excel schützen**

Es kann bestimmte Szenarien geben, in denen Sie nur einige Zellen im Arbeitsblatt sperren müssen. Wenn Sie bestimmte Zellen im Arbeitsblatt sperren möchten, müssen Sie alle anderen Zellen im Arbeitsblatt entsperren. Alle Zellen in einem Arbeitsblatt sind bereits für das Sperren initialisiert, dies können Sie überprüfen, indem Sie eine Excel-Datei in MS Excel öffnen und auf **Format | Zellen...** klicken, um das Dialogfeld **Zellen formatieren** anzuzeigen. Klicken Sie dann auf die Registerkarte **Schutz** und prüfen Sie, ob ein Kontrollkästchen mit der Bezeichnung "Gesperrt" standardmäßig aktiviert ist.

Die folgenden Punkte beschreiben, wie Sie mit MS Excel einige Zellen sperren können. Diese Methode gilt für Microsoft Office Excel 97, 2000, 2002, 2003 und neuere Versionen.

1. Wählen Sie das gesamte Arbeitsblatt aus, indem Sie auf die Schaltfläche **Alles auswählen** klicken (das graue Rechteck direkt über der Zeilennummer von Zeile 1 und links von Spaltenbuchstabe A).
1. Klicken Sie auf **Zellen** im **Format**-Menü, klicken Sie auf die Registerkarte **Schutz** und deaktivieren Sie das Kontrollkästchen **Gesperrt**.
   Dies entsperrt alle Zellen im Arbeitsblatt
   Wenn der Befehl **Zellen** nicht verfügbar ist, können Teile des Arbeitsblatts bereits gesperrt sein. Klicken Sie im **Menü Extras** auf **Schutz**, und klicken Sie dann auf **Arbeitsblatt schützen**.
1. Wählen Sie nur die Zellen aus, die Sie sperren möchten, und wiederholen Sie Schritt 2, aber wählen Sie dieses Mal das Kontrollkästchen **Gesperrt**.
1. Im **Menü Extras** zeigen Sie auf **Schutz**, klicken Sie auf **Arbeitsblatt schützen** und dann auf **OK**.
1. Im Dialogfeld **Arbeitsblatt schützen** haben Sie die Möglichkeit, ein Passwort zu spezifizieren und die Elemente auszuwählen, die Benutzer ändern dürfen.

### **Schützen Sie ein paar Zellen im Arbeitsblatt mit Aspose Cells**

In dieser Methode verwenden wir nur die Aspose.Cells-API, um die Aufgabe zu erledigen.

Beispiel: Das folgende Beispiel zeigt, wie man ein paar Zellen im Arbeitsblatt schützt. Es entsperrt zunächst alle Zellen im Arbeitsblatt und sperrt dann 3 Zellen (A1, B1, C1). Schließlich wird das Arbeitsblatt geschützt. Das [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style)-Objekt enthält eine boolesche Eigenschaft, [**IsLocked**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/islocked). Sie können die [**IsLocked**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/islocked)-Eigenschaft auf true oder false setzen und die Methode *Column/Row.ApplyStyle()* verwenden, um die Zeile/Spalte mit Ihren gewünschten Attributen zu sperren oder zu entsperren.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Security-Protecting-ProtectingSpecificCellsinaWorksheet-1.cs" >}}

### **Schützen Sie eine Zeile im Arbeitsblatt**

Mit Aspose.Cells können Sie leicht eine beliebige Zeile im Arbeitsblatt sperren. Hier können wir die Methode [**ApplyStyle()**](https://reference.aspose.com/cells/net/aspose.cells/row/methods/applystyle) der Klasse [**Aspose.Cells.Row**](https://reference.aspose.com/cells/net/aspose.cells/row) verwenden, um [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) auf eine bestimmte Zeile im Arbeitsblatt anzuwenden. Diese Methode benötigt zwei Argumente: ein [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style)-Objekt und ein [**StyleFlag**](https://reference.aspose.com/cells/net/aspose.cells/styleflag)-Objekt, das alle Elemente im Zusammenhang mit der angewandten Formatierung enthält.

Das folgende Beispiel zeigt, wie man eine Zeile im Arbeitsblatt schützt. Es entsperrt zunächst alle Zellen im Arbeitsblatt und sperrt dann die erste Zeile. Schließlich wird das Arbeitsblatt geschützt. Das [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style)-Objekt enthält eine boolesche Eigenschaft, [**IsLocked**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/islocked). Sie können die [**IsLocked**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/islocked)-Eigenschaft auf true oder false setzen, um die Zeile/Spalte mit dem [**StyleFlag**](https://reference.aspose.com/cells/net/aspose.cells/styleflag)-Objekt zu sperren oder zu entsperren.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Security-Protecting-ProtectingSpecificRowInWorksheet-1.cs" >}}

### **Schützen Sie eine Spalte im Arbeitsblatt**

Mit Aspose.Cells können Sie leicht eine beliebige Spalte im Arbeitsblatt sperren. Hier können wir die Methode [**ApplyStyle()**](https://reference.aspose.com/cells/net/aspose.cells/column/methods/applystyle) der Klasse [**Aspose.Cells.Column**](https://reference.aspose.com/cells/net/aspose.cells/column) verwenden, um [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) auf eine bestimmte Spalte im Arbeitsblatt anzuwenden. Diese Methode benötigt zwei Argumente: ein [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style)-Objekt und ein [**StyleFlag**](https://reference.aspose.com/cells/net/aspose.cells/styleflag)-Objekt, das alle Elemente im Zusammenhang mit der angewandten Formatierung enthält.

Das folgende Beispiel zeigt, wie man eine Spalte im Arbeitsblatt schützt. Es entsperrt zunächst alle Zellen im Arbeitsblatt und sperrt dann die erste Spalte. Schließlich wird das Arbeitsblatt geschützt. Das [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style)-Objekt enthält eine boolesche Eigenschaft, [**IsLocked**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/islocked). Sie können die [**IsLocked**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/islocked)-Eigenschaft auf true oder false setzen, um die Zeile/Spalte mit dem [**StyleFlag**](https://reference.aspose.com/cells/net/aspose.cells/styleflag)-Objekt zu sperren oder zu entsperren.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Security-Protecting-ProtectColumnWorksheet-1.cs" >}}

### **Benutzern das Bearbeiten von Bereichen ermöglichen**

Das folgende Beispiel zeigt, wie man Benutzern das Bearbeiten eines Bereichs in einem geschützten Arbeitsblatt erlaubt.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Security-Protecting-EditRangesWorksheet-1.cs" >}}
