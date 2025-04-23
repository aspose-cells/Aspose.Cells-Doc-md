---
title: Arbeitsblatt entsperren
type: docs
weight: 20
url: /de/net/unprotect-a-worksheet/
---

{{% alert color="primary" %}}

Wenn ein Entwickler den Schutz von einem geschützten Arbeitsblatt zur Laufzeit entfernen muss, damit einige Änderungen an der Datei vorgenommen werden können? Dies kann mit Aspose.Cells einfach gemacht werden.

{{% /alert %}}

## **Arbeitsblatt entsperren**

### **Verwendung von Microsoft Excel**

Um den Schutz von einem Arbeitsblatt zu entfernen:

Wählen Sie im **Tools**-Menü **Schutz** gefolgt von **Arbeitsblatt entsperren**. Der Schutz wird entfernt, es sei denn, das Arbeitsblatt ist passwortgeschützt. In diesem Fall wird ein Dialogfeld zur Eingabe des Passworts angezeigt. Geben Sie das Passwort ein und das Arbeitsblatt wird dann nicht geschützt sein.

### **Entsperren eines einfach geschützten Arbeitsblatts mit Aspose.Cells**

Ein Arbeitsblatt kann entsperrt werden, indem die Methode [**Unprotect**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/unprotect/index) der Klasse [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) aufgerufen wird.
Ein einfach geschütztes Arbeitsblatt ist ein Arbeitsblatt, das nicht mit einem Passwort geschützt ist. Solche Arbeitsblätter können entsperrt werden, indem die Methode [**Unprotect**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/unprotect/index) aufgerufen wird, ohne einen Parameter zu übergeben.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Security-Unprotect-UnprotectingSimplyProtectedWorksheet-1.cs" >}}

### **Entsperren eines passwortgeschützten Arbeitsblatts mit Aspose.Cells**

Ein mit einem Passwort geschütztes Arbeitsblatt ist ein Arbeitsblatt, das mit einem Passwort geschützt ist. Solche Arbeitsblätter können entsperrt werden, indem eine überladene Version der Methode [**Unprotect**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/unprotect/methods/1) aufgerufen wird, die das Passwort als Parameter akzeptiert.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Security-Unprotect-UnprotectingPasswordProtectedWorksheet-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
