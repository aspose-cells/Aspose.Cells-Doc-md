---
title: Ändra teckensnittet på bara de specifika Unicode-tecken samtidigt som du sparar till PDF
type: docs
weight: 150
url: /sv/java/change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf/
---
{{% alert color="primary" %}}

 Vissa Unicode-tecken kan inte visas med det användarspecificerade teckensnittet. Ett sådant Unicode-tecken är**Icke-brytande bindestreck** (U+2011) och dess Unicode-nummer är 8209. Detta tecken kan inte visas med**Times New Roman** , men det kan visas med andra typsnitt som**Arial Unicode MS**.

När ett sådant tecken förekommer i ett ord eller en mening som är i något specifikt teckensnitt som Times New Roman, ändrar Aspose.Cells teckensnittet för hela ordet eller meningen till teckensnitt som kan visa detta tecken som Arial Unicode till MS.

Detta är dock ett oönskat beteende för vissa användare och de vill bara att den specifika karaktärens teckensnitt måste ändras istället för att ändra teckensnittet för hela ordet eller meningen.

 För att hantera detta problem tillhandahåller Aspose.Cells[**PdfSaveOptions.setFontSubstitutionCharGranularity()**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#IsFontSubstitutionCharGranularity) egenskap som bör ställas in**Sann** så att endast teckensnittet för det specifika tecknet som inte kan visas ändras och teckensnittet för resten av ordet eller meningen förblir detsamma.

{{% /alert %}}

## **Exempel**

 Följande skärmdump jämför de två utgående PDF-filerna som genereras av exempelkoden nedan. En genererades utan inställning[**PdfSaveOptions.setFontSubstitutionCharGranularity()**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#IsFontSubstitutionCharGranularity) egendom och den andra genererades efter att ha ställt in[**PdfSaveOptions.setFontSubstitutionCharGranularity()**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#IsFontSubstitutionCharGranularity) egendom till**Sann**. Som du kan se i den första PDF, har teckensnittet för hela meningen ändrats från Times New Roman till Arial Unicode MS på grund av Non-Breaking Hyphen. Medan i den andra PDF har bara teckensnittet för Non-Breaking Hyphen ändrats.

![todo:image_alt_text](change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ChangeFontonspecificUnicodecharacters-ChangeFontonspecificUnicodecharacters.java" >}}
