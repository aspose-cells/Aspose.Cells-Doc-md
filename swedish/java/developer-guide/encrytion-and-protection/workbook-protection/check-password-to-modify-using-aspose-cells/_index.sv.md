---
title: Kontrollera lösenordet för att ändra med Aspose.Cells
type: docs
weight: 190
url: /sv/java/check-password-to-modify-using-aspose-cells/
---

{{% alert color="primary" %}}

Du kan tilldela ett **lösenord för att öppna** och ett **lösenord för att ändra** när du skapar dina arbetsböcker i Microsoft Excel. Vänligen se denna skärmdump som visar gränssnittet Microsoft Excel tillhandahåller för att ange dessa lösenord.

![todo:image_alt_text](check-password-to-modify-using-aspose-cells_1.png)

Ibland behöver du kontrollera om det angivna lösenordet överensstämmer med **lösenordet för att ändra** programmatiskt. Aspose.Cells tillhandahåller [**workbook.getSettings().getWriteProtection().validatePassword()**](https://reference.aspose.com/cells/java/com.aspose.cells/writeprotection#validatePassword-java.lang.String-)-metoden som du kan använda för att kontrollera om det angivna lösenordet för ändring är korrekt eller inte.

{{% /alert %}}

## Java-kod för att kontrollera lösenordet för att ändra med Aspose.Cells

Följande exempelkoder laddar [käll-Excel-filen](5473057.xlsx). Den har ett lösenord för att öppna som *1234* och lösenord för att ändra som *5678*. Koden kontrollerar först om *567* är korrekt lösenord för att ändra och den returnerar **false** och sedan kontrollerar den om *5678* är lösenord för att ändra och den returnerar **true**.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CheckPassword-CheckPassword.java" >}}

## Konsolutmatning genererad av Java-koden

Här är konsolresultatet av den ovanstående exempelkoden efter att ha laddat [käll-Excel-filen](5473057.xlsx).

{{< highlight java >}}

Is 567 correct Password to modify: false

Is 5678 correct Password to modify: true

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
