---
title: Lägg till arbetsblad
type: docs
weight: 20
url: /sv/net/add-worksheets/
---
{{% alert color="primary" %}} 

Arbetsblad är en integrerad del av Aspose.Cells.GridWeb. All data hanteras och lagras i form av arbetsblad. Aspose.Cells.GridWeb tillåter utvecklare att lägga till ett eller flera kalkylblad till Aspose.Cells.GridWeb-kontrollen. Det här ämnet visar enkla metoder för att lägga till kalkylblad till Aspose.Cells.GridWeb.

{{% /alert %}} 
## **Lägga till ett arbetsblad**
### **Utan att ange arbetsbladsnamn**
Det enklaste sättet att lägga till ett kalkylblad till Aspose.Cells.GridWeb är att anropa GridWorksheetCollection-samlingens Add-metod i GridWeb-kontrollen. Detta skapar kalkylblad som använder standardnamn (det vill säga Sheet1, Sheet2, Sheet3 och så vidare) och lägger till dem i GridWeb-kontrollen.

**Utdata: ett kalkylblad med standardnamn har lagts till i GridWeb** 

![todo:image_alt_text](add-worksheets_1.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-AddWorksheets.aspx-AddWorksheetWithoutName.cs" >}}

{{% alert color="primary" %}} 

 Metoden Lägg till returnerar det nya kalkylbladets index som kan användas för att komma åt instansen av detta kalkylblad. För mer information om hur du kommer åt arbetsblad, läs[Få tillgång till arbetsblad](/cells/sv/net/access-worksheets/).

{{% /alert %}} 
### **Med specificerat bladnamn**
För att lägga till ett kalkylblad med ett specifikt namn till GridWeb-kontrollen istället för att använda standardnamnschemat, anropar du en överbelastad version av Add-metoden som tar det angivna SheetName. Exempelvis lägger exemplet nedan till ett kalkylblad med namnet Faktura.

**Utdata: ett kalkylblad med ett angivet namn har lagts till i GridWeb** 

![todo:image_alt_text](add-worksheets_2.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-AddWorksheets.aspx-AddWorksheetWithName.cs" >}}

{{% alert color="primary" %}} 

Metoden Add som accepterar kalkylbladets namn som sträng returnerar en instans av GridWorksheet.

{{% /alert %}}
