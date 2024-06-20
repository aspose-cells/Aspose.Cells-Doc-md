---
title: Sök och ersätt data i ett intervall
type: docs
weight: 60
url: /sv/java/search-and-replace-data-in-a-range/
description: Denna artikel visar hur du söker och ersätter data i ett intervall i Excel med Javakod.
keywords: java sök och ersätt data i excel, java sök data i excel, java sök och ersätt data i ett intervall, java sök data i ett intervall, java söker data i ett intervall, java söker data i intervall, java söker data i excel, java sök data i ett intervall, sök och ersätt data i excel med java, sök och ersätt data i ett intervall med java, sök och ersätt data i intervall med java
---

{{% alert color="primary" %}}

Ibland behöver du söka efter och ersätta specifika data i ett intervall och ignorera eventuella cellvärden utanför det önskade intervallet. Aspose.Cells låter dig begränsa en sökning till ett specifikt intervall. Denna artikel förklarar hur.

{{% /alert %}}

Aspose.Cells tillhandahåller [**FindOptions.setRange()**](https://reference.aspose.com/cells/java/com.aspose.cells/findoptions#setRange(com.aspose.cells.CellArea)) metoden för att ange ett intervall vid sökning efter data.

Anta att du vill söka efter strängen **"sök"** och ersätta den med **"ersätt"** i intervallet **E3:H6**. I skärmdumpen nedan kan strängen "sök" ses i flera celler men vi vill endast ersätta den i ett givet intervall, här markerat i gult.

**Ingångsfil**

![todo:image_alt_text](search-and-replace-data-in-a-range_1.png)

Efter att koden har körts ser utdatafilen ut som nedan. Alla "sök" strängar inom intervallet har ersatts med "ersätt".

**Utgångsfil**

![todo:image_alt_text](search-and-replace-data-in-a-range_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SearchReplaceDataInRange-SearchReplaceDataInRange.java" >}}

## Relaterade artiklar

- [Hitta eller Sök Data](/cells/sv/java/find-or-search-data/)
