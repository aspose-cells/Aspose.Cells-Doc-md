---
title: Kontrollera lösenord för att ändra med Aspose.Cells för Python via .NET
type: docs
weight: 2400
url: /sv/python-net/check-password-to-modify-using-aspose-cells/
---

{{% alert color="primary" %}}

Ibland måste du kontrollera om det angivna lösenordet stämmer överens med programmet **Lösenord för att ändra**. Aspose.Cells för Python via .NET tillhandahåller metoden WorkbookSettings.write_protection.validate_password() som du kan använda för att kontrollera om det angivna lösenordet för att ändra är korrekt eller inte.

{{% /alert %}}

## **Kontrollera lösenord för modifiering i Microsoft Excel**

Du kan tilldela **Lösenord för att öppna** och **Lösenord för att modifiera** när du skapar dina arbetsböcker i Microsoft Excel. Se denna skärmbild som visar gränssnittet som Microsoft Excel tillhandahåller för att ange dessa lösenord.

|![todo:image_alt_text](check-password-to-modify-using-aspose-cells_1.png)|
| :- |

## ** Kontrollera lösenord för att ändra med Aspose.Cells för Python via .NET**

Följande kodexempel laddar den [käll-Excel-filen](5112232.xlsx). Den har ett Lösenord för att öppna som 1234 och ett Lösenord för att modifiera som 5678. Koden kontrollerar först om 567 är korrekt lösenord för modifiering och returnerar falskt och sedan kontrollerar den om 5678 är lösenord för modifiering och det returnerar sant.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-CheckPasswordToModifyUsingAsposeCells.py" >}}

### **Konsoloutput**

Här är konsolens utmatning av ovanstående kod efter att ha laddat den [käll-Excel-filen](5112232.xlsx).

{{< highlight java >}}

Is 567 correct Password to modify: False

Is 5678 correct Password to modify: True

{{< /highlight >}}

{{< app/cells/assistant language="python-net" >}}
