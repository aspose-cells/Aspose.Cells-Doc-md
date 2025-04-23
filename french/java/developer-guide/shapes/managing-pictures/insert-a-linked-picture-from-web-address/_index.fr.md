---
title: Insérer une image liée à partir de l adresse Web
type: docs
weight: 50
url: /fr/java/insert-a-linked-picture-from-web-address/
---

{{% alert color="primary" %}}

Parfois, vous devez insérer une image à partir du web (http://) dans une feuille de calcul. Pour ce faire, spécifiez l'URL de l'image et l'image sera téléchargée à chaque ouverture de la feuille de calcul dans Microsoft Excel. L'image n'est pas physiquement intégrée dans le document Excel, mais pointe vers une ressource web.

{{% /alert %}}

## **Insertion d'une image liée à partir de l'adresse web**

### **Utilisation de Microsoft Excel**

Dans Microsoft Excel (par exemple 2007) :

1. Cliquez sur le menu **Insérer** et sélectionnez **Image**.

![todo:image_alt_text](insert-a-linked-picture-from-web-address_1.png)

1. Spécifiez l'adresse web de l'image dans la boîte de dialogue Insérer une image. 

![todo:image_alt_text](insert-a-linked-picture-from-web-address_2.png)

L'image est insérée.

![todo:image_alt_text](insert-a-linked-picture-from-web-address_3.png)

### **Utilisation de Aspose.Cells for Java**

Aspose.Cells for Java prend en charge l'ajout d'une image liée à l'aide de la méthode [**ShapeCollection.addLinkedPicture(int upperLeftRow, int upperLeftColumn, int height, int width, java.lang.String sourceFullName)**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addLinkedPicture-int-int-int-int-java.lang.String-).

La méthode renvoie un objet [**Picture**](https://reference.aspose.com/cells/java/com.aspose.cells/Picture).

L'exemple suivant montre comment ajouter une image liée à partir de l'adresse Web à une feuille de calcul.

Après l'exécution du code, le fichier Excel généré contient une image liée sur la première feuille de calcul.

**Le fichier de sortie** 

![todo:image_alt_text](insert-a-linked-picture-from-web-address_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-InsertLinkedPicturefromWebAddress-InsertLinkedPicturefromWebAddress.java" >}}
{{< app/cells/assistant language="java" >}}
