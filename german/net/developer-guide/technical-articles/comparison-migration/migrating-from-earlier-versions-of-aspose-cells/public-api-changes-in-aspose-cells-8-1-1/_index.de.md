---
title: Änderungen an der öffentlichen API in Aspose.Cells 8.1.1
type: docs
weight: 50
url: /de/net/public-api-changes-in-aspose-cells-8-1-1/
---

{{% alert color="primary" %}} 

Dieses Dokument beschreibt Änderungen an der Aspose.Cells-API von Version 8.1.0 auf 8.1.1, die für Modul-/Anwendungsentwickler interessant sein könnten. Es umfasst nicht nur neue und aktualisierte öffentliche Methoden, sondern auch eine Beschreibung eventueller Änderungen im Verhalten hinter den Kulissen von Aspose.Cells.

{{% /alert %}} 
## **Hinzugefügte HtmlSaveOptions.PresentationPreference-Eigenschaft**
Die HtmlSaveOptions-Klasse hat die Eigenschaft PresentationPreference freigegeben, die verwendet werden kann, um die Ergebnisse mit besserem Layout beim Exportieren von Tabellenkalkulationen in HTML oder MHTML darzustellen. Der Standardwert ist false. Wenn er auf true gesetzt wird, exportiert die Aspose.Cells-API die Arbeitsblattinhalte mit besserer Darstellung.

{{% alert color="primary" %}} 

Bitte prüfen Sie den detaillierten Artikel zu [Verwendung der PresentationPreference-Option für besseres Layout](/cells/de/net/excel-to-html-use-presentationpreference-option-for-better-layout/)

{{% /alert %}}
## **Unterstützung für Arbeitsblattszenarien hinzugefügt**
Ein Szenario ist ein sogenanntes Was-wäre-wenn-Modell, das aus variablen Eingabezellen besteht, die durch eine oder mehr Formeln miteinander verknüpft sind. Aspose.Cells-API hat die Eigenschaft Worksheet.Scenarios sowie die folgenden Klassen freigegeben, um den Benutzern beim Erstellen, Manipulieren und Entfernen von Szenarien aus Arbeitsblättern zu helfen, 

1. Szenario: Stellt ein einzelnes Szenario dar.
1. ScenarioCollection: Stellt eine Sammlung von Szenarien dar.
1. ScenarioInputCellCollection: Stellt eine Liste von Eingabezellen für ein bestimmtes Szenario dar.
1. ScenarioInputCell: Stellt eine Eingabezelle aus der Sammlung von Eingabezellen für ein bestimmtes Szenario dar.

{{% alert color="primary" %}} 

Bitte prüfen Sie den ausführlichen Artikel zu [Wie man Szenarien in Tabellenkalkulationen erstellt, manipuliert oder entfernt](/cells/de/net/create-manipulate-or-remove-scenarios-from-worksheets/).

{{% /alert %}}
