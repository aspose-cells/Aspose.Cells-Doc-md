---
title: Gérer les événements côté serveur du filtre de colonne
type: docs
weight: 90
url: /fr/net/aspose-cells-gridweb/handle-column-filter-server-side-events/
keywords: GridWeb,filter,OnBeforeColumnFilter,OnAfterColumnFilter
description: Cet article présente comment gérer l événement de filtre de colonne dans GridWeb.
---

{{% alert color="primary" %}} 

La filtrage des données est probablement la fonctionnalité Excel la plus largement utilisée qui permet de filtrer les données en fonction de critères spécifiques. Les données filtrées affichent uniquement les lignes qui répondent à la condition en masquant les lignes qui ne remplissent pas les critères.
Le composant Aspose.Cells.GridWeb offre la possibilité d'effectuer le filtrage des données en utilisant son interface. Afin d'étendre ses capacités, le composant Aspose.Cells.GridWeb fournit également deux événements qui peuvent servir de rappel au mécanisme de filtrage effectué via l'interface GridWeb.

{{% /alert %}} 
## **Gestion de l'événement côté serveur lors de l'application du filtre de colonne**
Il existe deux événements principaux comme détaillé ci-dessous.

1. OnBeforeColumnFilter: Se déclenche avant que le filtre soit appliqué sur une colonne.
1. OnAfterColumnFilter: Se déclenche après l'application du filtre sur une colonne.

Voici le script ASPX du composant Aspose.Cells.GridWeb pour ajouter et attribuer les événements mentionnés ci-dessus.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-HandleColumnFilterEvents-HandleColumnFilterEvents.aspx" >}}



Ces événements peuvent être utilisés pour obtenir des informations utiles sur le processus de filtrage telles que l'indice de colonne et la valeur sur laquelle le filtre doit être appliqué. Voici un extrait démontrant l'utilisation de l'événement OnBeforeColumnFilter pour récupérer l'indice de colonne et la valeur sélectionnée par l'utilisateur sur l'interface GridWeb pour le filtrage.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-HandleColumnFilterEvents.aspx-BeforeColumnFilter.cs" >}}


D'autre part, si l'exigence est d'obtenir le nombre de lignes filtrées après l'application du filtre, vous pouvez utiliser l'événement OnAfterColumnFilter comme démontré ci-dessous.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-HandleColumnFilterEvents.aspx-AfterColumnFilter.cs" >}}

{{% alert color="primary" %}} 

Consultez l'introduction à tous les [Événements de travail avec GridWeb](/cells/fr/net/aspose-cells-gridweb/working-with-gridweb-events/) ainsi que quelques détails sur la manière de gérer ces événements.

{{% /alert %}}
