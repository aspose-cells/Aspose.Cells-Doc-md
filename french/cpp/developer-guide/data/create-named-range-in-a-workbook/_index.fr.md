---
title: Créer une plage nommée dans un classeur
type: docs
weight: 60
url: /fr/cpp/create-named-range-in-a-workbook/
---
## **Scénarios d'utilisation possibles**
 Aspose.Cells prend en charge la création d'une plage nommée. Il existe différentes manières de créer une plage nommée. L'un des moyens les plus simples consiste à créer d'abord[IRange](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_range) objet, puis définissez son nom à l'aide[IRange.SetName()](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_range#a78480b6b6db0f24cffc8acc2b06552eb) méthode. Vous pouvez voir toutes les plages nommées dans votre fichier Excel via Microsoft Excel*Gestionnaire de noms*interface.
## **Créer une plage nommée dans un classeur**
 L'exemple de code suivant explique comment créer un*Plage nommée* via Aspose.Cells. Une fois, le*Plage nommée* est créé, il est visible à l'intérieur du[IWorkbook.GetIWorksheets().GetINames()](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection#aa9e7bc07917a152a2c0de161cca133fa) le recueil. Veuillez consulter le[fichier excel de sortie](23167006.xlsx) généré par le code pour une référence.
## **Exemple de code**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-CreateNamedRangeInWorkbook.cpp" >}}
## **Sortie console**
 La sortie de console suivante imprime les valeurs de[GetFullText](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_name#a5b450ef193365dec035c58280fbe9563) et `GetRefersTo` méthodes du créé*Plage nommée*dans le code ci-dessus.

{{< highlight "java" >}}

 Full Text: MyNamedRange

Refers To: =Sheet1!$A$5:$C$10

{{< /highlight >}}
