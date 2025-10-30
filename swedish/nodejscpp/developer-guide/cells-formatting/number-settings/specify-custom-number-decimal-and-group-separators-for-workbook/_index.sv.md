---
title: Ange anpassade decimal och grupptalsavskiljare för arbetsboken
linktitle: Ange anpassade decimal och grupptalsavskiljare för arbetsboken
type: docs
weight: 110
url: /sv/nodejs-cpp/specify-custom-number-decimal-and-group-separators-for-workbook/
description: Ändra nummerdecimals och grupperingsseparatorer i Excel med Aspose.Cells for Node.js via C++. 
keywords: ange anpassad decimalseparator i excel node.js via C++, ange anpassad grupperingsseparator i excel node.js via C++, ändra decimal och grupperingsseparator i excel node.js via C++
---

{{% alert color="primary" %}}

I Microsoft Excel kan du ange anpassade decimal- och tusentalsavskiljare istället för att använda systemavskiljare från **Avancerade Excel-alternativ** enligt skärmbilden nedan.

Aspose.Cells tillhandahåller metoderna [**WorkbookSettings.setNumberDecimalSeparator(string)**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#setNumberDecimalSeparator-string-) och [**WorkbookSettings.setNumberGroupSeparator(string)**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#setNumberGroupSeparator-string-) för att ställa in anpassade separatorer för formatering/parsing av nummer.

{{% /alert %}}

## **Ange anpassade avskiljare i Microsoft Excel**

Följande skärmbild visar **Avancerade Excel-alternativ** och markerar avsnittet för att ange **Anpassade avskiljare**.

![todo:image_alt_text](specify-custom-number-decimal-and-group-separators-for-workbook_1.png)

## **Ange anpassade separatorer med Aspose.Cells for Node.js via C++**

Följande exempelkod illustrerar hur man anger anpassade avskiljare med Aspose.Cells API. Det specificerar anpassade decimal- och grupptalsavskiljare som punkt och mellanslag respektive.

### Node.js-kod för att ange anpassade nummerdecimala och grupperingsseparatorer

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-NumberSetting-SpecifyCustomNumberDecimalAndGroupSeparators.js" >}}


{{< app/cells/assistant language="nodejs-cpp" >}}
