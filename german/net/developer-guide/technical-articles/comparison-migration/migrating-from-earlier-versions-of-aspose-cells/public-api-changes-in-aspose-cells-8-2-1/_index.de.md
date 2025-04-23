---
title: Öffentliche API Änderungen in Aspose.Cells 8.2.1
type: docs
weight: 80
url: /de/net/public-api-changes-in-aspose-cells-8-2-1/
---

{{% alert color="primary" %}} 

Dieses Dokument beschreibt Änderungen in der Aspose.Cells-API von Version 8.2.0 auf 8.2.1, die für Modul-/Anwendungsentwickler von Interesse sein können. Es umfasst nicht nur neue und aktualisierte öffentliche Methoden, sondern auch eine Beschreibung etwaiger Änderungen im Verhalten hinter den Kulissen in Aspose.Cells.

{{% /alert %}} 
## **Hinzugefügte Methode GetValidation() für die Cell-Klasse**
Die Datenvalidierung ist eine der Funktionen, die Tabellendesigner verwenden, um Benutzer davon abzuhalten, ungültige Werte in eine bestimmte Zelle einzugeben. Mit Aspose.Cells for .NET 8.2.1 hat die API einen einfachen Mechanismus freigelegt, der identifiziert, ob eine Datenvalidierung auf eine Zelle angewendet wurde. Verwenden Sie die Methode GetValidation der Cell-Klasse, um eventuelle angewendete Validierungen zu erhalten. Wenn keine Validierung vorliegt, gibt die Methode null zurück. Ebenso können Sie mit der Methode GetValidationInCell der ValidationCollection-Klasse die auf eine Zelle angewendete Validierung abrufen, indem Sie deren Zeilen- und Spaltenindizes angeben.

{{% alert color="primary" %}} 

Bitte überprüfen Sie den ausführlichen Artikel zu [Erhalten der auf eine Zelle angewendeten Validierung](/cells/de/net/get-validation-applied-on-a-cell/) für weitere Informationen.

{{% /alert %}}
## **Hinzugefügte Methode GetValidationValue() für die Cell-Klasse**
Zusätzlich zur Feststellung, ob eine Validierung angewendet wurde, können Sie auch überprüfen, ob ein bestimmter Wert die Datenvalidierungsregeln für eine bestimmte Zelle erfüllt. Diese Funktion ist nützlich in Szenarien, in denen Sie überprüfen möchten, ob der in die Zelle eingegebene Wert die Datenvalidierungsregeln sofort erfüllt. Die Aspose.Cells API hat die Methode GetValidationValue für die Cell-Klasse freigelegt. Wenn der in eine Zelle eingegebene Wert die Datenvalidierungsregeln nicht erfüllt, gibt die Methode GetValidationValue für die Cell-Klasse false zurück.

{{% alert color="primary" %}} 

Bitte überprüfen Sie den ausführlichen Artikel zu [Überprüfen, ob der Zellenwert die Datenvalidierungsregeln erfüllt](/cells/de/net/verify-that-cell-value-satisfies-data-validation-rules/) für weitere Informationen.

{{% /alert %}}
## **Hinzugefügte Überladung der Methode ToPrinter(PrinterSettings printerSettings) für die WorkbookRender-Klasse**
Sie können die überladene Methode verwenden, um die Arbeitsmappe über die PrinterSettings auf den Drucker zu rendern.
{{< app/cells/assistant language="csharp" >}}
