---
title: Aspose.Cells for Java 21.2 Release Notes
type: docs
weight: 11
url: /sv/java/aspose-cells-for-java-21-2-release-notes/
---
{{% alert color="primary" %}}

 Den här sidan innehåller release notes för[Aspose.Cells for Java 21.2](https://downloads.aspose.com/cells/java/new-releases/aspose.cells-for-java-21.2/).

{{% /alert %}}

|**Nyckel**|**Sammanfattning**|**Kategori**|
|:- |:- |:- |
|CELLSJAVA-43382|Kopiera producerar skadad arbetsbok|
|CELLSJAVA-43364|Problem när du sparar diagram med bild i markören till bild|
|CELLSJAVA-43389|Arbetsbok/arbetsblad Lösenordsskyddsinställningar förlorade när du sparade som XLSB-filformat|
|CELLSJAVA-43392|Kopiering av ark ger en korrupt arbetsbok|
|CELLSJAVA-43387|Export av ett ark till HTML ger undantag|

## **Offentlig API och bakåtinkompatibla ändringar**

Följande är en lista över alla ändringar som gjorts för allmänheten API, såsom tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts till Aspose.Cells for Java. Om du har frågor om någon ändring som anges, vänligen ta upp den på supportforumet Aspose.Cells.

### **Ändrar beteendet för Cells.DeleteBlankRows()/Cells.DeleteBlankRows(DeleteOptions)**

gamla versioner tar vi bort alla kolumninställningar samtidigt som vi raderar tomma rader om kalkylbladet är tomt (inga celldata). Detta gör det omöjligt för användaren att bara ta bort tomma rader och behålla alla kolumninställningar. Från 21.2 rensar vi inte längre kolumninställningar. Om användaren behöver ta bort kolumninställningar för tomt kalkylblad, bör han kontrollera att det inte finns några data i arket och sedan rensa kolumnsamlingen manuellt.
I gamla versioner tar vi inte bort tomma rader under form. Detta gör det omöjligt för användaren att ta bort alla tomma rader som de förväntar sig. Från 12.2 tar vi bort de tomma raderna under form tillsammans med andra vanliga tomma rader.

### **Föråldrad Range.CellCount-egenskap.**

Använd Range.RowCount och Range.ColumnCount för att få det totala cellantalet istället.

### **Lägger till egenskapen AutoFilter.ShowFilterButton.**

Indikerar om filterknappen för autofiltret visas.

### **Tar bort egenskapen SeriesCollection.SecondCatergoryData.**

Använd egenskapen SeriesCollection.SecondCategoryData istället.

### **Tar bort StyleModifyFlag.Spacing enum.**

Den är inte använd.
