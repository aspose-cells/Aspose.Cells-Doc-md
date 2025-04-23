---
title: Öffentliche API Änderungen in Aspose.Cells 8.5.0
type: docs
weight: 170
url: /de/java/public-api-changes-in-aspose-cells-8-5-0/
---

{{% alert color="primary" %}} 

Dieses Dokument beschreibt die Änderungen an der Aspose.Cells-API von Version 8.4.2 auf 8.5.0, die für Modul-/Anwendungsentwickler von Interesse sein können. Es enthält nicht nur neue und aktualisierte öffentliche Methoden, [hinzugefügte Klassen usw.](/cells/de/java/public-api-changes-in-aspose-cells-8-5-0/), sondern auch eine Beschreibung von Änderungen im Verhalten hinter den Kulissen in Aspose.Cells.

{{% /alert %}} 
## **Hinzugefügte APIs**
### **Die ICustomFunction.CalculateCustomFunction-Parameter wurden geändert**
Wenn ein Parameter für die benutzerdefinierte Funktion ein Zellbezug ist, hat die alte Version der Aspose.Cells-APIs den Zellbezug in einen Zellwert oder ein Objektarray aller Zellwerte im bezogenen Bereich umgewandelt. Jedoch ist für viele Funktionen und Benutzer das Zellwert-Array für alle Zellen im bezogenen Bereich nicht erforderlich, sie benötigen nur eine einzelne Zelle, die der Position der Formel entspricht, oder benötigen nur den Verweis selbst anstelle des Zellwerts oder des Wertearrays. In manchen Situationen erhöhte das Abrufen aller Zellwerte sogar das Risiko eines zirkulären Bezugsfehlers.

Um eine solche Anforderung zu unterstützen, hat Aspose.Cells for Java 8.5.0 den Parameterwert in die "paramsList" für den bezogenen Bereich geändert. Seit Version 8.5.0 legt die API einfach das ReferredArea-Objekt in die "paramsList", wenn der entsprechende Parameter ein Bezug ist oder dessen berechnetes Ergebnis ein Bezug ist. Wenn Sie den Verweis selbst benötigen, können Sie direkt ReferredArea verwenden. Wenn Sie einen einzelnen Zellwert aus dem Verweis benötigen, der der Position der Formel entspricht, können Sie die Methode ReferredArea.getValue(rowOffset, int colOffset) verwenden. Wenn Sie das Zellwert-Array für den gesamten Bereich benötigen, können Sie die Methode ReferredArea.getValues verwenden.

Da Aspose.Cells for Java 8.5.0 den ReferredArea in "paramsList" gibt, wird die ReferredAreaCollection in "contextObjects" nicht mehr benötigt (in alten Versionen konnte es nicht immer die parameter der benutzerdefinierten Funktion eins zu eins abbilden), daher wurde diese Version auch aus "contextObjects" entfernt.

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

            o = ra.getValues();

        }

        else

        {

            o = ra.getValue(0, 0);

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
Aspose.Cells for Java 8.5.0 hat die CalculationOptions-Klasse freigelegt, um der Formelberechnungsmaschine mehr Flexibilität und Erweiterbarkeit zu bieten. Die neu hinzugefügte Klasse hat die folgenden Eigenschaften. 

1. CalculationOptions.CalcStackSize: Gibt die Stackgröße für die rekursive Berechnung von Zellen an. -1 gibt an, dass die Berechnung die WorkbookSettings.CalcStackSize des entsprechenden Arbeitsmappen verwendet.
1. CalculationOptions.CustomFunction: Erweitert die Formelberechnungsmaschine mit benutzerdefinierter Formel.
1. CalculationOptions.IgnoreError: Ein boolescher Wert gibt an, ob Fehler beim Berechnen der Formeln ausgeblendet werden sollen, wobei die Fehler aufgrund der nicht unterstützten Funktion, externen Verknüpfung oder mehr sein könnten.
1. CalculationOptions.PrecisionStrategy: CalculationPrecisionStrategy-Typwert, der die Strategie für die Verarbeitung der Genauigkeit der Berechnung angibt.
### **Enumeration CalculationPrecisionStrategy hinzugefügt**
Aspose.Cells for Java 8.5.0 hat die Enumeration CalculationPrecisionStrategy freigelegt, um der Formelberechnungsmaschine mehr Flexibilität zu bieten, um die gewünschten Ergebnisse zu erzielen. Diese Enumeration ermöglicht die Behandlung der Berechnungsgenauigkeit. Aufgrund des Genauigkeitsproblems der IEEE 754 Floating-Point-Arithmetik können einige scheinbar einfache Formeln möglicherweise nicht berechnet werden, um die erwarteten Ergebnisse zu liefern. Daher hat die neueste API-Build die folgenden Felder freigelegt, um die gewünschten Ergebnisse gemäß der Auswahl zu erhalten.

1. CalculationPrecisionStrategy.DECIMAL: Verwendet Dezimalzahl als Operand, wo möglich, und ist aus Effizienzgründen am ineffizientesten.
1. CalculationPrecisionStrategy.ROUND: Rundet die Berechnungsergebnisse gemäß der signifikanten Ziffer.
1. CalculationPrecisionStrategy.NONE: Es wird keine Strategie angewendet, daher verwendet die Berechnungsmaschine während der Berechnung den ursprünglichen Double-Wert als Operand und gibt das Ergebnis direkt zurück. Diese Option ist am effizientesten und gilt für die meisten Fälle.
### **Hinzugefügte Methoden zur Verwendung von CalculationOptions**
Mit der Veröffentlichung von v8.5.0 hat die Aspose.Cells-API Überladungsversionen der calculateFormula-Methode hinzugefügt, wie unten aufgeführt.

- Workbook.calculateFormula(CalculationOptions)
- Worksheet.calculateFormula(CalculationOptions options, bool recursive)
- Cell.calculate(CalculationOptions)
### **Enumerationsfeld PasteType.ROW_HEIGHTS hinzugefügt**
Aspose.Cells-APIs haben das Enumerationsfeld PasteType.ROW_HEIGHTS für das Kopieren der Zeilenhöhen beim Kopieren der Bereiche bereitgestellt. Wenn die PasteOptions.PasteType-Eigenschaft auf ((PasteType.ROW_HEIGHTS} eingestellt wird, werden die Höhen aller Zeilen innerhalb des Quellbereichs in den Zielbereich kopiert.

**Java**

{{< highlight csharp >}}

 //Create workbook object

Workbook workbook = new Workbook();

//Source worksheet

Worksheet srcSheet = workbook.getWorksheets().get(0);

//Add destination worksheet

Worksheet dstSheet = workbook.getWorksheets().add("Destination Sheet");

//Set the row height of the 4th row

//This row height will be copied to destination range

srcSheet.getCells().setRowHeight(3, 50);

//Create source range to be copied

Range srcRange = srcSheet.getCells().createRange("A1:D10");

//Create destination range in destination worksheet

Range dstRange = dstSheet.getCells().createRange("A1:D10");

//PasteOptions, we want to copy row heights of source range to destination range

PasteOptions opts = new PasteOptions();

opts.setPasteType(PasteType.ROW_HEIGHTS);

//Copy source range to destination range with paste options

dstRange.copy(srcRange, opts);

//Write informative message in cell D4 of destination worksheet

dstSheet.getCells().get("D4").putValue("Row heights of source range copied to destination range");

//Save the workbook in xlsx format

workbook.save("output.xlsx", SaveFormat.XLSX);

{{< /highlight >}}
### **Eigenschaft SheetRender.PageScale hinzugefügt**
Wenn Sie die Seiteneinrichtungsskalierung mit der Option **Passen Sie n Seite(n) in der Breite um m in der Höhe an.**, festlegen, berechnet Microsoft Excel den Skalierungsfaktor der Seiteneinrichtung. Das Gleiche kann mit der von Aspose.Cells for Java 8.5.0 freigegebenen SheetRender.PageScale-Eigenschaft erreicht werden. Diese Eigenschaft gibt einen doppelten Wert zurück, der in einen Prozentwert umgerechnet werden kann. Wenn beispielsweise 0,507968245 zurückgegeben wird, bedeutet dies, dass der Skalierungsfaktor 51 % beträgt.

**Java**

{{< highlight csharp >}}

 //Create workbook object

Workbook workbook = new Workbook();

//Access first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Put some data in these cells

worksheet.getCells().get("A4").putValue("Test");

worksheet.getCells().get("S4").putValue("Test");

//Set paper size

worksheet.getPageSetup().setPaperSize(PaperSizeType.PAPER_A_4);

//Set fit to pages wide as 1

worksheet.getPageSetup().setFitToPagesWide(1);

//Calculate page scale via sheet render

SheetRender sr = new SheetRender(worksheet, new ImageOrPrintOptions());

//Write the page scale value

System.out.println(sr.getPageScale());

{{< /highlight >}}
### **Aufzählung CellValueFormatStrategy hinzugefügt**
Aspose.Cells for Java 8.5.0 hat eine neue Aufzählung CellValueFormatStrategy hinzugefügt, um Situationen zu behandeln, in denen Zellenwerte mit oder ohne Formatierung extrahiert werden müssen. Aufzählung CellValueFormatStrategy mit folgenden Feldern. 

1. CellValueFormatStrategy.CELL_STYLE: Nur mit der ursprünglichen Formatierung der Zelle formatiert.
1. CellValueFormatStrategy.DISPLAY_STYLE: Mit der angezeigten Formatierung der Zelle formatiert.
1. CellValueFormatStrategy.NONE: Nicht formatiert.
### **Methode Cell.getStringValue hinzugefügt**
Um die Aufzählung CellValueFormatStrategy zu verwenden, hat v8.5.0 die Methode Cell.getStringValue freigegeben, die einen Parameter vom Typ CellValueFormatStrategy akzeptieren und den Wert je nach angegebener Option zurückgeben könnte.

Im folgenden Codeausschnitt wird gezeigt, wie die neu freigegebene Methode Cells.getStringValue verwendet werden kann.

**Java**

{{< highlight csharp >}}

 //Create workbook

Workbook workbook = new Workbook();

//Access first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Access cell A1

Cell cell = worksheet.getCells().get("A1");

//Put value inside the cell

cell.putValue(0.012345);

//Format the cell that it should display 0.01 instead of 0.012345

Style style = cell.getStyle();

style.setNumber(2);

cell.setStyle(style);

//Get string value as Cell Style

String value = cell.getStringValue(CellValueFormatStrategy.CELL_STYLE);

System.out.println(value);

//Get string value without any formatting

value = cell.getStringValue(CellValueFormatStrategy.NONE);

System.out.println(value);

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
