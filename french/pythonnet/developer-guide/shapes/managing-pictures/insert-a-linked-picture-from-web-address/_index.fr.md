---
title: Insérer une image liée à partir de l adresse Web
type: docs
weight: 450
url: /fr/python-net/insert-a-linked-picture-from-web-address/
---

{{% alert color="primary" %}}

Parfois, vous devez insérer une image à partir du web (http://) dans une feuille de calcul. Pour ce faire, spécifiez l'URL de l'image et l'image sera téléchargée à chaque ouverture de la feuille de calcul dans Microsoft Excel. L'image n'est pas physiquement intégrée dans le document Excel, mais pointe vers une ressource web.

{{% /alert %}}

## **Utilisation de Microsoft Excel**

Dans Microsoft Excel (par exemple 2007) :

1. Cliquez sur le menu **Insérer** et sélectionnez **Image**.
1. Spécifiez l'adresse web de l'image dans la boîte de dialogue Insérer une image.

## **Utiliser Aspose.Cells pour Python via .NET**

Aspose.Cells pour Python via .NET permet d'ajouter une image liée à l’aide de [**ShapeCollection.add_linked_picture(int upper_left_row, int upper_left_column, int height_pixels, int width_pixels, str source_full_name)**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_linked_picture). La méthode retourne un objet [**Picture**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/picture).

L'exemple suivant montre comment ajouter une image liée à partir de l'adresse Web à une feuille de calcul.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-Pictures-InsertLinkedPicture-1.py" >}}
