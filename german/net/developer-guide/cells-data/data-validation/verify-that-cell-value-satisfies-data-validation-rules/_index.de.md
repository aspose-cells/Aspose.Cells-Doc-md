---
title: Stellen Sie sicher, dass der Wert Cell die Datenvalidierungsregeln erfüllt
type: docs
weight: 210
url: /de/net/verify-that-cell-value-satisfies-data-validation-rules/
---
{{% alert color="primary" %}} 

Microsoft Excel ermöglicht es Benutzern, Datenvalidierungsregeln zu Zellen hinzuzufügen. Beispielsweise gibt eine Dezimalvalidierung an, dass nur Zahlen zwischen 10 und 20 eingegeben werden können. Wenn ein Benutzer eine andere Nummer eingibt. Microsoft Excel zeigt eine Fehlermeldung an und fordert sie auf, eine Zahl im richtigen Bereich einzugeben. Wenn Sie eine Zahl, z. B. 3, kopieren und in die Zelle einfügen, führt Excel keine Validierungsprüfung durch und zeigt keine Fehlermeldung an.

Manchmal muss überprüft werden, ob ein Wert die Datenüberprüfungsregeln erfüllt, die programmgesteuert auf die Zelle angewendet werden. Im obigen Fall sollte beispielsweise der Eintrag fehlschlagen.

{{% /alert %}} 
## **Einführung**
 Aspose.Cells bietet die[Cell.GetValidationValue()](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getvalidationvalue) Methode zum programmgesteuerten Validieren von Zellwerten. Wenn der Wert in einer Zelle die auf diese Zelle angewendete Datenvalidierungsregel nicht erfüllt, wird er zurückgegeben**FALSCH** , anders**Wahr**.

 Der folgende Beispielcode veranschaulicht, wie die[Cell.GetValidationValue()](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getvalidationvalue) Methode funktioniert. Zuerst trägt er den Wert 3 in C1 ein. Da dies die Datenvalidierungsregel nicht erfüllt, wird die[Cell.GetValidationValue()](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getvalidationvalue) Methode zurück**FALSCH** . Dann trägt er den Wert 15 in C1 ein. Da dieser Wert die Datenvalidierungsregel erfüllt, wird die[Cell.GetValidationValue()](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getvalidationvalue) Methode zurück**Wahr** . Ebenso kehrt es zurück**FALSCH** für Wert 30.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-DataValidationRules-1.cs" >}}
### **Ausgabe**
{{< highlight "java" >}}

 Is 3 a Valid Value for this Cell: False

Is 15 a Valid Value for this Cell: True

Is 30 a Valid Value for this Cell: False

{{< /highlight >}}
