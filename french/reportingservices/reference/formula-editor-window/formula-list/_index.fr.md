---
title: Liste de formules
type: docs
weight: 10
url: /fr/reportingservices/formula-list/
---
**Champs de rapport**

|**Définir le nom** |**Nom de la formule**|**Description**|
|:- |:- |:- |
| Champs globaux| Temps d'exécution| La date et l'heure auxquelles le rapport a commencé à s'exécuter.|
|| ReportServerUrl| URL du serveur de rapports sur lequel le rapport est exécuté.|
|| NomRapport|Nom du rapport tel qu'il est stocké dans la base de données du serveur de rapports.|
|| RapportDossier| Chemin d'accès complet au dossier contenant le rapport. Cela n'inclut pas l'URL du serveur de rapports.|
| Utilisateur| Identifiant d'utilisateur| ID de l'utilisateur qui exécute le rapport.|
|| Langue| ID de langue de l'utilisateur exécutant le rapport.|
**Champs de rapport**

|**Définir le nom**|**Description**|
|:- |:- |
| Paramètres| La collection Parameters contient les paramètres de rapport dans le rapport. Les paramètres peuvent être transmis aux requêtes, utilisés dans des filtres ou utilisés dans d'autres fonctions qui modifient l'apparence du rapport en fonction du paramètre.|
| Des champs| La collection Fields contient les champs de l'ensemble de données actuel.|
| Base de données||
**Les opérateurs**
Les opérateurs arithmétiques sont utilisés pour combiner des nombres, des variables numériques, des champs numériques et des fonctions numériques pour obtenir un autre nombre. Les opérateurs de comparaison sont généralement utilisés pour comparer les opérandes d'une condition dans une structure de contrôle telle qu'une instruction If. Les opérateurs booléens sont généralement utilisés avec des opérateurs de comparaison pour générer des conditions pour les structures de contrôle.

|**Définir le nom**|**Nom de la formule**|**Description**|
|:- |:- |:- |
| Arithmétique|^ | Exponentiation, par exemple 2^3.|
||* | Multiplication, par exemple 2*3.|
||/ | Division, par exemple 2/3.|
||\\\ | Division entière, par exemple 2\\\3.|
|| Mode| Module, par exemple 4 Mod 3.|
||+ | Addition, par exemple 4 + 3.|
||- | Soustraction, par exemple 4 – 3.|
| Comparaison|< | Moins de, par exemple 4< 3 false. |
||<= | Inférieur ou égal, par exemple 4<= 3 false. |
||> | Supérieur à, par exemple 4 > 3 vrai.|
||>= | Supérieur ou égal, par exemple 4 >= 3 vrai.|
||= | Égal, par exemple 4 = 3 faux.|
||<> | Pas égal, par exemple 4<> 3 vrai.|
|| Comme|Compare une chaîne à un modèle. Par exemple result = string Like pattern.|
|| Est| Compare deux variables de référence d'objet, par exemple asp Is aspose.|
| Enchaînement|& | Génère une concaténation de chaîne de deux expressions.|
||+ | Additionne deux nombres ou renvoie la valeur positive d'une expression numérique. Peut également être utilisé pour concaténer deux expressions de chaîne.|
| Logique/au niveau du bit| Et| Effectue une conjonction logique sur deux expressions booléennes ou une conjonction au niveau du bit sur deux expressions numériques.|
|| Pas| Effectue une négation logique sur une expression booléenne ou une négation au niveau du bit sur une expression numérique.|
|| Ou alors| Effectue une disjonction logique sur deux expressions booléennes ou une disjonction au niveau du bit sur deux expressions numériques.|
|| Xou| Effectue une exclusion logique sur deux expressions booléennes ou une exclusion au niveau du bit sur deux expressions numériques.|
|| Et aussi| Effectue une conjonction logique de court-circuit sur deux expressions.|
|| Ou sinon|Effectue une disjonction logique inclusive en court-circuit sur deux expressions.|
| Décalage de bits|>> | Effectue un décalage arithmétique vers la gauche sur un motif binaire.|
||<< | Effectue un décalage arithmétique vers la droite sur un motif binaire.|

