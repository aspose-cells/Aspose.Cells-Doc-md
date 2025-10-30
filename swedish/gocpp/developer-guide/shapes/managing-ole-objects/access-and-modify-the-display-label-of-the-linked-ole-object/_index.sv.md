---
title: Åtkomst och modifiera displayetiketten för den länkade Ole objektet med Golang via C++
linktitle: Åtkomst och ändring av visningsmärket för det länkade OLE objektet
type: docs
weight: 100
url: /sv/go-cpp/access-and-modify-the-display-label-of-the-linked-ole-object/
description: Läs hur du får åtkomst till och ändrar visningsetiketten för länkade Ole objekt i Excel filer med Aspose.Cells for C++.
---

## **Möjliga användningsscenario**

Microsoft Excel gör det möjligt att ändra displayetiketten för Ole-objektet, som visas i följande skärmbild. Du kan också komma åt eller ändra displayetiketten för Ole-objektet med Aspose.Cells API:er med [**GetLabel()**](https://reference.aspose.com/cells/go-cpp/oleobject/getlabel/) och [**SetLabel(const U16String\& value)**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/oleobject/setlabel/)-metoderna.

![todo:image_alt_text](access-and-modify-the-display-label-of-the-linked-ole-object_1.png)

## **Åtkomst och ändring av visningsmärket för det länkade OLE-objektet**

Vänligen se följande provkod, den laddar [provexempel Excel-fil](64716810.xlsx) som innehåller Ole Object. Koden kommer åt Ole-objektet och ändrar dess etikett från prov API till Aspose API:er. Vänligen se konsolerna outputen nedan som visar effekten av provkoden på prov Excel-filen för referens.

## **Exempelkod**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AccessAndModifyTheDisplayLabelOfTheLinkedOleObject.go" >}}
## **Konsoloutput**

{{< highlight java >}}

Ole Object Label - Before: Sample APIs

Ole Object Label - After: Aspose APIs

{{< /highlight >}}
