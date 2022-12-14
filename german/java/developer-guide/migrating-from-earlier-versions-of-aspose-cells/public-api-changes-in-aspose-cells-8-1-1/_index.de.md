---
title: Öffentlich API Änderungen in Aspose.Cells 8.1.1
type: docs
weight: 60
url: /de/java/public-api-changes-in-aspose-cells-8-1-1/
---
{{% alert color="primary" %}} 

Dieses Dokument beschreibt Änderungen der Aspose.Cells API von Version 8.1.0 auf 8.1.1, die für Modul- und Anwendungsentwickler von Interesse sein könnten. Es beinhaltet nicht nur[neue und aktualisierte öffentliche Methoden](/cells/de/java/public-api-changes-in-aspose-cells-8-1-1/) , sondern auch eine Beschreibung von allen[Veränderungen im Verhalten](/cells/de/java/public-api-changes-in-aspose-cells-8-1-1/) Hinter den Kulissen unter Aspose.Cells.

{{% /alert %}} 
## **Eigenschaften und Funktionen hinzugefügt**
### **HtmlSaveOptions.PresentationPreference-Eigenschaft hinzugefügt**
Die HtmlSaveOptions-Klasse hat Getter/Setter für die PresentationPreference-Eigenschaft verfügbar gemacht, die verwendet werden können, um die Ergebnisse beim Exportieren von Tabellenkalkulationen in HTML oder MHTML mit einem besseren Layout zu rendern. Der Standardwert ist falsch. Wenn dagegen Aspose.Cells API auf true gesetzt ist, werden die Arbeitsblattinhalte mit besserer Darstellung exportiert.

{{% alert color="primary" %}} 

 Bitte lesen Sie den ausführlichen Artikel auf[Verwenden Sie die PresentationPreference-Option für ein besseres Layout](/cells/de/java/excel-to-html-use-presentationpreference-option-for-better-layout/)

{{% /alert %}} 
### **Unterstützung für Arbeitsblattszenarien hinzugefügt**
Ein Szenario ist ein Was-wäre-wenn-Modell, das variable Eingabezellen enthält, die durch eine oder mehrere Formeln miteinander verknüpft sind. Aspose.Cells hat einen Getter und Setter für die Worksheet.Scenarios-Eigenschaft zusammen mit den folgenden Klassen verfügbar gemacht, um Entwickler beim Erstellen, Bearbeiten und Entfernen von Szenarien zu unterstützen.

1. Szenario: Stellt ein individuelles Szenario dar.
1. ScenarioCollection: Stellt eine Sammlung von Szenarien dar.
1. ScenarioInputCellCollection: Stellt eine Liste von Eingabezellen für ein bestimmtes Szenario dar.
1. ScenarioInputCell: Stellt eine Eingabezelle aus der Sammlung von Eingabezellen für ein bestimmtes Szenario dar.

{{% alert color="primary" %}} 

 Bitte lesen Sie den ausführlichen Artikel auf[So erstellen, bearbeiten oder entfernen Sie Szenarien aus Arbeitsblättern](/cells/de/java/create-manipulate-or-remove-scenarios-from-worksheets/).

{{% /alert %}}
## **Verhaltensänderung für CellsException**
Bei früheren Versionen von Aspose.Cells for Java API neigte API dazu, eine allgemeine Meldung auszulösen, wenn eine möglicherweise beschädigte Tabelle in eine Instanz von Workbook geladen wurde, ohne zu erwähnen, wo das Problem liegen könnte. Wir haben dieses Verhalten für 8.1.1 geändert, sodass die API eine Ausnahme mit einer aussagekräftigen Meldung auslöst, die darauf hinweist, wo (welche Zelle) und was (Formelausdruck) die Ausnahme beim Lesen der Vorlagendatei verursacht.
