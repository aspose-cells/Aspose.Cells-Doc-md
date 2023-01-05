---
title: Insérer une image liée à partir d'une adresse Web
type: docs
weight: 50
url: /fr/java/insert-a-linked-picture-from-web-address/
---
{{% alert color="primary" %}}

Parfois, vous devez insérer une image provenant du Web (http://) dans une feuille de calcul. Pour ce faire, indiquez l'URL de l'image et l'image sera téléchargée à chaque ouverture de la feuille de calcul dans Microsoft Excel. L'image n'est pas physiquement intégrée dans le document Excel, mais pointe vers une ressource Web.

{{% /alert %}}

## **Insertion d'une image liée à partir d'une adresse Web**

### **Utilisation d'Excel Microsoft**

Dans Microsoft Excel (par exemple 2007) :

1.  Clique le**Insérer** menu et sélectionnez**Photo**.

![tâche : image_autre_texte](insert-a-linked-picture-from-web-address_1.png)

1.  Spécifiez l'adresse Web de l'image dans la boîte de dialogue Insérer une image.

![tâche : image_autre_texte](insert-a-linked-picture-from-web-address_2.png)

L'image est insérée.

![tâche : image_autre_texte](insert-a-linked-picture-from-web-address_3.png)

### **En utilisant Aspose.Cells for Java**

 Aspose.Cells for Java prend en charge l'ajout d'une image liée à l'aide de la méthode[**ShapeCollection.addLinkedPicture(int upperLeftRow, int upperLeftColumn, int hauteur, int largeur, java.lang.String sourceFullName)**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addLinkedPicture(int,%20int,%20int,%20int,%20java.lang.String)).

 La méthode retourne un[**Photo**](https://reference.aspose.com/cells/java/com.aspose.cells/Picture)objet.

L'exemple suivant montre comment ajouter une image liée à partir d'une adresse Web à une feuille de calcul.

Après avoir exécuté le code, le fichier Excel généré contient une image liée sur la première feuille de calcul.

**Le fichier de sortie** 

![tâche : image_autre_texte](insert-a-linked-picture-from-web-address_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-InsertLinkedPicturefromWebAddress-InsertLinkedPicturefromWebAddress.java" >}}
