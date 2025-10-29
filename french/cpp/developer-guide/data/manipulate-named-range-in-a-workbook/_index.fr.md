---
title: Manipuler une plage nommée dans un classeur
type: docs
weight: 90
url: /fr/cpp/manipulate-named-range-in-a-workbook/
---

## **Scénarios d'utilisation possibles**
Aspose.Cells prend en charge la manipulation des plages nommées existantes. Toutes les plages nommées existantes peuvent être consultées à partir de la collection [Workbook.GetWorksheets().GetNames()](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/getnames/). Une fois que vous accédez à la plage nommée, vous pouvez modifier ses différentes méthodes telles que [GetFullText](https://reference.aspose.com/cells/cpp/aspose.cells/name/getfulltext/) et [GetRefersTo](https://reference.aspose.com/cells/cpp/aspose.cells/name/getrefersto/).
## **Manipuler une plage nommée dans un classeur**
Le code d'exemple suivant lit la première plage nommée dans le [fichier Excel source](23167008.xlsx) et affiche ses propriétés [FullText](https://reference.aspose.com/cells/cpp/aspose.cells/name/getfulltext/) et [RefersTo](https://reference.aspose.com/cells/cpp/aspose.cells/name/getrefersto/) sur la console. Ensuite, il modifie la propriété `RefersTo` et enregistre le [fichier Excel de sortie](23167009.xlsx).
## **Code d'exemple**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-ManipulateNamedRangeInWorkbook-new.cpp" >}}
## **Sortie console**
La sortie de la console suivante affiche les valeurs des membres [FullText](https://reference.aspose.com/cells/cpp/aspose.cells/name/getfulltext/) et [RefersTo](https://reference.aspose.com/cells/cpp/aspose.cells/name/getrefersto/) de la *plage nommée* existante dans le code ci-dessus.

{{< highlight java >}}

 Full Text: TestRange

Refers To: =Sheet1!$D$3:$G$6

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
