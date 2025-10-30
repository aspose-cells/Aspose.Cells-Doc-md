---
title: Überprüfen Sie, ob der Zellenwert den Datenvalidierungsregeln entspricht
type: docs
weight: 210
url: /de/python-net/verify-that-cell-value-satisfies-data-validation-rules/
description: Erfahren Sie, wie Sie über die Aspose.Cells für Python via .NET API überprüfen, ob der Zellenwert den Datenvalidierungsregeln entspricht.
keywords: Python Excel Bibliothek, Python Zellenvalidierungswert abrufen, Python Zellenvalidierungswert erhalten, Python Überprüfen, ob ein Wert den auf die Zelle angewendeten Datenvalidierungsregeln entspricht.
---

{{% alert color="primary" %}} 

Microsoft Excel ermöglicht es Benutzern, Datenvalidierungsregeln für Zellen hinzuzufügen. Zum Beispiel gibt eine Dezimalvalidierung an, dass nur Zahlen zwischen 10 und 20 eingegeben werden können. Wenn ein Benutzer eine andere Zahl eingibt, zeigt Microsoft Excel eine Fehlermeldung an und fordert ihn auf, eine Zahl im richtigen Bereich einzugeben. Wenn Sie beispielsweise eine Zahl, sagen wir 3, in die Zelle kopieren und einfügen, führt Excel keine Validierungsprüfung durch oder zeigt eine Fehlermeldung an.

Manchmal ist es erforderlich, programmgesteuert zu überprüfen, ob ein Wert den auf die Zelle angewendeten Datenvalidierungsregeln entspricht. Im obigen Fall sollte der Eintrag beispielsweise fehlschlagen.

{{% /alert %}} 
## **Einführung**
Aspose.Cells für Python via .NET bietet die Methode [Cell.get_validation_value()](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_validation_value/#), um Zellenwerte programmgesteuert zu validieren. Wenn der Wert in einer Zelle nicht den Datenvalidierungsregeln entspricht, die auf diese Zelle angewendet werden, gibt sie **False** zurück, ansonsten **True**.

Der folgende Beispielcode veranschaulicht, wie die Methode [Cell.get_validation_value()](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_validation_value/#) funktioniert. Zuerst gibt es den Wert 3 in C1 ein. Da dies nicht den Datenvalidierungsregeln entspricht, gibt die Methode [Cell.get_validation_value()](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_validation_value/#) **False** zurück. Dann gibt es den Wert 15 in C1 ein. Da dieser Wert den Datenvalidierungsregeln entspricht, gibt die Methode [Cell.get_validation_value()](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_validation_value/#) **True** zurück. Ebenso gibt sie für den Wert 30 **False** zurück.



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-FilteringAndValidation-DataValidationRules-1.py" >}}

### **Ergebnis**
{{< highlight java >}}

 Is 3 a Valid Value for this Cell: False

Is 15 a Valid Value for this Cell: True

Is 30 a Valid Value for this Cell: False

{{< /highlight >}}
{{< app/cells/assistant language="python-net" >}}
