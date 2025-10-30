---
title: Spara fil till svar objekt med Golang via C++
linktitle: Spara fil till responsobjekt
type: docs
weight: 50
url: /sv/go-cpp/saving-file-to-response-object/
description: Lär dig hur du dynamiskt sparar filer och skickar dem direkt till en klientwebbläsare med Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Aspose.Cells gör det möjligt att manipulera filer. Den här artikeln förklarar de olika sätten på vilka filer kan sparas till ett responsobjekt.

{{% /alert %}}

## **Spara fil till responsobjekt**

Det är också möjligt att generera en fil dynamiskt och skicka den direkt till en klientwebbläsare. För att göra det, använd en speciell överlagrad version av [**Save**](https://reference.aspose.com/cells/go-cpp/workbook/save_string_saveformat/) metoden som accepterar följande parametrar:

- **HttpResponse**-objektet.
- Filnamn.
- [**ContentDisposition**](https://reference.aspose.com/cells/go-cpp/contentdisposition/), utdatafilens content-disposition-typ.
- [**SaveOptions**](https://reference.aspose.com/cells/go-cpp/saveoptions/), filformattypen.

Uppräkningen [**ContentDisposition**](https://reference.aspose.com/cells/go-cpp/contentdisposition/) avgör om filen som skickas till webbläsaren ger möjlighet att öppnas av sig själv direkt i webbläsaren eller i en applikation associerad med .xls/.xlsx eller en annan förlängning.

Uppräkningen innehåller följande fördefinierade sparalternativ:

|**Typ**|**Beskrivning**|
| :- | :- |
|Bilaga|Skickar kalkylarket till webbläsaren och öppnas i en applikation som en bilaga associerad med .xls/.xlsx eller andra filändelser|
|Inline|Skickar dokumentet till webbläsaren och presenterar ett alternativ att spara kalkylarket på disken eller öppna det inne i webbläsaren|

### **XLS-filer**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SavingFileToResponseObject.go" >}}
### **XLSX-filer**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SavingFileToResponseObject-1.go" >}}
### **PDF-filer**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SavingFileToResponseObject-2.go" >}}
### **Obs**

På grund av objektet "System.Web.HttpResponse" som inte inkluderas i .NET5 och .Netstandard,
Funktionen finns därför inte i Aspose.Cells .NET5 och .Netstandard-versionen, du kan hänvisa till följande kod för att spara filen i strömmen och utföra operationer med strömmen.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SavingFileToResponseObject-3.go" >}}
