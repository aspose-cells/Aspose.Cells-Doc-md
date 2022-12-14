---
title: Datei im Antwortobjekt speichern
type: docs
weight: 50
url: /de/net/saving-file-to-response-object/
---
{{% alert color="primary" %}}

Aspose.Cells ermöglicht die Manipulation von Dateien. In diesem Artikel werden die verschiedenen Möglichkeiten erläutert, wie Dateien in einem Antwortobjekt gespeichert werden können.

{{% /alert %}}

## **Datei im Antwortobjekt speichern**

 Es ist auch möglich, eine Datei dynamisch zu generieren und direkt an einen Client-Browser zu senden. Verwenden Sie dazu eine spezielle überladene Version von**[Speichern](https://reference.aspose.com/cells/net/aspose.cells.workbook/save/methods/5)**Methode, die die folgenden Parameter akzeptiert:

-  ASP.NET**[HttpResponse](https://docs.microsoft.com/en-gb/dotnet/api/system.web.httpresponse?view=netframework-4.8)**Objekt.
- Dateiname.
- **[ContentDisposition](https://reference.aspose.com/cells/net/aspose.cells/contentdisposition)**, der Inhaltsdispositionstyp der Ausgabedatei.
- **[Speicheroptionen](https://reference.aspose.com/cells/net/aspose.cells/saveoptions)**, der Dateiformattyp

 Das**[ContentDisposition](https://reference.aspose.com/cells/net/aspose.cells/contentdisposition)**Die Enumeration bestimmt, ob die an den Browser gesendete Datei die Option bietet, sich selbst direkt im Browser oder in einer Anwendung zu öffnen, die mit .xls/.xlsx oder einer anderen Erweiterung verknüpft ist.

Die Enumeration enthält die folgenden vordefinierten Speichertypen:

|**Typ**|**Beschreibung**|
|:- |:- |
|Anhang|Sendet die Tabelle an den Browser und wird in einer Anwendung als Anhang geöffnet, der mit .xls/.xlsx oder anderen Erweiterungen verknüpft ist|
|In der Reihe|Sendet das Dokument an den Browser und bietet eine Option zum Speichern der Tabelle auf der Festplatte oder zum Öffnen im Browser|

### **XLS-Dateien**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SaveXLSFile-1.cs" >}}

### **XLSX-Dateien**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SaveXLSXFile-1.cs" >}}

### **PDF-Dateien**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SaveInPdfFormat-1.cs" >}}

### **Notiz**

Da das Objekt „System.Web.HttpResponse“ nicht in .NET5 und .Netstandard enthalten ist,
Diese Funktion existiert also nicht in Aspose.Cells .NET5- und .Netstandard-Version, Sie können auf den folgenden Code verweisen, um die Datei im Stream zu speichern, und dann den Vorgang im Stream ausführen.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SavingFiletoStream-1.cs" >}}

