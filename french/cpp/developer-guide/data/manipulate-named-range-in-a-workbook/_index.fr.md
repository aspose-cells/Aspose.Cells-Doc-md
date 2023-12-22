---
title: Manipuler une plage nommée dans un classeur
type: docs
weight: 90
url: /fr/cpp/manipulate-named-range-in-a-workbook/
---
##  **Scénarios d'utilisation possibles**
 Aspose.Cells prend en charge la manipulation des plages nommées existantes. Toutes les plages nommées existantes sont accessibles depuis[Workbook.GetWorksheets().GetNames()](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/getnames/) collection. Une fois que vous accédez à la plage nommée, vous pouvez modifier ses différentes méthodes, par exemple[ObtenirFullText](https://reference.aspose.com/cells/cpp/aspose.cells/name/getfulltext/)et[ObtenirRefersTo](https://reference.aspose.com/cells/cpp/aspose.cells/name/getrefersto/).
##  **Manipuler une plage nommée dans un classeur**
 L'exemple de code suivant lit la première plage nommée à l'intérieur du[fichier Excel source](23167008.xlsx) et imprime son[Texte intégral](https://reference.aspose.com/cells/cpp/aspose.cells/name/getfulltext/)et[Fait référence à](https://reference.aspose.com/cells/cpp/aspose.cells/name/getrefersto/) propriétés sur la console. Après cela, il modifie la propriété `RefersTo` et enregistre le[sortie du fichier Excel](23167009.xlsx).
##  **Exemple de code**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-ManipulateNamedRangeInWorkbook-new.cpp" >}}
##  **Sortie console**
 La sortie de console suivante imprime les valeurs de[Texte intégral](https://reference.aspose.com/cells/cpp/aspose.cells/name/getfulltext/)et[Fait référence à](https://reference.aspose.com/cells/cpp/aspose.cells/name/getrefersto/) membres de l'existant*Plage nommée*dans le code ci-dessus.

{{< highlight "java" >}}

 Full Text: TestRange

Refers To: =Sheet1!$D$3:$G$6

{{< /highlight >}}
