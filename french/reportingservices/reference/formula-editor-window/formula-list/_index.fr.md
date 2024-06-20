---
title: Liste de formules
type: docs
weight: 10
url: /fr/reportingservices/formula-list/
---

**Champs de rapport**

|**Nom de l'ensemble** |**Nom de la formule**|**Description**|
| :- | :- | :- |
|Champs globaux |Temps d'exécution |La date et l'heure de début de l'exécution du rapport. |
| |URL de ReportServer |L'URL du serveur de rapports sur lequel le rapport est en cours d'exécution. |
| |Nom du rapport |Le nom du rapport tel qu'il est stocké dans la base de données du serveur de rapports. |
| |Dossier du rapport |Le chemin complet vers le dossier contenant le rapport. Cela n'inclut pas l'URL du serveur de rapports. |
|Utilisateur |IDUtilisateur |L'ID de l'utilisateur exécutant le rapport. |
| |Langue |L'ID de langue de l'utilisateur exécutant le rapport. |
**Champs de rapport**

|**Nom de l'ensemble**|**Description**|
| :- | :- |
|Parameters |La collection de paramètres contient les paramètres du rapport dans le rapport. Les paramètres peuvent être transmis aux requêtes, utilisés dans des filtres ou utilisés dans d'autres fonctions qui modifient l'apparence du rapport en fonction du paramètre. |
|Champs |La collection Champs contient les champs dans l'ensemble de données actuel. |
|EnsembleDeDonnées ||
**Opérateurs**
Les opérateurs arithmétiques sont utilisés pour combiner des nombres, des variables numériques, des champs numériques et des fonctions numériques afin d'obtenir un autre nombre. Les opérateurs de comparaison sont généralement utilisés pour comparer des opérandes pour une condition dans une structure de contrôle telle qu'une déclaration If. Les opérateurs booléens sont généralement utilisés avec des opérateurs de comparaison pour générer des conditions pour les structures de contrôle.

|**Nom de l'ensemble**|**Nom de la formule**|**Description**|
| :- | :- | :- |
|Arithmétique |^ |Exponentiation, par exemple 2^3. |
| |* |Multiplication, par exemple 2*3. |
| |/ |Division, par exemple 2/3. |
| |\\\ |Division entière, par exemple 2\\\3. |
| |Mod |Modulus, par exemple 4 Mod 3. |
| |+ |Addition, par exemple 4 + 3. |
| |- |Soustraction, par exemple 4 – 3. |
|Comparaison |< |Inférieur à, par exemple 4 < 3 faux. |
| |<= |Inférieur ou égal, par exemple 4 <= 3 faux. |
| |> |Supérieur à, par exemple 4 > 3 vrai. |
| |>= |Supérieur ou égal, par exemple 4 >= 3 vrai. |
| |= |Égal, par exemple 4 = 3 faux. |
| |<> |Différent, par exemple 4 <> 3 vrai. |
| |Like |Compare une chaîne à un motif. Par exemple résultat = chaîne Like motif. |
| |Is |Compare deux variables de référence d'objet, par exemple asp Is aspose. |
|Concaténation |& |Génère une concaténation de chaînes à partir de deux expressions. |
| |+ |Ajoute deux nombres ou renvoie la valeur positive d'une expression numérique. Peut également être utilisé pour concaténer deux expressions de chaîne. |
|Logique/Bit à bit |Et |Effectue une conjonction logique sur deux expressions booléennes, ou une conjonction bit à bit sur deux expressions numériques. |
| |Non |Effectue une négation logique sur une expression booléenne, ou une négation bit à bit sur une expression numérique. |
| |Ou |Effectue une disjonction logique sur deux expressions booléennes, ou une disjonction bit à bit sur deux expressions numériques. |
| |Xor |Effectue une exclusion logique sur deux expressions booléennes, ou une exclusion bit à bit sur deux expressions numériques. |
| |EtAussi |Effectue une conjonction logique à court-circuit sur deux expressions. |
| |OuAussi |Effectue une disjonction logique inclusive à court-circuit sur deux expressions. |
|Décalage de bits |>> |Effectue un décalage arithmétique vers la gauche sur un motif de bits. |
| |<< |Effectue un décalage arithmétique vers la droite sur un motif de bits. |

