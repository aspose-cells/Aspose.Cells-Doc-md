---
title: Öffentliche API Änderungen in Aspose.Cells 8.7.1
type: docs
weight: 240
url: /de/net/public-api-changes-in-aspose-cells-8-7-1/
---

{{% alert color="primary" %}} 

Dieses Dokument beschreibt die Änderungen an der Aspose.Cells-API von Version 8.7.0 auf 8.7.1, die für Modul-/Anwendungs-Entwickler interessant sein könnten. Es umfasst nicht nur neue und aktualisierte öffentliche Methoden, hinzugefügte & entfernte Klassen usw., sondern auch eine Beschreibung von Änderungen im Verhalten hinter den Kulissen in Aspose.Cells.

{{% /alert %}} 
## **Hinzugefügte APIs**
### **Added LookInType.OriginalValues-Eigenschaft**
Aspose.Cells APIs unterstützen bereits das Feature zum Suchen von Daten in Tabellenkalkulationen, um bestimmte Inhalte in Zellwert & Formel zu finden. Dieses Feature mangelte jedoch an dem Aspekt der auf die Zelle angewendeten Formatierung, die das Erscheinungsbild sowie den Wert der Inhalte ändern kann und folglich den Text unsearchable macht, indem der Originalwert verwendet wird. Mit dieser Version der Aspose.Cells APIs wurde eine weitere Konstante namens LookInType.OriginalValues in die öffentliche API freigelegt, die es ermöglicht, die oben diskutierte Situation zu überwinden.

{{% alert color="primary" %}} 

Für weitere Details zu diesem Feature lesen Sie bitte den ausführlichen Artikel zu [Suchen von Daten mithilfe der Originalwerte](/cells/de/net/search-data-using-original-values/)

{{% /alert %}} 

Im Folgenden wird das einfache Anwendungsszenario beschrieben.

**C#**

{{< highlight csharp >}}

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


### **Hinzugefügtes OnBeforeColumnFilter-Ereignis für GridWeb**
Aspose.Cells.GridWeb für .NET 8.7.1 hat das OnBeforeColumnFilter-Ereignis freigegeben, das als Rückrufmechanismus für den Filtermechanismus über die GridWeb-Benutzeroberfläche dient. Wie der Name schon sagt, wird das Ereignis ausgelöst, bevor die Spaltenfilterung angewendet wird, und kann verwendet werden, um die Filterinformationen wie Spaltenindex und Wert zu erhalten, auf die der Filter angewendet werden soll.

Das einfache Anwendungsszenario sieht wie folgt aus.

**C#**

{{< highlight csharp >}}

 protected void GridWeb1_ColumnFilter(object sender, Aspose.Cells.GridWeb.RowColumnEventArgs e)

{

    string msg = "Column index: " + (e.Num) + ", Filtered Value:" + e.Argument;

}

{{< /highlight >}}

{{% alert color="primary" %}} 

Do not forget to register the event to GridWeb control <acw:gridweb OnBeforeColumnFilter="GridWeb1_ColumnFilter"/>

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
