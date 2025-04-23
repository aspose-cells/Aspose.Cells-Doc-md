---
title: Öffentliche API Änderungen in Aspose.Cells 8.7.1
type: docs
weight: 250
url: /de/java/public-api-changes-in-aspose-cells-8-7-1/
---

{{% alert color="primary" %}} 

Dieses Dokument beschreibt die Änderungen an der Aspose.Cells-API von Version 8.7.0 auf 8.7.1, die für Modul-/Anwendungs-Entwickler interessant sein könnten. Es umfasst nicht nur neue und aktualisierte öffentliche Methoden, hinzugefügte & entfernte Klassen usw., sondern auch eine Beschreibung von Änderungen im Verhalten hinter den Kulissen in Aspose.Cells.

{{% /alert %}} 
## **Hinzugefügte APIs**
### **Hinzugefügte LookInType.ORIGINAL_VALUES-Eigenschaft**
Aspose.Cells-APIs unterstützen bereits die [Suchen oder Suchen von Daten](/cells/de/java/find-or-search-data/) in Tabellenkalkulationen, um bestimmte Inhalte in Zellwert & Formel zu finden. Diese Funktion mangelte jedoch am Aspekt des Formats, das auf die Zelle angewendet wurde und das Aussehen sowie den Wert des Inhalts ändern könnte, und somit den Text bei Verwendung des Originalwerts unfindbar machen könnte. Mit diesem Release der Aspose.Cells-APIs wurde eine weitere Konstante namens LookInType.ORIGINAL_VALUES in der öffentlichen API freigegeben, die es ermöglicht, die oben diskutierte Situation zu überwinden. 

{{% alert color="primary" %}} 

Für weitere Details zu dieser Funktion lesen Sie bitte den ausführlichen Artikel über [Suchen von Daten mit Originalwerten](https://docs.aspose.com/cells/java/search-data-using-original-values/)

{{% /alert %}} 

Im Folgenden wird das einfache Anwendungsszenario beschrieben.

**Java**

{{< highlight csharp >}}

 //Create workbook object

Workbook workbook = new Workbook();

//Access first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Add 10 in cell A1 and A2

worksheet.getCells().get("A1").putValue(10);

worksheet.getCells().get("A2").putValue(10);

//Add Sum formula in cell D4 but customize it as ---

Cell cell = worksheet.getCells().get("D4");

Style style = cell.getStyle();

style.setCustom("---");

cell.setStyle(style);

//The result of formula will be 20

//but 20 will not be visible because

//the cell is formated as ---

cell.setFormula("=Sum(A1:A2)");

//Calculate the workbook

workbook.calculateFormula();

//Create find options

FindOptions options = new FindOptions();

options.setLookInType(LookInType.ORIGINAL_VALUES);

options.setLookAtType(LookAtType.ENTIRE_CONTENT);

Cell foundCell = null;

Object obj = 20;

//Find 20 which is Sum(A1:A2) and formatted as ---

foundCell = worksheet.getCells().find(obj, foundCell, options);

//Print the found cell

System.out.println(foundCell);

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
