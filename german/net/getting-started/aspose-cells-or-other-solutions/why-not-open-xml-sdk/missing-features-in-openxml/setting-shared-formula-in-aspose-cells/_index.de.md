---
title: Geteilte Formel in Aspose.Cells einstellen
type: docs
weight: 110
url: /de/net/setting-shared-formula-in-aspose-cells/
---

{{% alert color="primary" %}} 

Angenommen, Sie haben ein mit Daten gefülltes Arbeitsblatt.

Sie möchten eine Funktion in B2 hinzufügen, die die Umsatzsteuer für die erste Datensatzreihe berechnet. Die Steuer beträgt **9%**. Die Formel zur Berechnung der Umsatzsteuer lautet: **"=A2*0,09"**. In diesem Artikel wird erläutert, wie diese Formel mit Aspose.Cells angewendet wird.

{{% /alert %}} 

Aspose.Cells ermöglicht es Ihnen, eine Formel mithilfe der Cell.Formula-Eigenschaft anzugeben.

Es gibt zwei Möglichkeiten, Formeln zu den anderen Zellen (B3, B4, B5 usw.) in der Spalte hinzuzufügen.

Entweder wiederholen Sie den Vorgang für die erste Zelle und setzen die Formel für jede Zelle, wobei Sie den Zellenverweis entsprechend aktualisieren (A3*0,09, A4*0,09, A5*0,09 usw.). Dadurch müssen die Zellenverweise für jede Zeile aktualisiert werden. Es erfordert auch, dass Aspose.Cells jede Formel individuell analysiert, was bei großen Tabellenblättern und komplexen Formeln zeitaufwändig sein kann. Es fügt auch extra Codezeilen hinzu, obwohl Schleifen diese etwas reduzieren können.

Ein anderer Ansatz ist die Verwendung einer **geteilten Formel**. Mit einer geteilten Formel werden die Formeln automatisch für die Zellenverweise in jeder Zeile aktualisiert, sodass die Steuer ordnungsgemäß berechnet wird. Die Methode Cell.SetSharedFormula ist effizienter als die erste Methode.

Das folgende Beispiel zeigt, wie es verwendet wird.

**C#**

{{< highlight csharp >}}

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
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20OpenXML%20Spreadsheets/OpenXML%20Missing%20Features/Setting%20Shared%20Formula)
## **Laufendes Beispiel herunterladen**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
{{< app/cells/assistant language="csharp" >}}
