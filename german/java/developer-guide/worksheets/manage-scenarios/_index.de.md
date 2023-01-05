---
title: Erstellen, bearbeiten oder entfernen Sie Szenarien aus Arbeitsblättern
linktitle: Szenarien verwalten
type: docs
weight: 120
url: /de/java/create-manipulate-or-remove-scenarios-from-worksheets/
---
{{% alert color="primary" %}}

Manchmal müssen Sie Szenarien in Tabellenkalkulationen erstellen, bearbeiten oder löschen. Ein Szenario ist ein benanntes Was-wäre-wenn-Modell, das variable Eingabezellen enthält, die durch eine oder mehrere Formeln miteinander verknüpft sind. Entwerfen Sie vor dem Erstellen eines Szenarios ein Arbeitsblatt, das mindestens eine Formel enthält, die von Zellen abhängt, in die unterschiedliche Werte eingefügt werden können. Das folgende Beispiel zeigt, wie Szenarien mithilfe der Aspose.Cells-APIs aus einem Arbeitsblatt erstellt und entfernt werden.

{{% /alert %}}

 Aspose.Cells bietet zum Beispiel einige nützliche Klassen[**Szenariosammlung**](https://reference.aspose.com/cells/java/com.aspose.cells/ScenarioCollection), [**Szenario**](https://reference.aspose.com/cells/java/com.aspose.cells/Scenario), [**SzenarioInputCellCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ScenarioInputCellCollection) und[**SzenarioInputCell**](https://reference.aspose.com/cells/java/com.aspose.cells/ScenarioInputCell) . Es bietet auch die[**Arbeitsblatt.Szenarien**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Scenarios)Eigentum. Der folgende Beispielcode öffnet eine Excel-Datei XLSX (die einige Szenarien enthält) und entfernt ein vorhandenes Szenario aus dem Arbeitsblatt. Außerdem wird vor dem Speichern der Excel-Datei ein neues Szenario hinzugefügt. Es verwendet eine sehr einfache Vorlagendatei, die ein Szenario enthält.

Nach dem Ausführen des Codes wird ein vorhandenes Szenario entfernt und dem Arbeitsblatt ein neues Szenario hinzugefügt.

**Die Ausgabedatei**

![todo: Bild_alt_Text](create-manipulate-or-remove-scenarios-from-worksheets_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CreateScenariosfromWorksheets-CreateScenariosfromWorksheets.java" >}}
