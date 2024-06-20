---
title: Änderungen an der öffentlichen API in Aspose.Cells 8.1.1
type: docs
weight: 60
url: /de/java/public-api-changes-in-aspose-cells-8-1-1/
---

{{% alert color="primary" %}} 

Dieses Dokument beschreibt Änderungen an der Aspose.Cells-API von Version 8.1.0 auf 8.1.1, die für Modul- und Anwendungs-Entwickler interessant sein können. Es umfasst nicht nur [neue und aktualisierte öffentliche Methoden](/cells/de/java/public-api-changes-in-aspose-cells-8-1-1/), sondern auch eine Beschreibung von [Änderungen im Verhalten](/cells/de/java/public-api-changes-in-aspose-cells-8-1-1/) hinter den Kulissen von Aspose.Cells.

{{% /alert %}} 
## **Hinzugefügte Eigenschaften und Funktionen**
### **Hinzugefügt: HtmlSaveOptions.PresentationPreference-Eigenschaft**
Die HtmlSaveOptions-Klasse verfügt über Getter/Setter für die PresentationPreference-Eigenschaft, die verwendet werden kann, um die Ergebnisse beim Exportieren von Tabellenkalkulationen in HTML oder MHTML mit besserem Layout zu rendern. Der Standardwert ist false. Wenn er jedoch auf true gesetzt wird, exportiert die Aspose.Cells-API die Inhalte des Arbeitsblatts mit besserer Präsentation.

{{% alert color="primary" %}} 

Bitte überprüfen Sie den ausführlichen Artikel zu [Verwendung der Option PresentationPreference für besseres Layout](/cells/de/java/excel-to-html-use-presentationpreference-option-for-better-layout/)

{{% /alert %}} 
### **Unterstützung für Arbeitsblattszenarien hinzugefügt**
Ein Szenario ist ein sogenanntes 'Was-Wäre-Wenn'-Modell, das variable Eingabezellen umfasst, die durch eine oder mehrere Formeln verknüpft sind. Aspose.Cells hat ein Getter und Setter für die Worksheet.Scenarios-Eigenschaft freigelegt, zusammen mit den folgenden Klassen, um Entwicklern dabei zu helfen, Szenarien zu erstellen, zu manipulieren und zu entfernen.

1. Szenario: Stellt ein einzelnes Szenario dar.
1. ScenarioCollection: Stellt eine Sammlung von Szenarien dar.
1. ScenarioInputCellCollection: Stellt eine Liste von Eingabezellen für ein bestimmtes Szenario dar.
1. ScenarioInputCell: Stellt eine Eingabezelle aus der Sammlung von Eingabezellen für ein bestimmtes Szenario dar.

{{% alert color="primary" %}} 

Bitte überprüfen Sie den ausführlichen Artikel zu [Erstellen, Manipulieren oder Entfernen von Szenarien aus Arbeitsblättern](/cells/de/java/create-manipulate-or-remove-scenarios-from-worksheets/).

{{% /alert %}}
## **Änderung in Verhalten für CellsException**
Bei früheren Versionen der Aspose.Cells for Java API warf die API bei Laden einer möglicherweise beschädigten Arbeitsmappe in einer Workbook-Instanz tendenziell eine allgemeine Meldung ohne den Ort des Problems zu nennen. In Version 8.1.1 haben wir dieses Verhalten geändert, sodass die API eine Ausnahme mit einer aussagekräftigen Meldung wirft, die darauf hinweist, wo (welche Zelle) und was (Formelausdruck) die Ausnahme beim Lesen der Vorlagendatei verursacht.
