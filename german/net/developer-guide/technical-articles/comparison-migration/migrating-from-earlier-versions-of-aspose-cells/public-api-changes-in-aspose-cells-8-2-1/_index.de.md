---
title: Öffentlich API Änderungen in Aspose.Cells 8.2.1
type: docs
weight: 80
url: /de/net/public-api-changes-in-aspose-cells-8-2-1/
---
{{% alert color="primary" %}} 

Dieses Dokument beschreibt Änderungen an Aspose.Cells API von Version 8.2.0 zu 8.2.1, die für Modul-/Anwendungsentwickler von Interesse sein könnten. Es enthält nicht nur neue und aktualisierte öffentliche Methoden, sondern auch eine Beschreibung aller Änderungen im Verhalten hinter den Kulissen in Aspose.Cells.

{{% /alert %}} 
## **Methode GetValidation() für Klasse Cell hinzugefügt**
Die Datenvalidierung ist eine der Funktionen, die Tabellenkalkulationsdesigner verwenden, um Benutzer daran zu hindern, ungültige Werte in eine bestimmte Zelle einzufügen. Mit Aspose.Cells for .NET 8.2.1 hat API einen einfachen Mechanismus offengelegt, der identifiziert, ob eine Datenvalidierung auf eine Zelle angewendet wurde. Verwenden Sie die GetValidation-Methode der Cell-Klasse, um eine angewendete Validierung abzurufen. Wenn keine Validierung erfolgt, gibt die Methode null zurück. In ähnlicher Weise können Sie die GetValidationInCell-Methode der ValidationCollection-Klasse verwenden, um die auf eine beliebige Zelle angewendete Validierung abzurufen, indem Sie ihre Zeilen- und Spaltenindizes bereitstellen.

{{% alert color="primary" %}} 

 Bitte lesen Sie den ausführlichen Artikel auf[Lassen Sie sich die Validierung auf Cell anwenden](/cells/de/net/get-validation-applied-on-a-cell/) für mehr Informationen.

{{% /alert %}}
## **Methode GetValidationValue() für Klasse Cell hinzugefügt**
Sie können nicht nur feststellen, ob die Validierung angewendet wurde, sondern auch überprüfen, ob ein bestimmter Wert die Datenvalidierungsregeln für eine bestimmte Zelle erfüllt. Diese Funktion ist in Szenarien nützlich, in denen Sie überprüfen möchten, ob der in die Zelle eingegebene Wert die Datenvalidierungsregeln im laufenden Betrieb erfüllt. Der Aspose.Cells API hat die GetValidationValue-Methode für die Cell-Klasse verfügbar gemacht. Wenn der in eine Zelle eingegebene Wert die Datenvalidierungsregeln nicht erfüllt, gibt die Methode „GetValidationValue“ für die Klasse „Cell“ „false“ zurück.

{{% alert color="primary" %}} 

 Bitte lesen Sie den ausführlichen Artikel auf[Stellen Sie sicher, dass der Wert Cell die Datenvalidierungsregeln erfüllt](/cells/de/net/verify-that-cell-value-satisfies-data-validation-rules/).

{{% /alert %}}
## **Überladung ToPrinter(PrinterSettings printerSettings)-Methode für WorkbookRender-Klasse hinzugefügt**
Sie können die überladene Methode verwenden, um die Arbeitsmappe über PrinterSettings für den Drucker zu rendern.
