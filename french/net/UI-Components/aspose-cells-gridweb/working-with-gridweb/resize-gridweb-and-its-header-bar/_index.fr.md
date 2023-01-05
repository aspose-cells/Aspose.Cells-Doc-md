---
title: Redimensionner GridWeb et sa barre d'en-tête
type: docs
weight: 30
url: /fr/net/resize-gridweb-and-its-header-bar/
---
{{% alert color="primary" %}} 

[Ajouter GridWeb au formulaire Web](/cells/fr/net/add-gridweb-to-web-form/), ont discuté du redimensionnement du contrôle Aspose.Cells.GridWeb à l'aide de WYSIWYG. Cet article explique comment faire la même chose mais lors de l'exécution en utilisant le Aspose.Cells.GridWeb API. Il explique également comment redimensionner les barres d'en-tête du contrôle Aspose.Cells.GridWeb pour faciliter la lecture de leurs données.

{{% /alert %}} 
## **Modification de la largeur et de la hauteur de Aspose.Cells.GridWeb**
Changer la largeur et la hauteur du contrôle Aspose.Cells.GridWeb est une fonctionnalité simple mais importante. Le contrôle Aspose.Cells.GridWeb est représenté par la classe GridWeb dans le API. Pour redimensionner la largeur et la hauteur du contrôle GridWeb, utilisez simplement ses propriétés width et height.

{{% alert color="primary" %}} 

La largeur et la hauteur du champ peuvent être définies en pixels ou en points.

{{% /alert %}} 

La sortie de l'extrait de code qui suit est illustrée ci-dessous.

**Modification de la largeur et de la hauteur du contrôle GridWeb** 

![tâche : image_autre_texte](resize-gridweb-and-its-header-bar_1.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ResizeGridWeb.aspx-ResizeGridWeb.cs" >}}
### **Modification de la largeur et de la hauteur de la barre d'en-tête**
Le contrôle Aspose.Cells.GridWeb contient deux barres d'en-tête comme suit :

- Barre d'en-tête supérieure, cette barre d'en-tête représente les colonnes comme A , B , C , D etc.
- Barre d'en-tête gauche, cette barre d'en-tête représente les lignes sous la forme 1 , 2 , 3 , 4 etc.

Ces deux barres d'en-tête sont illustrées ci-dessous.

**Barres d'en-tête** 

![tâche : image_autre_texte](resize-gridweb-and-its-header-bar_2.png)

Modifiez la hauteur de la barre d'en-tête supérieure et la largeur de la barre d'en-tête gauche à l'aide des propriétés HeaderBarHeight et HeaderBarWidth du contrôle GridWeb respectivement. La figure ci-dessous montre la sortie de l'exemple de code qui suit.

**Modification de la largeur et de la hauteur de la barre d'en-tête** 

![tâche : image_autre_texte](resize-gridweb-and-its-header-bar_3.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ResizeHeaderBar.aspx-ResizeHeaderBar.cs" >}}
