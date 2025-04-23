---
title: Datei im Antwortobjekt speichern
type: docs
weight: 50
url: /de/net/saving-file-to-response-object/
---

{{% alert color="primary" %}}

Mit Aspose.Cells ist es möglich, Dateien zu manipulieren. In diesem Artikel werden die verschiedenen Möglichkeiten erläutert, wie Dateien in einem Antwortobjekt gespeichert werden können.

{{% /alert %}}

## **Speichern der Datei im Antwortobjekt**

Es ist auch möglich, eine Datei dynamisch zu generieren und direkt an den Client-Browser zu senden. Verwenden Sie dazu eine spezielle überladene Version der [**Save**](https://reference.aspose.com/cells/net/aspose.cells.workbook/save/methods/5) Methode, die die folgenden Parameter akzeptiert:

- ASP.NET [**HttpResponse**](https://docs.microsoft.com/en-gb/dotnet/api/system.web.httpresponse?view=netframework-4.8) Objekt.
- Dateiname.
- [**ContentDisposition**](https://reference.aspose.com/cells/net/aspose.cells/contentdisposition), der Inhalt-Dispositionstyp der Ausgabedatei.
- [**SaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/saveoptions), der Dateiformat-Typ

Die [**ContentDisposition**](https://reference.aspose.com/cells/net/aspose.cells/contentdisposition) Enumeration bestimmt, ob die Datei, die an den Browser gesendet wird, die Option bietet, direkt im Browser oder in einer Anwendung mit der Erweiterung .xls/.xlsx oder einer anderen geöffnet zu werden.

Die Enumeration enthält die folgenden vordefinierten Speichertypen:

|**Typ**|**Beschreibung**|
| :- | :- |
|Anhang|Sendet die Tabelle an den Browser und öffnet sie in einer Anwendung als Anhang, der mit .xls/.xlsx oder anderen Erweiterungen verknüpft ist|
|Inline|Sendet das Dokument an den Browser und bietet die Option, die Tabelle auf der Festplatte zu speichern oder im Browser zu öffnen|

### **XLS-Dateien**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SaveXLSFile-1.cs" >}}

### **XLSX-Dateien**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SaveXLSXFile-1.cs" >}}

### **PDF-Dateien**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SaveInPdfFormat-1.cs" >}}

### **Hinweis**

Aufgrund des Objekts "System.Web.HttpResponse", das nicht in .NET5 und .Netstandard enthalten ist,
Existiert diese Funktion nicht in Aspose.Cells .NET5 und .Netstandard Version, Sie können sich auf den folgenden Code beziehen, um die Datei im Stream zu speichern und dann den Stream zu bearbeiten.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SavingFiletoStream-1.cs" >}}

{{< app/cells/assistant language="csharp" >}}
