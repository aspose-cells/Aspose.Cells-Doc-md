---
title: Öffentlich API Änderungen in Aspose.Cells 8.2.1
type: docs
weight: 90
url: /de/java/public-api-changes-in-aspose-cells-8-2-1/
---
{{% alert color="primary" %}} 

Dieses Dokument beschreibt Änderungen an Aspose.Cells API von Version 8.2.0 zu 8.2.1, die für Modul-/Anwendungsentwickler von Interesse sein könnten. Es enthält nicht nur neue und aktualisierte öffentliche Methoden, sondern auch eine Beschreibung aller Änderungen im Verhalten hinter den Kulissen in Aspose.Cells.

{{% /alert %}} 
## **Methode getValidation() für Klasse Cell hinzugefügt**
Die Datenvalidierung ist eine der Funktionen, die Tabellenkalkulationsdesigner verwenden, um Benutzer daran zu hindern, ungültige Werte in eine bestimmte Zelle einzufügen. Mit Aspose.Cells for Java 8.2.1 hat API einen einfachen Mechanismus offengelegt, der identifiziert, ob eine Datenvalidierung auf eine Zelle angewendet wurde. Verwenden Sie die Methode getValidation der Klasse Cell, um eine angewendete Validierung abzurufen. Wenn keine Validierung erfolgt, gibt die Methode null zurück. In ähnlicher Weise können Sie die getValidationInCell-Methode der ValidationCollection-Klasse verwenden, um die auf eine beliebige Zelle angewendete Validierung abzurufen, indem Sie ihre Zeilen- und Spaltenindizes bereitstellen.

{{% alert color="primary" %}} 

 Bitte lesen Sie den ausführlichen Artikel auf[Lassen Sie sich die Validierung auf Cell anwenden](https://docs.aspose.com/cells/java/get-validation-applied-on-a-cell/) für mehr Informationen.

{{% /alert %}}
## **Methode getValidationValue() für Klasse Cell hinzugefügt**
Sie können nicht nur feststellen, ob die Validierung angewendet wurde, sondern auch überprüfen, ob ein bestimmter Wert die Datenvalidierungsregeln für eine bestimmte Zelle erfüllt. Diese Funktion ist in Szenarien nützlich, in denen Sie überprüfen möchten, ob der in die Zelle eingegebene Wert die Datenvalidierungsregeln im laufenden Betrieb erfüllt. Der Aspose.Cells API hat die getValidationValue-Methode für die Cell-Klasse verfügbar gemacht. Wenn der in eine Zelle eingegebene Wert die Datenvalidierungsregeln nicht erfüllt, gibt die getValidationValue-Methode für die Klasse Cell „false“ zurück.

{{% alert color="primary" %}} 

 Bitte lesen Sie den ausführlichen Artikel auf[Stellen Sie sicher, dass der Wert Cell die Datenvalidierungsregeln erfüllt](/cells/de/java/verify-that-cell-value-satisfies-data-validation-rules/).

{{% /alert %}}
## **Überladung zur Printer(PrinterSettings printerSettings)-Methode für die WorkbookRender-Klasse hinzugefügt**
Sie können die überladene Methode verwenden, um die Arbeitsmappe über PrinterSettings für den Drucker zu rendern.
