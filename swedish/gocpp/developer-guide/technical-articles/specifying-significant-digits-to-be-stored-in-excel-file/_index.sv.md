---
title: Specificera Signifikanta Siffror att lagra i Excel fil med Golang via C++
linktitle: Angivande av signifikanta siffror
type: docs
weight: 30
url: /sv/go-cpp/specifying-significant-digits-to-be-stored-in-excel-file/
description: Lär dig att specificera signifikanta siffror att lagra i Excel filer med Aspose.Cells med Golang via C++
---

## **Möjliga användningsscenario**

Som standard lagrar Aspose.Cells 17 signifikanta siffror av dubbelvärden inuti Excel-filen, till skillnad från MS-Excel som bara lagrar 15 signifikanta siffror. Du kan ändra Aspose.Cells standardbeteende från 17 till 15 signifikanta siffror med hjälp av [**GetSignificantDigits()**](https://reference.aspose.com/cells/go-cpp/cellshelper/getsignificantdigits/) egenskapen.

## **Ange signifikanta siffror som ska lagras i Excel-fil**

Följande kodsnutt tvingar Aspose.Cells att använda 15 signifikanta siffror när du lagrar dubbelvärden i Excel-filen. Kontrollera [utdata Excelfilen](22774105.xlsx). Byt ut dess extension till .zip och extrahera den, du kommer att se att endast 15 signifikanta siffror lagras i Excel-filen. Följande skärmbild förklarar effekten av [**GetSignificantDigits()**](https://reference.aspose.com/cells/go-cpp/cellshelper/getsignificantdigits/)-egenskapen på utdata Excel-filen.

![todo:image_alt_text](specifying-significant-digits-to-be-stored-in-excel-file_1.png)

## **Exempelkod**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SpecifyingSignificantDigitsToBeStoredInExcelFile.go" >}}
