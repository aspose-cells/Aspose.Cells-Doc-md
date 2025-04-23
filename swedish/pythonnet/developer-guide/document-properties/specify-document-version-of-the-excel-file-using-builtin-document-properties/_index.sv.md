---
title: Ange dokumentversionen för Excel filen med hjälp av inbyggda dokumentegenskaper
type: docs
weight: 20
url: /sv/python-net/specify-document-version-of-the-excel-file-using-builtin-document-properties/
---

## **Möjliga användningsscenario**

Du kan ändra **Versionsnumret** på Excel-filen genom att högerklicka på filen och välja Egenskaper > Detaljer och sedan redigera **Versionsnumret**-fältet. Använd [**BuiltInDocumentPropertyCollection.document_version**](https://reference.aspose.com/cells/python-net/aspose.cells.properties/builtindocumentpropertycollection/document_version)-egenskapen för att ändra det programatiskt med Aspose.Cells för Python via .NET API:er.

## **Ange dokumentversionen för Excel-filen med hjälp av inbyggda dokumentegenskaper**

Följande exempelkod skapar en arbetsbok och ändrar dess inbyggda dokumentegenskaper som inkluderar Titel, Författare och Versionsnummer. Se den [utdataexcel-fil](64716811.xlsx) genererad med koden och skärmbild som visar den modifierade **Versionsnumret** med [**BuiltInDocumentPropertyCollection.document_version**](https://reference.aspose.com/cells/python-net/aspose.cells.properties/builtindocumentpropertycollection/document_version)-egenskapen.

![todo:image_alt_text](specify-document-version-of-the-excel-file-using-builtin-document-properties_1.png)

## **Exempelkod**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Document-Properties-SpecifyDocumentVersionOfExcelFile.py" >}}

