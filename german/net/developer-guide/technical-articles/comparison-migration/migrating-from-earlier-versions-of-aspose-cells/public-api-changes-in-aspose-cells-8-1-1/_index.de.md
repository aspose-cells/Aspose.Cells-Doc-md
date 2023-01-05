---
title: Öffentlich API Änderungen in Aspose.Cells 8.1.1
type: docs
weight: 50
url: /de/net/public-api-changes-in-aspose-cells-8-1-1/
---
{{% alert color="primary" %}} 

Dieses Dokument beschreibt Änderungen an Aspose.Cells API von Version 8.1.0 zu 8.1.1, die für Modul-/Anwendungsentwickler von Interesse sein könnten. Es enthält nicht nur neue und aktualisierte öffentliche Methoden, sondern auch eine Beschreibung aller Änderungen im Verhalten hinter den Kulissen in Aspose.Cells.

{{% /alert %}} 
## **HtmlSaveOptions.PresentationPreference-Eigenschaft hinzugefügt**
Die HtmlSaveOptions-Klasse hat die PresentationPreference-Eigenschaft verfügbar gemacht, die verwendet werden kann, um die Ergebnisse beim Exportieren von Tabellenkalkulationen nach HTML oder MHTML mit einem besseren Layout zu rendern. Der Standardwert ist „false“. Wenn dagegen Aspose.Cells API auf true gesetzt ist, wird der Arbeitsblattinhalt mit besserer Darstellung exportiert.

{{% alert color="primary" %}} 

 Bitte lesen Sie den ausführlichen Artikel auf[Verwenden Sie die PresentationPreference-Option für ein besseres Layout](/cells/de/net/excel-to-html-use-presentationpreference-option-for-better-layout/)

{{% /alert %}}
## **Unterstützung für Arbeitsblattszenarien hinzugefügt**
 Ein Szenario wird als Was-wäre-wenn-Modell bezeichnet, das variable Eingabezellen enthält, die entsprechend durch eine oder mehrere Formeln miteinander verknüpft sind. Aspose.Cells API hat die Worksheet.Scenarios-Eigenschaft zusammen mit den folgenden Klassen verfügbar gemacht, um den Benutzern das Erstellen, Bearbeiten und Entfernen von Szenarien aus Arbeitsblättern zu erleichtern.

1. Szenario: Stellt ein individuelles Szenario dar.
1. ScenarioCollection: Stellt eine Sammlung von Szenarien dar.
1. ScenarioInputCellCollection: Stellt eine Liste von Eingabezellen für ein bestimmtes Szenario dar.
1. ScenarioInputCell: Stellt eine Eingabezelle aus der Sammlung von Eingabezellen für ein bestimmtes Szenario dar.

{{% alert color="primary" %}} 

 Bitte lesen Sie den ausführlichen Artikel auf[So erstellen, bearbeiten oder entfernen Sie Szenarien aus Arbeitsblättern](/cells/de/net/create-manipulate-or-remove-scenarios-from-worksheets/).

{{% /alert %}}
