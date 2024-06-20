---
title: Spara fil till responsobjekt
type: docs
weight: 50
url: /sv/net/saving-file-to-response-object/
---

{{% alert color="primary" %}}

Aspose.Cells gör det möjligt att manipulera filer. Den här artikeln förklarar de olika sätten på vilka filer kan sparas till ett responsobjekt.

{{% /alert %}}

## **Spara fil till responsobjekt**

Det är också möjligt att generera en fil dynamiskt och skicka den direkt till en klientwebbläsare. För att göra det, använd en speciell överlagrad version av [**Save**](https://reference.aspose.com/cells/net/aspose.cells.workbook/save/methods/5) metoden som accepterar följande parametrar:

- ASP.NET [**HttpResponse**](https://docs.microsoft.com/en-gb/dotnet/api/system.web.httpresponse?view=netframework-4.8) objekt.
- Filnamn.
- [**ContentDisposition**](https://reference.aspose.com/cells/net/aspose.cells/contentdisposition), utdatafilens content-disposition-typ.
- [**SaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/saveoptions), filformatstyp

Uppräkningen [**ContentDisposition**](https://reference.aspose.com/cells/net/aspose.cells/contentdisposition) avgör om filen som skickas till webbläsaren ger möjlighet att öppnas av sig själv direkt i webbläsaren eller i en applikation associerad med .xls/.xlsx eller en annan förlängning.

Uppräkningen innehåller följande fördefinierade sparalternativ:

|**Typ**|**Beskrivning**|
| :- | :- |
|Bilaga|Skickar kalkylarket till webbläsaren och öppnas i en applikation som en bilaga associerad med .xls/.xlsx eller andra filändelser|
|Inline|Skickar dokumentet till webbläsaren och presenterar ett alternativ att spara kalkylarket på disken eller öppna det inne i webbläsaren|

### **XLS-filer**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SaveXLSFile-1.cs" >}}

### **XLSX-filer**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SaveXLSXFile-1.cs" >}}

### **PDF-filer**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SaveInPdfFormat-1.cs" >}}

### **Obs**

På grund av objektet "System.Web.HttpResponse" som inte inkluderas i .NET5 och .Netstandard,
Funktionen finns därför inte i Aspose.Cells .NET5 och .Netstandard-versionen, du kan hänvisa till följande kod för att spara filen i strömmen och utföra operationer med strömmen.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SavingFiletoStream-1.cs" >}}

