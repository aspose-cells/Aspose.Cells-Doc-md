---
title: Rückverfolgung von Präzedenzfällen und Angehörigen in Aspose.Cells
type: docs
weight: 130
url: /de/net/tracing-precedents-and-dependents-in-aspose-cells/
---
{{% alert color="primary" %}} 

Komplexe Finanzarbeitsblätter, insbesondere solche, die gemeinsam entwickelt wurden, können die peinlichsten Fehler verbergen. Das Überprüfen von Formeln auf Genauigkeit und das Auffinden der Fehlerquelle kann schwierig sein, wenn die Formel Vorgängerzellen und abhängige Zellen verwendet.

- **Vorhergehende Zellen** sind Zellen, auf die durch eine Formel in einem anderen Cell verwiesen wird. Wenn beispielsweise Zelle D10 die Formel =B5 enthält, ist Zelle B5 ein Präzedenzfall für Zelle D10.
- **Abhängige Zellen** Formeln enthalten, die auf andere Zellen verweisen. Wenn beispielsweise Zelle D10 die Formel =B5 enthält, ist Zelle D10 von Zelle B5 abhängig.

Um die Tabellenkalkulation leicht lesbar zu machen, möchten Sie möglicherweise deutlich zeigen, welche Zellen in einer Tabellenkalkulation in einer Formel verwendet werden. Ebenso möchten Sie möglicherweise die abhängigen Zellen anderer Zellen extrahieren.

Aspose.Cells ermöglicht es Ihnen, Zellen zu verfolgen und herauszufinden, welche verknüpft sind.

{{% /alert %}} 
## **Ablaufverfolgung Präzedenzfall und abhängiger Cells: Microsoft Excel**
Formeln können sich aufgrund von Änderungen ändern, die von einem Kunden vorgenommen wurden. Wenn beispielsweise Zelle C1 von C3 und C4 abhängig ist, die eine Formel enthalten, und C1 geändert wird (so dass die Formel überschrieben wird), müssen C3 und C4 oder andere Zellen geändert werden, um die Tabelle basierend auf Geschäftsregeln auszugleichen.

Angenommen, C1 enthält die Formel "=(B1*22)/(M2*N32)". Ich möchte die Zellen finden, von denen C1 abhängt, also die vorangegangenen Zellen B1, M2 und N32.

Möglicherweise müssen Sie die Abhängigkeit einer bestimmten Zelle von anderen Zellen nachverfolgen. Wenn Geschäftsregeln in Formeln eingebettet sind, möchten wir die Abhängigkeit herausfinden und einige Regeln darauf basierend ausführen. Wenn der Wert einer bestimmten Zelle geändert wird, welche Zellen im Arbeitsblatt sind von dieser Änderung betroffen?

Microsoft Excel ermöglicht es Benutzern, Präzedenzfälle und Abhängige zu verfolgen.

1.  Auf der**Symbolleiste anzeigen** , auswählen**Formel Auditing**.
 Das Dialogfeld "Formelprüfung" wird angezeigt.
   **Das Dialogfeld "Formelprüfung".** 

![todo: Bild_alt_Text](tracing-precedents-and-dependents-in-aspose-cells_1.png)

1. Präzedenzfälle verfolgen:
1. Wählen Sie die Zelle aus, die die Formel enthält, für die Sie vorangegangene Zellen suchen möchten.
 1. Um einen Verfolgungspfeil zu jeder Zelle anzuzeigen, die direkt Daten für die aktive Zelle bereitstellt, klicken Sie auf**Präzedenzfälle verfolgen** auf der**Formel Auditing** Symbolleiste.
1. Verfolgen Sie Formeln, die auf eine bestimmte Zelle verweisen (abhängige Zellen)
 1. Wählen Sie die Zelle aus, für die Sie die abhängigen Zellen identifizieren möchten.
 1. Um einen Verfolgungspfeil zu jeder Zelle anzuzeigen, die von der aktiven Zelle abhängig ist, klicken Sie in der Symbolleiste „Formelprüfung“ auf Abhängigkeiten verfolgen.
## **Verfolgung von Präzedenzfällen und abhängigen Cells: Aspose.Cells**
### **Präzedenzfälle verfolgen**
Aspose.Cells macht es einfach, Präzedenzzellen zu erhalten. Es kann nicht nur Zellen abrufen, die Daten für einfache Formelpräzedenzfälle bereitstellen, sondern auch Zellen finden, die Daten für komplexe Formelpräzedenzfälle mit benannten Bereichen bereitstellen.

Im folgenden Beispiel wird eine Excel-Vorlagendatei, Book1.xls, verwendet. Die Tabelle enthält Daten und Formeln auf dem ersten Arbeitsblatt.

**Die Eingabetabelle** 

![todo: Bild_alt_Text](tracing-precedents-and-dependents-in-aspose-cells_2.png)

Aspose.Cells stellt die GetPrecedents-Methode der Cell-Klasse bereit, die verwendet wird, um die Präzedenzfälle einer Zelle zu verfolgen. Es gibt eine ReferredAreaCollection zurück. Wie Sie oben sehen können, enthält Zelle B7 in Book1.xls eine Formel „=SUMME(A1:A3)“. Die Zellen A1:A3 sind also die Vorgängerzellen von Zelle B7. Das folgende Beispiel demonstriert das Tracing-Precedence-Feature unter Verwendung der Vorlagendatei Book1.xls.

**C#**

{{< highlight "csharp" >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook("book1.xls");

Cells cells = workbook.Worksheets[0].Cells;

Aspose.Cells.Cell cell = cells["B7"];

//Tracing precedents of the cell B7.

//The return array contains ranges and cells.

ReferredAreaCollection ret = cell.GetPrecedents();

//Printing all the precedent cells' name.

if(ret != null)

{

  for(int m = 0 ; m < ret.Count; m++)

  {

    ReferredArea area = ret[m];

    StringBuilder stringBuilder = new StringBuilder();

    if (area.IsExternalLink)

    {

        stringBuilder.Append("[");

        stringBuilder.Append(area.ExternalFileName);

        stringBuilder.Append("]");

     }

     stringBuilder.Append(area.SheetName);

     stringBuilder.Append("!");

     stringBuilder.Append(CellsHelper.CellIndexToName(area.StartRow, area.StartColumn));

     if (area.IsArea)

      {

          stringBuilder.Append(":");

          stringBuilder.Append(CellsHelper.CellIndexToName(area.EndRow, area.EndColumn));

      }


      Console.WriteLine(stringBuilder.ToString());

   }

}



{{< /highlight >}}
### **Abhängigkeiten verfolgen**
Mit Aspose.Cells können Sie abhängige Zellen in Tabellenkalkulationen abrufen. Aspose.Cells kann nicht nur Zellen abrufen, die Daten zu einer einfachen Formel liefern, sondern auch Zellen finden, die Daten zu komplexen Formelabhängigen mit benannten Bereichen liefern.

Aspose.Cells stellt die GetDependents-Methode der Cell-Klasse bereit, die verwendet wird, um die abhängigen Elemente einer Zelle zu verfolgen. Beispielsweise gibt es in Book1.xlsx Formeln: „=A1+20“ und „=A1+30“ in den B2- bzw. C2-Zellen. Das folgende Beispiel zeigt, wie die abhängigen Elemente für die A1-Zelle mithilfe der Vorlagendatei Book1.xlsx nachverfolgt werden.

**C#**

{{< highlight "csharp" >}}

 string path = "Book1.xlsx";

Workbook workbook = new Workbook(path);

Worksheet worksheet = workbook.Worksheets[0];

var c = worksheet.Cells["A1"];

var dependents = c.GetDependents(true);

foreach (var dependent in dependents)

{

     Debug.WriteLine(string.Format("{0} ---- {1} : {2}", dependent.Worksheet.Name, dependent.Name, dependent.Value));

}

{{< /highlight >}}
## **Laufcode herunterladen**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20VSTO%20Spreadsheets/Aspose.Cells%20Features%20missing%20in%20VSTO/Tracing%20Precedents%20and%20Dependents)
## **Beispielcode herunterladen**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesAsposeCellsForVSTO1.1)

