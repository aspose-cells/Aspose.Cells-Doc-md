---
title: Ange dokumentversionen för Excel filen med hjälp av inbyggda dokumentegenskaper
type: docs
weight: 20
url: /sv/java/specify-document-version-of-the-excel-file-using-builtin-document-properties/
---

## **Möjliga användningsscenario**

Du kan ändra *Versionsnummer* för Excel-filen genom att högerklicka på filen och sedan välja *Egenskaper > Detaljer* och sedan redigera fältet *Versionsnummer*. Använd [**BuiltInDocumentPropertyCollection.DocumentVersion**](https://reference.aspose.com/cells/java/com.aspose.cells/builtindocumentpropertycollection#DocumentVersion)-egenskapen för att ändra den programmatiskt med hjälp av Aspose.Cells API:er.

## **Ange dokumentversionen för Excel-filen med hjälp av inbyggda dokumentegenskaper**

Följande exempelkod skapar en arbetsbok och ändrar dess inbyggda dokumentegenskaper som inkluderar *Titel*, *Författare* och *Versionsnummer*. Se den [utdata Excel-filen](64716836.xlsx) genererad av koden och skärmdumpen som visar den modifierade *Versionsnumret* med [**BuiltInDocumentPropertyCollection.DocumentVersion**](https://reference.aspose.com/cells/java/com.aspose.cells/builtindocumentpropertycollection#DocumentVersion)-egenskapen.

![todo:image_alt_text](specify-document-version-of-the-excel-file-using-builtin-document-properties_1.png)

## **Exempelkod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "LoadingSavingConvertingAndManaging-SpecifyDocumentVersionOfExcelFile.java" >}}
