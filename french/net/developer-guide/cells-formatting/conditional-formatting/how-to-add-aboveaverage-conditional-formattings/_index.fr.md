---
title: Comment ajouter un format conditionnel au dessus de la moyenne
description: Comment utiliser la bibliothèque Aspose.Cells en C# pour appliquer un format conditionnel au dessus de la moyenne. En ajustant ces critères, vous avez plus de contrôle sur l apparence des cellules.
keywords: Aspose.Cells, Formatage Conditionnel Au dessus de la Moyenne, C#, Conditionnel, Formatage
type: docs
weight: 70
url: /fr/net/how-to-add-above-average-conditional-formatting/
---

## **Scénarios d'utilisation possibles**
L'utilisation du formatage conditionnel au-dessus de la moyenne dans des outils comme Microsoft Excel ou Google Sheets est un moyen rapide et visuel de mettre en évidence des données qui se démarquent — notamment, des valeurs supérieures à la moyenne dans une plage. Voici pourquoi vous pourriez l'utiliser :
1. Identifier rapidement les tendances : Il vous aide à repérer instantanément les valeurs performantes sans calculs manuels ni balayage numérique.
1. Simplifier l'analyse des données : Vous n'avez pas besoin de calculer ou d'entrer des formules — c'est une manière automatique d'appliquer une mise en forme basée sur une logique, ce qui fait gagner du temps.
1. Améliorer l'attrait visuel : La coloration aide à rendre votre feuille de calcul plus facile à lire et plus attrayante visuellement, notamment lors de présentations.
1. Soutenir la prise de décision : Identifier rapidement les valeurs supérieures à la moyenne peut conduire à des actions, comme récompenser les meilleurs ou enquêter sur les raisons pour lesquelles certains produits surpassent les autres.

## **Comment ajouter un formatage conditionnel au-dessus de la moyenne avec Excel**
Pour ajouter un formatage conditionnel au-dessus de la moyenne dans Excel, voici comment procéder étape par étape :

1. Sélectionnez la plage de cellules à laquelle vous souhaitez appliquer le formatage. Par exemple : A1:A20.
1. Allez à l'onglet Accueil dans le ruban.
1. Cliquez sur Mise en forme conditionnelle dans le groupe Styles.
1. Survolez Règles supérieur/inferieur.
1. Cliquez sur « Au-dessus de la moyenne... »
1. Dans la boîte de dialogue qui apparaît : Elle détectera automatiquement « Mettre en forme les cellules qui sont AU-DESSUS de la moyenne ». Vous pouvez modifier le style de mise en forme en cliquant sur la liste déroulante à côté (par exemple, choisir un fond de couleur ou un format personnalisé).
1. Cliquez sur OK. Toutes les cellules de votre plage sélectionnée qui sont supérieures à la moyenne de cette plage seront mises en évidence.


## **Comment ajouter un formatage conditionnel au-dessus de la moyenne avec Aspose.Cells for .NET**

Aspose.Cells prend entièrement en charge le formatage conditionnel fourni par Microsoft Excel 2007 et versions ultérieures au format XLSX en temps réel sur les cellules. Cet exemple démontre une utilisation du formatage conditionnel au-dessus de la moyenne avec différents ensembles d'attributs.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-Formatting-Advanced-AboveAverage.cs" >}}

{{< app/cells/assistant language="csharp" >}}
