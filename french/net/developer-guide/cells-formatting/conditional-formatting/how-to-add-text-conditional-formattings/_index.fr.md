---
title: Comment ajouter une mise en forme conditionnelle de texte
description: Comment utiliser la bibliothèque Aspose.Cells en C# pour appliquer une mise en forme conditionnelle de texte. En ajustant ces critères, vous controllez davantage l apparence des cellules.
keywords: Aspose.Cells, Mise en forme conditionnelle de texte, C#, Conditionnelle, Mise en forme
type: docs
weight: 70
url: /fr/net/how-to-add-text-conditional-formatting/
---

## **Scénarios d'utilisation possibles**
L'utilisation de la mise en forme conditionnelle basée sur du texte dans les feuilles de calcul est utile pour mettre en évidence les cellules répondant à des critères textuels spécifiques. Cela peut améliorer l'analyse des données et faciliter la recherche d'informations clés dans un grand ensemble de données. Voici quelques raisons d'utiliser la mise en forme conditionnelle de texte :

1. Mettre en évidence un texte spécifique : Vous pouvez appliquer une mise en forme en fonction de mots, phrases ou caractères spécifiques. Par exemple, vous pourriez vouloir mettre en surbrillance toutes les cellules contenant le mot "Urgent" ou "Terminé" pour différencier facilement les tâches d’un projet.
1. Identifier les motifs ou tendances : Si vous travaillez avec des catégories ou statuts (comme "Élevé", "Moyen", "Faible"), la mise en forme conditionnelle de texte peut visuellement distinguer entre eux, facilitant le suivi de l'avancement ou la priorisation des tâches.
1. Alertes d’erreur ou de saisie de données : La mise en forme du texte peut signaler des entrées incohérentes ou erronées, comme des mots mal orthographiés, du texte incomplet ou des valeurs incorrectes. Cela est particulièrement utile dans des ensembles de données avec beaucoup de texte.
1. Amélioration de la lisibilité : La codification par couleur du texte ou la modification de son style (gras, italique, etc.) aide à faire ressortir les informations importantes, améliorant la lisibilité globale de votre feuille.
1. Retour d'information dynamique : Vous pouvez mettre en place des règles qui ajustent automatiquement la mise en forme lorsque le texte correspond à certaines conditions. Cela évite de devoir mettre à jour manuellement la mise en forme à mesure que les données changent.

En résumé, la mise en forme conditionnelle de texte vous aide à repérer rapidement les informations pertinentes, les erreurs et les tendances, ce qui en fait un outil puissant pour gérer et interpréter des données textuelles.

## **Comment ajouter une mise en forme conditionnelle de texte avec Excel**
Pour ajouter une mise en forme conditionnelle basée sur du texte dans Excel, suivez ces étapes :

1. Sélectionnez la plage de cellules : Mettez en surbrillance les cellules où vous souhaitez appliquer la mise en forme conditionnelle.
1. Ouvrez le menu Mise en forme conditionnelle : Allez à l'onglet Accueil dans le ruban Excel. Cliquez sur Mise en forme conditionnelle dans le groupe "Styles".
1. Choisissez “Nouvelle règle” : Dans le menu déroulant, sélectionnez Nouvelle règle.
1. Sélectionnez “Mettre en forme uniquement les cellules qui contiennent” : Dans la boîte de dialogue Nouvelle règle de mise en forme, choisissez Mettre en forme uniquement les cellules qui contiennent sous la section "Type de règle".
1. Définissez les critères de la règle : Dans la section "Mettre en forme les cellules avec", choisissez Texte spécifique dans le menu déroulant. Sélectionnez soit contenant, commence par ou se terminant par, selon la condition que vous souhaitez appliquer. Entrez le texte que vous souhaitez mettre en forme (par exemple un mot spécifique comme "Urgent" ou "Terminé").
1. Choisissez la mise en forme : Cliquez sur le bouton Mettre en forme. Dans la boîte de dialogue Format de cellules, vous pouvez sélectionner la couleur de police, la couleur de remplissage ou d'autres options de mise en forme selon vos préférences.
1. Appliquez la règle : Une fois que vous avez défini votre mise en forme souhaitée, cliquez sur OK pour appliquer la règle. Cliquez de nouveau sur OK dans la boîte de dialogue Nouvelle règle de mise en forme pour la fermer.
1. Visualisez les résultats : Les cellules contenant le texte spécifié auront désormais la mise en forme appliquée, ce qui facilite la détection des informations pertinentes.


## **Comment ajouter une mise en forme conditionnelle de texte avec Aspose.Cells for .NET**

Aspose.Cells supporte pleinement la mise en forme conditionnelle fournie par Microsoft Excel 2007 et versions ultérieures en format XLSX sur des cellules à l'exécution. Ces exemples illustrent des exercices pour des types avancés de mise en forme conditionnelle, y compris BeginsWith, ContainsBlank, ContainsText, etc.

### **Mettre en forme la cellule lorsque la valeur commence par un texte spécifié**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-Formatting-Advanced-Text-BeginsWith.cs" >}}

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-Formatting-Advanced-Text.cs" >}}
### **Formatage de cellule lorsque la valeur contient une case vide**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-Formatting-Advanced-Text-ContainsBlank.cs" >}}

### **Formatage de cellule lorsque la valeur contient des erreurs**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-Formatting-Advanced-Text-ContainsErrors.cs" >}}

### **Formatage de cellule lorsque la valeur contient un texte spécifié**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-Formatting-Advanced-Text-ContainsText.cs" >}}

### **Formatage de cellule lorsque la valeur contient des valeurs en double**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-Formatting-Advanced-Text-DuplicateValues.cs" >}}

### **Formatage de cellule lorsque la valeur se termine par un texte spécifié**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-Formatting-Advanced-Text-EndsWith.cs" >}}

### **Formatage de cellule lorsque la valeur ne contient pas une case vide**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-Formatting-Advanced-Text-NotContainsBlank.cs" >}}

### **Formatage de cellule lorsque la valeur ne contient pas d'erreurs**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-Formatting-Advanced-Text-NotContainsErrors.cs" >}}

### **Formatage de cellule lorsque la valeur ne contient pas un texte spécifié**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-Formatting-Advanced-Text-NotContainsText.cs" >}}

### **Formatage de cellule lorsque la valeur contient des valeurs uniques**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-Formatting-Advanced-Text-UniqueValues.cs" >}}

{{< app/cells/assistant language="csharp" >}}
