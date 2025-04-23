---
title: Byt typsnitt på specifika Unicode tecken vid sparande till PDF
type: docs
weight: 260
url: /sv/net/change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf/
---

{{% alert color="primary" %}} 

Vissa unicode-tecken är inte visbara med det användarspecificerade teckensnittet. Ett sådant unicode-tecken är **icke-brytande bindestreck** (U+2011) och dess unicode-nummer är 8209. Detta tecken kan inte visas med **Times New Roman**, men det kan visas med andra teckensnitt som **Arial Unicode MS**.

När ett sådant tecken förekommer inuti ett ord eller en mening som är i något specifikt teckensnitt som Times New Roman, ändrar Aspose.Cells teckensnittet för hela ordet eller meningen till det teckensnitt som kan visa detta tecken som Arial Unicode till MS.

Emellertid är detta oönskat beteende för vissa användare och de vill att endast detta specifika teckens teckensnitt ska ändras istället för att ändra teckensnittet för hela ordet eller meningen.

För att hantera detta problem tillhandahåller Aspose.Cells egenskapen PdfSaveOptions.IsFontSubstitutionCharGranularity som bör ställas in till true så att endast teckensnittet för specifika tecken som inte kan visas ändras till ett visbart teckensnitt och resten av ordet eller meningen ska förbli i originalteckensnitt.

{{% /alert %}} 
## **Exempel**
Följande skärmbild jämför de två utdata-PDF:erna som genererats av koden nedan.

En är genererad utan att ställa in PdfSaveOptions.IsFontSubstitutionCharGranularity-egenskapen och den andra genererades efter att ha ställt in PdfSaveOptions.IsFontSubstitutionCharGranularity-egenskapen till true.

Som du kan se i den första PDF:en har teckensnittet för hela meningen ändrats från Times New Roman till Arial Unicode MS på grund av icke-brytande bindestreck. Medan i den andra PDF:en har endast teckensnittet för icke-brytande bindestreck ändrats.

|**Första PDF-filen**|
| :- |
|![todo:image_alt_text](change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf_1.png)|


|**Andra PDF-filen**|
| :- |
|![todo:image_alt_text](change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf_2.png)|
### **Exempelkod**


{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-ChangeFontUnicodeCharacterToPdf-ChangeFontUnicodeCharacterWhileSavingToPdf.cs" >}}



{{< app/cells/assistant language="csharp" >}}
