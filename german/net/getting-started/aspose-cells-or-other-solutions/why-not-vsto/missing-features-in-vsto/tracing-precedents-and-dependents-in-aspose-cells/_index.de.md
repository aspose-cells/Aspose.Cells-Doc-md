---
title: Vorgänger und Abhängigkeiten in Aspose.Cells nachverfolgen
type: docs
weight: 130
url: /de/net/tracing-precedents-and-dependents-in-aspose-cells/
---

{{% alert color="primary" %}} 

Komplexe Finanzarbeitsblätter, insbesondere solche, die in Zusammenarbeit entwickelt wurden, können die peinlichsten Fehler verbergen. Formeln auf ihre Genauigkeit zu überprüfen und die Fehlerquelle zu finden, kann schwierig sein, wenn die Formel Vorgänger- und Abhängigenzellen verwendet.

- **Vorgängerzellen** sind Zellen, auf die in einer anderen Zelle eine Formel verweist. Wenn beispielsweise Zelle D10 die Formel =B5 enthält, dann ist die Zelle B5 ein Vorgänger von Zelle D10.
- **Abhängige Zellen** enthalten Formeln, die sich auf andere Zellen beziehen. Wenn beispielsweise Zelle D10 die Formel =B5 enthält, dann ist Zelle D10 abhängig von Zelle B5.

Um die Tabelle übersichtlicher zu gestalten, möchten Sie möglicherweise klar zeigen, welche Zellen in einer Tabelle in einer Formel verwendet werden. Ebenso möchten Sie die abhängigen Zellen anderer Zellen extrahieren.

Aspose.Cells ermöglicht es Ihnen, die Zellen zu verfolgen und herauszufinden, welche verknüpft sind.

{{% /alert %}} 
## **Vorgänger- und Abhängige Zellen verfolgen: Microsoft Excel**
Formeln können sich aufgrund von Änderungen, die von einem Client vorgenommen wurden, ändern. Beispielsweise, wenn Zelle C1 von C3 und C4 abhängt und eine Formel enthält, und Zelle C1 geändert wird (also die Formel überschrieben wird), dann müssen sich C3 und C4 oder andere Zellen ändern, um das Tabellenblatt gemäß den Geschäftsregeln auszugleichen.

Angenommen, C1 enthält die Formel "=(B1*22)/(M2*N32)". Ich möchte die Zellen finden, von denen C1 abhängt, also die Vorgängerzellen B1, M2 und N32.

Möglicherweise müssen Sie die Abhängigkeit einer bestimmten Zelle zu anderen Zellen nachverfolgen. Wenn Geschäftsregeln in Formeln eingebettet sind, möchten wir die Abhängigkeit herausfinden und einige Regeln entsprechend ausführen. Ebenso, wenn der Wert einer bestimmten Zelle geändert wird, welche Zellen im Arbeitsblatt sind von dieser Änderung betroffen?

Microsoft Excel ermöglicht es Benutzern, Vorgänger und Abhängige zu verfolgen.

1. Wählen Sie in der **Ansichts-Symbolleiste** **Formelüberwachung** aus.
   Der Dialog zur Formelüberwachung wird angezeigt. 
   **Der Dialog zur Formelüberwachung** 

![todo:image_alt_text](tracing-precedents-and-dependents-in-aspose-cells_1.png)

1. Vorgänger verfolgen:
   1. Wählen Sie die Zelle aus, die die Formel enthält, für die Sie Vorgängerzellen finden möchten.
   1. Um an jede Zelle einen Tracer-Pfeil anzuzeigen, die direkt Daten an die aktive Zelle bereitstellt, klicken Sie auf **Vorgänger verfolgen** auf der **Formelüberwachungs**-Symbolleiste.
1. Formeln verfolgen, die auf eine bestimmte Zelle verweisen (Abhängige)
   1. Wählen Sie die Zelle aus, für die Sie die abhängigen Zellen identifizieren möchten.
   1. Um an jede Zelle, die von der aktiven Zelle abhängig ist, einen Tracer-Pfeil anzuzeigen, klicken Sie auf **Abhängige verfolgen** auf der **Formelüberwachungs**-Symbolleiste.
## **Vorgänger- und Abhängige Zellen verfolgen: Aspose.Cells**
### **Vorgänger verfolgen**
Mit Aspose.Cells können Sie Vorgängerzellen problemlos abrufen. Es kann nicht nur Zellen abrufen, die Daten zu einfachen Formelvorgängern liefern, sondern auch Zellen finden, die Daten zu Vorgängern komplexer Formeln mit benannten Bereichen liefern.

Im folgenden Beispiel wird eine Vorlagen-Excel-Datei, Book1.xls, verwendet. Das Arbeitsblatt enthält Daten und Formeln.

**Die Eingabe-Arbeitsmappe** 

![todo:image_alt_text](tracing-precedents-and-dependents-in-aspose-cells_2.png)

Aspose.Cells bietet die Methode GetPrecedents der Zellenklasse zum Verfolgen von Zellenvorgängern. Es gibt eine referenzierte Bereichssammlung zurück. Wie oben zu sehen ist, enthält die Zelle B7 in Book1.xls die Formel "=SUM(A1:A3)". Daher sind die Zellen A1:A3 die Vorgängerzellen der Zelle B7. Das folgende Beispiel zeigt die Verfolgung der Vorgängerzellen mit der Vorlagendatei Book1.xls.

**C#**

{{< highlight csharp >}}

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
### **Abhängige verfolgen**
Aspose.Cells bietet die Methode GetDependents der Zellenklasse zum Verfolgen von Zellennachfolgern. Zum Beispiel gibt es in Book1.xlsx die Formeln "=A1+20" und "=A1+30" in den Zellen B2 und C2. Das folgende Beispiel zeigt, wie man die Nachfolgerzellen für die Zelle A1 mit der Vorlagendatei Book1.xlsx verfolgen kann.

Aspose.Cells bietet die GetDependents-Methode der Zellenklasse, um die Abhängigen einer Zelle zu verfolgen. Zum Beispiel gibt es in Book1.xlsx Formeln: "=A1+20" und "=A1+30" in den Zellen B2 und C2. Das folgende Beispiel zeigt, wie die Abhängigen für die Zelle A1 anhand der Vorlagendatei Book1.xlsx verfolgt werden.

**C#**

{{< highlight csharp >}}

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
## **Laufenden Code herunterladen**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20VSTO%20Spreadsheets/Aspose.Cells%20Features%20missing%20in%20VSTO/Tracing%20Precedents%20and%20Dependents)
## **Beispielcode herunterladen**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesAsposeCellsForVSTO1.1)

