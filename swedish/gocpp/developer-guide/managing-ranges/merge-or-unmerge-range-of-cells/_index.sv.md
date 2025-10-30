---
title: Sammanfoga eller avsammanfoga cellområden med Golang via C++
linktitle: Slå samman eller dela upp cellintervall
type: docs
weight: 190
url: /sv/go-cpp/merge-or-unmerge-range-of-cells/
description: Sammanfoga och avsammanfoga celler i ett område i Excel med Golang via C++ kod.
keywords: c++ foga samman och avfoga celler i ett område, c++ foga samman och avfoga celler i ett område, foga samman och avfoga celler i ett område med c++, foga samman och avfoga celler i ett område med c++, foga samman och avfoga celler i Excel med c++, f++ foga samman och avfoga celler i Excel, c++ foga samman celler i Excel, c++ avfoga celler i Excel, foga samman celler i område med c++
---

{{% alert color="primary" %}}

Du kan använda Aspose.Cells för att slå samman eller dela upp ett cellintervall. Aspose.Cells tillhandahåller [**Range.Merge()**](https://reference.aspose.com/cells/go-cpp/range/merge/) och [**Range.UnMerge()**](https://reference.aspose.com/cells/cpp/aspose.cells/range/unmerge/) metoder för detta ändamål. Denna artikel förklarar hur man slår samman ett cellintervall till en enda cell.

{{% /alert %}}

## **Exempel**

Följande exempel skapar först ett område - A1:D4 - och fusionerar sedan cellerna i området till en enda cell med hjälp av [**Range.Merge()**](https://reference.aspose.com/cells/go-cpp/range/merge/)-metoden. På liknande sätt kan du dela upp celler genom att skapa ett område och använda [**Range.UnMerge()**](https://reference.aspose.com/cells/cpp/aspose.cells/range/unmerge/)-metoden.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-MergeOrUnmergeRangeOfCells.go" >}}
