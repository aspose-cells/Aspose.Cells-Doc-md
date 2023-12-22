---
title: Angeben einer Sortierwarnung beim Sortieren von Daten
type: docs
weight: 140
url: /de/net/specifying-sort-warning-while-sorting-data/
description: Erfahren Sie, wie Sie beim Sortieren von Daten mithilfe von Aspose.Cells for .NET API eine Sortierwarnung angeben.
keywords: Add sort warning when sorting data, set sort warning while sorting data, select sort warning when sorting data.
---
##  **Mögliche Nutzungsszenarien**

Bitte berücksichtigen Sie diese Textdaten, z. B. {11, 111, 22}. Diese Textdaten werden sortiert, weil in Bezug auf den Text 111 vor 22 steht. Wenn Sie diese Daten jedoch nicht als Text, sondern als Zahlen sortieren möchten, werden sie zu {11, 22, 111}, da numerisch 111 nach 22 kommt .Aspose.Cells bietet[**DataSorter.SortAsNumber**](https://reference.aspose.com/cells/net/aspose.cells/datasorter/properties/sortasnumber)Eigentum, um dieses Problem zu lösen. Bitte legen Sie diese Eigenschaft fest**WAHR**und Ihre Textdaten werden als numerische Daten sortiert. Der folgende Screenshot zeigt die Sortierwarnung von Microsoft Excel, wenn Textdaten, die wie numerische Daten aussehen, sortiert werden.

![todo:image_alt_text](specifying-sort-warning-while-sorting-data_1.png)

##  **Beispielcode**

 Der folgende Beispielcode veranschaulicht die Verwendung von[**DataSorter.SortAsNumber**](https://reference.aspose.com/cells/net/aspose.cells/datasorter/properties/sortasnumber) Eigentum wie zuvor erläutert. Bitte überprüfen Sie es[Beispiel-Excel-Datei](43352075.xlsx) Und[Excel-Datei ausgeben](43352076.xlsx) für weitere Hilfe.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-SpecifyingSortWarningWhileSortingData.cs" >}}
