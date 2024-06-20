---
title: FAQ
type: docs
weight: 100
url: /fr/net/faq/
---

## **Comment réparer l'exception System.StackOverflowException sur Workbook.CalculateFormula?**
Parfois, les utilisateurs sont confrontés à l'exception System.StackOverFlowException lors de l'utilisation de la méthode Workbook.CalculateFormula. Cette exception se produit généralement parce que la taille de pile par défaut de l'IIS est trop petite (seulement 265ko). Vous pouvez corriger cette erreur en créant un autre thread avec une taille de pile augmentée, puis en déplaçant votre code lié à Workbook.CalculateFormula à l'intérieur.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Controllers-GridWebFAQController-FixStackOverflowException.cs" >}}
## **Problème d'épaisseur des lignes lors du rendu d'Excel en PDF**
Parfois, lors de la conversion de fichiers Excel en PDF, l'épaisseur des lignes est différente dans le PDF de sortie. Ce problème n'est pas causé par Aspose.Cells. Il est causé par **Adobe Reader** lorsque ses paramètres **"Lissage des dessins"** et **"Amélioration des lignes fines"** sont activés. Désactiver ces options permettra d'afficher le PDF correctement.

Si vous cochez **"Lissage des dessins"** et **"Amélioration des lignes fines"**, l'épaisseur des lignes est différente. Voici comment procéder :

- Allez dans **Édition**
- Sélectionnez **Préférences**
- Dans la catégorie **Affichage de la Page**, cochez **"Lissage des dessins"** et **"Amélioration des lignes fines"**

Si vous décochez **"Lissage des dessins"** et **"Amélioration des lignes fines"**, l'épaisseur des lignes est la même. Pour ce faire, suivez les étapes ci-dessous :

- Allez dans **Édition**
- Sélectionnez **Préférences**
- Dans la catégorie **Affichage de la Page**, décochez **"Lissage des dessins"** et **"Amélioration des lignes fines"**
## **Comment réparer l'exception System.OutOfMemoryException lors du chargement de grandes feuilles de calcul ?**
Il existe de fortes chances que le constructeur Workbook génère une exception System.OutOfMemoryException lors du chargement de grandes feuilles de calcul. Cette exception suggère que la mémoire disponible est insuffisante pour charger complètement la feuille de calcul dans la mémoire, donc la feuille de calcul doit être chargée tout en activant les [Préférences de Mémoire](/cells/fr/net/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/).

Les API Aspose.Cells fournissent des Préférences de Mémoire pour optimiser la consommation de mémoire lors du chargement et du traitement de feuilles de calcul. Ces options sont également utiles pour charger efficacement de grandes feuilles de calcul contenant de grands ensembles de données dans l'objet Workbook, comme le montre l'exemple ci-dessous.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-KnowledgeBase-FAQs-FixOutOfMemoryException-1.cs" >}}

## **Déterminer la taille de pile nécessaire pour un certain Workbook**
Bien que nous ayons amélioré le moteur de calcul de formules Aspose.Cells et, dans la plupart des cas, vous devriez être en mesure de calculer toutes les formules avec succès pour un fichier modèle donné sans spécifier une taille de pile plus petite. Cependant, parfois l'exception System.StackOverFlowException sur la méthode Workbook.CalculateFormula peut être inévitable. Nous proposons de nouvelles API aux utilisateurs pour suivre les calculs de formules. Nous avons ajouté une classe nommée "AbstractCalculationMonitor" et fourni une propriété, à savoir *CalculationOptions.CalculationMonitor* pour faire face à/trace l'issue.

Les utilisateurs peuvent suivre la taille de la pile eux-mêmes en utilisant les APIs. Veuillez noter que vérifier la pile pour chaque cellule va sûrement dégrader les performances dans une plus grande mesure. Consultez le segment de code d'exemple pour votre référence :

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "CalculationMonitor-CustomStackTrace.cs" >}}

{{% alert color="primary" %}} 

Il n'y a pas de meilleur moyen d'obtenir la taille de la pile utilisée à l'exécution. Le code ci-dessus que nous avons fourni est juste un exemple. Les performances seront certainement dégradées. Ainsi, nous pensons que le code peut être optimisé par les utilisateurs (qui veulent vraiment l'utiliser) selon leurs scénarios et exigences différents. Par exemple, vérifier la pile lorsque le nombre de cellules récursives atteint un certain nombre, rassembler le taux d'augmentation moyen de la pile pour une cellule récursive et déterminer la fréquence pour vérifier la pile, etc.

{{% /alert %}}

