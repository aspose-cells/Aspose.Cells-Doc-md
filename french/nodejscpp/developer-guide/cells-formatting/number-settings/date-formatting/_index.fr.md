---
title: Comment formater un nombre en date
type: docs
weight: 10
url: /fr/nodejs-cpp/format-number-to-date/
description: Cet article expliquera comment formater un nombre en date en utilisant l API Aspose.Cells for Node.js via C++.
keywords: formater un nombre en date, paramètres de la cellule, formater un nombre en date, paramètres de date, format de date.
---

## **Scénarios d'utilisation possibles**
Formater des nombres en dates dans Excel (ou tout autre logiciel de tableur) est important pour plusieurs raisons, notamment lorsque vous travaillez avec des données comprenant des informations temporelles ou de planification. Voici pourquoi le formatage des nombres en dates est avantageux :

1. Interprétation correcte des valeurs de date : dans Excel, les dates sont stockées sous forme de numéros de série (par exemple, 1 représente le 1er janvier 1900, et 44210 représente le 6 septembre 2021). Si ces nombres ne sont pas formatés comme des dates, les utilisateurs pourraient voir des nombres sans signification au lieu de dates reconnaissables. Les formater correctement permet à Excel de les afficher en tant que véritables dates (par exemple, 06/09/2021 au lieu de 44210).
1. Simplifie les calculs liés au temps : Excel peut effectuer de nombreux calculs en utilisant des dates, comme calculer le nombre de jours entre deux dates, ajouter ou soustraire des jours, ou déterminer le jour de la semaine. Si les nombres ne sont pas formatés comme des dates, Excel ne pourra pas effectuer ces opérations efficacement. Par exemple, si vous voulez connaître le nombre de jours entre le 01/09/2023 et le 01/10/2023, Excel peut le calculer facilement si les nombres sont en format de date.
1. Garantit la cohérence : lorsque toutes les valeurs liées aux dates sont formatées correctement, cela garantit que toutes les dates apparaissent dans un style uniforme et lisible. Cette cohérence est importante dans les rapports commerciaux, les calendriers de projets et les bases de données où la cohérence des dates est cruciale.
Différentes régions utilisent différents formats de date (par exemple, MM/JJ/AAAA aux États-Unis contre JJ/MM/AAAA dans de nombreux autres pays), donc le formatage aide à garantir que les dates sont interprétées correctement.
1. Améliore la lisibilité : les dates présentées dans un format standard (par exemple, 01/01/2024) sont plus faciles à lire que des numéros de série bruts comme 45000. Un format de date approprié rend votre feuille de calcul plus conviviale et évite la confusion. Ceci est particulièrement important dans des scénarios tels que la planification, les chronologies, la gestion d'événements ou les données historiques.
1. Facilite le tri et le filtrage : lorsque les dates sont formatées correctement, Excel les reconnaît comme de véritables dates, ce qui facilite le tri ou le filtrage des données de manière chronologique. Par exemple, vous pouvez trier une liste d'événements par date ou filtrer une plage de données pour n’afficher que les enregistrements entre deux dates spécifiques. Sans un format de date approprié, le tri pourrait s’effectuer en fonction du nombre brut au lieu de vraies dates du calendrier.
1. Permet l’utilisation des fonctions de date : Excel propose une gamme étendue de fonctions de date puissantes, telles que : TODAY(), DATEDIF(), WORKDAY(), YEAR(), MONTH(), DAY(). Ces fonctions nécessitent que les dates soient correctement formatées pour des calculs précis.
1. Supporte la visualisation (graphes/chronologies) : les dates formatées correctement peuvent être utilisées pour créer des graphiques où le temps est un axe clé. Par exemple, dans un graphique de chronologie, Excel a besoin de dates dans un format reconnu pour tracer les événements avec précision dans le temps. Des nombres mal formatés ou non formatés peuvent entraîner des graphiques qui n’ont pas de sens ou reflètent des informations incorrectes.
1. Empêche la mauvaise interprétation : les nombres bruts peuvent facilement être mal interprétés. Par exemple, 44210 pourrait être lu comme une valeur numérique générale, mais lorsqu’il est formaté en date, il est clair qu’il représente le 6 septembre 2021. Des dates correctement formatées permettent d’éviter les erreurs d’interprétation des données.
1. Facilite la saisie de données : lorsque les cellules sont formatées comme des dates, les utilisateurs sont incités à entrer des données dans un format de date valide, ce qui évite les erreurs de saisie et garantit que les valeurs de date sont correctement capturées.
1. Crucial pour la planification et le suivi : dans toute situation impliquant la planification, le suivi ou les délais (comme la gestion de projet, la prévision financière ou les rapports sensibles au temps), le formatage des nombres en dates est essentiel pour la précision et la compréhension. Il permet une meilleure planification et exécution.


## **Comment formater un nombre en date dans Excel**
Pour formater un nombre en date dans Excel, suivez ces étapes :

### **Utilisation du ruban (onglet Accueil)**
1. Sélectionnez les cellules contenant les nombres que vous souhaitez formater en dates.
1. Allez dans l'onglet Accueil du ruban.
1. Dans le groupe Nombre, cliquez sur la flèche déroulante dans la boîte Format de nombre (qui peut afficher "Général" ou "Nombre" par défaut).
1. Choisissez Date courte ou Date longue dans la liste déroulante. Date courte : Affiche la date dans un format concis, par exemple, JJ/MM/AAAA (format international) ou MM/JJ/AAAA (format américain). Date longue : Affiche la date dans un format plus descriptif, par exemple, lundi 1er janvier 2024.
<br>
<img src="1.png" width=60% />

### **Utilisation de la boîte de dialogue Format de cellule**
1. Sélectionnez les cellules que vous souhaitez formater.
1. Faites un clic droit sur les cellules sélectionnées et choisissez Format de cellule, ou appuyez sur Ctrl + 1 (Windows) ou Cmd + 1 (Mac).
1. Dans la boîte de dialogue Format de cellule, allez à l'onglet Nombre.
1. Dans la liste à gauche, sélectionnez Date.
1. Choisissez le format de date souhaité dans la liste à droite (par exemple, JJ/MM/AA, MM/JJ/AA, ou formats personnalisés).
<br>
<img src="2.png" width=60% />
1. Cliquez sur OK pour appliquer le format de date.

## **Comment formater un nombre en date dans Aspose.Cells**

Pour formater des nombres en date dans la bibliothèque Aspose.Cells for Node.js via C++ pour travailler avec des fichiers Excel, vous pouvez appliquer le format de date aux cellules de manière programmatique. Voici comment faire avec Aspose.Cells for Node.js via C++ :

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-FormatNumberToDate.js" >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
