---
title: Appliquer le formatage conditionnel dans les feuilles de calcul
type: docs
weight: 40
url: /fr/java/apply-conditional-formatting-in-worksheets/
---

{{% alert color="primary" %}}

Cet article est conçu pour fournir une compréhension détaillée de comment ajouter un formatage conditionnel à une plage de cellules dans une feuille de calcul.

Le formatage conditionnel est une fonctionnalité avancée de Microsoft Excel qui vous permet d'appliquer des formats à une plage de cellules et d'avoir ce formatage modifié en fonction de la valeur de la cellule ou de la valeur d'une formule. Par exemple, l'arrière-plan d'une cellule peut être rouge pour mettre en évidence une valeur négative, ou la couleur du texte pourrait être verte pour une valeur positive. Lorsque la valeur de la cellule répond à la condition de formatage, le format est appliqué. Si la valeur de la cellule ne répond pas à la condition de formatage, le formatage par défaut de la cellule est utilisé.

Il est possible d'appliquer un formatage conditionnel avec l'automatisation Microsoft Office, mais cela présente des inconvénients. Il y a plusieurs raisons et problèmes impliqués : par exemple, la sécurité, la stabilité, la scalabilité et la vitesse. La principale raison de trouver une autre solution est que Microsoft recommande fortement de ne pas utiliser l'automatisation Office pour les solutions logicielles.

Cet article montre comment créer une application console, ajouter un formatage conditionnel sur des cellules avec quelques lignes de code les plus simples à l'aide de l'API Aspose.Cells.

{{% /alert %}}

## **Travailler avec le formatage conditionnel**

Cet article aborde les tâches suivantes :

1. [Utilisation d'Aspose.Cells pour appliquer un formatage conditionnel en fonction de la valeur de la cellule](/cells/fr/java/apply-conditional-formatting-in-worksheets/#task-1-using-asposecells-to-apply-conditional-formatting-based-on-cell-value).
1. [Utilisation d'Aspose.Cells pour appliquer un formatage conditionnel en fonction d'une formule](/cells/fr/java/apply-conditional-formatting-in-worksheets/#task-2-using-asposecells-to-apply-conditional-formatting-based-on-a-formula).

### **Tâche 1 : Utilisation d'Aspose.Cells pour appliquer un formatage conditionnel en fonction de la valeur de la cellule**

1. **Téléchargez et installez Aspose.Cells.zip** :
   1. [Téléchargez](https://downloads.aspose.com/cells/java) Aspose.Cells for Java.
   1. Décompressez-le sur votre ordinateur de développement.
      Tous les composants Aspose, lorsqu'ils sont installés, fonctionnent en mode d'évaluation. Le mode d'évaluation n'a pas de limite de temps et ne produit que des documents avec des filigranes.
1. **Créer un projet**.
   Soit créez un projet à l'aide d'un éditeur Java tel qu'Eclipse, soit créez un programme simple à l'aide d'un éditeur de texte.
1. **Ajouter le chemin de classe**.
   Pour définir un chemin de classe en utilisant Eclipse, veuillez suivre les étapes suivantes :
   1. Extrayez le fichier Aspose.Cells.jar et dom4j_1.6.1.jar du fichier Aspose.Cells.zip.
   1. Définissez le chemin de classe du projet dans Eclipse :
      1. Sélectionnez votre projet dans Eclipse, puis sélectionnez ** Propriétés ** dans le menu ** Projet **.
      1. Sélectionnez "Chemin de construction Java" à gauche de la boîte de dialogue.
      1. Sur l'onglet ** Bibliothèques **, sélectionnez ** Ajouter des JAR ** ou ** Ajouter des JAR externes ** pour sélectionner Aspose.Cells.jar et dom4j_1.6.1.jar et les ajouter aux chemins de construction.
   1. Écrivez une application pour appeler les API des composants d'Aspose.
      Ou vous pouvez définir le chemin à l'exécution sur une invite DOS dans Windows.

{{< highlight java >}}

  javac -classpath %classpath%;e:\Aspose.Cells.jar;  ClassName .javajava -classpath %classpath%;e:\Aspose.Cells.jar;  ClassName  

{{< /highlight >}}

1. ** Appliquer une mise en forme conditionnelle en fonction de la valeur de la cellule **.
   Ci-dessous se trouve le code utilisé par le composant pour accomplir la tâche. Il applique une mise en forme conditionnelle sur une cellule.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ConditionalFormattingOnCellValue-ApplyConditionalFormattingOnCellValue.java" >}}

Lorsque le code ci-dessus est exécuté, une mise en forme conditionnelle est appliquée à la cellule "A1" dans la première feuille de calcul du fichier de sortie (output.xls). La mise en forme conditionnelle appliquée à A1 dépend de la valeur de la cellule. Si la valeur de la cellule A1 est comprise entre 50 et 100, la couleur de fond est rouge en raison de la mise en forme conditionnelle appliquée. Veuillez consulter les captures d'écran suivantes du fichier XLS généré.

** Fichier Excel de sortie avec une valeur A1 inférieure à 50 **

![todo:image_alt_text](apply-conditional-formatting-in-worksheets_1.png)

** Fichier Excel de sortie avec une valeur A1 entre 50 et 100 **

![todo:image_alt_text](apply-conditional-formatting-in-worksheets_2.png)

### **Tâche 2: Utiliser Aspose.Cells pour appliquer une mise en forme conditionnelle en fonction d'une formule**

1. ** Appliquer une mise en forme conditionnelle en fonction d'une formule **.
   Ci-dessous se trouve le code réel utilisé par le composant pour accomplir la tâche. Il applique une mise en forme conditionnelle sur “B3”.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ConditionalFormattingBasedOnFormula-ConditionalFormattingBasedOnFormula.java" >}}

Lorsque le code ci-dessus est exécuté, une mise en forme conditionnelle est appliquée à la cellule “B3” dans la première feuille de calcul du fichier de sortie (output.xls). La mise en forme conditionnelle appliquée dépend de la formule qui calcule la valeur de “B3” comme la somme de B1 & B2. Veuillez consulter les captures d'écran suivantes du fichier XLS généré.

** Fichier Excel de sortie avec une valeur B3 inférieure à 100 **

![todo:image_alt_text](apply-conditional-formatting-in-worksheets_3.png)

** Fichier Excel de sortie avec une valeur B3 supérieure à 100 **

![todo:image_alt_text](apply-conditional-formatting-in-worksheets_4.png)

### **Conclusion**

{{% alert color="primary" %}}

Cet article montre comment appliquer une mise en forme conditionnelle aux cellules dans une feuille de calcul avec l'API Aspose.Cells. Espérons que cela vous donnera un aperçu afin que vous puissiez utiliser ces options dans vos propres scénarios.

Aspose.Cells offre une grande flexibilité pour les solutions et fournit une vitesse, une efficacité et une fiabilité exceptionnelles pour répondre aux exigences spécifiques des applications métier. Aspose.Cells bénéficie d'années de recherche, de conception et d'accord minutieux.

Nous sommes à votre disposition pour répondre à vos questions, commentaires et suggestions dans le [forum Aspose.Cells](https://forum.aspose.com/c/cells/9). Nous garantissons une réponse rapide.

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
