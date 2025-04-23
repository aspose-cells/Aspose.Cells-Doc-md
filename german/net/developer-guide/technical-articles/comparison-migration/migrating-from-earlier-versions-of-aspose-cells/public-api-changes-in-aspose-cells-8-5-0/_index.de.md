---
title: Öffentliche API Änderungen in Aspose.Cells 8.5.0
type: docs
weight: 160
url: /de/net/public-api-changes-in-aspose-cells-8-5-0/
---

{{% alert color="primary" %}} 

Dieses Dokument beschreibt die Änderungen an der Aspose.Cells API von Version 8.4.2 auf 8.5.0, die für Modul-/Anwendungs-Entwickler von Interesse sein können. Es umfasst nicht nur neue und aktualisierte öffentliche Methoden, [hinzugefügte Klassen usw.](/cells/de/net/public-api-changes-in-aspose-cells-8-5-0/), sondern auch eine Beschreibung etwaiger Änderungen im Verhalten hinter den Kulissen in Aspose.Cells.

{{% /alert %}} 
## **Hinzugefügte APIs**
### **Die ICustomFunction.CalculateCustomFunction-Parameter wurden geändert**
Wenn ein Parameter für die benutzerdefinierte Funktion ein Zellbezug ist, hat die alte Version der Aspose.Cells-APIs den Zellbezug in einen Zellwert oder ein Objektarray aller Zellwerte im bezogenen Bereich umgewandelt. Jedoch ist für viele Funktionen und Benutzer das Zellwert-Array für alle Zellen im bezogenen Bereich nicht erforderlich, sie benötigen nur eine einzelne Zelle, die der Position der Formel entspricht, oder benötigen nur den Verweis selbst anstelle des Zellwerts oder des Wertearrays. In manchen Situationen erhöhte das Abrufen aller Zellwerte sogar das Risiko eines zirkulären Bezugsfehlers.

Um solche Anforderungen zu unterstützen, hat Aspose.Cells for .NET 8.5.0 den Parameterwert auf "paramsList" für den betreffenden Bereich geändert. Seit v8.5.0 platziert die API das ReferredArea-Objekt einfach in die "paramsList", wenn der entsprechende Parameter ein Verweis ist oder sein berechnetes Ergebnis ein Verweis ist. Wenn Sie den Verweis selbst benötigen, können Sie ReferredArea direkt verwenden. Wenn Sie einen einzelnen Zellwert aus dem Verweis, der der Position der Formel entspricht, erhalten müssen, können Sie die Methode ReferredArea.GetValue(rowOffset, int colOffset) verwenden. Wenn Sie ein Zellwerte-Array für den gesamten Bereich benötigen, können Sie die Methode ReferredArea.GetValues verwenden.

Da Aspose.Cells for .NET 8.5.0 das ReferredArea in "paramsList" liefert, wird ReferredAreaCollection in "contextObjects" nicht mehr benötigt (in älteren Versionen konnte sie nicht immer eine eins-zu-eins-Zuordnung zu den Parametern der benutzerdefinierten Funktion bereitstellen), daher wurde es jetzt auch aus "contextObjects" entfernt.

Diese Änderung erfordert einige Änderungen im Code der Implementierung für ICustomFunction, wenn Sie den Wert/Werte des Referenzparameters benötigen.

**Alte Implementierung**

{{< highlight csharp >}}

 public object CalculateCustomFunction(string functionName, ArrayList paramsList, ArrayList contextObjects)

{

    ...

    object o = paramsList[i];

    if (o is Array)

    {

        ...

    }

    else if...

    ...

}

{{< /highlight >}}

**Neue Implementierung**

{{< highlight csharp >}}

 public object CalculateCustomFunction(string functionName, ArrayList paramsList, ArrayList contextObjects)

{

    ...

    object o = paramsList[i];

    if(o is ReferredArea) //fetch data from reference

    {

        ReferredArea ra = (ReferredArea)o;

        if(ra.IsArea)

        {

            o = ra.GetValues();

        }

        else

        {

            o = ra.GetValue(0, 0);

        }

    }

    if (o is Array)

    {

        ...

    }

    else if...

    ...

}

{{< /highlight >}}


### **Klasse CalculationOptions hinzugefügt**
Aspose.Cells for .NET 8.5.0 hat die CalculationOptions-Klasse freigegeben, um die Flexibilität und Erweiterbarkeit des Formelberechnungsmotors zu erhöhen. Die neu hinzugefügte Klasse verfügt über die folgenden Eigenschaften.

1. CalculationOptions.CalcStackSize: Gibt die Stackgröße für die rekursive Berechnung von Zellen an. -1 gibt an, dass die Berechnung die WorkbookSettings.CalcStackSize des entsprechenden Arbeitsmappen verwendet.
1. CalculationOptions.CustomFunction: Erweitert die Formelberechnungsmaschine mit benutzerdefinierter Formel.
1. CalculationOptions.IgnoreError: Ein boolescher Wert gibt an, ob Fehler beim Berechnen der Formeln ausgeblendet werden sollen, wobei die Fehler aufgrund der nicht unterstützten Funktion, externen Verknüpfung oder mehr sein könnten.
1. CalculationOptions.PrecisionStrategy: CalculationPrecisionStrategy-Typwert, der die Strategie für die Verarbeitung der Genauigkeit der Berechnung angibt.
### **Enumeration CalculationPrecisionStrategy hinzugefügt**
Aspose.Cells for .NET 8.5.0 hat die Enumeration CalculationPrecisionStrategy freigegeben, um dem Formelberechnungsmotor mehr Flexibilität für die gewünschten Ergebnisse zu bieten. Diese Enumeration steuert die Behandlung der Berechnungsgenauigkeit. Aufgrund des Genauigkeitsproblems von IEEE 754 Floating-Point-Arithmetik werden einige scheinbar einfache Formeln möglicherweise nicht mit den erwarteten Ergebnissen berechnet, daher hat die neueste API-Build die folgenden Felder freigegeben, um die gewünschten Ergebnisse je nach Auswahl zu erhalten.

1. CalculationPrecisionStrategy.Decimal: Verwendet Dezimalzahl als Operand, wo möglich, und ist aus Leistungssicht am ineffizientesten.
1. CalculationPrecisionStrategy.Round: Rundet die Berechnungsergebnisse entsprechend der signifikanten Ziffer.
1. CalculationPrecisionStrategy.None: Es wird keine Strategie angewendet, daher verwendet der Motor während der Berechnung den ursprünglichen doppelten Wert als Operand und gibt das Ergebnis direkt zurück. Diese Option ist am effizientesten und gilt für die meisten Fälle.
### **Hinzugefügte Methoden zur Verwendung von CalculationOptions**
Mit der Veröffentlichung von v8.5.0 hat die Aspose.Cells-API Überlastversionen der CalculateFormula-Methode hinzugefügt, wie unten aufgeführt.

- Workbook.CalculateFormula(CalculationOptions)
- Worksheet.CalculateFormula(CalculationOptions options, bool recursive)
- Cell.Calculate(CalculationOptions)
### **Enumerationsfeld PasteType.RowHeights hinzugefügt**
Die Aspose.Cells-APIs haben das Enumerationsfeld PasteType.RowHeights für das Kopieren der Zeilenhöhen beim Kopieren der Bereiche bereitgestellt. Durch Festlegen der PasteOptions.PasteType-Eigenschaft auf ((PasteType.RowHeights}} werden die Höhen aller Zeilen im Quellbereich in den Zielbereich kopiert.

**C#**

{{< highlight csharp >}}

 //Create workbook object

Workbook workbook = new Workbook();

//Source worksheet

Worksheet srcSheet = workbook.Worksheets[0];

//Add destination worksheet

Worksheet dstSheet = workbook.Worksheets.Add("Destination Sheet");

//Set the row height of the 4th row

//This row height will be copied to destination range

srcSheet.Cells.SetRowHeight(3, 50);

//Create source range to be copied

Range srcRange = srcSheet.Cells.CreateRange("A1:D10");

//Create destination range in destination worksheet

Range dstRange = dstSheet.Cells.CreateRange("A1:D10");

//PasteOptions, we want to copy row heights of source range to destination range

PasteOptions opts = new PasteOptions();

opts.PasteType = PasteType.RowHeights;

//Copy source range to destination range with paste options

dstRange.Copy(srcRange, opts);

//Write informative message in cell D4 of destination worksheet

dstSheet.Cells["D4"].PutValue("Row heights of source range copied to destination range");

//Save the workbook in xlsx format

workbook.Save("output.xlsx", SaveFormat.Xlsx);

{{< /highlight >}}


### **Eigenschaft SheetRender.PageScale hinzugefügt**
Wenn Sie die Seiteneinrichtungsskalierung mit der Option **Passen an n Seiten breit und m Seiten hoch** festlegen, berechnet Microsoft Excel den Skalierungsfaktor der Seiteneinrichtung. Dasselbe kann mit der von Aspose.Cells for .NET 8.5.0 freigegebenen Eigenschaft SheetRender.PageScale erreicht werden. Diese Eigenschaft gibt einen Dezimalwert zurück, der in einen Prozentwert umgewandelt werden kann. Wenn beispielsweise 0,507968245 zurückgegeben wird, bedeutet dies, dass der Skalierungsfaktor 51% beträgt.

**C#**

{{< highlight csharp >}}

 //Create workbook object

Workbook workbook = new Workbook();

//Access first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Put some data in these cells

worksheet.Cells["A4"].PutValue("Test");

worksheet.Cells["S4"].PutValue("Test");

//Set paper size

worksheet.PageSetup.PaperSize = PaperSizeType.PaperA4;

//Set fit to pages wide as 1

worksheet.PageSetup.FitToPagesWide = 1;

//Calculate page scale via sheet render

SheetRender sr = new SheetRender(worksheet, new ImageOrPrintOptions());

//Convert page scale double value to percentage

string strPageScale = sr.PageScale.ToString("0%");

//Write the page scale value

Console.WriteLine(strPageScale);

{{< /highlight >}}


### **Aufzählung CellValueFormatStrategy hinzugefügt**
Aspose.Cells for .NET 8.5.0 hat eine neue Enumeration CellValueFormatStrategy hinzugefügt, um Situationen zu behandeln, in denen Zellenwerte mit oder ohne Formatierung extrahiert werden müssen. Enumeration CellValueFormatStrategy hat folgende Felder.

1. CellValueFormatStrategy.CellStyle: Nur mit der Originalformatierung der Zelle formatiert.
1. CellValueFormatStrategy.DisplayStyle: Mit der angezeigten Zellformatierung formatiert.
1. CellValueFormatStrategy.None: Nicht formatiert.
### **Hinzugefügt Cell.GetStingValue Methode**
Um die Enumeration CellValueFormatStrategy zu verwenden, hat v8.5.0 die Methode Cell.GetStingValue freigegeben, die einen Parameter vom Typ CellValueFormatStrategy akzeptieren kann und den Wert je nach gewählter Option zurückgibt.

Der folgende Code-Schnipsel zeigt, wie die neu freigegebene Methode Cells.GetStingValue verwendet wird.

**C#**

{{< highlight csharp >}}

 //Create workbook

Workbook workbook = new Workbook();

//Access first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Access cell A1

Cell cell = worksheet.Cells["A1"];

//Put value inside the cell

cell.PutValue(0.012345);

//Format the cell that it should display 0.01 instead of 0.012345

Style style = cell.GetStyle();

style.Number = 2;

cell.SetStyle(style);

//Get string value as Cell Style

string value = cell.GetStingValue(CellValueFormatStrategy.CellStyle);

Console.WriteLine(value);

//Get string value without any formatting

value = cell.GetStingValue(CellValueFormatStrategy.None);

Console.WriteLine(value);

{{< /highlight >}}


### **Hinzugefügt ExportTableOptions.FormatStrategy Eigenschaft**
Aspose.Cells for .NET 8.5.0 hat die Eigenschaft ExportTableOptions.FormatStrategy für Benutzer freigegeben, die die Daten mit oder ohne Formatierung in eine DataTable exportieren möchten. Diese Eigenschaft verwendet die Enumeration CellValueFormatStrategy und exportiert die Daten entsprechend der spezifizierten Option.

Der folgende Code erklärt die Verwendung der Eigenschaft ExportTableOptions.FormatStrategy.

**C#**

{{< highlight csharp >}}

 //Create workbook

Workbook workbook = new Workbook();

//Access first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Access cell A1

Cell cell = worksheet.Cells["A1"];

//Put value inside the cell

cell.PutValue(0.012345);

//Format the cell that it should display 0.01 instead of 0.012345

Style style = cell.GetStyle();

style.Number = 2;

cell.SetStyle(style);

//Print the cell values as it displays in excel

Console.WriteLine("Cell String Value: " + cell.StringValue);

//Print the cell value without any format

Console.WriteLine("Cell String Value without Format: " + cell.StringValueWithoutFormat);

//Export Data Table Options with FormatStrategy as CellStyle

ExportTableOptions opts = new ExportTableOptions();

opts.ExportAsString = true;

opts.FormatStrategy = CellValueFormatStrategy.CellStyle;

//Export Data Table

DataTable dt = worksheet.Cells.ExportDataTable(0, 0, 1, 1, opts);

//Print the value of very first cell

Console.WriteLine("Export Data Table with Format Strategy as Cell Style: " + dt.Rows[0][0].ToString());

//Export Data Table Options with FormatStrategy as None

opts.FormatStrategy = CellValueFormatStrategy.None;

dt = worksheet.Cells.ExportDataTable(0, 0, 1, 1, opts);

//Print the value of very first cell

Console.WriteLine("Export Data Table with Format Strategy as None: " + dt.Rows[0][0].ToString());

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
