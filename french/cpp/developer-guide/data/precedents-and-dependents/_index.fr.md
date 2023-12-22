---
title: Précédents et personnes à charge
type: docs
weight: 100
url: /fr/cpp/precedents-and-dependents/
---
{{% alert color="primary" %}} 

Des feuilles de calcul financières complexes, en particulier celles élaborées en collaboration, peuvent cacher les erreurs les plus embarrassantes. Vérifier l'exactitude des formules et trouver la source d'une erreur peut être difficile lorsque la formule utilise des cellules précédentes et des cellules dépendantes.

{{% /alert %}} 
##  **Introduction**
- **Cellules précédentes** sont des cellules auxquelles une formule fait référence dans une autre cellule. Par exemple, si la cellule D10 contient la formule =B5, la cellule B5 est un précédent à la cellule D10.
- **Cellules dépendantes** contiennent des formules qui font référence à d’autres cellules. Par exemple, si la cellule D10 contient la formule =B5, la cellule D10 dépend de la cellule B5.

Pour rendre la feuille de calcul facile à lire, vous souhaiterez peut-être afficher clairement quelles cellules d'une feuille de calcul sont utilisées dans une formule. De même, vous souhaiterez peut-être extraire les cellules dépendantes d’autres cellules.

Aspose.Cells permet de tracer les cellules et de savoir lesquelles sont liées.
##  **Traçage des précédents et des dépendants Cells : Microsoft Excel**
Les formules peuvent changer en fonction des modifications apportées par un client. Par exemple, si la cellule C1 dépend de C3 et C4 contenant une formule et que C1 est modifié (la formule est donc remplacée), C3 et C4, ou d'autres cellules, doivent être modifiées pour équilibrer la feuille de calcul en fonction des règles métier.

De même, supposons que C1 contienne la formule "=(B1*22)/(M2*N32)". Je veux trouver les cellules dont dépend C1, c'est-à-dire les cellules précédentes B1, M2 et N32.

Vous devrez peut-être retracer la dépendance d'une cellule particulière par rapport à d'autres cellules. Si des règles métier sont intégrées dans des formules, nous aimerions connaître la dépendance et exécuter certaines règles basées sur celle-ci. De même, si la valeur d’une cellule particulière est modifiée, quelles cellules de la feuille de calcul sont affectées par ce changement ?

Microsoft Excel permet aux utilisateurs de retracer les précédents et les dépendances.

1.  Sur le**Afficher la barre d'outils**, sélectionnez **Audit de formule**
1. Tracer des précédents :
 1. Sélectionnez la cellule contenant la formule pour laquelle vous souhaitez rechercher les cellules précédentes.
 1. Pour afficher une flèche de suivi sur chaque cellule qui fournit directement des données à la cellule active, cliquez sur**Tracer des précédents** sur le**Audit de formule** barre d'outils.
1. Tracer des formules qui font référence à une cellule particulière (dépendantes)
 1. Sélectionnez la cellule pour laquelle vous souhaitez identifier les cellules dépendantes.
1. Pour afficher une flèche de suivi sur chaque cellule qui dépend de la cellule active, cliquez sur Tracer les dépendances dans la barre d'outils Audit de formule.
##  **Recherche des précédents et des personnes à charge Cells : Aspose.Cells**
###  **Retracer les précédents**
Aspose.Cells facilite l’obtention de cellules précédentes. Non seulement il peut récupérer des cellules qui fournissent des données sur des précédents de formules simples, mais également trouver des cellules qui fournissent des données sur des précédents de formules complexes avec des plages nommées.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-C-main-TracingPrecedents-new.cpp" >}}
###  **Recherche des personnes à charge**
Aspose.Cells vous permet d'obtenir des cellules dépendantes dans des feuilles de calcul. Aspose.Cells peut non seulement récupérer des cellules qui fournissent des données concernant une formule simple, mais également trouver des cellules qui fournissent des données à des personnes dépendantes de formules complexes avec des plages nommées.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-C-main-TracingDependents-new.cpp" >}}
