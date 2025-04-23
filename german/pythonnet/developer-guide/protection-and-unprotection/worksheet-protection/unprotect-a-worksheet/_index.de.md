---
title: Arbeitsblatt entsperren
type: docs
weight: 20
url: /de/python-net/unprotect-a-worksheet/
---

{{% alert color="primary" %}}

Wenn ein Entwickler die Schutzfunktion eines geschützten Arbeitsblatts zur Laufzeit entfernen muss, um Änderungen an der Datei vorzunehmen? Dies kann leicht mit Aspose.Cells für Python via .NET gemacht werden.

{{% /alert %}}

## **Arbeitsblatt entsperren**

### **Verwendung von Microsoft Excel**

Um den Schutz von einem Arbeitsblatt zu entfernen:

Wählen Sie im **Tools**-Menü **Schutz** gefolgt von **Arbeitsblatt entsperren**. Der Schutz wird entfernt, es sei denn, das Arbeitsblatt ist passwortgeschützt. In diesem Fall wird ein Dialogfeld zur Eingabe des Passworts angezeigt. Geben Sie das Passwort ein und das Arbeitsblatt wird dann nicht geschützt sein.

### **Entsperren eines einfach geschützten Arbeitsblatts mit Aspose.Cells für Python via .NET**

Ein Arbeitsblatt kann entsperrt werden, indem die Methode [**unprotect**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/unprotect) der Klasse [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) aufgerufen wird.
Ein einfach geschütztes Arbeitsblatt ist ein Arbeitsblatt, das nicht mit einem Passwort geschützt ist. Solche Arbeitsblätter können entsperrt werden, indem die Methode [**unprotect**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/unprotect) aufgerufen wird, ohne einen Parameter zu übergeben.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-UnprotectingSimplyProtectedWorksheet-1.py" >}}

### **Entsperren eines passwortgeschützten Arbeitsblatts mit Aspose.Cells für Python via .NET**

Ein mit einem Passwort geschütztes Arbeitsblatt ist ein Arbeitsblatt, das mit einem Passwort geschützt ist. Solche Arbeitsblätter können entsperrt werden, indem eine überladene Version der Methode [**unprotect**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/unprotect/) aufgerufen wird, die das Passwort als Parameter akzeptiert.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-UnprotectingPasswordProtectedWorksheet-1.py" >}}

