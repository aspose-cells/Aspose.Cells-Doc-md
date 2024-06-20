---
title: Ändra decimalavskiljaren från numeriskt tangentbord
type: docs
weight: 150
url: /sv/net/aspose-cells-gridweb/change-the-decimal-separator-from-numeric-keypad/
keywords: GridWeb, decimal, decimalavskiljare
description: Den här artikeln introducerar hur man ändrar decimalavskiljaren i GridWeb.
---

## **Möjliga användningsscenario**
Som standard visar Aspose.Cells.GridWeb numeriska data i enlighet med inställningarna för språk och region på maskinen. Du kan ändra decimalavgränsaren från den numeriska tangentbordet genom att använda Aspose.Cells.GridWeb API. Så när en fil importeras till GridWeb-matrisen eller när du anger några numeriska data (från det numeriska tangentbordet) i en ny kalkylbladscell, ska det se ut enligt önskad decimalavgränsare. 
## **Ändra decimalavgränsaren från den numeriska tangentbordet**
Genom att använda egenskapen **GridWorksheetCollection.NumberDecimalSeparator** kan du ändra decimalavgränsaren från den numeriska tangentbordet programmatiskt. Se gärna skärmbilderna som visar hur det fungerar

![todo:image_alt_text](change-the-decimal-separator-from-numeric-keypad_1.png)

![todo:image_alt_text](change-the-decimal-separator-from-numeric-keypad_2.png)
## **Exempelkod**
{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Worksheets-ChangeDecimalSeparatorFromNumericKeypad.aspx.cs" >}}

{{% alert color="primary" %}} 

Observera att ändringen av decimalavgränsaren endast gäller för användarnas visuella upplevelse i GridWeb. När du redigerar och sparar din arbetsbok lagras numeriska värden (i kalkylarket) fortfarande enligt din språk- eller regionsavgränsare.

{{% /alert %}}
