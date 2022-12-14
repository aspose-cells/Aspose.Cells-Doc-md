---
title: Ändra decimalavgränsaren från det numeriska tangentbordet
type: docs
weight: 150
url: /sv/net/change-the-decimal-separator-from-numeric-keypad/
---
## **Möjliga användningsscenarier**
Som standard visar Aspose.Cells.GridWeb numeriska data baserat på lokala/regionala inställningar på maskinen. Du kan ändra decimalavgränsaren från det numeriska tangentbordet programmatiskt med Aspose.Cells.GridWeb API. Så när en fil importeras till GridWeb-matrisen eller du matar in några numeriska data (från det numeriska tangentbordet) i en ny kalkylbladscell, bör den ha önskad decimalavgränsare inställd visuellt.
## **Ändra decimalavgränsaren från det numeriska tangentbordet**
Använda**GridWorksheetCollection.NumberDecimalSeparator**egenskap, kan du ändra decimalavgränsaren från den numeriska knappsatsen programmatiskt. Se skärmdumparna som visar hur det fungerar

![todo:image_alt_text](change-the-decimal-separator-from-numeric-keypad_1.png)

![todo:image_alt_text](change-the-decimal-separator-from-numeric-keypad_2.png)
## **Exempelkod**
{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Worksheets-ChangeDecimalSeparatorFromNumericKeypad.aspx.cs" >}}

{{% alert color="primary" %}} 

Observera att ändring av decimalavgränsare endast är för användarnas visuella upplevelse i GridWeb. När du redigerar och sparar din arbetsbok kommer den fortfarande att lagra de numeriska värdena (i kalkylarket) enligt din lokala/regionala decimalavgränsare.

{{% /alert %}}
