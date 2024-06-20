---
title: Szenarien in Arbeitsblättern erstellen, bearbeiten oder entfernen
linktitle: Szenarien verwalten
type: docs
weight: 190
url: /de/net/create-manipulate-or-remove-scenarios-from-worksheets/
description: In diesem Artikel erfahren Sie, wie Sie Szenarien in Excel Arbeitsblättern programmgesteuert mit der C# Bibliothek und der .NET API erstellen, manipulieren oder entfernen können.
keywords: Szenario Arbeitsblatt c# erstellen, Szenario Excel Arbeitsblatt c# entfernen, Szenario Arbeitsblatt c# manipulieren
---

{{% alert color="primary" %}}

Manchmal müssen Sie Szenarien in Tabellenkalkulationen erstellen, manipulieren oder löschen. Ein Szenario ist ein benanntes 'Was-wäre-wenn?'-Modell, das variable Eingabezellen enthält, die durch eine oder mehrere Formeln verknüpft sind. Vor dem Erstellen eines Szenarios entwerfen Sie das Arbeitsblatt so, dass es mindestens eine Formel enthält, die von Zellen abhängt, in die unterschiedliche Werte eingegeben werden können. Das folgende Beispiel zeigt, wie Sie Szenarien in einem Arbeitsblatt einer Arbeitsmappe über die Aspose.Cells-APIs erstellen und entfernen.

{{% /alert %}}

Aspose.Cells bietet einige nützliche Klassen, wie z.B. [**ScenarioCollection**](https://reference.aspose.com/cells/net/aspose.cells/scenariocollection), [**Scenario**](https://reference.aspose.com/cells/net/aspose.cells/scenario), [**ScenarioInputCellCollection**](https://reference.aspose.com/cells/net/aspose.cells/scenarioinputcellcollection) und [**ScenarioInputCell**](https://reference.aspose.com/cells/net/aspose.cells/scenarioinputcell) Klassen. Es bietet auch die [**Worksheet.Scenarios**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/scenarios)-Eigenschaft. Der Beispielscode unten öffnet eine XLSX-Excel-Datei, die einige Szenarien enthält, und entfernt ein vorhandenes Szenario. Es fügt auch ein neues Szenario zum Arbeitsblatt hinzu, bevor die Excel-Datei gespeichert wird. Das Beispiel verwendet eine sehr einfache Vorlagendatei, die ein Szenario enthält.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CreateManipulateRemoveScenarios-1.cs" >}}
