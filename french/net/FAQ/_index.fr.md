---
title: FAQ
type: docs
weight: 100
url: /fr/net/faq/
---
## **Comment réparer l'exception System.StackOverFlowException sur Workbook.CalculateFormula ?**
Parfois, les utilisateurs sont confrontés à System.StackOverFlowException sur la méthode Workbook.CalculateFormula. Cette exception se produit généralement parce que la taille de pile par défaut d'IIS est trop petite (265 Ko uniquement). Vous pouvez corriger cette erreur en créant un autre thread avec une taille de pile accrue, puis en déplaçant votre code associé Workbook.CalculateFormula à l'intérieur.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Controllers-GridWebFAQController-FixStackOverflowException.cs" >}}
## **Problème d'épaisseur des lignes lors du rendu d'Excel à PDF**
Parfois, lorsque le fichier Excel est converti en PDF, l'épaisseur des lignes est différente dans la sortie PDF. Ce problème n'est pas causé par Aspose.Cells. Il est causé par**Adobe Reader** quand ses réglages**"Dessin au trait lisse"** et**"Améliorer les lignes fines"** sont vérifiés. Décocher ces options affichera PDF bien.

 Si vérifier**"Dessin au trait lisse"** et**"Améliorer les lignes fines"**, l'épaisseur des lignes est différente. Voir les étapes suivantes comment c'est fait:

-  Aller à**Éditer**
-  Sélectionner**Préférences**
-  Dans le**Affichage des pages** Catégorie Vérifiez la**"Dessin au trait lisse"** et**"Améliorer les lignes fines"**

 Si décocher**"Dessin au trait lisse"** et**"Améliorer les lignes fines"**, l'épaisseur des lignes est la même. Pour y parvenir, suivez simplement les étapes ci-dessous :

-  Aller à**Éditer**
-  Sélectionner**Préférences**
-  Dans le**Affichage des pages** Catégorie Décochez la**"Dessin au trait lisse"** et**"Améliorer les lignes fines"**
## **Comment réparer l'exception System.OutOfMemoryException lors du chargement de feuilles de calcul volumineuses ?**
Il y a de bonnes chances que le constructeur Workbook lève System.OutOfMemoryException lors du chargement de feuilles de calcul volumineuses. Cette exception suggère que la mémoire disponible est insuffisante pour charger complètement la feuille de calcul dans la mémoire. Par conséquent, la feuille de calcul doit être chargée tout en activant le[Préférences de mémoire](/cells/fr/net/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/).

Les API Aspose.Cells fournissent des préférences de mémoire pour optimiser la consommation de mémoire lors du chargement et du traitement des feuilles de calcul. Ces options sont également utiles pour charger efficacement les grandes feuilles de calcul contenant d'énormes ensembles de données dans l'objet Workbook, comme illustré ci-dessous.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-KnowledgeBase-FAQs-FixOutOfMemoryException-1.cs" >}}

## **Déterminer quelle taille de pile est nécessaire pour un certain classeur**
Bien que nous ayons amélioré le moteur de calcul de formule Aspose.Cells et dans la plupart des cas, vous devriez pouvoir obtenir toutes les formules calculées avec succès pour un fichier de modèle donné sans spécifier une taille de pile plus petite. Mais encore, parfois StackOverFlowException sur la méthode Workbook.CalculateFormula peut être inévitable. Nous fournissons de nouvelles API aux utilisateurs pour suivre les calculs des formules. Nous avons ajouté une classe nommée "AbstractCalculationMonitor" et fourni une propriété, c'est-à-dire,*CalculationOptions.CalculationMonitor*pour faire face à / tracer le problème.

Les utilisateurs peuvent tracer eux-mêmes la taille de la pile à l'aide des API. Veuillez noter que la vérification de la pile pour chaque cellule dégradera sûrement davantage les performances. Consultez l'exemple de segment de code pour votre référence :

`     `classe publique MyCalculationMonitor : AbstractCalculationMonitor
`     `{  ` `public override void BeforeCalculate(int sheetIndex, int rowIndex, int colIndex)  ` `{  ` `if(new StackTrace(false).FrameCount > 2000)  ` `{  ` `throw new Exception( Arrêtez le calcul de la formule car risque de StackOverflowException");  ` `}  ` `}  ` `} 



{{% alert color="primary" %}} 

Il n'y a pas de meilleur moyen d'obtenir la taille de la pile utilisée lors de l'exécution. Le code ci-dessus que nous avons fourni est juste à titre d'exemple. Les performances seront certainement dégradées de manière significative. Nous pensons donc que le code peut être optimisé par les utilisateurs (qui veulent vraiment l'utiliser) en fonction de leurs différents scénarios et exigences. Par exemple, vérifier la pile lorsque le nombre de cellules récursives atteint un certain nombre, collecter le taux d'augmentation moyen de la pile pour une cellule récursive et déterminer la fréquence de vérification de la pile, etc.

{{% /alert %}}

