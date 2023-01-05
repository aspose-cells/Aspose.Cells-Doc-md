---
title: Anpassad rad och anpassad kolumntext av GridDesktop-arbetsblad
type: docs
weight: 120
url: /sv/net/custom-row-and-custom-column-caption-of-griddesktop-worksheet/
---
## **Möjliga användningsscenarier**
Du kan anpassa rad- och kolumntexten i GridDesktop-kalkylbladet. Normalt börjar rad från 1 och kolumn börjar från A. Du kan ändra detta beteende och använda dina egna bildtexter för rader och kolumner i GridDesktop-kalkylbladet. För att ändra bildtexterna för rader och kolumner, implementera gränssnitten ICustomRowCaption och ICustomColumnCaption.
## **Anpassad rad och anpassad kolumntext av GridDesktop-arbetsblad**
Följande exempelkod implementerar gränssnitten ICustomRowCaption och ICustomColumnCaption och ändrar bildtexterna för rader och kolumner. Skärmdumpen visar resultatet av exekveringen av denna exempelkod som referens.



![todo:image_alt_text](custom-row-and-custom-column-caption-of-griddesktop-worksheet_1.png)

## **Exempelkod**
{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples-GridDesktop-CSharp-WorkingWithRowsandColumns-Form_CustomRowAndCustomColumnCaptionOfGridDesktopWorksheet.cs" >}}
