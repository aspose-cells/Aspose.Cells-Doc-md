---
title: Lägga till arbetsblad
type: docs
weight: 20
url: /sv/net/aspose-cells-gridweb/add-worksheet/
keywords: GridWeb,add,worksheet,add GridWorksheet
description: Den här artikeln introducerar hur du lägger till arbetsblad (GridWorksheet) i GridWeb.
---

{{% alert color="primary" %}} 

Arbetsblad är en integrerad del av Aspose.Cells.GridWeb. All data hanteras och lagras i form av arbetsblad. Aspose.Cells.GridWeb tillåter utvecklare att lägga till ett eller flera arbetsblad i Aspose.Cells.GridWeb-kontrollen. Detta ämne visar enkla tillvägagångssätt för att lägga till arbetsblad i Aspose.Cells.GridWeb.

{{% /alert %}} 
## **Lägga till ett arbetsblad**
### **Utan att ange bladnamn**
Det enklaste sättet att lägga till ett arbetsblad i Aspose.Cells.GridWeb är att använda Add-metoden i GridWorksheetCollection-samlingen i GridWeb-kontrollen. Detta skapar arbetsblad som använder standardnamn (som Sheet1, Sheet2, Sheet3 osv) och lägger till dem i GridWeb-kontrollen.

**Utdata: Ett arbetsblad med standardnamn har lagts till i GridWeb** 

![todo:image_alt_text](add-worksheets_1.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-AddWorksheets.aspx-AddWorksheetWithoutName.cs" >}}

{{% alert color="primary" %}} 

Add-metoden returnerar det nya arbetsbladets index som kan användas för att få åtkomst till instansen av detta arbetsblad. För mer detaljer om hur du får åtkomst till arbetsblad, läs [Få åtkomst till arbetsblad](/cells/sv/net/aspose-cells-gridweb/access-worksheets/).

{{% /alert %}} 
### **Med angivet bladnamn**
För att lägga till ett arbetsblad med ett specifikt namn i GridWeb-kontrollen istället för att använda standardnamnsschemat, anropa en överlagrad version av Add-metoden som tar det angivna bladnamnet. Till exempel lägger följande exempel till ett arbetsblad med namnet Faktura.

**Utdata: Ett arbetsblad med ett angivet namn har lagts till i GridWeb** 

![todo:image_alt_text](add-worksheets_2.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-AddWorksheets.aspx-AddWorksheetWithName.cs" >}}

{{% alert color="primary" %}} 

Add-metoden som accepterar bladnamnet som en sträng returnerar en instans av GridWorksheet.

{{% /alert %}}
