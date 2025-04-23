---
title: Spécifiez les champs de formule lors de l importation de données dans la feuille de calcul
type: docs
weight: 220
url: /fr/java/specify-formula-fields-while-importing-data-to-worksheet/
---

## **Scénarios d'utilisation possibles**

Vous pouvez spécifier des champs de formule lorsque vous importez des données dans votre feuille de calcul en utilisant la méthode [**ImportTableOptions.setFormulas()**](https://reference.aspose.com/cells/java/com.aspose.cells/importtableoptions#IsFormulas). Cette méthode prend le tableau booléen où la valeur **true** signifie que le champ est un champ de formule. Par exemple, si le troisième champ est un champ de formule, alors la troisième valeur dans le tableau sera **true**.

## **Spécifier les champs de formule lors de l'importation de données dans la feuille de calcul**

Veuillez consulter le code d'exemple suivant qui explique comment spécifier le champ de formule lors de l'importation de données dans une feuille de calcul. Veuillez consulter le [fichier Excel de sortie](61767850.xlsx) généré par le code et la capture d'écran montrant l'effet du code sur le fichier Excel de sortie.

![todo:image_alt_text](specify-formula-fields-while-importing-data-to-worksheet_1.png)

## **Code d'exemple**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Data-SpecifyFormulaFieldsWhileImportingDataToWorksheet.java" >}}
{{< app/cells/assistant language="java" >}}
