---
title: Kontrollera lösenordet för att ändra med Aspose.Cells
type: docs
weight: 2400
url: /sv/net/check-password-to-modify-using-aspose-cells/
---

{{% alert color="primary" %}}

Ibland måste du kontrollera om det angivna lösenordet stämmer överens med **Lösenord för modifiering** programmatiskt. Aspose.Cells tillhandahåller metoden WorkbookSettings.WriteProtection.ValidatePassword() som du kan använda för att kontrollera om det angivna lösenordet för modifiering är korrekt eller inte.

{{% /alert %}}

## **Kontrollera lösenord för modifiering i Microsoft Excel**

Du kan tilldela **Lösenord för att öppna** och **Lösenord för att modifiera** när du skapar dina arbetsböcker i Microsoft Excel. Se denna skärmbild som visar gränssnittet som Microsoft Excel tillhandahåller för att ange dessa lösenord.

|![todo:image_alt_text](check-password-to-modify-using-aspose-cells_1.png)|
| :- |

## **Kontrollera lösenord för modifiering med Aspose.Cells**

Följande kodexempel laddar den [käll-Excel-filen](5112232.xlsx). Den har ett Lösenord för att öppna som 1234 och ett Lösenord för att modifiera som 5678. Koden kontrollerar först om 567 är korrekt lösenord för modifiering och returnerar falskt och sedan kontrollerar den om 5678 är lösenord för modifiering och det returnerar sant.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-CheckPasswordToModify-CheckPasswordToModifyUsingAsposeCells.cs" >}}

### **Konsoloutput**

Här är konsolens utmatning av ovanstående kod efter att ha laddat den [käll-Excel-filen](5112232.xlsx).

{{< highlight java >}}

Is 567 correct Password to modify: False

Is 5678 correct Password to modify: True

{{< /highlight >}}
