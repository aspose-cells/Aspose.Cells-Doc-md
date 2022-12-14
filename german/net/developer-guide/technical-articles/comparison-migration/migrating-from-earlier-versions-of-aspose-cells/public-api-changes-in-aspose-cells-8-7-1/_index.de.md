---
title: Öffentlich API Änderungen in Aspose.Cells 8.7.1
type: docs
weight: 240
url: /de/net/public-api-changes-in-aspose-cells-8-7-1/
---
{{% alert color="primary" %}} 

Dieses Dokument beschreibt die Änderungen an Aspose.Cells API von Version 8.7.0 zu 8.7.1, die für Modul-/Anwendungsentwickler von Interesse sein könnten. Es enthält nicht nur neue und aktualisierte öffentliche Methoden, hinzugefügte und entfernte Klassen usw., sondern auch eine Beschreibung aller Änderungen im Verhalten hinter den Kulissen in Aspose.Cells.

{{% /alert %}} 
## **APIs hinzugefügt**
### **LookInType.OriginalValues-Eigenschaft hinzugefügt**
 Aspose.Cells APIs unterstützen bereits die[Daten finden oder suchen](/cells/de/net/find-or-search-data/)Funktion für Tabellenkalkulationen, um bestimmte Inhalte in Zellenwerten und Formeln zu finden. Dieser Funktion fehlte jedoch der Aspekt der auf die Zelle angewendeten Formatierung, die das Erscheinungsbild sowie den Wert des Inhalts ändern kann und folglich den Text unter Verwendung des ursprünglichen Werts nicht durchsuchbar macht. Mit dieser Version der Aspose.Cells-APIs wurde eine weitere Konstante mit dem Namen LookInType.OriginalValues für die Öffentlichkeit API verfügbar gemacht, wodurch die oben beschriebene Situation überwunden werden kann.

{{% alert color="primary" %}} 

 Weitere Einzelheiten zu dieser Funktion finden Sie im ausführlichen Artikel unter[Daten mit Originalwerten suchen](/cells/de/net/search-data-using-original-values/)

{{% /alert %}} 

Es folgt das einfache Nutzungsszenario.

**C#**

{{< highlight "csharp" >}}

 //Create workbook object

Workbook workbook = new Workbook();

//Access first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Add 10 in cell A1 and A2

worksheet.Cells["A1"].PutValue(10);

worksheet.Cells["A2"].PutValue(10);

//Add Sum formula in cell D4 but customize it as ---

Cell cell = worksheet.Cells["D4"];

Style style = cell.GetStyle();

style.Custom = "---";

cell.SetStyle(style);

//The result of formula will be 20

//but 20 will not be visible because

//the cell is formatted as ---

cell.Formula = "=Sum(A1:A2)";

//Calculate the workbook

workbook.CalculateFormula();

//Create find options

FindOptions options = new FindOptions();

options.LookInType = LookInType.OriginalValues;

options.LookAtType = LookAtType.EntireContent;

Cell foundCell = null;

object obj = 20;

//Find 20 which is Sum(A1:A2) and formatted as ---

foundCell = worksheet.Cells.Find(obj, foundCell, options);

//Print the found cell

Console.WriteLine(foundCell);

{{< /highlight >}}


### **OnBeforeColumnFilter-Ereignis für GridWeb hinzugefügt**
Aspose.Cells.GridWeb for .NET 8.7.1 hat das OnBeforeColumnFilter-Ereignis verfügbar gemacht, das als Rückruf für den Filtermechanismus dient, der über die GridWeb-Benutzeroberfläche ausgeführt wird. Wie der Name schon sagt, wird das Ereignis ausgelöst, bevor die Spaltenfilterung angewendet wird, und kann verwendet werden, um die Filterinformationen wie den Spaltenindex und den Wert, auf den der Filter angewendet werden muss, abzurufen.

Ein einfaches Nutzungsszenario sieht wie folgt aus.

**C#**

{{< highlight "csharp" >}}

 protected void GridWeb1_ColumnFilter(object sender, Aspose.Cells.GridWeb.RowColumnEventArgs e)

{

    string msg = "Column index: " + (e.Num) + ", Filtered Value:" + e.Argument;

}

{{< /highlight >}}

{{% alert color="primary" %}} 

Vergessen Sie nicht, das Ereignis im GridWeb-Steuerelement zu registrieren<acw:gridweb OnBeforeColumnFilter="GridWeb1_ColumnFilter"/>

{{% /alert %}}
