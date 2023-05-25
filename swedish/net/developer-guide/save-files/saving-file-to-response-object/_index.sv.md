---
title: Sparar fil till svarsobjekt
type: docs
weight: 50
url: /sv/net/saving-file-to-response-object/
---
{{% alert color="primary" %}}

Aspose.Cells gör det möjligt att manipulera filer. Den här artikeln förklarar de olika sätten på vilka filer kan sparas till ett svarsobjekt.

{{% /alert %}}

##  **Sparar fil till svarsobjekt**

Det är också möjligt att generera en fil dynamiskt och skicka den direkt till en klientwebbläsare. För att göra det, använd en speciell överbelastad version av**[Spara](https://reference.aspose.com/cells/net/aspose.cells.workbook/save/methods/5)**metod som accepterar följande parametrar:

- ASP.NET **[HttpResponse](https://docs.microsoft.com/en-gb/dotnet/api/system.web.httpresponse?view=netframework-4.8)**objekt.
- Filnamn.
- *[Innehållsdisposition](https://reference.aspose.com/cells/net/aspose.cells/contentdisposition)**, innehållsdispositionstypen för utdatafilen.
- *[Spara Alternativ](https://reference.aspose.com/cells/net/aspose.cells/saveoptions)**, filformatstypen

 De**[ContentDisposition](https://reference.aspose.com/cells/net/aspose.cells/contentdisposition)**uppräkning avgör om filen som skickas till webbläsaren ger möjlighet att öppnas av sig själv direkt i webbläsaren eller i en applikation som är kopplad till .xls/.xlsx eller ett annat tillägg.

Uppräkningen innehåller följande fördefinierade spartyper:

|**Typ**|**Beskrivning**|
| :- | :- |
|Attachment|Skickar kalkylarket till webbläsaren och öppnas i en applikation som en bilaga kopplad till .xls/.xlsx eller andra tillägg|
|Inline|Skickar dokumentet till webbläsaren och presenterar ett alternativ för att spara kalkylarket på disk eller öppna i webbläsaren|

###  **XLS Filer**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SaveXLSFile-1.cs" >}}

###  **XLSX Filer**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SaveXLSXFile-1.cs" >}}

###  **PDF Filer**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SaveInPdfFormat-1.cs" >}}

###  **Notera**

På grund av objektet "System.Web.HttpResponse" som inte ingår i .NET5 och .Netstandard,
Så den här funktionen finns inte i Aspose.Cells .NET5- och .Netstandard-versionen, du kan hänvisa till följande kod för att spara filen i strömmen och sedan utföra operationen till strömmen.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SavingFiletoStream-1.cs" >}}

