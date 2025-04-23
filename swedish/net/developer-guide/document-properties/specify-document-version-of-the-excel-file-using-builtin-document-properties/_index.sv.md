---
title: Ange dokumentversionen för Excel filen med hjälp av inbyggda dokumentegenskaper
type: docs
weight: 20
url: /sv/net/specify-document-version-of-the-excel-file-using-builtin-document-properties/
---

## **Möjliga användningsscenario**

Du kan ändra **Versionsnumret** på Excel-filen genom att högerklicka på filen och sedan välja Egenskaper > Detaljer och sedan redigera fältet **Versionsnummer**. Använd [**BuiltInDocumentPropertyCollection.DocumentVersion**](https://reference.aspose.com/cells/net/aspose.cells.properties/builtindocumentpropertycollection/properties/documentversion)-egenskapen för att ändra det programmatiskt med Aspose.Cells API:er.

## **Ange dokumentversionen för Excel-filen med hjälp av inbyggda dokumentegenskaper**

Följande exempelkod skapar en arbetsbok och ändrar dess inbyggda dokumentegenskaper som inkluderar Titel, Författare och Versionsnummer. Se den [utdataexcel-fil](64716811.xlsx) genererad med koden och skärmbild som visar den modifierade **Versionsnumret** med [**BuiltInDocumentPropertyCollection.DocumentVersion**](https://reference.aspose.com/cells/net/aspose.cells.properties/builtindocumentpropertycollection/properties/documentversion)-egenskapen.

![todo:image_alt_text](specify-document-version-of-the-excel-file-using-builtin-document-properties_1.png)

## **Exempelkod**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "LoadingSavingConvertingAndManaging-SpecifyDocumentVersionOfExcelFile.cs" >}}
{{< app/cells/assistant language="csharp" >}}
