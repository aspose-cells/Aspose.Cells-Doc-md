---
title: Composant de canevas de rapport Ohal
type: docs
weight: 30
url: /fr/net/ohal-report-canvas-component/
---
{{% alert color="primary" %}}

[Rapport PDF](https://blog.aspose.com/2008/03/17/complete-excel-export-capabilities-using-apis/)

**Utilisation de Aspose.Cells dans le composant de canevas de rapport**

Robert Chilvers, 17 mars 2008

{{% /alert %}}

## **Contexte du produit**

Le composant Report Canvas permet à l'utilisateur de créer des rapports visuels basés sur un ensemble de données préchargé. L'utilisateur peut ajouter différents composants à son canevas, notamment des images, des zones de texte, des graphiques et des tableaux, puis spécifier les données et la manière dont elles doivent être agrégées. L'utilisateur peut alors réorganiser et redimensionner les objets pour les adapter à sa page. L'utilisateur peut spécifier des palettes de couleurs et enregistrer des modèles pour une utilisation future. Aspose.Cells est utilisé pour exporter tous les objets du canevas vers Excel avec les données correctes. Le composant est écrit avec VB.Net dans Visual Studio 2008.

## **Scénario d'exigences**

Nous avons sélectionné Aspose.Cells en raison de ses capacités d'exportation Excel Microsoft presque complètes. Le plus important pour nous est la possibilité d'exporter des graphiques et des tableaux, en particulier dans Microsoft Excel 2007 - ceux-ci manquaient dans d'autres composants tiers.

## **Implémentation de la solution**

Chaque objet sur le canevas de rapport a une fonction qui reçoit une instance de la feuille de calcul Aspose.Cells et s'ajoute à la feuille de calcul. Lorsque l'utilisateur demande une exportation, le classeur et les feuilles de calcul sont initialisés et chaque objet du canevas de rapport a cette fonction appelée.

## **Avantages**

Aspose.Cells nous a permis de créer le classeur Excel de manière entièrement indépendante d'Excel, puis d'enregistrer le classeur dans le format sélectionné par l'utilisateur. Cela a permis d'économiser des heures de débogage de l'interaction lors de l'utilisation de l'interopérabilité Excel et de la mise en œuvre de différentes routines pour enregistrer dans différentes versions d'Excel.

## **Mise en œuvre future**

Nous sommes susceptibles d'utiliser le Aspose.Cells pour tous les chargements et sauvegardes de fichiers Excel. Cela comprendra le chargement des modèles de données et l'exportation des résultats.

## **Conclusion**

{{% alert color="primary" %}}

Jusqu'à présent, nous n'avons eu aucun problème avec les composants Aspose.Cells et le composant devrait nous faire gagner du temps de développement à court et à long terme. Les questions d'assistance et de vente ont reçu une réponse rapide et utile.

{{% /alert %}}
