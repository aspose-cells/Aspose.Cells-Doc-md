---
title: Öffentlich API Änderungen in Aspose.Cells 8.7.1
type: docs
weight: 250
url: /de/java/public-api-changes-in-aspose-cells-8-7-1/
---
{{% alert color="primary" %}} 

Dieses Dokument beschreibt die Änderungen an Aspose.Cells API von Version 8.7.0 zu 8.7.1, die für Modul-/Anwendungsentwickler von Interesse sein könnten. Es enthält nicht nur neue und aktualisierte öffentliche Methoden, hinzugefügte und entfernte Klassen usw., sondern auch eine Beschreibung aller Änderungen im Verhalten hinter den Kulissen in Aspose.Cells.

{{% /alert %}} 
## **APIs hinzugefügt**
### **LookInType.ORIGINAL_VALUES-Eigenschaft hinzugefügt**
 Aspose.Cells APIs unterstützen bereits die[Daten finden oder suchen](/cells/de/java/find-or-search-data/)Funktion für Tabellenkalkulationen, um bestimmte Inhalte in Zellenwerten und Formeln zu finden. Dieser Funktion fehlte jedoch der Aspekt der auf die Zelle angewendeten Formatierung, die das Erscheinungsbild sowie den Wert des Inhalts ändern kann und folglich den Text unter Verwendung des ursprünglichen Werts nicht durchsuchbar macht. Mit dieser Version der Aspose.Cells-APIs wurde eine weitere Konstante mit dem Namen LookInType.ORIGINAL_VALUES für die Öffentlichkeit API verfügbar gemacht, wodurch die oben beschriebene Situation überwunden werden kann.

{{% alert color="primary" %}} 

 Weitere Einzelheiten zu dieser Funktion finden Sie im ausführlichen Artikel unter[Daten mit Originalwerten suchen](https://docs.aspose.com/cells/java/search-data-using-original-values/)

{{% /alert %}} 

Es folgt das einfache Nutzungsszenario.

**Java**

{{< highlight "csharp" >}}

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
