---
title: Kontrollera lösenord för att ändra med Aspose.Cells
type: docs
weight: 2400
url: /sv/net/check-password-to-modify-using-aspose-cells/
---
{{% alert color="primary" %}}

 Ibland måste du kontrollera om det angivna lösenordet matchar**Lösenord att ändra** programmatiskt. Aspose.Cells tillhandahåller metoden WorkbookSettings.WriteProtection.ValidatePassword() som du kan använda för att kontrollera om det angivna lösenordet som ska ändras är korrekt eller inte.

{{% /alert %}}

## **Markera Lösenord för att ändra i Microsoft Excel**

 Du kan tilldela**Lösenord för att öppna** och**Lösenord att ändra** medan du skapar dina arbetsböcker i Microsoft Excel. Se den här skärmdumpen som visar gränssnittet Microsoft Excel tillhandahåller för att ange dessa lösenord.

|![todo:image_alt_text](check-password-to-modify-using-aspose-cells_1.png)|
|:- |

## **Kontrollera lösenord för att ändra med Aspose.Cells**

 Följande exempelkoder laddar[käll Excel](5112232.xlsx) fil. Den har ett lösenord som ska öppnas som 1234 och lösenord som ska ändras som 5678. Koden kontrollerar först om 567 är korrekt Lösenord att ändra och den returnerar falskt och sedan kontrollerar den om 5678 är lösenord att ändra och den returnerar sant.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-CheckPasswordToModify-CheckPasswordToModifyUsingAsposeCells.cs" >}}

### **Konsolutgång**

 Här är konsolutgången för ovanstående exempelkod efter att ha laddat[käll Excel](5112232.xlsx) fil.

{{< highlight "java" >}}

Is 567 correct Password to modify: False

Is 5678 correct Password to modify: True

{{< /highlight >}}
