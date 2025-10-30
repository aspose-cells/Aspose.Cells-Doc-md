---
title: Få varningar vid inläsning av Excel fil med Node.js via C++
linktitle: Få varningar när Excel filen laddas
type: docs
weight: 110
url: /sv/nodejs-cpp/get-warnings-while-loading-excel-file/
description: Lär dig hur du fångar varningar vid inläsning av en Excel fil med Aspose.Cells for Node.js via C++. Hantera korrupta men inläsliga arbetsböcker effektivt.
---

## **Möjliga användningsscenario**

Ibland försöker användaren ladda en arbetsbok som är något korrupt men ändå kan läsas in. I sådana fall ger Aspose.Cells varningar vid inläsning av arbetsboken. Du kan fånga dessa varningar genom att implementera [**IWarningCallback**](https://reference.aspose.com/cells/nodejs-cpp/iwarningcallback)-gränssnittet och sätta [**LoadOptions.getWarningCallback()**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions/#getWarningCallback--)-egenskapen.

## **Få varningar vid inläsning av Excel-fil**

Följande exempel förklarar hur man får varningar vid inläsning av en Excel-fil. Koden laddar [exempel Excel-fil](sampleDuplicateDefinedName.xlsx) som genererar en [**DuplicateDefinedName**](https://reference.aspose.com/cells/nodejs-cpp/warningtype)-varning vid inläsning. Denna varning fångas sedan av [**IWarningCallback.warning(WarningInfo)**](https://reference.aspose.com/cells/nodejs-cpp/iwarningcallback/#warning-warninginfo-)-metoden som skriver varningsmeddelanden till konsolen. Koden sparar därefter arbetsboken som [utgångs Excel-fil](outputDuplicateDefinedName.xlsx). Om du öppnar exempel-Excel-filen i Microsoft Excel visas denna varning, som visas i skärmbilden. Vänligen kontrollera även kodens konsolutdata nedan för mer förståelse.

![todo:image_alt_text](get-warnings-while-loading-excel-file_1.png)

## **Exempelkod**

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// Implement IWarningCallback interface to catch warnings while loading workbook
class WarningCallback extends AsposeCells.IWarningCallback {
    warning(warningInfo) {
        if (warningInfo.getType() === AsposeCells.WarningType.DuplicateDefinedName) {
            console.log("Duplicate Defined Name Warning: " + warningInfo.getDescription());
        }
    }
}

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create load options and set the WarningCallback property 
// to catch warnings while loading workbook
const options = new AsposeCells.LoadOptions();
options.setWarningCallback(new WarningCallback());

// Load the source excel file
const book = new AsposeCells.Workbook(path.join(dataDir, "sampleDuplicateDefinedName.xlsx"), options);

// Save the workbook 
book.save(path.join(dataDir, "outputDuplicateDefinedName.xlsx"));
```

## **Konsoloutput**

Här är konsolens utdata för ovanstående kod när den körs med den medföljande [exempelfilen](sampleDuplicateDefinedName.xlsx).

{{< highlight java >}}

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:Introduction!$D$16:$D$17

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:Panel!$B$228

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:'Queries '!$D$14:$D$16

{{< /highlight >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
