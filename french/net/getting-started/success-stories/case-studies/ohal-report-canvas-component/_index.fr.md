---
title: Composant du canevas de rapport Ohal
type: docs
weight: 30
url: /fr/net/ohal-report-canvas-component/
---

{{% alert color="primary" %}}

[Rapport PDF](https://blog.aspose.com/2008/03/17/complete-excel-export-capabilities-using-apis/)

**Utilisation d'Aspose.Cells dans le composant du canevas de rapport**

Robert Chilvers, 17 mars 2008

{{% /alert %}}

## **Contexte du Produit**

Le composant Rapport Canvas permet à l'utilisateur de créer des rapports visuels basés sur un ensemble de données pré-chargé. L'utilisateur peut ajouter différents composants à leur toile, y compris des images, des zones de texte, des graphiques et des tables. Ensuite, ils spécifient les données et comment elles doivent être agrégées. L'utilisateur peut ensuite réarranger et redimensionner les objets pour les adapter à leur page. L'utilisateur peut spécifier des palettes de couleurs et enregistrer des modèles pour une utilisation future. Aspose.Cells est utilisé pour exporter tous les objets sur la toile vers Excel avec les données correctes. Le composant est écrit avec VB.Net dans Visual Studio 2008.

## **Scénario de Besoins**

Nous avons choisi Aspose.Cells en raison de ses capacités presque complètes d'exportation vers Microsoft Excel. Ce qui est le plus important pour nous, c'est la capacité à exporter des graphiques et des tables, notamment vers Microsoft Excel 2007 - cela faisait défaut dans d'autres composants tiers.

## **Implémentation de la Solution**

Chaque objet sur la toile du rapport a une fonction qui reçoit une instance de la feuille de calcul Aspose.Cells et s'ajoute à la feuille de calcul. Lorsque l'utilisateur demande une exportation, le classeur et les feuilles de calcul sont initialisés et chaque objet sur la toile du rapport appelle cette fonction.

## **Avantages**

Aspose.Cells nous a permis de construire le classeur Excel entièrement indépendamment d'Excel, puis d'enregistrer le classeur dans le format sélectionné par l'utilisateur. Cela a permis d'économiser des heures de débogage de l'interaction lors de l'utilisation de l'interopérabilité Excel et de la mise en œuvre de différentes routines pour enregistrer dans diverses versions d'Excel.

## **Implémentation Future**

Nous sommes susceptibles d'utiliser Aspose.Cells pour le chargement et l'enregistrement de tous les fichiers Excel. Cela comprend le chargement de modèles de données et l'exportation de résultats.

## **Conclusion**

{{% alert color="primary" %}}

Jusqu'à présent, nous n'avons rencontré aucun problème avec les composants Aspose.Cells et le composant devrait nous faire gagner du temps de développement à court et long terme. Les requêtes de support et de vente ont été traitées rapidement et de manière utile.

{{% /alert %}}
