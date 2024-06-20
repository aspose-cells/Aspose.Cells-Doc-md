---
title: Prédécesseurs et dépendants
type: docs
weight: 230
url: /fr/java/precedents-and-dependents/
---

{{% alert color="primary" %}} 

Les feuilles de calcul financières complexes, en particulier celles développées en collaboration, peuvent cacher les erreurs les plus gênantes. Vérifier la précision des formules et trouver la source d'une erreur peut être difficile lorsque la formule utilise des cellules précédentes et des cellules dépendantes.

{{% /alert %}} 
## **Introduction**
- **Cellules précédentes** sont des cellules auxquelles une formule d'une autre cellule fait référence. Par exemple, si la cellule D10 contient la formule =B5, la cellule B5 est une cellule précédente de la cellule D10.
- **Cellules dépendantes** contiennent des formules qui font référence à d'autres cellules. Par exemple, si la cellule D10 contient la formule =B5, la cellule D10 est dépendante de la cellule B5.

Pour rendre la feuille de calcul facile à lire, vous voudrez peut-être clairement indiquer quelles cellules d'une feuille de calcul sont utilisées dans une formule. De même, vous voudrez peut-être extraire les cellules dépendantes d'autres cellules.

Aspose.Cells vous permet de tracer les cellules et de savoir lesquelles sont liées.
## **Tracer les cellules précédentes et dépendantes : Microsoft Excel**
Les formules peuvent changer en fonction des modifications apportées par un client. Par exemple, si la cellule C1 dépend de C3 et C4 contenant une formule, et que C1 est modifiée (la formule étant remplacée), C3 et C4, ou d'autres cellules, doivent changer pour équilibrer la feuille de calcul en fonction des règles métier.

De même, supposons que C1 contient la formule "=(B1*22)/(M2*N32)". Je veux trouver les cellules dont C1 dépend, c'est-à-dire les cellules précédentes B1, M2 et N32.

Il se peut que vous deviez retracer la dépendance d'une cellule particulière à d'autres cellules. Si des règles métier sont intégrées dans des formules, nous aimerions connaître la dépendance et exécuter certaines règles en fonction de celle-ci. De même, si la valeur d'une cellule particulière est modifiée, quelles cellules dans la feuille de calcul sont impactées par ce changement ?

Microsoft Excel permet aux utilisateurs de tracer les cellules précédentes et dépendantes.

1. Sur la **Barre d'outils Affichage**, sélectionnez **Audit des formules**. La boîte de dialogue Audit des formules s'affichera.
1. Tracer les cellules précédentes :
   1. Sélectionnez la cellule contenant la formule pour laquelle vous souhaitez trouver les cellules précédentes.
   1. Pour afficher une flèche de traçage vers chaque cellule qui fournit directement des données à la cellule active, cliquez sur **Tracer les cellules précédentes** sur la **Barre d'outils Audit de formules**.
1. Tracer les formules qui référencent une cellule particulière (dépendantes)
   1. Sélectionnez la cellule pour laquelle vous souhaitez identifier les cellules dépendantes.
   1. Pour afficher une flèche de traçage vers chaque cellule qui dépend de la cellule active, cliquez sur Traçage des dépendances sur la barre d'outils d'Audit de formules.
## **Tracer les cellules précédentes et dépendantes : Aspose.Cells**
### **Tracer les cellules précédentes**
Aspose.Cells facilite l'obtention de cellules précédentes. Il peut non seulement récupérer les cellules fournissant des données aux précédents de formule simples, mais aussi trouver les cellules fournissant des données aux précédents de formule complexes avec des plages nommées.

Dans l'exemple ci-dessous, un fichier excel modèle, Book1.xls, est utilisé. La feuille de calcul contient des données et des formules sur la première feuille de calcul.

Aspose.Cells fournit la classe [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/Cell) avec la méthode [GetPrecedents](https://reference.aspose.com/cells/java/com.aspose.cells/Cell#getPrecedents--) utilisée pour tracer les précédents d'une cellule. Elle renvoie une [ReferredAreaCollection](https://reference.aspose.com/cells/java/com.aspose.cells/ReferredAreaCollection). Comme vous pouvez le voir ci-dessus, dans Book1.xls, la cellule B7 contient une formule "=SUM(A1:A3)". Les cellules A1:A3 sont donc les cellules précédentes de la cellule B7. L'exemple suivant illustre la fonctionnalité de traçage des précédents à l'aide du fichier modèle Book1.xls.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-TracingPrecedents.java" >}}
### **Tracé des dépendances**
Aspose.Cells vous permet d'obtenir des cellules dépendantes dans les feuilles de calcul. Aspose.Cells peut non seulement récupérer les cellules qui fournissent des données concernant une formule simple, mais aussi trouver les cellules qui fournissent des données à des formules complexes dépendantes de plages nommées.

Aspose.Cells fournit la méthode [GetDependents](https://reference.aspose.com/cells/java/com.aspose.cells/Cell#getDependents(boolean)) de la classe [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/Cell) utilisée pour tracer les dépendances d'une cellule. Par exemple, dans Book1.xlsx, il y a les formules: "=A1+20" et "=A1+30" dans les cellules B2 et C2 respectivement. L'exemple suivant montre comment tracer les dépendances pour la cellule A1 en utilisant le fichier modèle Book1.xlsx.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-TracingDependents.java" >}}
### **Tracer les cellules précédentes et dépendantes selon la chaîne de calcul**
Les API ci-dessus pour tracer les cellules précédentes et dépendantes sont basées sur l'expression de la formule elle-même. Elles fournissent simplement un moyen pratique pour l'utilisateur de tracer les interdépendances pour quelques formules. S'il y a un grand nombre de formules dans le classeur et que l'utilisateur a besoin de tracer les cellules précédentes et dépendantes pour chaque cellule, elles offriront de mauvaises performances. Pour une telle situation, l'utilisateur devrait envisager d'utiliser les méthodes [GetPrecedentsInCalculation](https://reference.aspose.com/cells/java/com.aspose.cells/Cell#getPrecedentsInCalculation--) et [GetDependentsInCalculation](https://reference.aspose.com/cells/java/com.aspose.cells/Cell#getDependentsInCalculation(boolean)/). Ces deux méthodes tracent les dépendances selon la chaîne de calcul. Ainsi, pour les utiliser, vous devez d'abord activer la chaîne de calcul en [Workbook.Settings.FormulaSettings.EnableCalculationChain](https://reference.aspose.com/cells/java/com.aspose.cells/FormulaSettings#EnableCalculationChain). Ensuite, vous devez effectuer un calcul complet pour le classeur avec [Workbook.CalculateFormula()](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula(com.aspose.cells.CalculationOptions)). Ensuite, vous pouvez tracer les cellules précédentes ou dépendantes pour toutes les cellules dont vous avez besoin.

Pour certaines formules, les précédents résultants peuvent être différents pour GetPrecedents et GetPrecedentsInCalculation, et les dépendants résultants peuvent être différents pour GetDependents et GetDependentsInCalculation. Par exemple, si la formule de la cellule A1 est "=IF(TRUE,B2,C3)", GetPrecedents fournira B2 et C3 comme précédents de A1. En conséquence, B2 et C3 ont tous deux la dépendance A1 lorsqu'on utilise GetDependents. Cependant, pour le calcul de cette formule, il est évident que seule B2 peut affecter le résultat calculé. Ainsi, GetPrecedentsInCalculation ne fournira pas C3 pour A1, et GetDependentsInCalculation ne fournira pas A1 pour C3. Parfois, l'utilisateur peut simplement avoir besoin de tracer ces interdépendances qui affectent réellement le résultat calculé des formules en fonction des données actuelles du classeur, alors ils doivent aussi utiliser GetDependentsInCalculation/GetPrecedentsInCalculation au lieu de GetDependents/GetPrecedents.

L'exemple suivant montre comment tracer les précédents et les dépendants selon la chaîne de calcul pour les cellules:


{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-TracingDependenciesInCalculation.java" >}}
