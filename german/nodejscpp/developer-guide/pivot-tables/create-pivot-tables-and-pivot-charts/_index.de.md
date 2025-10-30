---
title: Erstellen von Pivot Tabellen und Pivot Diagrammen
type: docs
weight: 20
url: /de/nodejs-cpp/create-pivot-tables-and-pivot-charts/
description: Wie man Pivot Tabellen und Pivot Diagramme mit Aspose.Cells for Node.js via C++ hinzufügt.
keywords: Aspose.Cells for Node.js via C++ Excel, Excel Node.js Bibliothek, Pivot Tabellen und Pivot Diagramme mit Aspose.Cells for Node.js via C++ hinzufügen.
---

{{% alert color="primary" %}}

Eine Pivot-Tabelle ist eine interaktive Zusammenfassung von Datensätzen. Sie können beispielsweise Hunderte von Rechnungseinträgen in einer Liste in einem Arbeitsblatt haben. Eine Pivot-Tabelle kann die Rechnungen nach Kunden, Produkt oder Datum zusammenfassen. Mit Microsoft Excel ist es möglich, die Informationen in der Pivot-Tabelle schnell neu anzuordnen, indem Sie Schaltflächen an eine neue Position ziehen.

Ein Pivot-Diagramm ist eine interaktive grafische Darstellung der Daten in einer Pivot-Tabelle. Pivot-Diagramme wurden in Excel 2000 eingeführt. Durch die Verwendung eines Pivot-Diagramms wird es noch einfacher, die Daten zu verstehen, da die Pivot-Tabelle automatisch Teil- und Gesamtsummen erstellt.

Aspose.Cells for Node.js via C++ unterstützt [Pivot-Tabellen](/cells/de/nodejs-cpp/create-pivot-tables-and-pivot-charts/) und [Pivot-Diagramme](/cells/de/nodejs-cpp/create-pivot-tables-and-pivot-charts/).

{{% /alert %}}

## **Pivot-Tabellen und Diagramme mit Aspose.Cells for Node.js via C++ hinzufügen**

Aspose.Cells for Node.js via C++ bietet eine spezielle Klasse zur Erstellung von Pivot-Tabellen. Diese Klassen werden verwendet, um PivotTable-Objekte zu erstellen und einzustellen, die als Grundbausteine eines PivotTable-Objekts dienen:

- PivotField, ein Feld in einem Pivot-Tabellenbericht.
- PivotFields, eine Sammlung aller PivotField-Objekte in einer Pivot-Tabelle.
- PivotTable, ein Pivot-Tabellenbericht auf einem Arbeitsblatt.
- PivotTables, eine Sammlung aller PivotTable-Objekte auf dem Arbeitsblatt.

### **Vorbereitung der Verwendung von Aspose.Cells for Node.js via C++**
1. Installieren Sie Aspose.Cells for Node.js via C++ aus NPM, verwenden Sie den Befehl: $ npm install aspose.cells.node.
1. Sie können auch die Schritt-für-Schritt-Anleitung zur Installation von “Aspose.Cells for Node.js via C++” in Ihrer Entwicklerumgebung befolgen.


### **So fügen Sie eine Pivot-Tabelle mit Aspose.Cells for Node.js via C++ hinzu**

Um eine Pivot-Tabelle mit Aspose.Cells for Node.js via C++ zu erstellen:

1. Fügen Sie einige Daten zu Zellen auf einem Arbeitsblatt hinzu, indem Sie die put_value-Methode eines Cell-Objekts verwenden. Sie verwenden auch eine Vorlagendatei, die bereits mit Daten gefüllt ist. Die Daten werden als Datenquelle der Pivot-Tabelle verwendet.
1. Fügen Sie dem Arbeitsblatt eine Pivot-Tabelle hinzu, indem Sie die Methode add der PivotTables-Sammlung aufrufen (die im Arbeitsblatt-Objekt gekapselt ist).
1. Greifen Sie auf das neue PivotTable-Objekt aus der PivotTables-Sammlung zu, indem Sie seinen Index übergeben. # Verwenden Sie eines der in dem PivotTable-Objekt gekapselten Pivot-Tabellenobjekte, um die Tabelle zu verwalten.

Codebeispiele finden Sie unten.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-CreatePivotTablesPivotCharts-CreatePivotTable-1.js" >}}

### **Wie man ein Pivot-Diagramm mit der Aspose.Cells for Node.js via C++ Bibliothek hinzufügt**

Um ein PivotChart mit Aspose.Cells for Node.js via C++ zu erstellen:

1. Fügen Sie ein Diagramm hinzu.
1. Setzen Sie den PivotSource des Diagramms so, dass er auf eine vorhandene Pivot-Tabelle in der Tabelle verweist.
1. Setzen Sie andere Attribute.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-CreatePivotTablesPivotCharts-CreatePivotChart-1.js" >}}

{{< app/cells/assistant language="nodejs-cpp" >}}
