---
title: Hur man ändrar bakgrund i kommentar i Excel med Golang via C++
linktitle: Kommentarbakgrund
type: docs
weight: 190
url: /sv/go-cpp/how-to-set-comment-background/
description: Hur man ändrar färg på kommentar i Excel. Hur man infogar bild eller bild i kommentar i Excel med C++.
keywords: lägg till infälld bild färg kommentar bakgrund excel
---

{{% alert color="primary" %}}

Kommentarer läggs till celler för att registrera kommentarer, allt från detaljer om hur en formel fungerar, var en värde kommer ifrån, eller frågor från granskare. Kommentarer spelar en extremt viktig roll när flera personer diskuterar eller granskar samma dokument vid olika tillfällen. Hur kan man skilja olika personers kommentarer? Ja, vi kan ställa in en annan bakgrundsfärg för varje kommentar. Men när vi behöver behandla många dokument och många kommentarer är det en mardröm att göra det manuellt. Lyckligtvis erbjuder [**Aspose.Cells**](https://products.aspose.com/cells/go-cpp/) ett API som låter dig göra detta i kod.

{{% /alert %}}

## **Hur man ändrar färg i kommentar i Excel**

När du inte behöver standardbakgrundsfärgen för kommentarer kan du vilja ersätta den med en färg du är intresserad av. Hur ändrar jag bakgrundsfärgen på kommentarrutan i Excel?

Följande kod kommer att guida dig hur du använder [**Aspose.Cells**](https://products.aspose.com/cells/go-cpp/) för att lägga till din favoritbakgrundsfärg till valfria kommentarer.

Här har vi förberett en [exempel fil](exmaple.xlsx) för dig. Denna fil används för att initialisera Workbook-objektet i koden nedan.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-HowToSetCommentBackground.go" >}}
Kör ovanstående kod, och du får en [utdata fil](result.xlsx).

## **Hur man infogar bild eller bild i kommentar i Excel**

Microsoft Excel låter användare anpassa utseendet och känslan av kalkylblad i stor utsträckning. Det är till och med möjligt att lägga till bakgrundsbilder i kommentarer. Att lägga till en bakgrundsbild kan vara ett estetiskt val eller användas för att stärka varumärket.

Exempelkoden nedan skapar en XLSX-fil från början med [**Aspose.Cells**](https://products.aspose.com/cells/go-cpp/) API, och lägger till en kommentar med bakgrundsbild i cell A1.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-HowToSetCommentBackground-1.go" >}}
