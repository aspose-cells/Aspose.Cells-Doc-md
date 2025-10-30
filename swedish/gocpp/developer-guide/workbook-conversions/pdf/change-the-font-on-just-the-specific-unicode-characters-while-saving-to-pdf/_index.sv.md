---
title: Ändra teckensnittet för enskilda Unicode tecken när du sparar till PDF med Golang via C++
linktitle: Ändra typsnitt för Unicode tecken
type: docs
weight: 260
url: /sv/go-cpp/change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf/
description: Lär dig hur du ändrar teckensnitt för specifika Unicode tecken när du sparar till PDF med Aspose.Cells med Golang via C++
---

{{% alert color="primary" %}}

Vissa Unicode-tecken visas inte med det användarvalda typsnittet. Ett sådant Unicode-tecken är **Icke-linjär bindestreck** (U+2011) och dess Unicode-nummer är 8209. Detta tecken kan inte visas med **Times New Roman**, men det kan visas med andra typsnitt som **Arial Unicode MS**.

När ett sådant tecken förekommer inuti ett ord eller en mening som är i någon specifik typsnitt som Times New Roman, ändrar Aspose.Cells typsnittet för hela ordet eller meningen till ett typsnitt som kan visa detta tecken, som Arial Unicode MS.

Detta är dock oönskat för vissa användare, och de vill bara att typsnittet för det specifika tecknet ska ändras, inte hela ordet eller meningen.

För att hantera detta problem tillhandahåller Aspose.Cells egenskapen `PdfSaveOptions.IsFontSubstitutionCharGranularity`, som ska sättas till `true` så att bara typsnittet för det specifika tecknet som inte kan visas ändras till ett visas-typsnitt, och resten av ordet eller meningen förblir i det ursprungliga typsnittet.

{{% /alert %}}

## **Exempel**

Följande skärmbild jämför de två utdata-PDF:erna som genererats av koden nedan.

Ett genereras utan att ställa in egenskapen `PdfSaveOptions.IsFontSubstitutionCharGranularity`, och det andra genererades efter att egenskapen satts till `true`.

Som du kan se i den första PDF-filen har typsnittet för hela meningen ändrats från Times New Roman till Arial Unicode MS på grund av icke-brytande bindestrecket. I den andra PDF-filen har endast typsnittet för icke-brytande bindestrecket ändrats.

|**Första PDF-fil**|
| :- |
|![todo:image_alt_text](change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf_1.png)|

|**Andra PDF-fil**|
| :- |
|![todo:image_alt_text](change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf_2.png)|

### **Exempelkod**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ChangeTheFontOnJustTheSpecificUnicodeCharactersWhileSavingToPdf.go" >}}
