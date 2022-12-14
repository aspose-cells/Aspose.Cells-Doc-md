---
title: Öffentlich API Änderungen in Aspose.Cells 8.8.0
type: docs
weight: 260
url: /de/net/public-api-changes-in-aspose-cells-8-8-0/
---
{{% alert color="primary" %}} 

Dieses Dokument beschreibt die Änderungen an Aspose.Cells API von Version 8.7.2 zu 8.8.0, die für Modul-/Anwendungsentwickler von Interesse sein könnten. Es enthält nicht nur neue und aktualisierte öffentliche Methoden, hinzugefügte und entfernte Klassen usw., sondern auch eine Beschreibung aller Änderungen im Verhalten hinter den Kulissen in Aspose.Cells.

{{% /alert %}} 
## **APIs hinzugefügt**
### **Rufen Sie Cell-Referenzen für die externe Verbindung ab**
Aspose.Cells for .NET 8.8.0 hat die folgenden neuen Eigenschaften verfügbar gemacht, die beim Abrufen der Ziel- und Ausgabezellreferenzen für externe Verbindungen, die in der Tabelle gespeichert sind, hilfreich sind.

1. QueryTable.ConnectionId: Ruft die Verbindungs-ID der Abfragetabelle ab.
1. ExternalConnection.Id: Ruft die ID der externen Verbindung ab.
1. ListObject.QueryTable: Ruft die verknüpfte QueryTable ab.

{{% alert color="primary" %}} 

 Weitere Einzelheiten zu dieser Funktion finden Sie im ausführlichen Artikel unter[Suchen Sie Abfragetabellen und listen Sie Objekte auf, die sich auf externe Datenverbindungen beziehen](/cells/de/net/find-query-tables-and-list-objects-related-to-external-data-connections/)

{{% /alert %}} 
### **HTMLLoadOptions.KeepPrecision-Eigenschaft hinzugefügt**
Aspose.Cells for .NET 8.8.0 hat die HTMLLoadOptions.KeepPrecision-Eigenschaft hinzugefügt, um die Konvertierung langer numerischer Werte in Exponentialschreibweise beim Importieren von HTML-Dateien zu steuern. Standardmäßig wird jeder Wert mit mehr als 15 Ziffern in die Exponentialschreibweise konvertiert, wenn die Daten aus einer HTML-Zeichenfolge oder -Datei importiert werden. Jetzt können die Benutzer dieses Verhalten jedoch mithilfe der HTMLLoadOptions.KeepPrecision-Eigenschaft steuern. Wenn die besagte Eigenschaft auf „true“ gesetzt ist, werden die Werte so importiert, wie sie in der Quelle sind.

{{% alert color="primary" %}} 

 Weitere Einzelheiten zu dieser Funktion finden Sie im ausführlichen Artikel unter[ Vermeiden Sie die Umwandlung großer numerischer Werte in die Exponentialschreibweise](/cells/de/net/avoid-exponential-notation-of-large-numbers-while-importing-from/)

{{% /alert %}} 

Es folgt das einfache Nutzungsszenario.

**C#**

{{< highlight "csharp" >}}

 string html = @" 

<table data-cache=""not-cached"" class=""sortable""> 

   <tbody> 

    <tr> 

     <td class=""even"">9999999999999999</td> 

     <td class=""odd"">10.8%</td> 

    </tr> 

   </tbody> 

</table> 

";

byte[]byteArray = Encoding.UTF8.GetBytes(html);

HTMLLoadOptions loadOptions = new Aspose.Cells.HTMLLoadOptions(LoadFormat.Html);

loadOptions.KeepPrecision = true;

MemoryStream stream = new MemoryStream(byteArray);

Workbook workbook = new Workbook(stream, loadOptions);

Worksheet sheet = workbook.Worksheets[0];

sheet.AutoFitColumns();

workbook.Save(dir + "output.xlsx");

{{< /highlight >}}


### **HTMLLoadOptions.DeleteRedundantSpaces-Eigenschaft hinzugefügt**
Aspose.Cells for .NET 8.8.0 hat die Eigenschaft HTMLLoadOptions.DeleteRedundantSpaces verfügbar gemacht, um die zusätzlichen Leerzeichen nach dem Zeilenumbruch-Tag (<br>-Tag) beim Importieren der Daten aus der HTML-Zeichenfolge oder -Datei. Die Eigenschaft „HTMLLoadOptions.DeleteRedundantSpaces“ hat den Standardwert „false“, was bedeutet, dass alle zusätzlichen Leerzeichen beibehalten und in das Workbook-Objekt importiert werden. Wenn sie jedoch auf „true“ gesetzt ist, löscht API alle überflüssigen Leerzeichen nach dem Zeilenumbruch-Tag.

{{% alert color="primary" %}} 

 Weitere Einzelheiten zu dieser Funktion finden Sie im ausführlichen Artikel unter[Löschen Sie redundante Leerzeichen aus HTML](/cells/de/net/delete-redundant-spaces-after-line-break-while-importing/)

{{% /alert %}} 

Ein einfaches Nutzungsszenario sieht wie folgt aus.

**C#**

{{< highlight "csharp" >}}

 string html = @" 

<html>

    <body>

        <table>

            <tr>

                <td>

                    <br>    This is sample data 

                    <br>    This is sample data

                    <br>    This is sample data

                </td>

            </tr>

        </table>

    </body>

</html>

";

byte[]byteArray = Encoding.UTF8.GetBytes(html);

HTMLLoadOptions loadOptions = new Aspose.Cells.HTMLLoadOptions(LoadFormat.Html);

loadOptions.DeleteRedundantSpaces = true;

MemoryStream stream = new MemoryStream(byteArray);

Workbook workbook = new Workbook(stream, loadOptions);

workbook.Save(dir + "output.xlsx");

{{< /highlight >}}


### **Style.QuotePrefix-Eigenschaft hinzugefügt**
Aspose.Cells for .NET 8.8.0 hat die Style.QuotePrefix-Eigenschaft verfügbar gemacht, um zu erkennen, ob ein Zellenwert mit einem einfachen Anführungszeichen beginnt.

{{% alert color="primary" %}} 

 Weitere Einzelheiten zu dieser Funktion finden Sie im ausführlichen Artikel unter[Einfaches Anführungszeichen am Anfang des Werts Cell erkennen](/cells/de/net/find-if-the-cell-value-starts-with-single-quote-mark/)

{{% /alert %}} 

Ein einfaches Nutzungsszenario sieht wie folgt aus.

**C#**

{{< highlight "csharp" >}}

 Workbook book = new Workbook();

Worksheet sheet = book.Worksheets[0];

Cell a1 = sheet.Cells["A1"];

Cell a2 = sheet.Cells["A2"];

a1.PutValue("sample");

a2.PutValue("'sample");

Console.WriteLine("String value of A1: " + a1.StringValue);

Console.WriteLine("String value of A2: " + a2.StringValue);

Style s1 = a1.GetStyle();

Style s2 = a2.GetStyle();

Console.WriteLine("A1 has a quote prefix: " + s1.QuotePrefix);

Console.WriteLine("A2 has a quote prefix: " + s2.QuotePrefix);

{{< /highlight >}}
## **Veraltete APIs**
### **Veraltete LoadOptions.ConvertNumericData-Eigenschaft**
Aspose.Cells 8.8.0 hat die Eigenschaft LoadOptions.ConvertNumericData als veraltet markiert. Bitte verwenden Sie die entsprechende Eigenschaft aus den Klassen HTMLLoadOptions oder TxtLoadOptions.
