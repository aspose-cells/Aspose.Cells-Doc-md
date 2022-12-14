---
title: Définir le commentaire d'un objet de table ou de liste
type: docs
weight: 60
url: /fr/python-java/set-the-comment-of-table-or-list-object/
---
## **Définir le commentaire de la table ou de l'objet de liste dans la feuille de calcul**
Aspose.Cells pour Python via Java prend en charge l'ajout du commentaire de l'objet de liste. Pour cela, le API fournit le[ListObject.Comment](https://reference.aspose.com/cells/python/asposecells.api/listobject#Comment)propriété. Le commentaire ajouté par le[ListObject.Comment](https://reference.aspose.com/cells/python/asposecells.api/listobject#Comment)propriété sera visible à l'intérieur du*xl/tables/tableName.xml* dossier.

La capture d'écran suivante montre le commentaire créé par l'exemple de code dans le rectangle rouge.

![tâche : image_autre_texte](setting-list-object-comment.png)

L'exemple de code suivant charge le[fichier excel source](source.xlsx), définit le commentaire du premier objet de table ou de liste dans la feuille de calcul

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Tables-SetTheCommentOfTableOrListObject.py" >}}
