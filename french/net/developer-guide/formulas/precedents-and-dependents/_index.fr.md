---
title: Antécédents et personnes à charge
type: docs
weight: 230
url: /fr/net/precedents-and-dependents/
---
{{% alert color="primary" %}} 

Les feuilles de calcul financières complexes, en particulier celles développées en collaboration, peuvent cacher les erreurs les plus embarrassantes. Vérifier l'exactitude des formules et trouver la source d'une erreur peut être difficile lorsque la formule utilise des cellules précédentes et des cellules dépendantes.

{{% /alert %}} 
## **Introduction**
- **Cellules précédentes** sont des cellules référencées par une formule dans un autre Cell. Par exemple, si la cellule D10 contient la formule =B5, la cellule B5 est un précédent de la cellule D10.
- **Cellules dépendantes** contiennent des formules faisant référence à d'autres cellules. Par exemple, si la cellule D10 contient la formule =B5, la cellule D10 dépend de la cellule B5.

Pour faciliter la lecture de la feuille de calcul, vous souhaiterez peut-être indiquer clairement quelles cellules d'une feuille de calcul sont utilisées dans une formule. De même, vous souhaiterez peut-être extraire les cellules dépendantes d'autres cellules.

Aspose.Cells vous permet de tracer des cellules et de découvrir lesquelles sont liées.
## **Traçage précédent et dépendant Cells : Microsoft Excel**
Les formules peuvent changer en fonction des modifications apportées par un client. Par exemple, si la cellule C1 dépend de C3 et C4 contenant une formule et que C1 est modifiée (la formule est donc remplacée), C3 et C4, ou d'autres cellules, doivent être modifiées pour équilibrer la feuille de calcul en fonction des règles métier.

De même, supposons que C1 contienne la formule "=(B1*22)/(M2*N32)". Je veux trouver les cellules dont dépend C1, c'est-à-dire les cellules précédentes B1, M2 et N32.

Vous devrez peut-être tracer la dépendance d'une cellule particulière à d'autres cellules. Si des règles métier sont intégrées dans des formules, nous aimerions découvrir la dépendance et exécuter certaines règles basées sur celle-ci. De même, si la valeur d'une cellule particulière est modifiée, quelles cellules de la feuille de calcul sont impactées par ce changement ?

Microsoft Excel permet aux utilisateurs de retracer les antécédents et les personnes à charge.

1.  Sur le**Afficher la barre d'outils** , sélectionner**Audit de formule**. La boîte de dialogue Audit de formule s'affiche.
1. Tracez des précédents :
 1. Sélectionnez la cellule contenant la formule pour laquelle vous souhaitez rechercher des cellules précédentes.
 1. Pour afficher une flèche de suivi sur chaque cellule qui fournit directement des données à la cellule active, cliquez sur**Tracer des précédents** sur le**Audit de formule** barre d'outils.
1. Formules de trace qui font référence à une cellule particulière (dépendants)
 1. Sélectionnez la cellule pour laquelle vous souhaitez identifier les cellules dépendantes.
1. Pour afficher une flèche de suivi sur chaque cellule qui dépend de la cellule active, cliquez sur Tracer les dépendants dans la barre d'outils Audit de formule.
## **Recherche de précédent et de personne à charge Cells : Aspose.Cells**
### **Retrouver les précédents**
Aspose.Cells facilite l'obtention de cellules précédentes. Non seulement il peut récupérer des cellules qui fournissent des données à des précédents de formules simples, mais également trouver des cellules qui fournissent des données à des précédents de formules complexes avec des plages nommées.

Dans l'exemple ci-dessous, un modèle de fichier Excel, Book1.xls, est utilisé. La feuille de calcul contient des données et des formules sur la première feuille de calcul.

 Aspose.Cells fournit le[Cell](https://reference.aspose.com/cells/net/aspose.cells/cell) classer'[Obtenir les précédents](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getprecedents) méthode utilisée pour retracer les antécédents d'une cellule. Il renvoie un[ReferredAreaCollectionReferredAreaCollection](https://reference.aspose.com/cells/net/aspose.cells/referredareacollection)Comme vous pouvez le voir ci-dessus, dans Book1.xls, la cellule B7 contient une formule "=SUM(A1:A3)". Ainsi, les cellules A1: A3 sont les cellules précédentes à la cellule B7. L'exemple suivant illustre la fonctionnalité de suivi des précédents à l'aide du fichier de modèle Book1.xls.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-TracingPrecedents-1.cs" >}}
### **Recherche des personnes à charge**
Aspose.Cells vous permet d'obtenir des cellules dépendantes dans des feuilles de calcul. Aspose.Cells peut non seulement récupérer des cellules qui fournissent des données concernant une formule simple, mais également trouver des cellules qui fournissent des données à une formule complexe dépendante avec des plages nommées.

 Aspose.Cells fournit le[Cell](https://reference.aspose.com/cells/net/aspose.cells/cell) classer'[GetDependents](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getdependents)méthode utilisée pour retracer les personnes à charge d'une cellule. Par exemple, dans Book1.xlsx, il existe des formules : "=A1+20" et "=A1+30" dans les cellules B2 et C2 respectivement. L'exemple suivant montre comment tracer les personnes à charge pour la cellule A1 à l'aide du fichier de modèle Book1.xlsx.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-TracingDependents-1.cs" >}}
### **Traçage des cellules précédentes et dépendantes selon la chaîne de calcul**
Ci-dessus, les API de traçage des précédents et des personnes à charge sont conformes à l'expression de la formule elle-même. Ils fournissent simplement un moyen pratique pour l'utilisateur de tracer les interdépendances pour quelques formules. S'il y a une grande quantité de formules dans le classeur et que l'utilisateur doit tracer les précédents et les personnes à charge pour chaque cellule, les performances seront médiocres. Pour une telle situation, l'utilisateur doit envisager d'utiliser[GetPrecedentsInCalculation](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getprecedentsincalculation/) et[GetDependentsInCalculation](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getdependentsincalculation/) méthodes. Ces deux méthodes tracent les dépendances selon la chaîne de calcul. Donc, pour les utiliser, vous devez d'abord activer la chaîne de calcul en[Workbook.Settings.FormulaSettings.EnableCalculationChain](https://reference.aspose.com/cells/net/aspose.cells/formulasettings/enablecalculationchain/) . Ensuite, vous devez effectuer un calcul complet pour le classeur en[Workbook.CalculateFormula()](https://reference.aspose.com/cells/net/aspose.cells.workbook/calculateformula/methods/1). Après cela, vous pouvez retracer les précédents ou les personnes à charge pour toutes les cellules dont vous avez besoin.

Pour certaines formules, les précédents résultants peuvent être différents pour GetPrecedents et GetPrecedentsInCalculation, et les dépendances résultantes peuvent être différentes pour GetDependents et GetDependentsInCalculation. Par exemple, si la formule de la cellule A1 est "=IF(TRUE,B2,C3)", GetPrecedents fournira B2 et C3 comme précédent de A1. En conséquence, B2 et C3 ont tous deux le A1 dépendant lors de la vérification par GetDependents. Cependant, pour le calcul de cette formule, il est évident que seul B2 peut affecter le résultat calculé. Ainsi GetPrecedentsInCalculation ne fournira pas C3 pour A1, et GetDependentsInCalculation ne fournira pas A1 pour C3. Parfois, l'utilisateur peut simplement avoir besoin de tracer ces interdépendances qui affectent réellement le résultat calculé des formules basées sur les données actuelles du classeur, puis ils doivent également utiliser GetDependentsInCalculation/GetPrecedentsInCalculation au lieu de GetDependents/GetPrecedents.

L'exemple suivant montre comment tracer les précédents et les dépendants selon la chaîne de calcul pour les cellules :


{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-TracingDependenciesInCalculation.cs" >}}
