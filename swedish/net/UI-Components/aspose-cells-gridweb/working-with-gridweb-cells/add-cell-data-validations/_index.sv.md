---
title: Lägg till Cell Datavalideringar
type: docs
weight: 90
url: /sv/net/add-cell-data-validations/
---
{{% alert color="primary" %}} 

 Aspose.Cells.GridWeb låter dig lägga till**Datavalidering** med metoden GridWorksheet.Validations.Add(). Med den här metoden måste du ange**Cell Räckvidd** Men om du vill skapa en datavalidering i en enda GridCell kan du göra det direkt med metoden GridCell.CreateValidation(). På samma sätt kan du ta bort**Datavalidering** från en GridCell med metoden GridCell.RemoveValidation().

{{% /alert %}} 
## **Skapa datavalidering i en GridCell av GridWeb**
 Följande exempelkod skapar en**Datavalidering** i en cell B3. Om du anger något värde som inte är mellan 20 och 40, visas cellen B3**Valideringsfel** i formen av**Röd XXXX** som visas i denna skärmdump.

![todo:image_alt_text](add-cell-data-validations_1.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AddDataValidation.aspx-AddDataValidation.cs" >}}
