---
title: Stellen Sie sicher, dass der Wert Cell den Datenvalidierungsregeln entspricht
type: docs
weight: 210
url: /de/net/verify-that-cell-value-satisfies-data-validation-rules/
description: Erfahren Sie, wie Sie mithilfe von Aspose.Cells for .NET API überprüfen können, ob der Wert Cell den Datenvalidierungsregeln entspricht.
keywords: Get Cell Validation Value, Obtain Cell Validation Value, Verify whether a value satisfies the data validation rules applied to the cell
---
{{% alert color="primary" %}} 

Microsoft Excel ermöglicht Benutzern das Hinzufügen von Datenvalidierungsregeln zu Zellen. Beispielsweise gibt eine Dezimalvalidierung an, dass nur Zahlen zwischen 10 und 20 eingegeben werden können. Wenn ein Benutzer eine andere Nummer eingibt. Microsoft Excel zeigt eine Fehlermeldung an und fordert Sie auf, eine Zahl im richtigen Bereich einzugeben. Wenn Sie eine Zahl, beispielsweise 3, kopieren und in die Zelle einfügen, führt Excel keine Validierungsprüfung durch und zeigt keine Fehlermeldung an.

Manchmal muss überprüft werden, ob ein Wert die programmgesteuert auf die Zelle angewendeten Datenvalidierungsregeln erfüllt. Im obigen Fall sollte beispielsweise die Eingabe fehlschlagen.

{{% /alert %}} 
##  **Einführung**
 Aspose.Cells bietet die[Cell.GetValidationValue()](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getvalidationvalue)Methode zur programmgesteuerten Validierung von Zellwerten. Wenn der Wert in einer Zelle die auf diese Zelle angewendete Datenvalidierungsregel nicht erfüllt, wird *False** zurückgegeben, andernfalls *True**.

 Der folgende Beispielcode veranschaulicht, wie die[Cell.GetValidationValue()](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getvalidationvalue) Methode funktioniert. Zunächst trägt es den Wert 3 in C1 ein. Da dies die Datenvalidierungsregel nicht erfüllt, wird die[Cell.GetValidationValue()](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getvalidationvalue) Methode gibt zurück**FALSCH**. Anschließend trägt es den Wert 15 in C1 ein. Da dieser Wert die Datenvalidierungsregel erfüllt, gibt die Methode [Cell.GetValidationValue()](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getvalidationvalue) **True** zurück. Ebenso wird **False zurückgegeben** für den Wert 30.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-DataValidationRules-1.cs" >}}
###  **Ausgabe**
{{< highlight "java" >}}

 Is 3 a Valid Value for this Cell: False

Is 15 a Valid Value for this Cell: True

Is 30 a Valid Value for this Cell: False

{{< /highlight >}}
