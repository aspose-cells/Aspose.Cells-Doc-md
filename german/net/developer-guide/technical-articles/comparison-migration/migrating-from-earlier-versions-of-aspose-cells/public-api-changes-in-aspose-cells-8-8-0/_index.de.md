---
title: Öffentliche API Änderungen in Aspose.Cells 8.8.0
type: docs
weight: 260
url: /de/net/public-api-changes-in-aspose-cells-8-8-0/
---

{{% alert color="primary" %}} 

Dieses Dokument beschreibt die Änderungen an der Aspose.Cells-API von Version 8.7.2 auf 8.8.0, die für Modul-/Anwendungsentwickler interessant sein könnten. Es umfasst nicht nur neue und aktualisierte öffentliche Methoden, hinzugefügte & entfernte Klassen usw., sondern auch eine Beschreibung etwaiger Änderungen im Verhalten hinter den Kulissen von Aspose.Cells.

{{% /alert %}} 
## **Hinzugefügte APIs**
### **Zellverweise für externe Verbindung abrufen**
Aspose.Cells for .NET 8.8.0 hat die folgenden neuen Eigenschaften freigelegt, die beim Abrufen der Ziel- und Ausgabe­zellenverweise für in der Arbeitsmappe gespeicherte externe Verbindungen hilfreich sind.

1. QueryTable.ConnectionId: Ruft die Verbindungs-ID der Abfrage-Tabelle ab.
1. ExternalConnection.Id: Ruft die ID der externen Verbindung ab.
1. ListObject.QueryTable: Ruft die verknüpfte QueryTable ab.

{{% alert color="primary" %}} 

Weitere Details zu diesem Feature finden Sie im ausführlichen Artikel zu [Suchen von Abfragetabellen und Listobjekten in Bezug auf externe Datenverbindungen](/cells/de/net/find-query-tables-and-list-objects-related-to-external-data-connections/)

{{% /alert %}} 
### **Hinzugefügte HTMLLoadOptions.KeepPrecision Eigenschaft**
Aspose.Cells for .NET 8.8.0 hat die HTMLLoadOptions.KeepPrecision-Eigenschaft hinzugefügt, um die Konvertierung langer numerischer Werte in Exponentialnotation zu kontrollieren, während HTML-Dateien importiert werden. Standardmäßig wird jeder Wert, der länger als 15 Ziffern ist, in Exponentialnotation umgewandelt, wenn die Daten aus einer HTML-Zeichenfolge oder -Datei importiert werden. Jetzt können die Benutzer dieses Verhalten jedoch mit Hilfe der HTMLLoadOptions.KeepPrecision-Eigenschaft steuern. Wenn die genannte Eigenschaft auf true gesetzt ist, werden die Werte so importiert, wie sie in der Quelle vorliegen.

{{% alert color="primary" %}} 

Weitere Details zu diesem Feature finden Sie im ausführlichen Artikel zu [Vermeiden Sie die Umwandlung großer numerischer Werte in Exponentialnotation](/cells/de/net/avoid-exponential-notation-of-large-numbers-while-importing-from/)

{{% /alert %}} 

Im Folgenden wird das einfache Anwendungsszenario beschrieben.

**C#**

{{< highlight csharp >}}

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

byte[] byteArray = Encoding.UTF8.GetBytes(html);

HTMLLoadOptions loadOptions = new Aspose.Cells.HTMLLoadOptions(LoadFormat.Html);

loadOptions.KeepPrecision = true;

MemoryStream stream = new MemoryStream(byteArray);

Workbook workbook = new Workbook(stream, loadOptions);

Worksheet sheet = workbook.Worksheets[0];

sheet.AutoFitColumns();

workbook.Save(dir + "output.xlsx");

{{< /highlight >}}


### **Hinzugefügte Eigenschaft HTMLLoadOptions.DeleteRedundantSpaces**
Aspose.Cells for .NET 8.8.0 has exposed the HTMLLoadOptions.DeleteRedundantSpaces property in order to keep or delete the extra spaces after the line break tag (<br> Tag) while importing the data from the HTML string or file. The HTMLLoadOptions.DeleteRedundantSpaces property has the default value as false that means, all extra spaces will be preserved and imported to the Workbook object, however, when set to true, the API will delete all the redundant spaces coming after the line break tag.

{{% alert color="primary" %}} 

Weitere Details zu diesem Feature finden Sie im ausführlichen Artikel zu [Löschen über­flüssiger Leerzeichen aus HTML](/cells/de/net/delete-redundant-spaces-after-line-break-while-importing/)

{{% /alert %}} 

Das einfache Anwendungsszenario sieht wie folgt aus.

**C#**

{{< highlight csharp >}}

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

byte[] byteArray = Encoding.UTF8.GetBytes(html);

HTMLLoadOptions loadOptions = new Aspose.Cells.HTMLLoadOptions(LoadFormat.Html);

loadOptions.DeleteRedundantSpaces = true;

MemoryStream stream = new MemoryStream(byteArray);

Workbook workbook = new Workbook(stream, loadOptions);

workbook.Save(dir + "output.xlsx");

{{< /highlight >}}


### **Hinzugefügte Eigenschaft Style.QuotePrefix**
Aspose.Cells for .NET 8.8.0 hat die Style.QuotePrefix-Eigenschaft freigelegt, um zu erkennen, ob ein Zellenwert mit einem einzelnen Anführungszeichen beginnt.

{{% alert color="primary" %}} 

Für weitere Details zu diesem Feature lesen Sie bitte den ausführlichen Artikel zu [Erkennen von Anführungszeichen am Anfang des Zellwerts](/cells/de/net/find-if-the-cell-value-starts-with-single-quote-mark/)

{{% /alert %}} 

Das einfache Anwendungsszenario sieht wie folgt aus.

**C#**

{{< highlight csharp >}}

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
Aspose.Cells 8.8.0 hat die LoadOptions.ConvertNumericData-Eigenschaft als veraltet markiert. Bitte verwenden Sie die entsprechende Eigenschaft der Klassen HTMLLoadOptions oder TxtLoadOptions.
{{< app/cells/assistant language="csharp" >}}
