---
title: Hitta celler med specifik stil
type: docs
weight: 80
url: /sv/java/find-cells-with-specific-style/
description: Denna artikel demonstrerar hur man hittar celler med specifik stil med hjälp av MS Excel och Aspose.Cells for Java SDK.
keywords: hitta celler med specifik stil, hitta celler med specifik stil excel, hitta celler med specifik stil excel java, sök celler med specifik stil, sök celler med specifik stil excel, sök celler med specifik stil excel java, hur man hittar celler med specifik stil, hur man hittar celler med specifik stil excel, hur man hittar celler med specifik stil excel java
---

{{% alert color="primary" %}}

Ibland behöver du hitta celler med en viss stil. Denna artikel demonstrerar hur du kan åstadkomma detta med hjälp av Microsoft Excel samt Aspose.Cells for Java SDK.

{{% /alert %}}

## Använda Microsoft Excel

Dessa är stegen som krävs för att söka celler med specifika stilar i MS Excel.

1. Välj **Sök & Markera** i **Startfliken**.
1. Välj **Hitta**.
1. Klicka på **Alternativ** om avancerade alternativ inte är synliga.
1. Välj **Välj format från cell...** från rullgardinsmenyn **Format**.
1. Välj cellen med den stil som du vill söka efter.
1. Klicka på **Hitta alla** för att hitta alla celler med stil liknande din valda cell.

## Använda Aspose.Cells for Java

Aspose.Cells for Java tillhandahåller funktionen att hitta celler i arbetsblad med en viss stil. För detta tillhandahåller API:et egenskapen [**FindOptions.setStyle()**](https://reference.aspose.com/cells/java/com.aspose.cells/findoptions#Style).

### Exempelkod

Följande kodsnutt hittar alla celler som har samma stil som cellen **A1** och ändrar texten i dessa celler. Se gärna skärmbilden av käll- och utdatafilerna för att analysera utdata av exempelkoden.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-FindCellsWithSpecificStyle-FindCellsWithSpecificStyle.java" >}}

Efter att koden har utförts kommer alla celler som har samma stil som cell A1 att ha texten "Hittad".

### Skärmbilder

![todo:image_alt_text](find-cells-with-specific-style_1.png)

**Figur:** Källfil med celler som har stilar

Här är utdatafilen som genererats av följande kod. Du kan se att alla celler som har samma stil som cellen **A1** har texten "Hittad"

![todo:image_alt_text](find-cells-with-specific-style_2.png)

**Figur:** Utdatafil med hittade celler efter sökning med stil **A1**
{{< app/cells/assistant language="java" >}}
