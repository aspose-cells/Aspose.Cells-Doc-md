---
title: Festlegen der gemeinsamen Formel in Aspose.Cells
type: docs
weight: 110
url: /de/net/setting-shared-formula-in-aspose-cells/
---
{{% alert color="primary" %}} 

Angenommen, Sie haben ein Arbeitsblatt, das mit Daten gefüllt ist.

 Sie möchten eine Funktion in B2 hinzufügen, die die Mehrwertsteuer für die erste Datenzeile berechnet. Die Steuer ist**9%** . Die Formel zur Berechnung der Umsatzsteuer lautet:**"=A2*0,09"**. Dieser Artikel erklärt, wie man diese Formel mit Aspose.Cells anwendet.

{{% /alert %}} 

Mit Aspose.Cells können Sie mithilfe der Eigenschaft Cell.Formula eine Formel angeben.

Es gibt zwei Optionen zum Hinzufügen von Formeln zu den anderen Zellen (B3, B4, B5 usw.) in der Spalte.

Machen Sie entweder das, was Sie für die erste Zelle getan haben, indem Sie effektiv die Formel für jede Zelle festlegen und die Zellreferenz entsprechend aktualisieren (A3*0,09, A4*0,09, A5*0,09 usw.). Dazu müssen die Zellbezüge für jede Zeile aktualisiert werden. Es erfordert auch Aspose.Cells, um jede Formel einzeln zu analysieren, was bei großen Tabellenkalkulationen und komplexen Formeln zeitaufwändig sein kann. Es fügt auch zusätzliche Codezeilen hinzu, obwohl Schleifen sie etwas reduzieren können.

 Ein anderer Ansatz ist die Verwendung von a**gemeinsame Formel**. Bei einer freigegebenen Formel werden die Formeln automatisch für die Zellbezüge in jeder Zeile aktualisiert, sodass die Steuer ordnungsgemäß berechnet wird. Die Methode Cell.SetSharedFormula ist effizienter als die erste Methode.

Das folgende Beispiel zeigt, wie es verwendet wird.

**C#**

{{< highlight "csharp" >}}

 string FilePath = @"..\..\..\Sample Files\";

string FileName = FilePath + "Setting Shared Formula.xlsx";

//Instantiate a Workbook from existing file

Workbook workbook = new Workbook(FileName);

//Get the cells collection in the first worksheet

Aspose.Cells.Cells cells = workbook.Worksheets[0].Cells;

//Apply the shared formula in the range i.e.., B2:B14

cells["B2"].SetSharedFormula("=A2*0.09", 13, 1);

//Save the excel file

workbook.Save(FileName, SaveFormat.Xlsx);

{{< /highlight >}}
## **Beispielcode herunterladen**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20OpenXML%20Spreadsheets/OpenXML%20Missing%20Features/Setting%20Shared%20Formula)
## **Laufendes Beispiel herunterladen**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
