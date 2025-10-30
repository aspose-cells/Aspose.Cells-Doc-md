---
title: Überprüfen, ob der Zellwert die Datenvalidierungsregeln erfüllt, mit Golang via C++
linktitle: Überprüfen Sie, ob der Zellenwert den Datenvalidierungsregeln entspricht
type: docs
weight: 210
url: /de/go-cpp/verify-that-cell-value-satisfies-data-validation-rules/
description: Erfahren Sie, wie Sie mit der API Aspose.Cells for C++ überprüfen, ob der Zellwert die Datenvalidierungsregeln erfüllt.
keywords: Zellenvalidierungswert erhalten, Zellenvalidierungswert erhalten, Überprüfen Sie, ob ein Wert den auf die Zelle angewendeten Datenvalidierungsregeln entspricht
---

{{% alert color="primary" %}} 

Microsoft Excel erlaubt es Benutzern, Datenvalidierungsregeln zu Zellen hinzuzufügen. Zum Beispiel gibt eine Dezimalvalidierung an, dass nur Zahlen zwischen 10 und 20 eingegeben werden können. Wenn ein Benutzer eine andere Zahl eingibt, zeigt Excel eine Fehlermeldung an und fordert ihn auf, eine Zahl im richtigen Bereich einzugeben. Wenn Sie eine Zahl, z.B. 3, in die Zelle kopieren und einfügen, überprüft Excel die Validierung nicht und zeigt keine Fehlermeldung an.

Manchmal ist es erforderlich, programmgesteuert zu überprüfen, ob ein Wert den auf die Zelle angewendeten Datenvalidierungsregeln entspricht. Im obigen Fall sollte der Eintrag beispielsweise fehlschlagen.

{{% /alert %}} 

## **Einführung**
Aspose.Cells bietet die Methode [Cell.GetValidationValue()](https://reference.aspose.com/cells/go-cpp/cell/getvalidationvalue/), um Zellwerte programmatisch zu validieren. Wenn der Wert in einer Zelle die angewandte Datenvalidierungsregel nicht erfüllt, gibt sie **False** zurück, sonst **True**.

Das folgende Beispiel zeigt, wie die Methode [Cell.GetValidationValue()](https://reference.aspose.com/cells/go-cpp/cell/getvalidationvalue/) funktioniert. Zuerst wird der Wert 3 in C1 eingegeben. Da dieser die Datenvalidierungsregel nicht erfüllt, gibt die Methode **False** zurück. Dann wird der Wert 15 in C1 eingegeben. Da dieser die Datenvalidierungsregel erfüllt, gibt die Methode **True** zurück. Ähnlich ist es bei Wert 30, die **False** zurückgibt.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-VerifyThatCellValueSatisfiesDataValidationRules.go" >}}
### **Ergebnis**
{{< highlight java >}}

Is 3 a Valid Value for this Cell: False

Is 15 a Valid Value for this Cell: True

Is 30 a Valid Value for this Cell: False

{{< /highlight >}}
