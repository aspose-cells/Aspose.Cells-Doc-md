---
title: Kontrollera lösenord för att ändra med Aspose.Cells
type: docs
weight: 190
url: /sv/java/check-password-to-modify-using-aspose-cells/
---
{{% alert color="primary" %}}

 Du kan tilldela en**Lösenord för att öppna** och a**Lösenord att ändra** medan du skapar dina arbetsböcker i Microsoft Excel. Se den här skärmdumpen som visar gränssnittet Microsoft Excel tillhandahåller för att ange dessa lösenord.

![todo:image_alt_text](check-password-to-modify-using-aspose-cells_1.png)

 Ibland måste du kontrollera om det angivna lösenordet matchar**Lösenord att ändra** programmatiskt. Aspose.Cells tillhandahåller[**workbook.getSettings().getWriteProtection().validatePassword()**](https://reference.aspose.com/cells/java/com.aspose.cells/writeprotection#validatePassword(java.lang.String)) metod som du kan använda för att kontrollera om det angivna lösenordet som ska ändras är korrekt eller inte.

{{% /alert %}}

## Java-kod för att kontrollera Lösenord för att ändra med Aspose.Cells

 Följande exempelkoder laddar[käll Excel](5473057.xlsx) fil. Den har ett lösenord att öppna som*1234* och lösenord att ändra som*5678* . Koden kontrollerar först om*567* är korrekt lösenord att ändra och det returneras**falsk** och sedan kontrollerar den om*5678* är lösenordet att ändra och det returneras**Sann**.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CheckPassword-CheckPassword.java" >}}

## Konsolutdata genererad av Java-koden

 Här är konsolutgången för ovanstående exempelkod efter att ha laddat[käll Excel](5473057.xlsx) fil.

{{< highlight "java" >}}

Is 567 correct Password to modify: false

Is 5678 correct Password to modify: true

{{< /highlight >}}
