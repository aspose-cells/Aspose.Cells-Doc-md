---
title: Szenarien in Arbeitsblättern erstellen, bearbeiten oder entfernen
linktitle: Szenarien verwalten
type: docs
weight: 120
url: /de/java/create-manipulate-or-remove-scenarios-from-worksheets/
---

{{% alert color="primary" %}}

Manchmal müssen Sie Szenarien in Tabellenkalkulationen erstellen, bearbeiten oder löschen. Ein Szenario ist ein benanntes Was-wäre-wenn-Modell, das durch Variableingabezellen verknüpft ist, die durch eine oder mehrere Formeln miteinander verbunden sind. Bevor Sie ein Szenario erstellen, entwerfen Sie ein Arbeitsblatt so, dass es mindestens eine Formel enthält, die von Zellen abhängt, in die verschiedene Werte eingefügt werden können. Das folgende Beispiel zeigt, wie Sie Szenarien mithilfe der Aspose.Cells-APIs erstellen und entfernen.

{{% /alert %}}

Aspose.Cells bietet einige nützliche Klassen, z. B. [**ScenarioCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ScenarioCollection), [**Scenario**](https://reference.aspose.com/cells/java/com.aspose.cells/Scenario), [**ScenarioInputCellCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ScenarioInputCellCollection) und [**ScenarioInputCell**](https://reference.aspose.com/cells/java/com.aspose.cells/ScenarioInputCell). Es bietet auch die Eigenschaft [**Worksheet.Scenarios**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Scenarios). Der Beispielcode öffnet eine XLSX-Excel-Datei (die einige Szenarien enthält) und entfernt ein vorhandenes Szenario aus dem Arbeitsblatt. Es fügt auch vor dem Speichern der Excel-Datei ein neues Szenario hinzu. Es verwendet eine sehr einfache Vorlagendatei, die ein Szenario enthält.

Nach Ausführung des Codes wird ein vorhandenes Szenario entfernt und ein neues Szenario dem Arbeitsblatt hinzugefügt.

**Die Ausgabedatei**

![todo:image_alt_text](create-manipulate-or-remove-scenarios-from-worksheets_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CreateScenariosfromWorksheets-CreateScenariosfromWorksheets.java" >}}
{{< app/cells/assistant language="java" >}}
