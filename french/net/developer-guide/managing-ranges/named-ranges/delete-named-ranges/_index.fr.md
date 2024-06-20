---
title: Supprimer les plages nommées
type: docs
weight: 90
url: /fr/net/Delete-named-ranges/
description: Vous pouvez apprendre comment supprimer les noms définis ou les plages nommées des fichiers Excel ou OpenOffice avec Aspose.Cells pour .Net.
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


## **Supprime la plage nommée en utilisant Aspose.Cells pour .Net**
Avec Aspose.Cells pour .Net, vous pouvez supprimer des plages nommées ou des noms définis par [texte](https://reference.aspose.com/cells/net/aspose.cells/namecollection/remove/#remove) ou [indice](https://reference.aspose.com/cells/net/aspose.cells/namecollection/removeat/#removeat) dans la liste.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Delete-named-range.cs" >}}

Remarque : si le nom défini est référencé par des formules, il ne peut pas être supprimé. Nous ne pouvons supprimer que la formule du nom défini.

## **Supprime certaines plages nommées**
Lorsque nous supprimons un nom défini, nous devons vérifier s'il est référencé par toutes les formules du fichier.
Afin d'améliorer les performances de suppression des plages nommées, nous pouvons en supprimer certaines ensemble.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Delete-named-ranges.cs" >}}

## **Supprimer les noms définis en double**
Certains fichiers Excel sont corrompus car certains noms définis sont en double. Nous pouvons donc supprimer ces noms en double pour réparer le fichier.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Delete-duplicate-defined-names.cs" >}}



