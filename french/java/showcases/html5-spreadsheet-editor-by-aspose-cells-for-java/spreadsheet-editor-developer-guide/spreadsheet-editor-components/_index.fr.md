---
title: Éditeur de feuille de calcul - Composants
type: docs
weight: 50
url: /fr/java/spreadsheet-editor-components/
---
**Table des matières**

- [Index.html](#SpreadsheetEditor-Components-Index.html)
- [Feuille de calcul](#SpreadsheetEditor-Components-WorksheetView)
- [Service de classeur](#SpreadsheetEditor-Components-WorkbookService)
- [LoaderService](#SpreadsheetEditor-Components-LoaderService)
- [CellsService](#SpreadsheetEditor-Components-CellsService)

HTML5 Spreadsheet Editor est construit à partir de quelques composants qui se rejoignent pour former le système complet. Nous décrivons ici le but et le rôle de chacun.
### **Index.html**
Il s'agit d'une page JSF qui décrit l'interface utilisateur de l'éditeur et le point de terminaison principal de notre application. Toutes les interactions effectuées entre le navigateur Web et le serveur sont effectuées via ce point de terminaison.

Outre la définition de l'interface utilisateur, tous les services backend sont attachés ici à l'aide des technologies JSF. Lorsque l'utilisateur interagit avec les événements de l'interface utilisateur et que les données sont transmises entre les services et l'utilisateur pour effectuer nos tâches, par exemple l'exportation de feuilles de calcul.

Il a deux centres d'intérêt principaux.

**Ruban**

La zone de la barre d'outils à onglets en haut est appelée ruban, techniquement. Il contient des boutons, des listes déroulantes, des menus radios, des zones de texte et des champs cachés qui sont utilisés pour effectuer de nombreuses opérations sur la feuille de calcul. Ces boutons, lorsqu'ils sont cliqués, envoient des commandes au serveur et mettent à jour la feuille en conséquence.

**Feuille**

La feuille est les lignes et les colonnes. Lorsque vous cliquez sur des cellules, le ruban est mis à jour en conséquence sans envoyer de requêtes au serveur car toutes les données nécessaires au ruban sont attachées à chaque cellule. Le ruban garde également une trace de la cellule, de la ligne et de la colonne sélectionnées lorsque l'utilisateur navigue dans la feuille.

Chaque cellule a son propre éditeur en ligne qui devient visible lorsqu'une cellule est en mode édition.
### **Feuille de calcul**
Il s'agit d'un bean backend JSF à portée de vue chargé de gérer le contenu dynamique de l'interface utilisateur décrit dans index.html. Il a des gestionnaires d'événements pour les requêtes Ajax qui sont déclenchées lorsque l'utilisateur interagit avec l'interface utilisateur.
### **Service de classeur**
Le WorkbookService est un bean backend JSF à portée de vue. Il fonctionne comme un composant de service et charge et décharge la feuille de calcul à l'aide d'autres services. Il a les points de terminaison suivants :

**initialiser**

 Le**initialiser** est**Post-construction** méthode qui est exécutée juste après la création de l'objet par le serveur d'applications Java. Il vérifie**URL** paramètre dans la carte des paramètres de demande et charge la feuille de calcul correspondante à partir d'un emplacement donné, si possible.

**détruire**

Il est responsable de nettoyer toutes les ressources acquises lorsqu'elles ne sont plus nécessaires.
### **LoaderService**
Il crée des instances de feuille de calcul et les garde en mémoire aussi longtemps qu'elles sont nécessaires.
### **CellsService**
 Le**CellsService** gère le cache des lignes, des colonnes, des cellules, du formatage et de la structure des feuilles de calcul.
