---
title: Byt typsnitt på specifika Unicode tecken vid sparande till PDF
type: docs
weight: 150
url: /sv/java/change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf/
---

{{% alert color="primary" %}}

Vissa Unicode-tecken visas inte med det användarvalda typsnittet. Ett sådant Unicode-tecken är **Icke-linjär bindestreck** (U+2011) och dess Unicode-nummer är 8209. Detta tecken kan inte visas med **Times New Roman**, men det kan visas med andra typsnitt som **Arial Unicode MS**.

När ett sådant tecken förekommer inne i ett ord eller en mening som är skriven med ett specifikt typsnitt som Times New Roman, då ändrar Aspose.Cells typsnitt för hela ordet eller meningen till ett typsnitt som kan visa detta tecken, som Arial Unicode MS.

Detta är emellertid ett oönskat beteende för vissa användare och de vill endast att det specifika tecknets typsnitt ska ändras istället för att ändra typsnittet för hela ordet eller meningen.

För att hantera detta problem tillhandahåller Aspose.Cells egenskapen [**PdfSaveOptions.setFontSubstitutionCharGranularity()**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#IsFontSubstitutionCharGranularity) som ska sättas till sant så att endast typsnittet för det specifika tecknet som inte kan visas ändras och typsnittet för resten av ordet eller meningen förblir detsamma.

{{% /alert %}}

## **Exempel**

Följande skärmdump jämför de två utdatan PDF-filerna som genererats av exempelkoden nedan. En genererades utan att sätta [**PdfSaveOptions.setFontSubstitutionCharGranularity()**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#IsFontSubstitutionCharGranularity)-egenskapen och den andra genererades efter att [**PdfSaveOptions.setFontSubstitutionCharGranularity()**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#IsFontSubstitutionCharGranularity)-egenskapen sattes till sant. Som du kan se i den första PDF-filen har typsnittet för hela meningen ändrats från Times New Roman till Arial Unicode MS på grund av Non-breaking Hyphen. Medan i den andra PDF-filen har endast typsnittet för Non-breaking Hyphen ändrats.

![todo:image_alt_text](change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ChangeFontonspecificUnicodecharacters-ChangeFontonspecificUnicodecharacters.java" >}}
