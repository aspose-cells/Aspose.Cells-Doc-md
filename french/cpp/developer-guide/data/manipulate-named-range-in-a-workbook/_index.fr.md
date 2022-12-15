---
title: Manipuler une plage nommée dans un classeur
type: docs
weight: 90
url: /fr/cpp/manipulate-named-range-in-a-workbook/
---
## **Scénarios d'utilisation possibles**
 Aspose.Cells prend en charge la manipulation des plages nommées existantes. Toutes les plages nommées existantes sont accessibles depuis[IWorkbook.GetIWorksheets().GetINames()](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection#aa9e7bc07917a152a2c0de161cca133fa) le recueil. Une fois que vous accédez à la plage nommée, vous pouvez modifier ses différentes méthodes, par exemple[GetFullText](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_name#a5b450ef193365dec035c58280fbe9563)et[GetRefersTo](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_name#afdb10a12d8d395ae81de231f017eba36).
## **Manipuler une plage nommée dans un classeur**
 L'exemple de code suivant lit la première plage nommée à l'intérieur du[fichier excel source](23167008.xlsx) et imprime son[Texte intégral](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_name#a5b450ef193365dec035c58280fbe9563)et[Fait référence à](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_name#afdb10a12d8d395ae81de231f017eba36) propriétés sur la console. Après cela, il modifie la propriété `RefersTo` et enregistre le[fichier excel de sortie](23167009.xlsx).
## **Exemple de code**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-ManipulateNamedRangeInWorkbook.cpp" >}}
## **Sortie console**
 La sortie de console suivante imprime les valeurs de[Texte intégral](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_name#a5b450ef193365dec035c58280fbe9563)et[Fait référence à](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_name#afdb10a12d8d395ae81de231f017eba36) membres de l'existant*Plage nommée*dans le code ci-dessus.

{{< highlight "java" >}}

 Full Text: TestRange

Refers To: =Sheet1!$D$3:$G$6

{{< /highlight >}}
