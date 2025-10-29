---
title: Spécifier les champs de formule lors de l importation de données dans une feuille de calcul avec Golang via C++
linktitle: Spécifiez les champs de formule lors de l importation de données dans la feuille de calcul
type: docs
weight: 300
url: /fr/go-cpp/specify-formula-fields-while-importing-data-to-worksheet/
description: Apprenez comment spécifier des champs de formule lors de l importation de données dans une feuille via l API Aspose.Cells for C++.
keywords: Spécifiez les champs de formule lors de l importation de données dans la feuille de calcul, Définissez les champs de formule lors de l ajout de données dans la feuille de calcul
---

## **Scénarios d'utilisation possibles**

Vous pouvez spécifier les champs de formule lors de l'importation de données dans votre feuille de calcul en utilisant le [**ImportTableOptions.GetIsFormulas()**](https://reference.aspose.com/cells/go-cpp/importtableoptions/getisformulas/). Cette propriété prend le tableau booléen où la valeur **true** signifie que le champ est un champ de formule. Par exemple, si le troisième champ est un champ de formule, alors la troisième valeur dans le tableau sera **true**.

## **Spécifier les champs de formule lors de l'importation de données dans la feuille de calcul**

Veuillez consulter le code d'exemple suivant qui explique comment spécifier le champ de formule lors de l'importation de données dans une feuille de calcul. Veuillez consulter le fichier Excel de sortie généré par le code et la capture d'écran montrant l'effet du code sur le fichier Excel de sortie.

![todo:image_alt_text](specify-formula-fields-while-importing-data-to-worksheet_1.png)

## **Code d'exemple**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SpecifyFormulaFieldsWhileImportingDataToWorksheet.go" >}}
