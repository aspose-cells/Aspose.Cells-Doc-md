---
title: Antécédents et personnes à charge
type: docs
weight: 100
url: /fr/cpp/precedents-and-dependents/
---
{{% alert color="primary" %}} 

Les feuilles de calcul financières complexes, en particulier celles développées en collaboration, peuvent cacher les erreurs les plus embarrassantes. Vérifier l'exactitude des formules et trouver la source d'une erreur peut être difficile lorsque la formule utilise des cellules précédentes et des cellules dépendantes.

{{% /alert %}} 
## **Introduction**
- **Cellules précédentes** sont des cellules auxquelles il est fait référence par une formule dans une autre cellule. Par exemple, si la cellule D10 contient la formule =B5, la cellule B5 est un précédent à la cellule D10.
- **Cellules dépendantes** contiennent des formules faisant référence à d'autres cellules. Par exemple, si la cellule D10 contient la formule =B5, la cellule D10 dépend de la cellule B5.

Pour faciliter la lecture de la feuille de calcul, vous souhaiterez peut-être indiquer clairement quelles cellules d'une feuille de calcul sont utilisées dans une formule. De même, vous souhaiterez peut-être extraire les cellules dépendantes d'autres cellules.

Aspose.Cells vous permet de tracer des cellules et de découvrir lesquelles sont liées.
## **Traçage précédent et dépendant Cells : Microsoft Excel**
Les formules peuvent changer en fonction des modifications apportées par un client. Par exemple, si la cellule C1 dépend de C3 et C4 contenant une formule et que C1 est modifiée (la formule est donc remplacée), C3 et C4, ou d'autres cellules, doivent être modifiées pour équilibrer la feuille de calcul en fonction des règles métier.

De même, supposons que C1 contienne la formule "=(B1*22)/(M2*N32)". Je veux trouver les cellules dont dépend C1, c'est-à-dire les cellules précédentes B1, M2 et N32.

Vous devrez peut-être tracer la dépendance d'une cellule particulière à d'autres cellules. Si des règles métier sont intégrées dans des formules, nous aimerions découvrir la dépendance et exécuter certaines règles basées sur celle-ci. De même, si la valeur d'une cellule particulière est modifiée, quelles cellules de la feuille de calcul sont impactées par ce changement ?

Microsoft Excel permet aux utilisateurs de retracer les antécédents et les personnes à charge.

1.  Sur le**Afficher la barre d'outils** , sélectionner**Audit de formule**
1. Tracez des précédents :
1. Sélectionnez la cellule contenant la formule pour laquelle vous souhaitez rechercher des cellules précédentes.
 1. Pour afficher une flèche de suivi sur chaque cellule qui fournit directement des données à la cellule active, cliquez sur**Tracer des précédents** sur le**Audit de formule** barre d'outils.
1. Formules de trace qui font référence à une cellule particulière (dépendants)
 1. Sélectionnez la cellule pour laquelle vous souhaitez identifier les cellules dépendantes.
 1. Pour afficher une flèche de suivi sur chaque cellule qui dépend de la cellule active, cliquez sur Tracer les dépendants dans la barre d'outils Audit de formule.
## **Recherche de précédent et de personne à charge Cells : Aspose.Cells**
### **Retrouver les précédents**
Aspose.Cells facilite l'obtention de cellules précédentes. Non seulement il peut récupérer des cellules qui fournissent des données à des précédents de formules simples, mais également trouver des cellules qui fournissent des données à des précédents de formules complexes avec des plages nommées.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-C-main-TracingPrecedents.cpp" >}}
### **Recherche des personnes à charge**
Aspose.Cells vous permet d'obtenir des cellules dépendantes dans des feuilles de calcul. Aspose.Cells peut non seulement récupérer des cellules qui fournissent des données concernant une formule simple, mais également trouver des cellules qui fournissent des données à des dépendants de formules complexes avec des plages nommées.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-C-main-TracingDependents.cpp" >}}
