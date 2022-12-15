---
title: Appliquer la mise en forme conditionnelle dans les feuilles de calcul
type: docs
weight: 40
url: /fr/java/apply-conditional-formatting-in-worksheets/
---
{{% alert color="primary" %}}

Cet article est conçu pour fournir une compréhension détaillée de la façon d'ajouter une mise en forme conditionnelle à une plage de cellules dans une feuille de calcul.

La mise en forme conditionnelle est une fonctionnalité avancée d'Excel Microsoft qui vous permet d'appliquer des formats à une plage de cellules et de modifier cette mise en forme en fonction de la valeur de la cellule ou de la valeur d'une formule. Par exemple, l'arrière-plan d'une cellule peut être rouge pour mettre en évidence une valeur négative, ou la couleur du texte peut être verte pour une valeur positive. Lorsque la valeur de la cellule répond à la condition de format, le format est appliqué. Si la valeur de la cellule ne répond pas à la condition de format, la mise en forme par défaut de la cellule est utilisée.

Il est possible d'appliquer une mise en forme conditionnelle avec Microsoft Office Automation mais cela a ses inconvénients. Il y a plusieurs raisons et problèmes impliqués : par exemple, la sécurité, la stabilité, l'évolutivité et la vitesse. La raison principale pour trouver une autre solution est que Microsoft eux-mêmes déconseillent fortement la bureautique pour les solutions logicielles.

Cet article montre comment créer une application console, ajouter une mise en forme conditionnelle sur des cellules avec quelques lignes de code les plus simples en utilisant le Aspose.Cells API.

{{% /alert %}}

## **Travailler avec la mise en forme conditionnelle**

Cet article exécute les tâches suivantes :

1. [Utilisation de Aspose.Cells pour appliquer une mise en forme conditionnelle basée sur la valeur de la cellule](/cells/fr/java/apply-conditional-formatting-in-worksheets/#task-1-using-asposecells-to-apply-conditional-formatting-based-on-cell-value).
1. [Utilisation de Aspose.Cells pour appliquer une mise en forme conditionnelle basée sur une formule](/cells/fr/java/apply-conditional-formatting-in-worksheets/#task-2-using-asposecells-to-apply-conditional-formatting-based-on-a-formula).

### **Tâche 1 : Utiliser Aspose.Cells pour appliquer une mise en forme conditionnelle basée sur la valeur Cell**

1. **Téléchargez et installez Aspose.Cells.zip**:
   1. [Télécharger](https://downloads.aspose.com/cells/java) Aspose.Cells for Java.
 1. Décompressez-le sur votre ordinateur de développement.
 Tous les composants Aspose, une fois installés, fonctionnent en mode d'évaluation. Le mode d'évaluation n'a pas de limite de temps et injecte uniquement des filigranes dans les documents produits.
1. **Créer un projet**.
 Créez un projet à l'aide d'un éditeur Java tel qu'Eclipse ou créez un programme simple à l'aide d'un éditeur de texte.
1. **Ajouter un chemin de classe**.
 Pour définir un chemin de classe à l'aide d'Eclipse, veuillez suivre les étapes suivantes :
1. Extrayez les fichiers Aspose.Cells.jar et dom4j_1.6.1.jar de Aspose.Cells.zip.
 1. Définissez le chemin de classe du projet dans Eclipse :
 1. Sélectionnez votre projet dans Eclipse puis sélectionnez**Propriétés** du**Projet** menu.
 1. Sélectionnez "Java Build Path" à gauche de la boîte de dialogue.
 1. Sur le**Bibliothèques** onglet, sélectionnez**Ajouter des JAR** ou**Ajouter des fichiers JAR externes** pour sélectionner Aspose.Cells.jar et dom4j_1.6.1.jar et les ajouter dans les chemins de génération.
 1. Écrivez une application pour invoquer les API des composants de Aspose.
 Ou vous pouvez définir le chemin lors de l'exécution sur une invite DOS dans Windows.

{{< highlight "java" >}}

  javac -classpath %classpath%;e:\Aspose.Cells.jar;  ClassName .javajava -classpath %classpath%;e:\Aspose.Cells.jar;  ClassName  

{{< /highlight >}}

1. **Appliquer une mise en forme conditionnelle en fonction de la valeur de la cellule**.
 Vous trouverez ci-dessous le code utilisé par le composant pour accomplir la tâche. Il applique une mise en forme conditionnelle sur une cellule.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ConditionalFormattingOnCellValue-ApplyConditionalFormattingOnCellValue.java" >}}

Lorsque le code ci-dessus est exécuté, la mise en forme conditionnelle est appliquée à la cellule "A1" dans la première feuille de calcul du fichier de sortie (output.xls). La mise en forme conditionnelle appliquée à A1 dépend de la valeur de la cellule. Si la valeur de cellule de A1 est comprise entre 50 et 100, la couleur d'arrière-plan est rouge en raison de la mise en forme conditionnelle appliquée. Veuillez consulter les captures d'écran suivantes du fichier XLS généré.

**Fichier Excel de sortie avec une valeur A1 inférieure à 50**

![tâche : image_autre_texte](apply-conditional-formatting-in-worksheets_1.png)

**Fichier Excel de sortie avec A1 entre 50 et 100**

![tâche : image_autre_texte](apply-conditional-formatting-in-worksheets_2.png)

### **Tâche 2 : Utiliser Aspose.Cells pour appliquer une mise en forme conditionnelle basée sur une formule**

1. **Appliquer une mise en forme conditionnelle en fonction de la formule**.
 Vous trouverez ci-dessous le code réel utilisé par le composant pour accomplir la tâche. Il applique une mise en forme conditionnelle sur "B3".

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ConditionalFormattingBasedOnFormula-ConditionalFormattingBasedOnFormula.java" >}}

Lorsque le code ci-dessus est exécuté, la mise en forme conditionnelle est appliquée à la cellule "B3" dans la première feuille de calcul du fichier de sortie (output.xls). La mise en forme conditionnelle appliquée dépend de la formule qui calcule la valeur de "B3" comme somme de B1 et B2. Veuillez consulter les captures d'écran suivantes du fichier XLS généré.

**Fichier Excel de sortie avec une valeur B3 inférieure à 100**

![tâche : image_autre_texte](apply-conditional-formatting-in-worksheets_3.png)

**Fichier Excel de sortie avec B3 supérieur à 100**

![tâche : image_autre_texte](apply-conditional-formatting-in-worksheets_4.png)

### **Conclusion**

{{% alert color="primary" %}}

Cet article montre comment appliquer une mise en forme conditionnelle aux cellules d'une feuille de calcul avec le Aspose.Cells API. J'espère qu'il vous donnera un aperçu afin que vous puissiez utiliser ces options dans vos propres scénarios.

Aspose.Cells offre une grande flexibilité pour les solutions et offre une vitesse, une efficacité et une fiabilité exceptionnelles pour répondre aux exigences spécifiques des applications commerciales. Aspose.Cells bénéficie d'années de recherche, de conception et de réglage minutieux.

 Nous accueillons vos questions, commentaires et suggestions dans le[Aspose.CellsForum](https://forum.aspose.com/c/cells/9). Nous garantissons une réponse rapide.

{{% /alert %}}
