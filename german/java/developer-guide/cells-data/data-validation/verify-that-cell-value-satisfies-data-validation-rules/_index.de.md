---
title: Überprüfen Sie, ob der Zellenwert den Datenvalidierungsregeln entspricht
type: docs
weight: 90
url: /de/java/verify-that-cell-value-satisfies-data-validation-rules/
---

{{% alert color="primary" %}}

Microsoft Excel ermöglicht es Benutzern, Datenvalidierungsregeln für Arbeitsblattzellen hinzuzufügen. Beispielsweise kann eine Dezimalvalidierung angewendet werden, um die Zahlen zwischen 10 und 20 einzuschränken. Wenn eine beliebige andere Zahl außerhalb dieses festgelegten Bereichs eingegeben wird, zeigt Microsoft Excel eine Fehlermeldung an und fordert den Benutzer auf, eine Zahl aus dem korrekten Bereich erneut einzugeben. Wenn der Benutzer eine Zahl, sagen wir 3, in die Zelle kopiert, führt Excel keine Validierungsprüfung durch oder zeigt eine Fehlermeldung an.

{{% /alert %}}

## Überprüfen Sie, ob der Zellenwert den Datenvalidierungsregeln entspricht

Manchmal ist es erforderlich, dynamisch zu überprüfen, ob ein bestimmter Wert den für die Zelle geltenden Datenvalidierungsregeln entspricht. Hierfür bieten die Aspose.Cells-APIs die Methode [**cell.getValidationValue()**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getValidationValue--). Wenn der Wert in einer Zelle den für diese Zelle geltenden Datenvalidierungsregeln nicht entspricht, gibt die Methode **False** zurück, andernfalls **True**.

Die folgende Beispielmicrosoft-excel-Datei wird mit dem unten stehenden Beispielcode verwendet, um die Methode [**cell.getValidationValue()**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getValidationValue--) zu testen. Wie in der Momentaufnahme zu sehen ist, hat die Zelle **C1** eine **dezimale Datenvalidierung** und akzeptiert nur Werte **zwischen 10 und 20**. Wann immer der Wert der Zelle zwischen 10 und 20 liegt, gibt die Methode [**cell.getValidationValue()**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getValidationValue--) **True** zurück, ansonsten gibt sie **False** zurück.

![todo:image_alt_text](verify-that-cell-value-satisfies-data-validation-rules_1.png)

Der folgende Beispielcode veranschaulicht, wie die Methode [**cell.getValidationValue()**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getValidationValue--) funktioniert. Zunächst gibt er den Wert 3 in C1 ein. Da dies den Datenvalidierungsregeln nicht entspricht, gibt die Methode [**cell.getValidationValue()**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getValidationValue--) **False** zurück. Dann gibt er den Wert 15 in C1 ein. Da dieser Wert den Datenvalidierungsregeln entspricht, gibt die Methode [**cell.getValidationValue()**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getValidationValue--) **True** zurück. Ebenso gibt sie für den Wert 30 ebenfalls **False** zurück.

## Java-Code zum Überprüfen, ob der Zellenwert den Datenvalidierungsregeln entspricht

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-VerifyCellValueSatisfiesDataValidationRules-VerifyCellValueSatisfiesDataValidationRules.java" >}}

## Von dem Beispielcode generierte Konsolenausgabe

Hier ist die von der Beispielmethode generierte Konsolenausgabe, wenn der Beispielcode mit der obigen Beispieldatei ausgeführt wird.

{{< highlight java >}}

Is 3 a Valid Value for this Cell: False

Is 15 a Valid Value for this Cell: True

Is 30 a Valid Value for this Cell: False

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
