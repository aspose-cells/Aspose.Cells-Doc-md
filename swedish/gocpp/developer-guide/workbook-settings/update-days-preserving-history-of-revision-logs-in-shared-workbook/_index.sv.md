---
title: Uppdatera dagar och behåll revisionsloggen i ett delat arbetsbok med Golang via C++
linktitle: Uppdatera antal sparade historikrevisioner på delad arbetsbok
type: docs
weight: 80
url: /sv/go-cpp/update-days-preserving-history-of-revision-logs-in-shared-workbook/
description: Lär dig hur du uppdaterar antalet dagar för att bevara historien i ett delat arbetsbok med Aspose.Cells med Golang via C++
---

## **Möjliga användningsscenario**

När du delar en arbetsbok får du alternativet att ***Spara ändringshistorik i N dagar*** som visas i följande skärmbild. Du kan uppdatera antalet dagar att spara historik med hjälp av Aspose.Cells med egenskapen [**WorksheetCollection.GetDaysPreservingHistory()**](https://reference.aspose.com/cells/go-cpp/revisionlogcollection/getdayspreservinghistory/).

![todo:image_alt_text](update-days-preserving-history-of-revision-logs-in-shared-workbook_1.png)

## **Uppdatera antal sparade historikrevisioner på delad arbetsbok**

Följande exempelkod skapar en tom arbetsbok, delar den sedan och uppdaterar revisionsloggar dagar med bibehållen historia till 7 dagar, vilket normalt är 30 dagar. Se [output Excel-filet](60489773.xlsx) som genereras av koden för en referens.

## **Exempelkod**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-UpdateDaysPreservingHistoryOfRevisionLogsInSharedWorkbook.go" >}}
