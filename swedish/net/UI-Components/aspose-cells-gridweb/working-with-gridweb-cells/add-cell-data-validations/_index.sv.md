---
title: Lägg till celldata validering
type: docs
weight: 90
url: /sv/net/aspose-cells-gridweb/add-cell-data-validations/
keywords: GridWeb, validering, data validering, GridValidation
description: Den här artikeln introducerar hur man lägger till datavalidering (GridValidation) i GridWeb.
---

{{% alert color="primary" %}} 

Aspose.Cells.GridWeb tillåter dig att lägga till **Data Validation** genom att använda metoden GridWorksheet.Validations.Add(). Med denna metod måste du specificera **Cell Range**. Men om du vill skapa en datavalidering i en enda GridCell kan du göra det direkt med metoden GridCell.CreateValidation(). På samma sätt kan du ta bort **Data Validation** från en GridCell med hjälp av metoden GridCell.RemoveValidation().

{{% /alert %}} 
## **Skapa datavalidering i en GridCell av GridWeb**
Följande exempelkod skapar en **Data Validering** i en cell B3. Om du anger något värde som inte ligger mellan 20 och 40, kommer cellen B3 att visa en **Valideringsfel** i form av **Rött XXXX** som visas på skärmdumpen.

![todo:image_alt_text](add-cell-data-validations_1.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AddDataValidation.aspx-AddDataValidation.cs" >}}
