---
title: Comment formater un nombre selon le format linguistique local
type: docs
weight: 10
url: /fr/net/how-to-format-number-to-local-language-format/
description: Cet article présente comment formater un nombre selon le format linguistique local Aspose.Cells for .NET API.
keywords: Convertir un nombre en un format de langue locale, Transformer un chiffre en format de langue locale, Changer un nombre en son format de langue locale correspondant, Formater une valeur numérique en format de langue locale, Exprimer un nombre en format de langue locale, Formater le nombre dans le format de la langue locale.
---

## **Scénarios d'utilisation possibles**

Le formatage des nombres dans Excel selon les formats locaux est essentiel pour garantir une compréhension claire, une interprétation précise et une présentation professionnelle dans différentes régions et cultures.

1. **Adaptation culturelle et régionale** : Différentes régions utilisent divers formats de nombres pour les décimales, les séparateurs de milliers, les monnaies et les dates. 
1. **Professionnalisme et clarté** : L'utilisation de formats locaux améliore l'apparence professionnelle de vos feuilles de calcul. Cela montre une attention aux détails et une considération pour le public, ce qui est crucial dans les rapports, les états financiers et les données partagées avec les parties prenantes.
1. **Cohérence dans l'affichage des données** : Le formatage local garantit la cohérence lors de la collaboration avec des équipes ou des clients de différentes régions. Il prévient les erreurs pouvant survenir lors de l'interprétation des données, comme la confusion entre séparateurs décimaux.
1. **Compatibilité avec les systèmes externes** : Lors de l'exportation de données vers d'autres formats (par exemple, CSV), le formatage local peut aider à maintenir l'intégrité des données.
1. **Accessibilité et convivialité** : Le formatage local rend les données plus accessibles aux utilisateurs peu familiers avec les formats étrangers. Par exemple, afficher les dates au format "JJ/MM/YYYY" (courant au Royaume-Uni) contre "MM/JJ/YYYY" (courant aux États-Unis) évite toute confusion.
1. **Validation et précision des données** : Un formatage incorrect peut entraîner des erreurs de calcul. Par exemple, si un nombre est mal interprété en raison de problèmes de séparateur décimal, les formules peuvent produire des résultats erronés. L'utilisation de formats locaux garantit que les données saisies par les utilisateurs sont conformes aux standards régionaux, réduisant ainsi le risque d'erreurs lors de la saisie ou de l'analyse des données.

## **Comment formater un nombre en format de langue locale dans Excel**

Pour formater des nombres en format de langue locale dans Excel, vous pouvez utiliser diverses fonctionnalités et fonctions intégrées qui s'adaptent aux paramètres régionaux. 

1. **Utilisez les paramètres de localisation intégrés d'Excel** : Accédez à Fichier > Options > Paramètres régionaux (ou similaire, selon votre version d'Excel). Sélectionnez la langue / région souhaitée (par exemple, allemand pour les séparateurs décimaux par la virgule, anglais pour le point). Les valeurs et formules existantes seront automatiquement converties au nouveau format.
1. **Utilisez la fonction TEXTE pour un formatage localisé personnalisé** : La fonction TEXTE peut forcer le formatage des nombres selon les modèles spécifiques à la région, utile pour afficher des numéros de téléphone ou des devises sans modifier les paramètres globaux. Syntaxe : =TEXTE(valeur, "code_de_format")
1. **Gestion programmée (VBA/APIs)** : Pour les développeurs utilisant VBA, vous pouvez utiliser NumberFormat avec des chaînes de format en anglais américain (par exemple, "#.##"). Excel s’adaptera automatiquement aux paramètres régionaux de l'utilisateur. Évitez NumberFormatLocal à moins d’avoir besoin explicitement de chaînes de format spécifiques à la région.
1. **Écraser les séparateurs système pour des cas spécifiques** : Si le formatage localisé se comporte de façon inattendue (par exemple, en raison de mises à jour Windows affectant les séparateurs), vous pouvez surcharger manuellement les paramètres par défaut : dans les options d'Excel, décochez « Utiliser les séparateurs système » et définissez manuellement les séparateurs décimal et de milliers.
1. **Formater le nombre en utilisant un format personnalisé** : Faites un clic droit sur la cellule, sélectionnez 'Format de cellule', puis trouvez 'Nombre' -> 'Personnalisé' et définissez le type de nombre personnalisé souhaité. En prenant l'exemple de la configuration des formats numériques personnalisés dans un environnement chinois.
<br>
<img src="1.png" width=60% />


## **Comment formater un nombre en format de langue locale dans Aspose.Cells for .NET**

Pour formater des nombres en format de langue locale dans Aspose.Cells for .NET, vous pouvez utiliser l’objet `Style` associé à une cellule ou une plage de cellules. L’objet `Style` vous permet de définir diverses options de mise en forme, y compris le format numérique personnalisé. 

Voici un exemple basique de comment appliquer un format numérique en langue locale à une cellule dans Aspose.Cells for .NET :

1. **Référence Aspose.Cells** : Assurez-vous que Aspose.Cells for .NET est référencé dans votre projet. Vous pouvez l'obtenir via NuGet ou le site Aspose.

2. **Créer ou ouvrir un classeur** : Commencez par créer un nouveau classeur ou ouvrir un classeur existant.

3. **Accéder à la cellule souhaitée** : Identifier et accéder à la ou aux cellules que vous souhaitez formater.

4. **Appliquer un format numérique personnalisé** : Définissez le format numérique de l'objet style de la cellule sur un format numérique en langue chinoise.

4. **Code exemple** : Voici un extrait de code illustrant ces étapes.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-Formatting-FormatNumber-To-LocalLanguageFormat.cs" >}}

## **Sortie générée par l'exemple de code**
Voici le résultat PDF du code d'exemple ci-dessus.
<br>
<img src="2.png" width=60% />

{{< app/cells/assistant language="csharp" >}}
