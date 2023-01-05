---
title: Heben Sie den Schutz eines Arbeitsblatts auf
type: docs
weight: 20
url: /de/net/unprotect-a-worksheet/
---
{{% alert color="primary" %}}

Wenn ein Entwickler zur Laufzeit den Schutz von einem geschützten Arbeitsblatt entfernen muss, damit einige Änderungen an der Datei vorgenommen werden können? Das geht ganz einfach mit Aspose.Cells.

{{% /alert %}}

## **Heben Sie den Schutz eines Arbeitsblatts auf**

### **Mit Microsoft Excel**

So entfernen Sie den Schutz von einem Arbeitsblatt:

 Von dem**Werkzeug** Menü, auswählen**Schutz** gefolgt von**Blattschutz aufheben**. Der Schutz wird entfernt, es sei denn, das Arbeitsblatt ist passwortgeschützt. In diesem Fall fragt ein Dialog nach dem Passwort. Geben Sie das Passwort ein und das Arbeitsblatt ist dann ungeschützt.

### **Aufheben des Schutzes eines einfach geschützten Arbeitsblatts mit Aspose.Cells**

 Der Schutz eines Arbeitsblatts kann durch Aufrufen von aufgehoben werden[**Arbeitsblatt**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) Klasse'[**Schutz aufheben**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/unprotect/index)Methode.
 Ein einfach geschütztes Arbeitsblatt ist eines, das nicht mit einem Passwort geschützt ist. Der Schutz solcher Arbeitsblätter kann durch Aufrufen von aufgehoben werden[**Schutz aufheben**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/unprotect/index)Methode ohne Übergabe eines Parameters.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Security-Unprotect-UnprotectingSimplyProtectedWorksheet-1.cs" >}}

### **Aufheben des Schutzes eines passwortgeschützten Arbeitsblatts mit Aspose.Cells**

Ein passwortgeschütztes Arbeitsblatt ist ein Arbeitsblatt, das mit einem Passwort geschützt ist. Der Schutz solcher Arbeitsblätter kann aufgehoben werden, indem eine überladene Version von aufgerufen wird[**Schutz aufheben**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/unprotect/methods/1)Methode, die das Passwort als Parameter akzeptiert.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Security-Unprotect-UnprotectingPasswordProtectedWorksheet-1.cs" >}}
