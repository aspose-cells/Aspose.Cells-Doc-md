---
title: Stellen Sie sicher, dass der Wert Cell die Datenvalidierungsregeln erfüllt
type: docs
weight: 90
url: /de/java/verify-that-cell-value-satisfies-data-validation-rules/
---
{{% alert color="primary" %}}

Microsoft Excel ermöglicht Benutzern das Hinzufügen von Datenvalidierungsregeln zu Arbeitsblattzellen. Beispielsweise kann eine Dezimalvalidierung angewendet werden, um die Zahlen zwischen 10 und 20 einzuschränken. Wenn eine andere Zahl außerhalb dieses angegebenen Bereichs eingegeben wird, zeigt Excel Microsoft eine Fehlermeldung an und fordert den Benutzer auf, eine Zahl aus dem richtigen Bereich erneut einzugeben. Wenn der Benutzer eine Zahl, z. B. 3, in die Zelle einfügt, führt Excel die Validierungsprüfung nicht aus oder zeigt eine Fehlermeldung an.

{{% /alert %}}

## Stellen Sie sicher, dass der Wert Cell die Datenvalidierungsregeln erfüllt

Manchmal ist es erforderlich, dynamisch zu überprüfen, ob ein bestimmter Wert die auf die Zelle angewendeten Datenvalidierungsregeln erfüllt. Hierfür stellen die Aspose.Cells APIs die[**cell.getValidationValue**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getValidationValue() ) Methode. Wenn der Wert in einer Zelle die auf diese Zelle angewendete Datenvalidierungsregel nicht erfüllt, wird er zurückgegeben**FALSCH** , anders**WAHR**.

Die folgende Excel-Beispieldatei Microsoft wird mit dem folgenden Beispielcode verwendet, um die[**cell.getValidationValue**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getValidationValue() ) Methode. Wie Sie im Schnappschuss sehen können, sind die Zellen**C1** hat**dezimale Datenvalidierung** angewendet und akzeptiert nur Werte**zwischen 10 und 20** . Immer wenn der Wert der Zelle zwischen 10 und 20 liegt,[**cell.getValidationValue**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getValidationValue() ) Methode zurück**WAHR** , andernfalls kehrt es zurück**FALSCH**.

![todo: Bild_alt_Text](verify-that-cell-value-satisfies-data-validation-rules_1.png)

 Der folgende Beispielcode veranschaulicht, wie die[**cell.getValidationValue**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getValidationValue() ) Methode funktioniert. Zuerst trägt er den Wert 3 in C1 ein. Da dies die Datenvalidierungsregel nicht erfüllt, wird die[**cell.getValidationValue**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getValidationValue() ) Methode gibt zurück**FALSCH** . Dann trägt er den Wert 15 in C1 ein. Da dieser Wert die Datenvalidierungsregel erfüllt, wird die[**cell.getValidationValue**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getValidationValue() ) Methode gibt zurück**WAHR** . Ebenso kehrt es zurück**FALSCH** für Wert 30.

## Java-Code, um zu überprüfen, ob ein Cell-Wert die Datenvalidierungsregeln erfüllt

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-VerifyCellValueSatisfiesDataValidationRules-VerifyCellValueSatisfiesDataValidationRules.java" >}}

## Vom Beispielcode generierte Konsolenausgabe

Hier ist die Konsolenausgabe, die generiert wird, wenn der Beispielcode mit der oben gezeigten Beispiel-Excel-Datei ausgeführt wird.

{{< highlight "java" >}}

Is 3 a Valid Value for this Cell: False

Is 15 a Valid Value for this Cell: True

Is 30 a Valid Value for this Cell: False

{{< /highlight >}}
