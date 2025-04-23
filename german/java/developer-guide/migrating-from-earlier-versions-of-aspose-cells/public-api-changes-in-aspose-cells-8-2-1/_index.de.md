---
title: Öffentliche API Änderungen in Aspose.Cells 8.2.1
type: docs
weight: 90
url: /de/java/public-api-changes-in-aspose-cells-8-2-1/
---

{{% alert color="primary" %}} 

Dieses Dokument beschreibt Änderungen in der Aspose.Cells-API von Version 8.2.0 auf 8.2.1, die für Modul-/Anwendungsentwickler von Interesse sein können. Es umfasst nicht nur neue und aktualisierte öffentliche Methoden, sondern auch eine Beschreibung etwaiger Änderungen im Verhalten hinter den Kulissen in Aspose.Cells.

{{% /alert %}} 
## **Hinzufügen der Methode getValidation() für die Zellenklasse**
Die Datenvalidierung ist eine der Funktionen, die von Tabellenkalkulationsentwicklern verwendet wird, um zu verhindern, dass Benutzer ungültige Werte in eine bestimmte Zelle einfügen. Mit Aspose.Cells for Java 8.2.1 hat die API einen einfachen Mechanismus freigelegt, der identifiziert, ob eine Datenvalidierung auf einer Zelle angewendet wurde. Verwenden Sie die Methode getValidation der Zellenklasse, um eine angewendete Validierung zu erhalten. Wenn keine Validierung vorliegt, liefert die Methode null zurück. Ebenso können Sie die Methode getValidationInCell der ValidationCollection-Klasse verwenden, um die Validierung auf einer Zelle zu erhalten, indem Sie ihre Zeilen- und Spaltenindizes angeben.

{{% alert color="primary" %}} 

Bitte lesen Sie den ausführlichen Artikel zu [Abrufen der auf eine Zelle angewendeten Validierung](https://docs.aspose.com/cells/java/get-validation-applied-on-a-cell/) für weitere Informationen.

{{% /alert %}}
## **Hinzufügen der Methode getValidationValue() für die Zellenklasse**
Zusätzlich zur Feststellung, ob eine Validierung angewendet wurde, können Sie auch überprüfen, ob ein bestimmter Wert die Datenvalidierungsregeln für eine bestimmte Zelle erfüllt. Diese Funktion ist nützlich, wenn Sie überprüfen möchten, ob der in die Zelle eingegebene Wert die Datenvalidierungsregeln sofort erfüllt. Die Aspose.Cells-API hat die Methode getValidationValue für die Zellenklasse freigelegt. Wenn der in eine Zelle eingegebene Wert die Datenvalidierungsregeln nicht erfüllt, gibt die Methode getValidationValue für die Zellenklasse false zurück.

{{% alert color="primary" %}} 

Bitte lesen Sie den ausführlichen Artikel zu [Überprüfen, dass der Zellenwert die Datenvalidierungsregeln erfüllt](/cells/de/java/verify-that-cell-value-satisfies-data-validation-rules/).

{{% /alert %}}
## **Hinzufügen einer Überladung der Methode toPrinter(PrinterSettings printerSettings) für die WorkbookRender-Klasse**
Sie können die überladene Methode verwenden, um die Arbeitsmappe über die PrinterSettings auf den Drucker zu rendern.
{{< app/cells/assistant language="java" >}}
