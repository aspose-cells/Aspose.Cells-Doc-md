---
title: Ange anpassade nummerdecimaler och gruppseparatorer för arbetsbok med Golang via C++
linktitle: Specificera anpassade decimala och grupperingsseparatorer
type: docs
weight: 110
url: /sv/go-cpp/specify-custom-number-decimal-and-group-separators-for-workbook/
description: Ändra nummerdecimala och gruppseparatorer i MS Excel och med Golang via C++ kod genom att använda Aspose.Cells for C++ API.
keywords: specificera anpassad decimalseparator i excel, specificera anpassad decimalseparator i excel c++, specificera anpassad gruppseparator i excel, specificera anpassad gruppseparator i excel c++, specificera anpassad decimal och gruppseparator i excel, specificera anpassad decimal och gruppseparator i excel c++, ändra decimal och gruppseparator i excel, ändra decimal och gruppseparator, ändra decimalseparator i excel, ändra decimalseparator i excel c++, ändra gruppseparator i excel, ändra gruppseparator i excel c++
---

{{% alert color="primary" %}}

I Microsoft Excel kan du ange anpassade decimal- och tusentalsavskiljare istället för att använda systemavskiljare från **Avancerade Excel-alternativ** enligt skärmbilden nedan.

Aspose.Cells tillhandahåller [**WorkbookSettings.GetNumberDecimalSeparator()**](https://reference.aspose.com/cells/go-cpp/workbooksettings/getnumberdecimalseparator/) och [**WorkbookSettings.GetNumberGroupSeparator()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getnumbergroupseparator/) egenskaper för att ange anpassade avskiljare för formatering/parsning av nummer.

{{% /alert %}}

## **Ange anpassade avskiljare i Microsoft Excel**

Följande skärmbild visar **Avancerade Excel-alternativ** och markerar avsnittet för att ange **Anpassade avskiljare**.

![todo:image_alt_text](specify-custom-number-decimal-and-group-separators-for-workbook_1.png)

## **Ange anpassade avskiljare med Aspose.Cells**

Följande exempelkod illustrerar hur man anger anpassade avskiljare med Aspose.Cells API. Det specificerar anpassade decimal- och grupptalsavskiljare som punkt och mellanslag respektive.

### C++ kod för att specificera anpassade nummerdecimala och grupperingsseparatorer

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SpecifyCustomNumberDecimalAndGroupSeparatorsForWorkbook.go" >}}
