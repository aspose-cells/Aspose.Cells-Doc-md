---
title: Erstellen, bearbeiten oder entfernen Sie Szenarien aus Arbeitsblättern
linktitle: Szenarien verwalten
type: docs
weight: 190
url: /de/net/create-manipulate-or-remove-scenarios-from-worksheets/
---
{{% alert color="primary" %}}

Manchmal müssen Sie Szenarien in Tabellenkalkulationen erstellen, bearbeiten oder löschen. Ein Szenario ist ein benanntes "Was wäre wenn?" Modell, das variable Eingabezellen enthält, die durch eine oder mehrere Formeln verknüpft sind. Entwerfen Sie vor dem Erstellen eines Szenarios das Arbeitsblatt so, dass es mindestens eine Formel enthält, die von Zellen abhängt, in die unterschiedliche Werte eingefügt werden können. Das folgende Beispiel zeigt, wie Szenarien aus einem Arbeitsblatt in einer Arbeitsmappe über Aspose.Cells-APIs erstellt und entfernt werden.

{{% /alert %}}

Aspose.Cells bietet einige nützliche Klassen, zum Beispiel,[**Szenariosammlung**](https://reference.aspose.com/cells/net/aspose.cells/scenariocollection), [**Szenario**](https://reference.aspose.com/cells/net/aspose.cells/scenario), [**SzenarioInputCellCollection**](https://reference.aspose.com/cells/net/aspose.cells/scenarioinputcellcollection) , und[**SzenarioInputCell**](https://reference.aspose.com/cells/net/aspose.cells/scenarioinputcell) Klassen. Es bietet auch die[**Arbeitsblatt.Szenarien**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/scenarios)Eigentum. Der folgende Beispielcode öffnet eine XLSX-Excel-Datei, die einige Szenarien enthält, und entfernt ein vorhandenes Szenario. Außerdem wird dem Arbeitsblatt ein neues Szenario hinzugefügt, bevor die Excel-Datei gespeichert wird. Das Beispiel verwendet eine sehr einfache Vorlagendatei, die ein Szenario enthält.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CreateManipulateRemoveScenarios-1.cs" >}}
