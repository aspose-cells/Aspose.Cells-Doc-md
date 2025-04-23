---
title: Insérer une image liée à partir de l adresse Web
type: docs
weight: 450
url: /fr/net/insert-a-linked-picture-from-web-address/
---

{{% alert color="primary" %}}

Parfois, vous devez insérer une image à partir du web (http://) dans une feuille de calcul. Pour ce faire, spécifiez l'URL de l'image et l'image sera téléchargée à chaque ouverture de la feuille de calcul dans Microsoft Excel. L'image n'est pas physiquement intégrée dans le document Excel, mais pointe vers une ressource web.

{{% /alert %}}

## **Utilisation de Microsoft Excel**

Dans Microsoft Excel (par exemple 2007) :

1. Cliquez sur le menu **Insérer** et sélectionnez **Image**.
1. Spécifiez l'adresse web de l'image dans la boîte de dialogue Insérer une image.

## **Utilisation de Aspose.Cells for .NET**

Aspose.Cells for .NET prend en charge l'ajout d'une image liée en utilisant le [**ShapeCollection.AddLinkedPicture(int upperLeftRow, int upperLeftColumn, int heightPixels, int widthPixels, string sourceFullName)**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addlinkedpicture). La méthode renvoie un objet [**Picture**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture).

L'exemple suivant montre comment ajouter une image liée à partir de l'adresse Web à une feuille de calcul.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-InsertLinkedPicture-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
