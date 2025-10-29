---
title: Prédécesseurs et dépendants
type: docs
weight: 100
url: /fr/cpp/precedents-and-dependents/
---

{{% alert color="primary" %}} 

Les feuilles de calcul financières complexes, en particulier celles développées en collaboration, peuvent cacher les erreurs les plus gênantes. Vérifier la précision des formules et trouver la source d'une erreur peut être difficile lorsque la formule utilise des cellules précédentes et des cellules dépendantes.

{{% /alert %}} 
## **Introduction**
- **Les cellules précédentes** sont des cellules auxquelles une formule dans une autre cellule fait référence. Par exemple, si la cellule D10 contient la formule =B5, la cellule B5 est une cellule précédente de la cellule D10.
- **Cellules dépendantes** contiennent des formules qui font référence à d'autres cellules. Par exemple, si la cellule D10 contient la formule =B5, la cellule D10 est dépendante de la cellule B5.

Pour rendre la feuille de calcul facile à lire, vous voudrez peut-être clairement indiquer quelles cellules d'une feuille de calcul sont utilisées dans une formule. De même, vous voudrez peut-être extraire les cellules dépendantes d'autres cellules.

Aspose.Cells vous permet de tracer les cellules et de savoir lesquelles sont liées.
## **Tracer les cellules précédentes et dépendantes : Microsoft Excel**
Les formules peuvent changer en fonction des modifications apportées par un client. Par exemple, si la cellule C1 dépend de C3 et C4 contenant une formule, et que C1 est modifiée (la formule étant remplacée), C3 et C4, ou d'autres cellules, doivent changer pour équilibrer la feuille de calcul en fonction des règles métier.

De même, supposons que C1 contient la formule "=(B1*22)/(M2*N32)". Je veux trouver les cellules dont C1 dépend, c'est-à-dire les cellules précédentes B1, M2 et N32.

Il se peut que vous deviez retracer la dépendance d'une cellule particulière à d'autres cellules. Si des règles métier sont intégrées dans des formules, nous aimerions connaître la dépendance et exécuter certaines règles en fonction de celle-ci. De même, si la valeur d'une cellule particulière est modifiée, quelles cellules dans la feuille de calcul sont impactées par ce changement ?

Microsoft Excel permet aux utilisateurs de tracer les cellules précédentes et dépendantes.

1. Sur la ** barre d'outils Affichage **, sélectionnez ** Audit de formules **
1. Tracer les cellules précédentes :
   1. Sélectionnez la cellule contenant la formule pour laquelle vous souhaitez trouver les cellules précédentes.
   1. Pour afficher une flèche de traçage vers chaque cellule qui fournit directement des données à la cellule active, cliquez sur **Tracer les cellules précédentes** sur la **Barre d'outils Audit de formules**.
1. Tracer les formules qui référencent une cellule particulière (dépendantes)
   1. Sélectionnez la cellule pour laquelle vous souhaitez identifier les cellules dépendantes.
   1. Pour afficher une flèche de traçage vers chaque cellule qui dépend de la cellule active, cliquez sur Traçage des dépendances sur la barre d'outils d'Audit de formules.
## **Tracer les cellules précédentes et dépendantes : Aspose.Cells**
### **Tracer les cellules précédentes**
Aspose.Cells facilite l'obtention de cellules précédentes. Il peut non seulement récupérer les cellules fournissant des données aux précédents de formule simples, mais aussi trouver les cellules fournissant des données aux précédents de formule complexes avec des plages nommées.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-C-main-TracingPrecedents-new.cpp" >}}
### **Tracé des dépendances**
Aspose.Cells vous permet d'obtenir des cellules dépendantes dans les feuilles de calcul. Aspose.Cells peut non seulement récupérer les cellules qui fournissent des données concernant une formule simple mais aussi trouver les cellules qui fournissent des données aux dépendants de formules complexes avec des plages nommées.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-C-main-TracingDependents-new.cpp" >}}
{{< app/cells/assistant language="cpp" >}}
