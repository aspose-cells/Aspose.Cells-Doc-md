---
title: Comment insérer le symbole de la coche
type: docs
weight: 10
url: /fr/net/how-to-insert-tick-symbol-to-excel/
description: Cet article présente comment insérer le symbole de la coche Aspose.Cells for .NET API.
keywords: Copiez collez le symbole de la coche, utilisez le menu Symbol ou Insertion, entrez un code Alt, utilisez AutoCorrect ou les raccourcis, utilisez le panneau d emoji/symbole, ajoutez une coche dans une case / case à bulletin.
---

## **Scénarios d'utilisation possibles**
Insérer un symbole de coche (✓) peut servir à diverses fins en fonction du contexte. Voici quelques raisons courantes pour lesquelles quelqu'un pourrait insérer un symbole de coche :

1. **Indiquer l'achèvement ou la réussite** : Il est couramment utilisé pour marquer qu'une tâche est terminée ou pour confirmer que quelque chose a été réalisé avec succès. Par exemple, dans une liste de choses à faire, vous pouvez utiliser une coche pour montrer qu'une tâche a été accomplie.

2. **Listes de contrôle et enquêtes** : Dans les sondages, formulaires ou listes de contrôle, un symbole de coche est utilisé pour indiquer les options sélectionnées, ou pour montrer qu'un élément particulier répond aux critères requis.

3. **Approbation ou validation** : Un symbole de coche peut indiquer l'approbation ou la validation d'une action, décision ou document. Il est souvent utilisé dans un contexte formel ou semi-formel.

4. **Esthétique du design** : Dans certains cas, le symbole de coche est simplement utilisé pour son attrait visuel ou comme partie d'un élément de design, comme dans les logos, infographies ou présentations.

5. **Réponse positive ou correcte** : Il peut être utilisé dans des supports éducatifs pour mettre en évidence des réponses correctes ou le résultat positif de quelque chose.

6. **Indiquer l'accord ou le consentement** : Une coche peut représenter l'accord, le consentement ou la reconnaissance d'une déclaration ou condition.


## **Comment insérer le symbole de coche dans Excel**
Voici un guide clair sur la façon d'insérer un symbole de coche (✓ ou ✔) dans Excel, en utilisant plusieurs méthodes :

### Utilisation du menu Symboles

1. Cliquez sur la cellule où vous souhaitez la coche.
2. Allez dans l'onglet Insertion du ruban.
3. Cliquez sur Symbole (tout à droite).
4. Dans la boîte de dialogue Symboles : Choisissez la police (Wingdings ou Segoe UI Symbol), Recherchez (✔ (code caractère 252) ou ✓ (code caractère 2713))
5. Cliquez sur Insérer, puis Fermer.

### Utilisation des raccourcis clavier
1. Code Alt (Windows uniquement) : Maintenez Alt et tapez le code avec le pavé numérique : Alt + 0252 (✔) — police Wingdings, Alt + 10003 (✓) — Segoe UI Symbol
2. Après avoir tapé, relâchez Alt pour insérer le symbole.

### Copier et Coller
Vous pouvez copier un symbole de coche et le coller dans n'importe quelle cellule Excel : ✓ (U+2713) et ✔ (U+2714). Il suffit de copier d'ici et de coller directement dans une cellule.

### Utilisation de la mise en forme conditionnelle avec une formule
Vous pouvez créer automatiquement des marques d'optation avec des formules et la mise en forme conditionnelle :

1. Entrez une formule comme : =SI(A1="oui"; "✓"; "").
2. Personnalisez la taille de la police et l'alignement pour l'apparence.

### Insertion avec la fonction CHAR (police Wingdings)
Si vous utilisez Wingdings : =CHAR(252) → ✔, Ensuite changez la police de la cellule en Wingdings pour qu'elle s'affiche correctement.

### Insérer à l'aide de cases à cocher Excel (optionnel)

Pour des cases à cocher interactives :
1. Allez à l'onglet Développeur (activez-le dans Options si caché).
2. Cliquez sur Insertion → Contrôles de formulaire → Case à cocher.
3. Positionnez la case à cocher dans la feuille.

## **Comment insérer le symbole de coche dans Aspose.Cells for .NET**
Pour insérer un symbole de coche (✓) dans une cellule en utilisant Aspose.Cells for .NET, vous pouvez utiliser les méthodes suivantes pour répondre aux exigences.

1. Ajoutez le symbole de coche en utilisant l'Unicode (U+2713).
2. Ajoutez le symbole de coche en utilisant une police de symboles (Wingdings 2 ou Webdings).
3. Ajoutez le symbole de coche en utilisant une image.
4. Ajoutez le symbole de coche en utilisant le contrôle case à cocher.
5. Ajoutez le symbole de coche à l'aide de formats conditionnels.
6. Ajoutez le symbole de coche à l'aide d'une formule.

Voici un exemple simple de comment insérer un symbole de coche dans une cellule en utilisant Aspose.Cells for .NET :

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Shapes-insert-tick-symbol.cs" >}}

## **Résultat de sortie**

La capture d'écran suivante montre les coches créées par Aspose.Cells for .NET dans le fichier Excel de sortie.
<br>
<img src="tick_result.png" width=70% />

{{< app/cells/assistant language="csharp" >}}
