---
title: Öffentlich API Änderungen in Aspose.Cells 8.5.0
type: docs
weight: 170
url: /de/java/public-api-changes-in-aspose-cells-8-5-0/
---
{{% alert color="primary" %}} 

 Dieses Dokument beschreibt die Änderungen an Aspose.Cells API von Version 8.4.2 zu 8.5.0, die für Modul-/Anwendungsentwickler von Interesse sein könnten. Es enthält nicht nur neue und aktualisierte öffentliche Methoden,[zusätzliche Klassen usw.](/cells/de/java/public-api-changes-in-aspose-cells-8-5-0/), sondern auch eine Beschreibung etwaiger Verhaltensänderungen hinter den Kulissen in Aspose.Cells.

{{% /alert %}} 
## **APIs hinzugefügt**
### **Die ICustomFunction.CalculateCustomFunction-Parameter wurden geändert**
Wenn ein Parameter für die benutzerdefinierte Funktion ein Zellbezug ist, wurden APIs in der alten Version Aspose.Cells verwendet, um den Zellbezug in einen Zellwert oder ein Objekt-Array aller Zellwerte im referenzierten Bereich zu konvertieren. Für viele Funktionen und Benutzer ist jedoch das Zellenwerte-Array für alle Zellen im referenzierten Bereich nicht erforderlich, sie benötigen nur eine einzelne Zelle, die der Position der Formel entspricht, oder benötigen nur die Referenz selbst anstelle des Zellenwerts oder des Wertearrays . In einigen Situationen erhöhte das Abrufen aller Zellenwerte sogar das Risiko eines zirkulären Referenzfehlers.

Um solche Anforderungen zu unterstützen, hat Aspose.Cells for Java 8.5.0 den Parameterwert in „paramsList“ für den angegebenen Bereich geändert. Seit v8.5.0 fügt API das ReferredArea-Objekt einfach in die „paramsList“ ein, wenn der entsprechende Parameter eine Referenz ist oder sein berechnetes Ergebnis eine Referenz ist. Wenn Sie die Referenz selbst benötigen, können Sie die ReferredArea direkt verwenden. Wenn Sie einen einzelnen Zellenwert aus der Referenz abrufen müssen, die der Position der Formel entspricht, können Sie die Methode ReferredArea.getValue(rowOffset, int colOffset) verwenden. Wenn Sie ein Zellenwerte-Array für den gesamten Bereich benötigen, können Sie die Methode ReferredArea.getValues verwenden.

Jetzt, da Aspose.Cells for Java 8.5.0 die ReferredArea in „paramsList“ angibt, wird die ReferredAreaCollection in „contextObjects“ nicht mehr benötigt (in alten Versionen konnte sie den Parametern der benutzerdefinierten Funktion nicht immer eine Eins-zu-Eins-Zuordnung geben), Daher hat diese Version es jetzt auch aus "contextObjects" entfernt.

Diese Änderung erfordert geringfügige Änderungen am Code der Implementierung für ICustomFunction, wenn Sie den Wert/die Werte des Referenzparameters benötigen.

**Alte Implementierung**

{{< highlight "csharp" >}}

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

{{< highlight "csharp" >}}

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
### **Klassenberechnungsoptionen hinzugefügt**
 Aspose.Cells for Java 8.5.0 hat die CalculationOptions-Klasse verfügbar gemacht, um mehr Flexibilität und Erweiterbarkeit für die Formelberechnungs-Engine hinzuzufügen. Die neu hinzugefügte Klasse hat die folgenden Eigenschaften.

1. CalculationOptions.CalcStackSize: Gibt die Stapelgröße für die rekursive Berechnung von Zellen an. -1 gibt an, dass die Berechnung WorkbookSettings.CalcStackSize der entsprechenden Arbeitsmappe verwendet.
1. CalculationOptions.CustomFunction: Erweitert die Formelberechnungs-Engine um eine benutzerdefinierte Formel.
1. CalculationOptions.IgnoreError: Der Wert vom Typ Boolean gibt an, ob Fehler beim Berechnen der Formeln ausgeblendet werden sollen, wobei die Fehler auf die nicht unterstützte Funktion, den externen Link oder mehr zurückzuführen sein könnten.
1. CalculationOptions.PrecisionStrategy: CalculationPrecisionStrategy-Typwert, der die Strategie für die Verarbeitungsgenauigkeit der Berechnung angibt.
### **AufzählungsberechnungPrecisionStrategy Hinzugefügt**
Aspose.Cells for Java 8.5.0 hat die Enumeration CalculationPrecisionStrategy verfügbar gemacht, um der Formelberechnungs-Engine mehr Flexibilität zu verleihen, um die gewünschten Ergebnisse zu erzielen. Diese Aufzählung behandelt die Handhabung der Berechnungsgenauigkeit. Aufgrund des Genauigkeitsproblems der IEEE 754-Gleitkommaarithmetik werden einige scheinbar einfache Formeln möglicherweise nicht berechnet, um die erwarteten Ergebnisse zu liefern. Daher hat der neueste API-Build die folgenden Felder verfügbar gemacht, um die gewünschten Ergebnisse gemäß der Auswahl zu erhalten.

1. CalculationPrecisionStrategy.DECIMAL: Verwendet nach Möglichkeit Dezimalzahlen als Operanden und ist aus Leistungsgründen am ineffizientesten.
1. CalculationPrecisionStrategy.ROUND: Rundet die Berechnungsergebnisse nach signifikanten Stellen.
1. CalculationPrecisionStrategy.NONE: Es wird keine Strategie angewendet, daher verwendet die Engine während der Berechnung den ursprünglichen Double-Wert als Operanden und gibt das Ergebnis direkt zurück. Diese Option ist am effizientesten und in den meisten Fällen anwendbar.
### **Methoden Hinzugefügt, um CalculationOptions zu verwenden**
Mit der Veröffentlichung von v8.5.0 hat Aspose.Cells API Überladungsversionen der Methode computeFormula wie unten aufgeführt hinzugefügt.

- Workbook.calculateFormula(Berechnungsoptionen)
- Worksheet.calculateFormula (Optionen für Berechnungsoptionen, bool rekursiv)
- Cell.calculate(Berechnungsoptionen)
### **Aufzählungsfeld PasteType.ROW_HEIGHTS Hinzugefügt**
Aspose.Cells APIs haben PasteType.ROW bereitgestellt_HEIGHTS-Aufzählungsfeld zum Kopieren der Zeilenhöhen beim Kopieren der Bereiche. Beim Festlegen der PasteOptions.PasteType-Eigenschaft auf ((PasteType.ROW_HEIGHTS}} werden die Höhen aller Zeilen innerhalb des Quellbereichs in den Zielbereich kopiert.

**Java**

{{< highlight "csharp" >}}

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
### **Eigenschaft SheetRender.PageScale Hinzugefügt**
Wenn Sie die Seiteneinrichtungsskalierung mit festlegen**Anpassen an n Seite(n) breit und m hoch** Option Microsoft Excel berechnet den Skalierungsfaktor für die Seiteneinrichtung. Dasselbe kann mit der SheetRender.PageScale-Eigenschaft erreicht werden, die von Aspose.Cells for Java 8.5.0 verfügbar gemacht wird. Diese Eigenschaft gibt einen Double-Wert zurück, der in einen Prozentwert konvertiert werden kann. Wenn beispielsweise 0,507968245 zurückgegeben wird, bedeutet dies, dass der Skalierungsfaktor 51 % beträgt.

**Java**

{{< highlight "csharp" >}}

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
### **Enumeration CellValueFormatStrategy Hinzugefügt**
 Aspose.Cells for Java 8.5.0 hat eine neue Aufzählung CellValueFormatStrategy hinzugefügt, um Situationen zu handhaben, in denen Zellwerte mit oder ohne angewendete Formatierung extrahiert werden müssen. Enumeration CellValueFormatStrategy hat folgende Felder.

1. CellValueFormatStrategy.CELL_STYLE: Nur mit dem Originalformat der Zelle formatiert.
1. CellValueFormatStrategy.DISPLAY_STYLE: Formatiert mit dem angezeigten Stil der Zelle.
1. CellValueFormatStrategy.NONE: Nicht formatiert.
### **Methode Cell.getStringValue hinzugefügt**
Um die CellValueFormatStrategy-Enumeration zu verwenden, hat v8.5.0 die Cell.getStringValue-Methode verfügbar gemacht, die einen Parameter des Typs CellValueFormatStrategy akzeptieren kann und den Wert abhängig von der angegebenen Option zurückgibt.

Der folgende Codeausschnitt zeigt, wie die neu bereitgestellte Methode Cells.getStringValue verwendet wird.

**Java**

{{< highlight "csharp" >}}

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
