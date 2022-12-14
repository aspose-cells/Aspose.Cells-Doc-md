---
title: Gérer les événements secondaires du serveur de filtre de colonne
type: docs
weight: 90
url: /fr/net/handle-column-filter-server-side-events/
---
{{% alert color="primary" %}} 

Le filtrage des données est probablement la fonctionnalité Excel la plus largement utilisée qui vous permet de filtrer les données en fonction de critères spécifiques. Les données filtrées affichent uniquement les lignes qui remplissent la condition en masquant les lignes qui ne remplissent pas les critères.
Le composant Aspose.Cells.GridWeb offre la possibilité d'effectuer le filtrage des données à l'aide de son interface. Afin d'étendre ses capacités, le composant Aspose.Cells.GridWeb fournit également deux événements qui peuvent servir de rappel au mécanisme de filtrage effectué via l'interface utilisateur GridWeb.

{{% /alert %}} 
## **Gestion des événements côté serveur lors de l'application du filtre de colonne**
Il y a deux événements principaux comme détaillé ci-dessous.

1. OnBeforeColumnFilter : se déclenche avant que le filtre ne soit appliqué sur une colonne.
1. OnAfterColumnFilter : se déclenche après l'application du filtre sur une colonne.

Voici le script ASPX du composant Aspose.Cells.GridWeb pour ajouter et affecter les événements susmentionnés.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-HandleColumnFilterEvents-HandleColumnFilterEvents.aspx" >}}



Ces événements peuvent être utilisés pour obtenir des informations utiles sur le processus de filtrage, telles que l'index de colonne et la valeur sur laquelle le filtre doit être appliqué. Voici l'extrait de code illustrant l'utilisation de l'événement OnBeforeColumnFilter pour récupérer l'index de colonne et la valeur que l'utilisateur a sélectionnés sur l'interface utilisateur GridWeb pour le filtrage.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-HandleColumnFilterEvents.aspx-BeforeColumnFilter.cs" >}}


D'autre part, si l'exigence est d'obtenir le nombre de lignes filtrées après l'application du filtre, vous pouvez utiliser l'événement OnAfterColumnFilter comme illustré ci-dessous.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-HandleColumnFilterEvents.aspx-AfterColumnFilter.cs" >}}

{{% alert color="primary" %}} 

 Vérifiez l'introduction à tous[Utilisation des événements GridWeb](/cells/fr/net/working-with-gridweb-events/) ainsi que quelques détails sur la façon de gérer ces événements.

{{% /alert %}}
