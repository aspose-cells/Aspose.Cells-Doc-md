---
title: Spara filer
type: docs
weight: 20
url: /sv/go-cpp/saving-files/
---

{{% alert color="primary" %}}

Aspose.Cells gör det möjligt att skapa och spara filer samt manipulera befintliga filer. Denna artikel förklarar olika sätt att spara filer på.

{{% /alert %}}

## **Olika sätt att spara filer**

Aspose.Cells tillhandahåller [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/), som representerar en Microsoft Excel-fil och erbjuder metoder som är nödvändiga för att arbeta med Excel-filer. Klassen [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) ger metoden [Save](https://reference.aspose.com/cells/go-cpp/workbook/save/) som används för att spara Excel-filer. Metoden [Save](https://reference.aspose.com/cells/go-cpp/workbook/save/) har många överlagringar som används för att spara filer på olika sätt. Filformatet som filen sparas i bestäms av enumerationen [SaveFormat](https://reference.aspose.com/cells/go-cpp/saveformat/).

## **Spara fil till en plats**

För att spara filer till en lagringsplats, specificera filnamnet (inklusive lagringsväg) och det önskade filformatet (från [SaveFormat](https://reference.aspose.com/cells/go-cpp/saveformat/)-enumen) när du anropar [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) objektets [Save](https://reference.aspose.com/cells/go-cpp/workbook/save_string/) metod.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SavingFileToSomeLocation.go" >}}

## **Spara fil till ström**

För att spara filer till en ström, skapa ett MemoryStream- eller FileStream-objekt och spara filen till den strömmen genom att anropa [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) objektets [Save](https://reference.aspose.com/cells/go-cpp/workbook/save_string/) metod. Specificera önskat filformat med hjälp av [SaveFormat](https://reference.aspose.com/cells/go-cpp/saveformat/)-enumerationen när du anropar [Save](https://reference.aspose.com/cells/go-cpp/workbook/save_saveFormat/) metod.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SavingFileToStream.go" >}}

## **Spara fil till PDF**

För att spara det önskade innehållet till en PDF-fil med biblioteket Aspose.Cells for Go via C++, skapa ett nytt [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) objekt eller bygg ett [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) objekt genom att läsa en befintlig Excel-fil, och sedan [spara](https://reference.aspose.com/cells/go-cpp/workbook/save_string_saveOptions/) filen till PDF genom att anropa sparmetoden för [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) objektet. Vid anrop av Save-metoden, använd [SaveFormat](https://reference.aspose.com/cells/go-cpp/saveformat/) enumerationen för att ange det önskade filformatet.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SavingFileToPdf.go" >}}
