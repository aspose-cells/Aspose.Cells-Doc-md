---
title: Insérer une image liée à partir d une adresse Web via Golang en C++
linktitle: Insérer une image liée à partir de l adresse Web
type: docs
weight: 450
url: /fr/go-cpp/insert-a-linked-picture-from-web-address/
description: Apprenez comment insérer une image liée depuis une adresse Web dans une feuille de calcul en utilisant Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Parfois, vous devez insérer une image à partir du web (http://) dans une feuille de calcul. Pour ce faire, spécifiez l'URL de l'image et l'image sera téléchargée à chaque ouverture de la feuille de calcul dans Microsoft Excel. L'image n'est pas physiquement intégrée dans le document Excel, mais pointe vers une ressource web.

{{% /alert %}}

## **Utilisation de Microsoft Excel**

Dans Microsoft Excel (par exemple 2007) :

1. Cliquez sur le menu **Insérer** et sélectionnez **Image**.
1. Spécifiez l'adresse web de l'image dans la boîte de dialogue Insérer une image.

## **Utilisation de Aspose.Cells for C++**

Aspose.Cells for C++ supporte l'ajout d'une image liée en utilisant la méthode [**ShapeCollection::AddLinkedPicture(int upperLeftRow, int upperLeftColumn, int heightPixels, int widthPixels, System::String sourceFullName)**](https://reference.aspose.com/cells/go-cpp/shapecollection/addlinkedpicture/). La méthode retourne un objet [**Picture**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/picture/).

L'exemple suivant montre comment ajouter une image liée depuis une adresse web dans une feuille de calcul.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-InsertALinkedPictureFromWebAddress.go" >}}
