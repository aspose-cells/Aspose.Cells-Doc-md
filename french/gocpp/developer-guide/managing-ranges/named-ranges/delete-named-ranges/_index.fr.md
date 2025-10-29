---
title: Supprimer les plages nommées avec Golang via C++
linktitle: Supprimer les plages nommées
type: docs
weight: 90
url: /fr/go-cpp/delete-named-ranges/
description: Apprenez comment supprimer les noms définis ou plages nommées des fichiers Excel ou OpenOffice en utilisant Aspose.Cells for C++.
---

## **Introduction**
S'il y a trop de noms définis ou de plages nommées dans les fichiers Excel, nous devons en effacer certains car ils ne sont plus référencés.

## **Supprimer une plage nommée dans MS Excel**

Pour supprimer une plage nommée dans Excel, suivez les étapes suivantes :
1. Ouvrez Microsoft Excel et ouvrez le classeur contenant la plage nommée.
2. Allez à l'onglet "Formules" dans le ruban Excel.
3. Cliquez sur le bouton "Gestionnaire de noms" dans le groupe "Noms définis". Cela ouvrira la boîte de dialogue Gestionnaire de noms.
4. Dans la boîte de dialogue Gestionnaire de noms, sélectionnez la plage nommée que vous souhaitez supprimer.
5. Cliquez sur le bouton "Supprimer". Confirmez la suppression lorsqu'on vous le demande.
6. Cliquez sur le bouton "Fermer" pour fermer la boîte de dialogue Gestionnaire de noms.
7. Enregistrez le classeur pour conserver les modifications.

## **Supprimer la plage nommée en utilisant Aspose.Cells for C++**
Avec Aspose.Cells for C++, vous pouvez supprimer les plages nommées ou les noms définis par [texte](https://reference.aspose.com/cells/go-cpp/namecollection/remove_stringarray/) ou [index](https://reference.aspose.com/cells/cpp/aspose.cells/namecollection/removeat/) dans la liste.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DeleteNamedRanges.go" >}}
Remarque : si le nom défini est référencé par des formules, il ne peut pas être supprimé. Nous pouvons uniquement supprimer la formule du nom défini.

## **Supprime certaines plages nommées**
Lorsque nous supprimons un nom défini, nous devons vérifier s'il est référencé par toutes les formules du fichier.
Pour améliorer la performance de la suppression des plages nommées, nous pouvons en supprimer plusieurs en même temps.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DeleteNamedRanges-1.go" >}}
## **Supprimer les noms définis en double**
Certains fichiers Excel se corrompent car certains noms définis sont en double. Nous pouvons donc supprimer ces doublons pour réparer le fichier.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DeleteNamedRanges-2.go" >}}
