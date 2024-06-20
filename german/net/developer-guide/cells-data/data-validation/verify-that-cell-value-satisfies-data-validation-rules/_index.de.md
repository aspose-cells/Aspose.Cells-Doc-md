---
title: Überprüfen Sie, ob der Zellenwert den Datenvalidierungsregeln entspricht
type: docs
weight: 210
url: /de/net/verify-that-cell-value-satisfies-data-validation-rules/
description: Erfahren Sie, wie Sie mit der API Aspose.Cells for .NET überprüfen können, ob der Zellenwert den Datenvalidierungsregeln entspricht.
keywords: Zellenvalidierungswert erhalten, Zellenvalidierungswert erhalten, Überprüfen Sie, ob ein Wert den auf die Zelle angewendeten Datenvalidierungsregeln entspricht
---

{{% alert color="primary" %}} 

Microsoft Excel ermöglicht es Benutzern, Datenvalidierungsregeln für Zellen hinzuzufügen. Zum Beispiel gibt eine Dezimalvalidierung an, dass nur Zahlen zwischen 10 und 20 eingegeben werden können. Wenn ein Benutzer eine andere Zahl eingibt, zeigt Microsoft Excel eine Fehlermeldung an und fordert ihn auf, eine Zahl im richtigen Bereich einzugeben. Wenn Sie beispielsweise eine Zahl, sagen wir 3, in die Zelle kopieren und einfügen, führt Excel keine Validierungsprüfung durch oder zeigt eine Fehlermeldung an.

Manchmal ist es erforderlich, programmgesteuert zu überprüfen, ob ein Wert den auf die Zelle angewendeten Datenvalidierungsregeln entspricht. Im obigen Fall sollte der Eintrag beispielsweise fehlschlagen.

{{% /alert %}} 
## **Einführung**
Aspose.Cells bietet die [Cell.GetValidationValue()](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getvalidationvalue) Methode, um Zellenwerte programmgesteuert zu validieren. Wenn der Wert in einer Zelle den auf diese Zelle angewendeten Datenvalidierungsregeln nicht entspricht, gibt sie **False** zurück, ansonsten **True**.

Der folgende Beispielcode veranschaulicht, wie die Methode [Cell.GetValidationValue()](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getvalidationvalue) funktioniert. Zuerst gibt es den Wert 3 in C1 ein. Da dies den Datenvalidierungsregeln nicht entspricht, gibt die Methode [Cell.GetValidationValue()](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getvalidationvalue) **False** zurück. Dann gibt es den Wert 15 in C1 ein. Da dieser Wert den Datenvalidierungsregeln entspricht, gibt die Methode [Cell.GetValidationValue()](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getvalidationvalue) **True** zurück. Ebenso gibt sie für den Wert 30 **False** zurück.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-DataValidationRules-1.cs" >}}
### **Ergebnis**
{{< highlight java >}}

 Is 3 a Valid Value for this Cell: False

Is 15 a Valid Value for this Cell: True

Is 30 a Valid Value for this Cell: False

{{< /highlight >}}
