---
title: Éditeur de feuille de calcul  Composants
type: docs
weight: 50
url: /fr/java/spreadsheet-editor-components/
---

**Table des matières**

- [Index.html](#SpreadsheetEditor-Components-Index.html)
- [WorksheetView](#SpreadsheetEditor-Components-WorksheetView)
- [WorkbookService](#SpreadsheetEditor-Components-WorkbookService)
- [LoaderService](#SpreadsheetEditor-Components-LoaderService)
- [CellsService](#SpreadsheetEditor-Components-CellsService)

L'éditeur de feuilles de calcul HTML5 est composé de quelques composants qui se rejoignent pour former le système complet. Ici, nous décrivons le but et le rôle de chacun.
### **Index.html**
C'est une page JSF qui décrit l'interface utilisateur de l'éditeur et le point d'entrée principal de notre application. Toutes les interactions entre le navigateur Web et le serveur sont effectuées via ce point d'entrée.

En plus de définir l'interface utilisateur, tous les services back-end sont attachés ici en utilisant les technologies JSF. Lorsque l'utilisateur interagit avec l'interface utilisateur, les événements et les données sont échangés entre les services et l'utilisateur pour accomplir nos tâches, par exemple l'exportation de feuilles de calcul.

Il y a deux principaux domaines d'intérêt.

**Ruban**

La zone de la barre d'outils onglet en haut est appelée ruban, techniquement. Il contient des boutons, des menus déroulants, des radios, des boîtes de dialogue et des champs cachés qui sont utilisés pour effectuer de nombreuses opérations sur la feuille de calcul. Lorsque ces boutons sont cliqués, ils envoient des commandes au serveur et mettent à jour la feuille en conséquence.

**Feuille**

La feuille est composée de lignes et de colonnes. Lorsque des cellules sont cliquées, le ruban est mis à jour en conséquence sans envoyer de demandes au serveur, car toutes les données nécessaires au ruban sont attachées à chaque cellule. Le ruban garde également une trace de la cellule, de la ligne et de la colonne sélectionnées lorsque l'utilisateur navigue dans la feuille.

Chaque cellule a son propre éditeur en ligne qui devient visible lorsque la cellule est en mode édition.
### **WorksheetView**
Il s'agit d'un bean back-end JSF à portée de vue responsable de la gestion du contenu dynamique de l'interface utilisateur décrite dans index.html. Il contient des gestionnaires d'événements pour les requêtes Ajax qui sont déclenchées lorsque l'utilisateur interagit avec l'interface utilisateur.
### **WorkbookService**
Le WorkbookService est un bean backend JSF à portée de vue. Il fonctionne comme un composant de service et charge et décharge la feuille de calcul avec l'aide d'autres services. Il possède les points d'extrémité suivants:

**init**

La **init** est une méthode **PostConstruct** qui est exécutée juste après la création de l'objet par le serveur d'application Java. Elle vérifie le paramètre **url** dans la carte des paramètres de la requête et charge la feuille de calcul correspondante à partir de l'emplacement donné, si possible.

**destroy**

Il est responsable de nettoyer toutes les ressources acquises lorsqu'elles ne sont plus nécessaires.
### **LoaderService**
Il crée des instances de feuilles de calcul et les garde en mémoire aussi longtemps qu'elles sont nécessaires.
### **CellsService**
Le **CellsService** gère le cache des lignes, des colonnes, des cellules, de la mise en forme et de la structure des feuilles de calcul.
