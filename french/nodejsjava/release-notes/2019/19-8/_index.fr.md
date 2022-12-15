---
title: Aspose.Cells for Node.js via Java 19.8 Notes de mise à jour
type: docs
weight: 10
url: /fr/nodejs-java/aspose-cells-for-node-js-via-java-19-8-release-notes/
---
{{% alert color="primary" %}} 

Cette page contient les notes de version pour Aspose.Cells for Node.js via Java 19.8.

{{% /alert %}} 

|**Clé**|**Sommaire**|**Catégorie**|
|:- |:- |:- |
|CELLSJAVA-42861|Impossible d'obtenir le texte alternatif de la forme au format de fichier ODS|Punaise|
|CELLSJAVA-42929|Modifications du titre du graphique lors de la conversion de XLSX en PDF|Punaise|
|CELLSJAVA-42933|La couleur des graphiques change lors de la conversion du fichier Excel en PDF|Punaise|
|CELLSJAVA-42946|Mauvais rendu du graphique à barres empilées avec des séries au format PDF|Punaise|
|CELLSJAVA-42942|Pages imprimées au niveau de la feuille de calcul et non au niveau du classeur|Punaise|
|CELLSJAVA-42952|Mauvaise indentation du haut de la cellule dans certains mots|Punaise|
|CELLSJAVA-42902|Le style de graphique en cascade n'est pas copié correctement lors de la copie du classeur|Punaise|
|CELLSJAVA-42939|Avertissement levé par Excel si nous appelons uniquement Workbook.getVbaProject() pour un classeur|Punaise|
|CELLSJAVA-42940|Avertissement de sécurité après la suppression de tous les scripts du module VBA|Punaise|
|CELLSJAVA-42955|L'ouverture de VBAProject corrompt le classeur|Punaise|
|CELLSJAVA-42945|Enregistrer au format HTML génère une exception si ExportImagesAsBase64 est défini|Exception|
|CELLSJAVA-42953|NullPointerException lors de la conversion de fichiers XLS en HTML|Exception|
|CELLSJAVA-42951|java.lang.NullPointerException levée par comment.setHtmlNote()|Exception|
|CELLSJAVA-42954|Exception levée lors du chargement et de l'enregistrement du fichier XLSX|Exception|
|CELLSJAVA-42957|Une valeur FontUnderlineType non valide est générée lors de l'enregistrement du fichier XLSX|Exception|
### **Public API et modifications incompatibles avec les versions antérieures**
Vous trouverez ci-dessous une liste de toutes les modifications apportées au public API, telles que les membres ajoutés, renommés, supprimés ou obsolètes, ainsi que toute modification non rétrocompatible apportée à Aspose.Cells for Node.js via Java. Si vous avez des préoccupations concernant l'un des changements répertoriés, veuillez le signaler. sur le forum d'assistance Aspose.Cells.
#### **Met à jour la bibliothèque BouncyCastle référencée vers 1.60**
La bibliothèque BouncyCastle incluse dans l'archive de la version a été mise à niveau vers la version 1.60. Cependant, Aspose.Cells est également compatible avec les anciennes versions, de sorte que l'utilisateur peut toujours utiliser les anciennes versions telles que 1.46.
#### **Obsolète la classe HTMLLoadOptions et ajoute la classe HtmlLoadOptions**
Utilisez plutôt la classe HtmlLoadOptions.
#### **Obsolète la classe ODSLoadOptions et ajoute la classe OdsLoadOptions**
Utilisez plutôt la classe OdsLoadOptions.
#### **Obsolète la classe JSONUtility et ajoute la classe JsonUtility**
Utilisez plutôt la classe JsonUtility.
#### **Ajoute l'interface IPageSavingCallback**
Contrôler/indiquer la progression du processus d'enregistrement de la page.
#### **Ajoute la classe PageSavingArgs**
Informations pour un processus d'enregistrement de page.
#### **Ajoute la classe PageStartSavingArgs**
Les informations d'une page lancent le processus d'enregistrement.
#### **Ajoute la classe PageEndSavingArgs**
Les informations d'une page terminent le processus d'enregistrement.
#### **Ajoute la propriété PdfSaveOptions.PageSavingCallback**
Contrôler/indiquer la progression du processus d'enregistrement de la page.

