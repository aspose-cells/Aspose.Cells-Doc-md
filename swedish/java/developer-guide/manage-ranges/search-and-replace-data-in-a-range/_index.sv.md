---
title: Sök och ersätt data i ett intervall
type: docs
weight: 60
url: /sv/java/search-and-replace-data-in-a-range/
description: Den här artikeln visar hur du söker och ersätter data i ett intervall i Excel med Java-kod.
keywords: java search and replace data in excel, java search data in excel, java search and replace data in a range, java search data in a range, java searching data in a range, java searching data in range, java searching data in excel, java search data in range, search and replace data in excel with java, search and replace data in a range with java, search and replace data in range with java
---
{{% alert color="primary" %}}

Ibland måste du söka efter och ersätta specifik data i ett intervall och ignorera eventuella cellvärden utanför det önskade intervallet. Aspose.Cells låter dig begränsa en sökning till ett specifikt område. Den här artikeln förklarar hur.

{{% /alert %}}

Aspose.Cells tillhandahåller[**FindOptions.setRange()**](https://reference.aspose.com/cells/java/com.aspose.cells/findoptions#setRange(com.aspose.cells.CellArea)) metod för att ange ett intervall när du söker efter data.

 Anta att du vill söka efter strängen**"Sök"** och byt ut den mot**"byta ut"** innom räckhåll**E3:H6**. I skärmdumpen nedan kan strängen "sök" ses i flera celler men vi vill ersätta den endast i ett givet intervall, här markerat med gult.

**Indatafil**

![todo:image_alt_text](search-and-replace-data-in-a-range_1.png)

Efter exekvering av koden ser utdatafilen ut som nedan. Alla "sök"-strängar inom intervallet har ersatts med "ersätt".

**Utdatafil**

![todo:image_alt_text](search-and-replace-data-in-a-range_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SearchReplaceDataInRange-SearchReplaceDataInRange.java" >}}

## relaterade artiklar

- [Hitta eller sök data](/cells/sv/java/find-or-search-data/)
