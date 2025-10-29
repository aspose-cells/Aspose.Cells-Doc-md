---
title: Comment formater un nombre en devise avec Golang via C++
linktitle: Comment formater un nombre en devise
type: docs
weight: 10
url: /fr/go-cpp/format-number-to-currency/
description: Cet article expliquera comment formater un nombre en devise en utilisant l API Aspose.Cells for C++.
keywords: formater le nombre en devise, paramètres des cellules, formatter le nombre en devise, paramètres de devise, format de devise.
---

## **Scénarios d'utilisation possibles**
Le formatage des nombres en devise dans Excel est important pour plusieurs raisons, en particulier lors du traitement de données financières. Voici pourquoi le formatage en devise est avantageux :

1. **Clarifie les valeurs financières** : le formatage d'un nombre en devise indique clairement que la valeur représente de l'argent. Par exemple, au lieu de voir 1000, ce qui pourrait signifier n'importe quoi, $1 000 indique clairement que la valeur est un montant monétaire.
1. **Inclut les symboles de devise** : lorsqu'on traite des devises internationales ou multiples, le formatage des nombres avec le symbole de devise approprié (par ex., $, €, £) clarifie le type de devise utilisée, réduisant la confusion dans les rapports ou transactions financières multi-nationale.
1. **Améliore la présentation professionnelle** : des valeurs en devise bien formatées apparaissent polies et professionnelles, ce qui est particulièrement important pour les rapports, présentations et documents commerciaux. $10 000,00 paraît plus crédible et organisé qu'un simple 10000.
1. **Améliore la lisibilité** : le formatage en devise ajoute des virgules comme séparateurs de milliers et des décimales, ce qui rend les grands nombres plus faciles à lire. Par exemple, 1000000 devient $1 000 000,00, ce qui est plus lisible et plus facile à comprendre en un coup d'œil.
1. **Assure la cohérence** : en appliquant un formatage en devise cohérent, vous garantissez que toutes les valeurs monétaires dans un ensemble de données sont affichées dans le même format. Cette cohérence est importante pour l'exactitude financière et la communication professionnelle, surtout dans de grands fichiers contenant de nombreux nombres.
1. **Montre la précision** : le formatage en devise inclut généralement deux décimales, permettant de voir facilement les montants monétaires exacts. Par exemple, $100,50 est clairement différent de $100,00, ce qui est important dans les rapports financiers où la précision a de l'importance.
1. **Simplifie les calculs financiers** : lors de réalisations de calculs financiers (comme additionner des totaux ou faire la moyenne des coûts), le formatage en devise aide Excel et les utilisateurs à comprendre que les données sont en termes monétaires. Il aide Excel à appliquer un formatage approprié dans les formules et fonctions, assurant la cohérence des résultats.
1. **Réduit les mauvaises interprétations** : sans formatage en devise, les nombres pourraient être mal interprétés comme des valeurs numériques générales plutôt que des montants d'argent. Par exemple, 500 pourrait être confondu avec un nombre d'articles ou d'unités, tandis que $500,00 représente clairement un montant financier.
1. **Fonctionne avec les fonctionnalités comptables** : le formatage en devise s'aligne bien avec les fonctions comptables dans Excel, telles que les bilans ou les rapports de flux de trésorerie. Il facilite l'utilisation des valeurs dans les états financiers où l'argent est le principal enjeu.
<br>
En résumé, le formatage des nombres en devise aide à distinguer les valeurs monétaires des autres types de nombres, augmente la clarté et facilite l'interprétation des données, notamment dans des contextes financiers.

## ** Comment formater le nombre en devise dans Excel**
 Pour formater les nombres en devise dans Excel, suivez ces étapes :

### ** Utiliser l'option de format de devise**
1. Sélectionnez les cellules que vous souhaitez formater en devise.
1. Allez à l'onglet Accueil dans le ruban.
1. Dans le groupe Numéro, cliquez sur la flèche déroulante à côté de la boîte de format numérique (celle-ci peut afficher "Général" par défaut).
<br>
<img src="1.png" width=60% />
1. Choisissez Devise dans la liste.

### **Utilisation de la boîte de dialogue Format de cellule**
1. Sélectionnez les cellules que vous souhaitez formater.
1. Faites un clic droit sur les cellules sélectionnées et choisissez Format Cells pour ouvrir la boîte de dialogue Format Cells.
1. Dans l'onglet Nombre, sélectionnez Monnaie dans la liste à gauche.
<br>
<img src="2.png" width=60% />
1. Vous pouvez personnaliser ce qui suit : Décimales, Symbole, Nombres négatifs.
1. Cliquez sur OK pour appliquer le formatage.

## **Comment formater un nombre en devise dans Aspose.Cells**

Pour formater les nombres en devise dans la bibliothèque Aspose.Cells for C++ pour travailler avec des fichiers Excel, vous pouvez appliquer un format monétaire aux cellules par programmation. Voici comment faire en utilisant C++ avec Aspose.Cells :

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CurrencyFormatting.go" >}}
