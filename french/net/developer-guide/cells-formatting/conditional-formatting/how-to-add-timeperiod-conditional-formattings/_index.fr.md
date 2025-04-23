---
title: Comment ajouter un formatage conditionnel pour les périodes de temps
description: Comment utiliser la bibliothèque Aspose.Cells en C# pour appliquer un formatage conditionnel pour les périodes de temps. En ajustant ces critères, vous avez plus de contrôle sur l apparence et la présentation des cellules.
keywords: Aspose.Cells, Formatage conditionnel pour les périodes de temps, C#, Conditionnel, Formatage
type: docs
weight: 70
url: /fr/net/how-to-add-time-periods-conditional-formatting/
---

## **Scénarios d'utilisation possibles**
L'utilisation du formatage conditionnel pour les périodes de temps dans Excel est très utile lorsque vous travaillez avec des dates — cela vous aide à suivre et à gérer visuellement rapidement les données liées au temps.
1. Aperçu instantané des données basées sur le temps : mettez en évidence rapidement des tâches d'aujourd'hui, des ventes du mois dernier, des échéances à venir, des rendez-vous de la semaine prochaine.
1. Meilleur gestion du temps : vous aide à respecter les dates limites, les événements ou les éléments expirants. Idéal pour les chronologies de projet, les factures ou les emplois du temps.
1. Mises à jour automatiques : se met à jour dynamiquement. Si la date d'aujourd'hui change, Excel mettra à jour le formatage sans que vous ayez à intervenir.

1. Clarté visuelle : met en évidence les informations sensibles au temps à l'aide de couleurs ou de styles en gras — afin qu'elles ne soient pas manquées.

## **Comment ajouter un formatage conditionnel pour les périodes de temps en utilisant Excel**
Voici comment vous pouvez ajouter un formatage conditionnel pour les périodes de temps dans Excel — très utile pour mettre en évidence des dates comme aujourd'hui, la semaine dernière, le mois prochain, etc.

Étapes pour ajouter un formatage conditionnel pour les périodes de temps :
1. Sélectionnez la plage de cellules de date que vous souhaitez formater. Exemple : A2:A50.
1. Allez à l'onglet Accueil dans le ruban.
1. Cliquez sur Mise en forme conditionnelle dans le groupe Styles.
1. Survolez les règles de mise en surbrillance des cellules.
1. Cliquez sur Une date apparaissant...
1. Dans la boîte de dialogue qui apparaît : utilisez le menu déroulant pour sélectionner une période (Aujourd'hui, Hier, Demain, 7 derniers jours, La semaine dernière, Le mois prochain, etc.).
1. Choisissez le format (par défaut, remplissage rouge clair avec texte rouge foncé, ou cliquez sur Format personnalisé pour choisir le vôtre).
1. Cliquez sur OK.


## **Comment ajouter un formatage conditionnel pour les périodes de temps en utilisant Aspose.Cells for .NET**

Aspose.Cells prend en charge entièrement le formatage conditionnel fourni par Microsoft Excel 2007 et les versions ultérieures au format XLSX sur les cellules en temps réel. Cet exemple démontre un exercice de formatage conditionnel pour les périodes de temps avec différents jeux d'attributs.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-Formatting-Advanced-TimePeriod.cs" >}}

{{< app/cells/assistant language="csharp" >}}
