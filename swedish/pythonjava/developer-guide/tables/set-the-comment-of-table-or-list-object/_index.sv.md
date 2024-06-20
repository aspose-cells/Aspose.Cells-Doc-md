---
title: Ange kommentaren för tabellen eller listobjektet
type: docs
weight: 60
url: /sv/python-java/set-the-comment-of-table-or-list-object/
---

## **Ange kommentaren för tabell eller listobjekt inne i kalkylbladet**
Aspose.Cells for Python via Java stödjer att lägga till Listobjektskommentaren. För detta tillhandahåller API:et egenskapen [ListObject.Comment](https://reference.aspose.com/cells/python/asposecells.api/listobject#Comment). Kommentaren som läggs till av egenskapen [ListObject.Comment](https://reference.aspose.com/cells/python/asposecells.api/listobject#Comment) kommer att vara synlig inuti filen *xl/tables/tableName.xml*.

Följande skärmbild visar kommentaren skapad av provkoden i den röda rektangeln.

![todo:image_alt_text](setting-list-object-comment.png)

Följande exempelkod laddar [käll Excel-filen](source.xlsx), ställer in kommentaren för den första tabellen eller listobjektet i kalkylbladet. 

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Tables-SetTheCommentOfTableOrListObject.py" >}}
