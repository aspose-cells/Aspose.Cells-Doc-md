---
title: Créer une plage nommée dans un classeur
type: docs
weight: 60
url: /fr/cpp/create-named-range-in-a-workbook/
---
##  **Scénarios d'utilisation possibles**
 Aspose.Cells prend en charge la création d'une plage nommée. Il existe différentes manières de créer une plage nommée. L'un des moyens les plus simples consiste à créer d'abord[Gamme](https://reference.aspose.com/cells/cpp/aspose.cells/range) objet, puis définissez son nom en utilisant[Range.SetName()](https://reference.aspose.com/cells/cpp/aspose.cells/range/setname) méthode. Vous pouvez voir toutes les plages nommées dans votre fichier Excel via Microsoft Excel*Gestionnaire de noms*interface.
##  **Créer une plage nommée dans un classeur**
 L'exemple de code suivant explique comment créer un*Plage nommée* via Aspose.Cells. Une fois, le*Plage nommée* est créé, il est visible à l'intérieur du[Workbook.GetWorksheets().GetNames()](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/getnames) collection. Veuillez consulter le[sortie du fichier Excel](23167006.xlsx) généré par le code pour une référence.
##  **Exemple de code**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-CreateNamedRangeInWorkbook-new.cpp" >}}
##  **Sortie console**
 La sortie de console suivante imprime les valeurs de[ObtenirFullText](https://reference.aspose.com/cells/cpp/aspose.cells/name/getfulltext/) et[ObtenirRefersTo](https://reference.aspose.com/cells/cpp/aspose.cells/name/getrefersto/) méthodes de création*Plage nommée*dans le code ci-dessus.

{{< highlight "java" >}}

 Full Text: MyNamedRange

Refers To: =Sheet1!$A$5:$C$10

{{< /highlight >}}
