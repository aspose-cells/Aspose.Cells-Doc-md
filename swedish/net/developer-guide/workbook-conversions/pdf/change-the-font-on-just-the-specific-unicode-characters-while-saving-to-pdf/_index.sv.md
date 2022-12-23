---
title: Ändra teckensnittet på bara de specifika Unicode-tecken samtidigt som du sparar till PDF
type: docs
weight: 260
url: /sv/net/change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf/
---
{{% alert color="primary" %}} 

 Vissa Unicode-tecken kan inte visas av det användarspecificerade teckensnittet. Ett sådant Unicode-tecken är**Icke-brytande bindestreck** (U+2011) och dess Unicode-nummer är 8209. Detta tecken kan inte visas med**Times New Roman** , men det kan visas med andra typsnitt som**Arial Unicode MS**.

När ett sådant tecken förekommer i ett ord eller en mening som är i något specifikt teckensnitt som Times New Roman, ändrar Aspose.Cells teckensnittet för hela ordet eller meningen till teckensnitt som kan visa detta tecken som Arial Unicode till MS.

Detta är dock ett oönskat beteende för vissa användare och de vill bara att den specifika karaktärens teckensnitt måste ändras istället för att ändra teckensnittet för hela ordet eller meningen.

För att komma till rätta med detta problem tillhandahåller Aspose.Cells egenskapen PdfSaveOptions.IsFontSubstitutionCharGranularity som ska ställas in som sann så att endast teckensnittet med ett specifikt tecken som inte går att visa ändras till ett visningsbart teckensnitt och resten av ordet eller meningen ska vara kvar i det ursprungliga teckensnittet.

{{% /alert %}} 
## **Exempel**
Följande skärmdump jämför de två utgående PDF-filerna som genereras av exempelkoden nedan.

Den ena genereras utan att ställa in egenskapen PdfSaveOptions.IsFontSubstitutionCharGranularity och den andra genererades efter att egenskapen PdfSaveOptions.IsFontSubstitutionCharGranularity ställdes in på true.

Som du kan se i den första pdf-filen har teckensnittet för hela meningen ändrats från Times New Roman till Arial Unicode MS på grund av Non-Breaking Hyphen. Medan i den andra PDF-filen har bara teckensnittet för Non-Breaking Hyphen ändrats.

|**Första pdf-filen**|
|:- |
|![todo:image_alt_text](change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf_1.png)|


|**Andra pdf-filen**|
|:- |
|![todo:image_alt_text](change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf_2.png)|
### **Exempelkod**


{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-ChangeFontUnicodeCharacterToPdf-ChangeFontUnicodeCharacterWhileSavingToPdf.cs" >}}



