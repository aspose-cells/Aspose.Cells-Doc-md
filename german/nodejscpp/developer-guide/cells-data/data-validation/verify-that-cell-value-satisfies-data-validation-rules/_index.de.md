---
title: Überprüfen Sie, ob der Zellenwert den Datenvalidierungsregeln entspricht
type: docs
weight: 210
url: /de/nodejs-cpp/verify-that-cell-value-satisfies-data-validation-rules/
description: Erfahren Sie, wie Sie mithilfe der API Aspose.Cells for Node.js via C++ überprüfen, ob der Zellwert die Datenvalidierungsregeln erfüllt.
keywords: Hole Zellvalidierungswert Node.js via C++, Erhalte Zellvalidierungswert Node.js via C++, Überprüfe, ob ein Wert die Datenvalidierungsregeln erfüllt, die auf die Zelle angewendet wurden, Node.js via C++
---

{{% alert color="primary" %}} 

Microsoft Excel erlaubt es Benutzern, Datenvalidierungsregeln zu Zellen hinzuzufügen. Zum Beispiel gibt eine Dezimalvalidierung an, dass nur Zahlen zwischen 10 und 20 eingegeben werden können. Wenn ein Benutzer eine andere Zahl eingibt, zeigt Excel eine Fehlermeldung an und fordert ihn auf, eine Zahl im richtigen Bereich einzugeben. Wenn Sie eine Zahl, z.B. 3, in die Zelle kopieren und einfügen, überprüft Excel die Validierung nicht und zeigt keine Fehlermeldung an.

Manchmal ist es erforderlich, programmgesteuert zu überprüfen, ob ein Wert den auf die Zelle angewendeten Datenvalidierungsregeln entspricht. Im obigen Fall sollte der Eintrag beispielsweise fehlschlagen.

{{% /alert %}} 
## **Einführung**
Aspose.Cells for Node.js via C++ stellt die Methode [Cell.getValidationValue()](https://reference.aspose.com/cells/nodejs-cpp/cell/#getValidationValue--) zur Validierung von Zellwerten programmatisch bereit. Wenn der Wert in einer Zelle die auf diese Zelle angewendete Datenvalidierungsregel nicht erfüllt, gibt sie **false** zurück, sonst **true**.

Der folgende Beispielcode veranschaulicht, wie die Methode [Cell.getValidationValue()](https://reference.aspose.com/cells/nodejs-cpp/cell/#getValidationValue--) funktioniert. Zuerst wird der Wert 3 in C1 eingegeben. Da dieser die Datenvalidierungsregel nicht erfüllt, gibt die Methode **false** zurück. Dann wird der Wert 15 in C1 eingegeben. Weil dieser die Datenvalidierungsregel erfüllt, gibt die Methode **true** zurück. Ebenso ergibt der Wert 30 **false**.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-DataValidation-VerifyValidationCellValues.js" >}}


### **Ergebnis**
{{< highlight javascript >}}

 Is 3 a Valid Value for this Cell: false

Is 15 a Valid Value for this Cell: true

Is 30 a Valid Value for this Cell: false

{{< /highlight >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
