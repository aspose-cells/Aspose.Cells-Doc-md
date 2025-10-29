---
title: Créer une plage nommée dans un classeur
type: docs
weight: 60
url: /fr/cpp/create-named-range-in-a-workbook/
---

## **Scénarios d'utilisation possibles**
Aspose.Cells prend en charge la création d'une plage nommée. Il existe différentes façons de créer une plage nommée. L'une des façons les plus simples est de d'abord créer un [objet Range](https://reference.aspose.com/cells/cpp/aspose.cells/range) puis définir son nom à l'aide de la méthode [Range.SetName()](https://reference.aspose.com/cells/cpp/aspose.cells/range/setname). Vous pouvez voir toutes les plages nommées dans votre fichier Excel via l'interface *Gestionnaire de noms* de Microsoft Excel.
## **Créer une plage nommée dans un classeur**
Le code d'exemple suivant explique comment créer une *plage nommée* via Aspose.Cells. Une fois la *plage nommée* créée, elle est visible dans la collection [Workbook.GetWorksheets().GetNames()](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/getnames). Veuillez consulter le [fichier Excel de sortie](23167006.xlsx) généré par le code pour référence.
## **Code d'exemple**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-CreateNamedRangeInWorkbook-new.cpp" >}}
## **Sortie console**
La sortie de la console suivante affiche les valeurs des méthodes [GetFullText](https://reference.aspose.com/cells/cpp/aspose.cells/name/getfulltext/) et [GetRefersTo](https://reference.aspose.com/cells/cpp/aspose.cells/name/getrefersto/) de la *plage nommée* créée dans le code ci-dessus.

{{< highlight java >}}

 Full Text: MyNamedRange

Refers To: =Sheet1!$A$5:$C$10

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
